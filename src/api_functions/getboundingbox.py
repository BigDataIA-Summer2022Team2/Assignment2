import os
import json
from json import load
from boto3 import client
import boto3
import torch
import torchvision
from torchvision.io import read_image
from torchvision.utils import draw_bounding_boxes
import io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image,ImageFont
from io import BytesIO
import torchvision.transforms as transforms
import numpy as np


def getboundingbox(filename):
    #filename= "0cd99a9ee135c7618006540f5b6d9b1b"
    key = 'csv/combined.csv'
    abs_path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    csv_path = abs_path+"/credentials/aws_s3_credentials.json"

    credentials = json.load(open(csv_path))

    s3_resource = boto3.client(
        service_name=credentials['service_name'],
        region_name=credentials['region_name'],
        aws_access_key_id=credentials['aws_access_key_id'],
        aws_secret_access_key=credentials['aws_secret_access_key'])


    bucket = credentials['aws_s3_bucket_name']

    obj = s3_resource.get_object(Bucket = bucket , Key = key)
    body_str = obj['Body'].read().decode()

    csv_header_value_list = body_str.split() # split body into 1 list (contain csv headers and values) header=str->  csv_header_value_list[0]        value=string
    inner_index_num = csv_header_value_list[0].split(',')   # header 0-7 [0] file_name
    box=[]
    class_name = []

    for i in range(len(csv_header_value_list)):
        if(i > 0):          
            csv_header_value_list[i] = csv_header_value_list[i].split(',') #  slipt value list ','

            if(filename == csv_header_value_list[i][0]):
                xmin = int(csv_header_value_list[i][4])
                ymin = int(csv_header_value_list[i][5])
                xmax = int(csv_header_value_list[i][6])
                ymax = int(csv_header_value_list[i][7])
                classname_for_each = csv_header_value_list[i][3]
                class_name.append(classname_for_each)
                box_for_each = [xmin,ymin,xmax,ymax]
                box.append(box_for_each)
                object = s3_resource.get_object(Bucket = bucket , Key =f'image/{filename}.jpg')
    if box == []:
        return {"error:":"No data Found!"}
    image_dl = object['Body'].read()
    image = Image.open(BytesIO(image_dl))
    transform = transforms.Compose([
        transforms.PILToTensor()
    ])
    img_tensor = transform(image)

    # bounding box are xmin, ymin, xmax, ymax
    
    box = torch.tensor(box)
    

    # draw bounding box and fill color
    img = draw_bounding_boxes(img_tensor,box,labels=class_name,width=3,colors="red",fill=False)

    # transform this image to PIL image
    img = torchvision.transforms.ToPILImage()(img)

    # display output
    b = io.BytesIO()
    img.save(b, 'jpeg')
    img = b.getvalue()
    

    return img
