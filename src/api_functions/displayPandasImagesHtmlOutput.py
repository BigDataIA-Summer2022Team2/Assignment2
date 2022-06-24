import os
# @Description: show Pandas Profiling img info Html page
# @Author: Cheng Wang
# @UpdateDate: 6/15/2022
def getPandasProfilingImageHtmlOutput():
    abs_path = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
    html_file_path=abs_path + "/notebooks/pandas_profiling/pandasprofilingimage.html"

    HtmlFile = open(html_file_path, 'r', encoding='utf-8')
    response = HtmlFile.read()


    return response