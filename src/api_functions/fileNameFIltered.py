import os
import json
from json import load
from tokenize import String
from boto3 import client
import boto3
# @Description: take file name as input, return information of that file
# @Author: Cheng Wang
# @UpdateDate: 6/12/2022


def getFileNameCsvInfo(filename: str):
    """
    DOCUMENT
    It takes a filename as an argument, and returns a dictionary of the file's metadata
    
    :param filename: str = the name of the file you want to get the information for
    :type filename: str
    """
    key = 'csv/combined.csv'
    abs_path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    csv_path = abs_path+"\\credentials\\aws_s3_credentials.json"

    credentials = json.load(open(csv_path))

    s3_resource = boto3.client(
        service_name=credentials['service_name'],
        region_name=credentials['region_name'],
        aws_access_key_id=credentials['aws_access_key_id'],
        aws_secret_access_key=credentials['aws_secret_access_key'])

    bucket = credentials['aws_s3_bucket_name']

    obj = s3_resource.get_object(Bucket=bucket, Key=key)
    body_str = obj['Body'].read().decode()

    # split body into 1 list (contain csv headers and values) header=str->  csv_header_value_list[0]        value=string
    csv_header_value_list = body_str.split()
    inner_index_num = csv_header_value_list[0].split(
        ',')   # header 0-7 [0] file_name
    index_no = 0
    result = {}

    for i in range(len(csv_header_value_list)):
        if(i > 0):
            index_no += 1  # +1 record(key+value)

            header_list = csv_header_value_list[0].split(
                ',')  # split key(header) list

            csv_header_value_list[i] = csv_header_value_list[i].split(
                ',')  # slipt value list ','

            if(filename == csv_header_value_list[i][0]):

                result[str(index_no)] = {}
                for j in range(len(inner_index_num)):  # ? 8 elements
                    # i = 0      |      j = 0 - 7
                    result[str((index_no))][header_list[j]
                                            ] = csv_header_value_list[i][j]

    return result


# if __name__ == '__main__':
#     try:
#         print(getFileNameCsvInfo(dfasdf))
#     except NameError:
#         print("Please input a correct file name!")
