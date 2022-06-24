import streamlit as st
import pandas as pd
import numpy as np
import time
import base64
from PIL import Image
import os
import requests

st.sidebar.markdown("# Military Aircraft Detection Dataset version 7 🎈")    
st.header("Military Aircraft Detection version 7 🎈")
markdown_info = """
## About Dataset
- [Kaggle Dataset Link](https://www.kaggle.com/datasets/a2015003713/militaryaircraftdetectiondataset/)
> - bounding box in PASCAL VOC format (xmin, ymin, xmax, ymax)
> - 40 aircraft types
> (A10, A400M, AG600, AV8B, B1, B2, B52 Be200, C130, C17, C5, E2, EF2000, F117, F14, F15, F16, F18, F22, F35, F4, J20, JAS39, MQ9, Mig31, Mirage2000, RQ4, Rafale, SR71(may contain A12), Su34, Su57, Tornado, Tu160, Tu95(may contain Tu142), U2, US2, V22, Vulcan, XB70, YF23)

## Team 2
- [Github Repo](https://github.com/BigDataIA-Summer2022Team2/Assignment2)
- Cheng Wang
    - NUID: 001280107
    - email: wang.cheng3@northeastern.edu
- Meihu Qin
    - NUID: 002190486
    - email: 
"""

st.markdown(markdown_info)

# display home page img cover
def showHomePageImgCover():
    file_path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    img_path = file_path + "\\0041e69431bf872309d1aff628b6494f.jpg"

    open_img = Image.open(img_path)
    img_data = np.asarray(open_img)
    return img_data

st.image(showHomePageImgCover())













