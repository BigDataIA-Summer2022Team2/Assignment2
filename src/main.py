from distutils.log import error
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
from datetime import datetime
from pydantic import BaseModel
#from fastapi_log.log_request import LoggingRoute
#from fastapi_log import dashboard
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

# Connect with database
con = pymysql.connect(host="localhost", user="root", password="1207", database="damg7245", charset="utf8")
c = con.cursor()

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project. 
                                      # This will get the root logger since no logger in the configuration has this name.

app = FastAPI()
#app.router.route_class = LoggingRoute
#app.include_router(dashboard.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# class User(BaseModel):
#     username: str
#     email: Union[str, None] = None
#     full_name: Union[str, None] = None
#     disabled: Union[bool, None] = None

# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
#     )

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     user = fake_decode_token(token)
#     return user

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
    message = ("Results Found!")           
    level=logging.getLevelName(logger.getEffectiveLevel())
    body = response_body[0].decode("utf-8")
    if body == '{"detail":"Item not found"}':
        logger.error("No data Found! please check your input.")
        level = 'ERROR'
        message = ("No data Found! please check your input.")
        
    if body == '{"detail":"Given number should be less than 10!"}':
        logger.error("Given number should be less than 10!")
        level = 'ERROR'
        message = ("Given number should be less than 10!")

    c.execute('INSERT INTO log_table(logId,userId,level,requestUrl,code,response,logTime,processTime) VALUES(%s,0,%s,%s,%s,%s,%s,%s)',(idem,level,request.url,response.status_code,message,logTime,formatted_process_time))
    con.commit()
    return response

# info 8 values for filter and return response
@app.get("/api/get/infoFilter/")
async def inputInfoFilterRequest(filename:str=None,
                              width:int=None,
                              height:int=None,
                              className:str=None,
                              xmin:int=None,
                              ymin:int=None,
                              xmax:int=None,
                              ymax:int=None):
    """
    You can search our files using any parameters below, and we will show you the eligible results.
    """
    
    response = getS3BucketBody.getS3BucketBodyInfo(filename,width,height,className,xmin,ymin,xmax,ymax) # get return response

    return  response

# fileName , class input and return response
@app.get("/api/get/fileNameAndClass/")
async def aircraftClassAndFileNameFilterRequest(className:str,
                              filename:str=None):
        """
        Type the class name and file name you want to search.
        """                      
        
        width=height=xmin=ymin=xmax=ymax = 0
        
        response = getS3BucketBody.getS3BucketBodyInfo(filename,width,height,className,xmin,ymin,xmax,ymax) # get return response
        if response =={"error": "No data Found"}:
            raise HTTPException(status_code=404, detail="Item not found")

        return  response


@app.get("/api/get/imgSizeRange/")
async def imgSzieRangeRequest(width:int,
                              height:int):
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
                                  ymax:int):
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
                                         className:Union[str,None] = Query(default="")):
    """
    Type in an integer number, we will show you all files that contains the same number of aircrafs.
    """
    className = className.upper()
    response = numAndClassNameFiltered.getNumAndClassFilteredResult(num,className)
    
    if response =={"error": "No data Found"}:
            raise HTTPException(status_code=404, detail="Item not found")
                
    return  response


# get random Num images info
@app.get("/api/get/random/{num}")
async def getNumRandomImage(num: int = Path(title="Number of random aircrafts", gt=0, le=9)): 
    """
    Type in an integer number, we will show you same number of image.
    """
    response =  getNumRandomImages.getNumRandomImageFileNames(num)
    
    if response == {"error": "Given number should be less than 10!"}:
            raise HTTPException(status_code=404, detail="Given number should be less than 10!")
               
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
@app.get("/display/image/", response_class=HTMLResponse)
async def displayImageInHTML():

    return displayImage.showRandomImg()


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
    className : str # 飞机种类的 class 为 python 内置关键字 需要转换
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
