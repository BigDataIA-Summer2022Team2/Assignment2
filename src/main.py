from distutils.log import error
from pickle import GLOBAL
import random
import string
from fastapi import FastAPI, Query, Path, Request,HTTPException, Depends
from typing import Union
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer
import time
from numpy import equal
from pydantic import BaseModel
from pathlib import Path
import sys
import logging
import logging.config
from requests import request
from starlette.concurrency import iterate_in_threadpool
import json
import os
import yaml
from fastapi.responses import Response

from datetime import datetime, timedelta
from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
################################################################


from datetime import datetime
from pydantic import BaseModel


from fastapi_log.log_request import LoggingRoute
from fastapi_log import dashboard
import pymysql
path = str(Path(Path(__file__).parent.absolute()))
sys.path.insert(0, path)
from api_functions import getS3BucketBody
from api_functions import numAndClassNameFiltered
from api_functions import fileNameAndClassNameFiltered
from api_functions import imgSizeRangeFiltered
from api_functions import aircraftPositionFilter
from api_functions import displayPandasCsvHtmlOutput
from api_functions import displayPandasImagesHtmlOutput
from api_functions import getNumRandomImages
from api_functions import displayImage
from api_functions import returnHomePage
from api_functions import displaymodelcardhtmloutput
from api_functions import getboundingbox


app = FastAPI()

global username
username = ""
# global accesstoken
# accesstoken =""

############################# Auth - JWT #################################
# > openssl rand -hex 32

if os.path.exists("key.txt"):
    os.remove("key.txt")
    os.system("openssl rand -hex 32 >> key.txt")
    f = open("key.txt", "r")
    key = f.read()
    
    f.close()
else:
    os.system("openssl rand -hex 32 >> key.txt")
    f = open("key.txt", "r")
    key = f.read()
    f.close()

SECRET_KEY = key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 30 mins expire

# connect to DB


abs_path = os.path.dirname((os.path.abspath(__file__)))
print(abs_path)
yaml_path = abs_path + "/mysql.yaml"
print(os.path.exists(yaml_path))

with open(yaml_path, 'r') as file:
    config = yaml.safe_load(file)
#print(config)
db_host = config['credentials']['host']
db_user = config['credentials']['user']
db_password = config['credentials']['password']
db_database = config['credentials']['database']

con = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_database, charset="utf8")
c = con.cursor()

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: Union[str, None] = None

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

class UserInDB(User):
    hashed_password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)



def get_user(username: str):
    # db connection

    sql_status = c.execute('SELECT username,full_name,email,hashed_password,disabled from user_table WHERE username =%s',(username))
    if sql_status == 1:
        sql_result = c.fetchall()[0] # Tuple ("cheng","cheng wang", "xxx@email.com","$2b$12$mXOwgkMw7fMDvVe5WMf8M.S16i.97eVmpQRbePhaZ0ISub8BO1yD.", 0)
        result = {}
        result[username] = {}
        result[username]['username'] = sql_result[0]
        result[username]['full_name'] = sql_result[1]
        result[username]['email'] = sql_result[2]
        result[username]['hashed_password'] = sql_result[3]
        #result['disabled'] = sql_result[0][4]
        if sql_result[4] == 0:
            result[username]['disabled'] = False
        else:
            result[username]['disabled'] = True
        user_dict = result[username]

        return UserInDB(**user_dict)



def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    global username
    username = current_user.username
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    global username
    username = user.username
    # global accesstoken
    # accesstoken = access_token
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# @app.get("/users/me/items/") # Auth Test
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     return [{"item_id": "Foo", "owner": current_user.username}]
############################# Auth - JWT #################################



############################# Logging #################################

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project. 
                                      # This will get the root logger since no logger in the configuration has this name.

#app.router.route_class = LoggingRoute
#app.include_router(dashboard.router)
app.mount("/static", StaticFiles(directory="static"), name="static")




