

body=b'filename,width,height,class,xmin,ymin,xmax,ymax\r\n03c9ba9a9d35977dee2c6841f948296c,2000,1365,F22,686,1014,1028,1200\r\n03c9ba9a9d35977dee2c6841f948296c,2000,1365,F22,1005,440,1485,588\r\n03c9ba9a9d35977dee2c6841f948296c,2000,1365,B2,1232,136,1720,336\r\n'

result={}
body_str = body.decode('utf-8')


csv_header_value_list = body_str.split() # split body into 1 list (contain csv headers and values) header=str->  csv_header_value_list[0]        value=string
        
        # csv_header_list = csv_header_value_list[0].split(',') # 'filename,width,height,class,xmin,ymin,xmax,ymax' -> [0] = 'filename'
        
        # csv_value_list = csv_header_value_list[1].split(',') # '00b2add164cb42440a52064e390ea3d2,1280,850,B1,322,112,893,618' [0] = '00b2add164cb42440a52064e390ea3d2'
inner_index = csv_header_value_list[0].split(',')
        
        
index_no = 0
for i in range(len(csv_header_value_list)):
    if(i > 0):
        index_no = i #?   +1 record(key+value)
        result[str(index_no)] = {} #? str(index_no)= outerkey       result[str(index_no)] = outer_value -> {inner_key : inner_value}
        
        header_list = csv_header_value_list[0].split(',') # split key(header) list
        #split_key_list=csv_header_value_list[i-1][j].split(',')
                    
        csv_header_value_list[i] = csv_header_value_list[i].split(',') #  slipt value list ','
        #split_value_list=csv_header_value_list[i][j].split(',')
    
        request = "03c9ba9a9d35977dee2c6841f948296c"

        if(csv_header_value_list[1][0] == request): #? request_file_name = file_name -> add json info   
            for j in range(len(inner_index)): #? 8 elements 
                result[str((index_no))][header_list[j]] = csv_header_value_list[i][j] # i = 0      |      j = 0 - 7
                


print(result)

