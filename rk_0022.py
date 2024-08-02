
'''
pands处理 xlsx 文件示例代码

基本 数据构造 写文件
'''

import pandas as pd

file = pd.ExcelFile('output.xlsx')  
with pd.ExcelFile("output.xlsx") as xls:  
    df1 = pd.read_excel(xls, "Sheet1")  
    print(df1)