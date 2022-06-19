



import boto3   

mybuckets = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='AKIAXUUXEPBEC4KILU6U',
    aws_secret_access_key='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'
)

result = {}
for obj in mybuckets.Bucket('damg7245-amazon-s3').objects.all():
    
    key = obj.key
    if "csv" not in key:
        continue

    body = obj.get()['Body'].read()
    body_str = body.decode('utf-8')
    csv_header_value_list = body_str.split()
    inner_index_num = csv_header_value_list[0].split(',')   # header 0-7 [0] file_name
    index_no = 0

    for i in range(len(csv_header_value_list)):
        if(i>0):
            index_no += 1 #?   +1 record(key+value)
                    
            header_list = csv_header_value_list[0].split(',') # split key(header) list
            #split_key_list=csv_header_value_list[i-1][j].split(',')
                    
            csv_header_value_list[i] = csv_header_value_list[i].split(',') #  slipt value list ','
                #split_value_list=csv_header_value_list[i][j].split(',')
            if(csv_header_value_list[1][0] != "7a3ba2561b132070c339daf3799ae398"): #? request_file_name = file_name -> add json info   
                continue
            else:
                result[str(index_no)] = {} #? str(index_no)= outerkey       result[str(index_no)] = outer_value -> {inner_key : inner_value}

            for j in range(len(inner_index_num)): #? 8 elements 
                result[str((index_no))][header_list[j]] = csv_header_value_list[i][j] # i = 0      |      j = 0 - 7    
                #print("csv Total Lines: ",len(csv_header_value_list),"image Total air num:",index_no,"\n")
                #print(result[str((index_no))])
print(result)





    



