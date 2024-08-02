'''
pands处理 xlsx 文件示例代码

基本 数据构造 写文件
'''


import pandas as pd

df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],        # 构造数据表格式
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])

# df1.to_excel("output.xlsx",                       # 文件写入
#              sheet_name='Sheet_name_1')   

df2 = df1.copy()                                    # 复制数据
with pd.ExcelWriter('output.xlsx') as writer:  
    df1.to_excel(writer, sheet_name='Sheet_name_1') 
    df2.to_excel(writer, sheet_name='Sheet_name_2')     # 数据表重命名
    
with pd.ExcelWriter('output.xlsx',                           # 数据追加
                    mode='a') as writer:  
    df1.to_excel(writer, sheet_name='Sheet_name_3')


