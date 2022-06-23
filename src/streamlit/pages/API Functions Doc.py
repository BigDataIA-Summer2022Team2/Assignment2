import streamlit as st



st.sidebar.markdown("# API Functions Document")

guide_info="""
# Guide
## API 1: infoFilter
### 1.1 Input Value
||filename|width|height|class|xmin|ymin|xmax|ymax|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Value Type|str|int|int|str|int|int|int|int|
|Description|image file name with max 32 length|image width|image height|aircraft class|aircraft position - xmin coordinate|aircraft position - ymin coordinate|aircraft position - xmax coordinate|aircraft position - ymax coordinate|
|isOption|True|True|True|True|True|True|True|True|
|Default value|""|0|0|""|0|0|0|0|
|Sample value|"03c9ba9a9d35977dee2c6841f948296c"|2000|1365|"F22"|686|1014|1028|1200|


### 1.2 Sample Request URL
> Tips: If you start FastAPI on your own machine, default documentation url will be: `http://127.0.0.1:8000/docs`

```
http://127.0.0.1:8000/api/get/infoFilter/?filename=03c9ba9a9d35977dee2c6841f948296c&width=0&height=0&className=F22&xmin=0&ymin=0&xmax=0&ymax=0
```

- Also if you are using Linux/Unix system machine, you can use Curl to test our APIs.
```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/get/infoFilter/?filename=03c9ba9a9d35977dee2c6841f948296c&width=0&height=0&className=F22&xmin=0&ymin=0&xmax=0&ymax=0' \
  -H 'accept: application/json'
```

### 1.3 Sample Response
> All return response will be in **Json** format
> outside number key is the index number in the csv file, not the index of images
```json
{
  "9": {
    "filename": "03c9ba9a9d35977dee2c6841f948296c",
    "width": "2000",
    "height": "1365",
    "class": "F22",
    "xmin": "686",
    "ymin": "1014",
    "xmax": "1028",
    "ymax": "1200"
  },
  "10": {
    "filename": "03c9ba9a9d35977dee2c6841f948296c",
    "width": "2000",
    "height": "1365",
    "class": "F22",
    "xmin": "1005",
    "ymin": "440",
    "xmax": "1485",
    "ymax": "588"
  }
}
```
"""



st.markdown(guide_info)


