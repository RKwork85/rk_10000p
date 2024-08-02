from openpyxl import load_workbook

# 加载工作簿
workbook = load_workbook('hello.xlsx')

# 选择工作表
sheet = workbook.active

# 读取单元格内容
cell_value = sheet['A1'].value
print(cell_value)