# Home page
@app.get("/", response_class=HTMLResponse)
async def home():
    response = returnHomePage.getHomePage()
    return response

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    params = request.query_params
    #logger.info(f"rid={idem} start request url={request.url}")
    #logger.info(f"rid={idem} input is:{params}")
    start_time = time.time()
    logTime = datetime.now()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} request url={request.url} completed_in={formatted_process_time}ms status_code={response.status_code}")
    response_body = [section async for section in response.body_iterator]
    response.body_iterator = iterate_in_threadpool(iter(response_body))
    level=logging.getLevelName(logger.getEffectiveLevel())
    statuscode = response.status_code
    try:    
        message = response_body[0].decode("utf-8")
        if response_body[0].decode("utf-8") == '{"detail":"Item not found"}':
            logger.error("No data Found! please check your input.")
            level = 'ERROR'
            message = ("No data Found! please check your input.")
            statuscode =status.HTTP_404_NOT_FOUND
        if response_body[0].decode("utf-8") == '{"detail":"Given number should be less than 10 and greater than 0!"}':
            logger.error("Given number should be less than 10 and greater than 0!")
            level = 'ERROR'
            message = ("Given number should be less than 10 and greater than 0!")
            statuscode =status.HTTP_400_BAD_REQUEST
        if response_body[0].decode("utf-8") == '{"detail":"Not authenticated"}':
            statuscode =status.HTTP_401_UNAUTHORIZED
            logger.error("Not authenticated.")
            level = 'ERROR'
            message = ("Error: Unauthorized.")
    except:
        message = "Results Found!"
    
    
    global username
    db = con.cursor()
    if request.url == 'http://127.0.0.1:8000/token/' or request.url=='http://127.0.0.1:8000/openapi.json':
        return response

    user_status = db.execute('SELECT userId from user_table where username = %s', (username))
    if user_status != 0:
        sqlresult = db.fetchall()
        userId = list(sqlresult)[0][0]
        db.execute('INSERT INTO log_table(logId,userId,level_,requestUrl,code_,response,logTime,processTime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(idem,userId,level,request.url,statuscode,message,logTime,formatted_process_time))
        con.commit()
        username = ""
    return response

############################# Logging #################################

############################# API Functions #################################

@app.get("/api/get/getboundingbox/")
async def getBoundingBox(filename:str,current_user: User = Depends(get_current_active_user)):
    """
    You can search our files using filename, and we will show you the image with bounding boxes.
    """
    
    image = getboundingbox.getboundingbox(filename)
    if image == {"error:":"No data Found!"}:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return Response(content=image, media_type="image/jpeg")

# info 8 values for filter and return response
@app.get("/api/get/infoFilter/")
async def inputInfoFilterRequest(filename:str=None,
                              width:int=None,
                              height:int=None,
                              className:str=None,
                              xmin:int=None,
                              ymin:int=None,
                              xmax:int=None,
                              ymax:int=None,
                              current_user: User = Depends(get_current_active_user)):
    """
    You can search our files using any parameters below, and we will show you the eligible results.
    """
    
    response = getS3BucketBody.getS3BucketBodyInfo(filename,width,height,className,xmin,ymin,xmax,ymax) # get return response

    return  response

# fileName , class input and return response
@app.get("/api/get/fileNameAndClass/")
async def aircraftClassAndFileNameFilterRequest(className:str=None,
                              filename:str=None,
                              current_user: User = Depends(get_current_active_user)):
        """
        Type the class name and file name you want to search.
        """                      
        idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        width=height=xmin=ymin=xmax=ymax = 0
        response = getS3BucketBody.getS3BucketBodyInfo(filename,width,height,className,xmin,ymin,xmax,ymax) # get return response
        if response =={"error": "No data Found"}:
            raise HTTPException(status_code=404, detail="Item not found")
        
        return  response


@app.get("/api/get/imgSizeRange/")
async def imgSzieRangeRequest(width:int,
                              height:int,
                              current_user: User = Depends(get_current_active_user)):
    """
    It takes in a width and height, and returns a dictionary of all the images in the S3 bucket that are
    smaller than the width and height
        
    :param width: The minimum width of the image
    
    :param height: The height of the image you want to filter by
    """

    xmin=ymin=xmax=ymax = 0
    filename=className=""
    
    response = getS3BucketBody.getS3BucketBodyInfo(filename,width,height,className,xmin,ymin,xmax,ymax) # get return response
    if response =={"error": "No data Found"}:
            raise HTTPException(status_code=404, detail="Item not found")
    return  response

# (xmin,ymin,xmax,ymax) range and get response
@app.get("/api/get/aircraftPositionRange/")
async def aircraftPositionRequest(xmin:int,
                                  ymin:int,
                                  xmax:int,
                                  ymax:int,
                                  current_user: User = Depends(get_current_active_user)):
    """
    Tell us the coordinate range of the aircraft, and we will show you every aircraft meets your requirement.
    """
    
    width = height = 0
    filename = className = ""
    
    response = getS3BucketBody.getS3BucketBodyInfo(filename,width,height,className,xmin,ymin,xmax,ymax) # get return response
    if response =={"error": "No data Found"}:
            raise HTTPException(status_code=404, detail="Item not found")
    return  response

# No input value and get response(all info)
@app.get('/api/get/allInfo/')
async def getAllImgInfo():

    """
    Get all info about our dataset.
    """
    response = getS3BucketBody.getS3BucketBodyInfo() # get return response
    
    
    return response

# input aircraft Num and output all images == numbers
# option: class -> input all filtered info contain input class name
@app.get("/api/get/aircraftNumandClass/")
async def numAndClassFiteredInfoRequest(num:int,
                                         className:str=None,
                                         current_user: User = Depends(get_current_active_user)):
    """
    Type in an integer number, we will show you all files that contains the same number of aircrafs.
    """
    className = className.upper()
    response = numAndClassNameFiltered.getNumAndClassFilteredResult(num,className)
    
    if response =={"error": "No data Found"}:
            raise HTTPException(status_code=404, detail="Item not found")
                
    return  response


# get random Num images info
@app.get("/api/get/random/")
async def getNumRandomImage(num: int = Path(title="Number of random aircrafts", gt=0, le=9),
                            current_user: User = Depends(get_current_active_user)): 
    """
    Type in an integer number, we will show you same number of image.
    """
    response =  getNumRandomImages.getNumRandomImageFileNames(num)
    
    if response == {"error": "Given number should be less than 10 and greater than 0!"}:
            raise HTTPException(status_code=400, detail="Given number should be less than 10 and greater than 0!")
               
    return response

######################### Featured API for display #########################

# display pandas csv info html output
@app.get("/pandas/html/csv/", response_class=HTMLResponse)
async def getPandasCsvOutputHtmlPage():

    """
    Get the Pandas-Profiling page of our csv dataset.
    """
    response = displayPandasCsvHtmlOutput.getPandasProfilingCsvHtmlOutput()


    return response


# display pandas profling img info html output
@app.get("/pandas/html/image/", response_class=HTMLResponse)
async def getPandasImageOutputHtmlPage():

    """
    Get the Pandas-Profiling page of our image dataset.
    """
    response = displayPandasImagesHtmlOutput.getPandasProfilingImageHtmlOutput()

    return response
    
@app.get("/modelcard/html/", response_class=HTMLResponse)
async def getModelCardOutputHtmlPage():
    """
    Get the data card page of our dataset.
    """
    response = displaymodelcardhtmloutput.displayModelCardHtmlOutput()

    return response

#Todo
# display random image and its info
@app.get("/display/image/")
async def displayImageInHTML(imgName:str,current_user: User = Depends(get_current_active_user)):
    image = displayImage.displayImageInHTML(imgName)
    if image == {"error:":"No data Found!"}:
        raise HTTPException(status_code=404, detail="Item not found")
    return Response(content=image, media_type="image/jpeg")


# @Description: input basemodel
# @Author: Cheng Wang
# @UpdateDate: 6/13/2022
class csvInfo(BaseModel):
    #description: Union[str, None] = None
    #price: float
    #tax: Union[float, None] = None
    fileName : str=None
    width : int=None
    height : int=None
    className : str # ??????????????? class ??? python ??????????????? ????????????
    xmin : int=None
    ymin : int=None
    xmax : int=None
    ymax : int=None
    base64 : str=None
    RGB : dict=None
    valid_width : int=None
    valid_height : int=None
    fileSize : str=None
    aircraft_more_than_1 : bool=None
    aircraft_num : int=None
    
    
