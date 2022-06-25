import os
# @Description: show Pandas Profiling csv info Html page
# @Author: Cheng Wang
# @UpdateDate: 6/17/2022
"""
    Get the Pandas-Profiling page of our csv dataset.
    """
def getPandasProfilingCsvHtmlOutput():
    abs_path = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
    html_file_path= abs_path + "/notebooks/pandas_profiling/pandasprofilingcsv.html"

    HtmlFile = open(html_file_path, 'r', encoding='utf-8')
    response = HtmlFile.read()


    return response
