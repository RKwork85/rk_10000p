# https://github.com/jmcnamara/XlsxWriter.git


from  other.XlsxWriter import xlsxwriter

## 示例一： hello.xlsx
# workbook = xlsxwriter.Workbook('hello.xlsx')
# worksheet = workbook.add_worksheet()

# worksheet.write('A1', 'Hello world')

# workbook.close()

## 示例二： 公式计算
# workbook = xlsxwriter.Workbook("array_formula.xlsx")
# worksheet = workbook.add_worksheet()

# # Write some test data.
# worksheet.write("B1", 500)
# worksheet.write("B2", 10)
# worksheet.write("B5", 1)
# worksheet.write("B6", 2)
# worksheet.write("B7", 3)
# worksheet.write("C1", 300)
# worksheet.write("C2", 15)
# worksheet.write("C5", 20234)
# worksheet.write("C6", 21003)
# worksheet.write("C7", 10000)

# # Write an array formula that returns a single value
# worksheet.write_formula("A1", "{=SUM(B1:C1*B2:C2)}")

# # Same as above but more verbose.
# worksheet.write_array_formula("A2:A2", "{=SUM(B1:C1*B2:C2)}")

# # Write an array formula that returns a range of values
# worksheet.write_array_formula("A5:A7", "{=TREND(C5:C7,B5:B7)}")

# workbook.close()

## 示例三： 合并单元格增加样式

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook("merge1.xlsx")
worksheet = workbook.add_worksheet()

# Increase the cell size of the merged cells to highlight the formatting.
worksheet.set_column("B:D", 12)
worksheet.set_row(3, 100)    ## 设置行高(第几行，多高)
worksheet.set_row(6, 10)
worksheet.set_row(7, 30)


# Create a format to use in the merged range.
merge_format = workbook.add_format(
    {
        "bold": 1,
        "border": 1,
        "align": "center",
        "valign": "vcenter",
        "fg_color": "yellow",
    }
)


# Merge 3 cells.
worksheet.merge_range("B4:D4", "Merged Range", merge_format)

# Merge 3 cells over two rows.
worksheet.merge_range("B7:D8", "Merged Range", merge_format)


workbook.close()