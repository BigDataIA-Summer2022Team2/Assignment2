from PIL import Image
import io
import numpy as np
import boto3
import base64

mybuckets = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIAXUUXEPBEC4KILU6U',
        aws_secret_access_key='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'
    )

num = 0
for obj in mybuckets.Bucket('damg7245-amazon-s3').objects.all():
    key = obj.key
    if "image" not in key:
        continue
    if(num < 1):
        num+=1
        continue
    body = obj.get()['Body'].read()
    break


#body -> bytes
img_base64_data = base64.b64encode(body)

img_string_data = img_base64_data.decode('utf-8')

print(img_string_data)
#print(type(encoded))
# covert byte to RGB image
# img = Image.open(io.BytesIO(body))
# Image 转numpy
# img_data = np.array(img)




# img_ = Image.fromarray(img_data)
# img_.show()
