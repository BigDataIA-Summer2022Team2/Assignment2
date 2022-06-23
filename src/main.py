from fastapi import FastAPI, Query, Path
from typing import Union
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from log.logger import logger
import time
from pydantic import BaseModel
from pathlib import Path
import sys

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

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Home page
@app.get("/", response_class=HTMLResponse)
async def home():
    logger.info('=============== API start ===============')
    logger.info('mode: HTTP GET')
    funcName = getattr(returnHomePage.getHomePage,'__name__')
    logger.info('Call: {interface}',interface=funcName)
    logger.info( 'Now time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    response = returnHomePage.getHomePage()
    logger.info('=============== API end ===============\n\n')

    return response

# info 8 values for filter and return response
@app.get("/api/get/infoFilter/") # 127.0.0.1/api/get/infoFilter/
async def inputInfoFilterRequest(filename:Union[str,None]= Query(default="", max_length=40),
                              width:Union[int,None] = Query(default=0),
                              height:Union[int,None] = Query(default=0),
                              className:Union[str,None] = Query(default=""),
                              xmin:Union[int,None] = Query(default=0),
                              ymin:Union[int,None] = Query(default=0),
                              xmax:Union[int,None] = Query(default=0),
                              ymax:Union[int,None] = Query(default=0)):
    logger.info('=============== API start ===============')
    logger.info('mode: HTTP GET')
    logger.info( 'Function start time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    funcName = getattr(getS3BucketBody.getS3BucketBodyInfo,'__name__') # return function name which is called
    logger.info('Call: {interface}',interface=funcName)
    
    className = className.upper() #v22 V22
    response = getS3BucketBody.getS3BucketBodyInfo(filename,width,height,className,xmin,ymin,xmax,ymax) # get return response
    
    if(response == {}):
        logger.error("No data Found: HTTP 404")
    
    
    logger.info( 'Function end time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    logger.info('=============== API end ===============\n\n')
    return  response

# fileName , class input and return response
@app.get("/api/get/fileNameAndClass/")
async def aircraftClassAndFileNameRequest(className:str,
                              filename:Union[str,None]= Query(default="", max_length=32)):
    logger.info('=============== API start ===============')
    logger.info('mode: HTTP GET')
    logger.info('Function start time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    funcName = getattr(fileNameAndClassNameFiltered.getFileNameClassNameFilteredResult,'__name__') # return function name which is called
    logger.info('Call: {interface}',interface=funcName)
    className = className.upper()
    
    response = fileNameAndClassNameFiltered.getFileNameClassNameFilteredResult(className,filename) # get return response
    
    if(response == {}):
        logger.error("No data Found: HTTP 404")
        
    logger.info( 'Function end time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    logger.info('=============== API end ===============\n\n')
    
    
    
    return  response

# (width , weight) range and get response
@app.get("/api/get/imgSizeRange/")
async def imgSzieRangeRequest(width:Union[int,None] = Query(default=0),
                              height:Union[int,None] = Query(default=0)):
     
    logger.info('=============== API start ===============')
    logger.info('mode: HTTP GET')
    logger.info('Function start time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    funcName = getattr(imgSizeRangeFiltered.getimgSizeRangeFilteredResult,'__name__') # return function name which is called
    logger.info('Call: {interface}',interface=funcName)
    
    response = imgSizeRangeFiltered.getimgSizeRangeFilteredResult(width,height) # get return response
    
    if(response == {}):
        logger.error("No data Found: HTTP 404")
    
    logger.info( 'Function end time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    logger.info('=============== API end ===============\n\n')
    return  response

# (xmin,ymin,xmax,ymax) range and get response
@app.get("/api/get/aircraftPositionRange/")
async def aircraftPositionRequest(xmin:Union[int,None] = Query(default=0),
                                  ymin:Union[int,None] = Query(default=0),
                                  xmax:Union[int,None] = Query(default=0),
                                  ymax:Union[int,None] = Query(default=0)):
    
    logger.info('=============== API start ===============')
    logger.info('mode: HTTP GET')
    logger.info('Function start time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    funcName = getattr(aircraftPositionFilter.getAircraftPositionFilterResult,'__name__') # return function name which is called
    logger.info('Call: {interface}',interface=funcName)
    
    response = aircraftPositionFilter.getAircraftPositionFilterResult(xmin,ymin,xmax,ymax) # get return response
    
    if(response == {}):
        logger.error("No data Found: HTTP 404")
    
    logger.info( 'Function end time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    logger.info('=============== API end ===============\n\n')
    return  response

# No input value and get response(all info)
@app.get('/api/get/allInfo/')
async def getAllImgInfo():
    logger.info('=============== API start ===============')
    logger.info('mode: HTTP GET')
    logger.info('Function start time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    funcName = getattr(getS3BucketBody.getS3BucketBodyInfo,'__name__') # return function name which is called
    logger.info('Call: {interface}',interface=funcName)
    
    response = getS3BucketBody.getS3BucketBodyInfo() # get return response
    
    if(response == {}):
        logger.error("No data Found: HTTP 404")
    
    logger.info( 'Function end time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    logger.info('=============== API end ===============\n\n')
    return response

# input aircraft Num and output all images == numbers
# option: class -> input all filtered info contain input class name
@app.get("/api/get/aircraftNumandClass/")
async def numAndClassFiteredInfoRequest(num:int,
                                         className:Union[str,None] = Query(default="")):
    logger.info('=============== API start ===============')
    logger.info('mode: HTTP GET')
    logger.info('Function start time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    
    funcName = getattr(numAndClassNameFiltered.getNumAndClassFilteredResult,'__name__') # return function name which is called
    logger.info('Call: {interface}',interface=funcName)
    
    className = className.upper()
    response = numAndClassNameFiltered.getNumAndClassFilteredResult(num,className)
    
    
    if(response == {}):
        logger.error("No data Found: HTTP 404")
        
    logger.info( 'Function end time: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    logger.info('=============== API end ===============\n\n')
    return  response


# get random Num images info
@app.get("/api/get/random/{num}")
async def getNumRandomImage(num: int = Path(title="Number of random aircrafts", gt=0, le=9)): 
    
    logger.info('=============== API start ===============')
    funcName = getattr(getNumRandomImages.getNumRandomImageFileNames,'__name__')
    logger.info('Call: {interface}',interface=funcName)
    logger.info( 'Process start: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    response =  getNumRandomImages.getNumRandomImageFileNames(num)
    
    if(response == {}):
        logger.error("No data Found: HTTP 404")
        
    logger.info( 'Process end: {tiems}',tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    logger.info('=============== API end ===============')
    return response

######################### Featured API for display #########################

# display pandas csv info html output
@app.get("/pandas/html/csv/", response_class=HTMLResponse)
async def getPandasCsvOutputHtmlPage():

    logger.info('=============== API start ===============')

    funcName = getattr(displayPandasCsvHtmlOutput.getPandasProfilingCsvHtmlOutput,'__name__')
    logger.info('Interface Name: {interface}\tNow Time: {tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


    response = displayPandasCsvHtmlOutput.getPandasProfilingCsvHtmlOutput()

    if(response == {}):
        logger.error("No data Found: HTTP 404")

    logger.info('=============== API end ===============\n\n')

    return response


# display pandas profling img info html output
@app.get("/pandas/html/image/", response_class=HTMLResponse)
async def getPandasImageOutputHtmlPage():
    logger.info('=============== API start ===============')

    funcName = getattr(displayPandasImagesHtmlOutput.getPandasProfilingImageHtmlOutput,'__name__')
    logger.info('Interface Name: {interface}\tNow Time: {tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


    response = displayPandasImagesHtmlOutput.getPandasProfilingImageHtmlOutput()

    if(response == {}):
        logger.error("No data Found: HTTP 404")

    logger.info('=============== API end ===============\n\n')

    return response
    
@app.get("/modelcard/html/", response_class=HTMLResponse)
async def getModelCardOutputHtmlPage():

    logger.info('=============== API start ===============')

    funcName = getattr(displaymodelcardhtmloutput.displayModelCardHtmlOutput,'__name__')
    logger.info('Interface Name: {interface}\tNow Time: {tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


    response = displaymodelcardhtmloutput.displayModelCardHtmlOutput()

    if(response == {}):
        logger.error("No data Found: HTTP 404")

    logger.info('=============== API end ===============\n\n')

    return response

#Todo 
# Bug
# display random image and its info
@app.get("/display/image/", response_class=HTMLResponse)
async def displayImageInHTML():
    logger.info('=============== API start ===============')

    funcName = getattr(displayImage.showRandomImg,'__name__')
    logger.info('Interface Name: {interface}\tNow Time: {tiems}',interface=funcName, tiems=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    logger.info('=============== API end ===============\n\n')

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
