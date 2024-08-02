from  other.XlsxWriter import xlsxwriter


workbook = xlsxwriter.Workbook("gzc_eval.xlsx")
worksheet = workbook.add_worksheet()        # 增加表格

worksheet.set_row(0, 20)
worksheet.set_column(7, 7, 15)

merge_format_title = workbook.add_format(
    {
        # "bold": 1,
        "border": 1,
        "align": "center",
        "valign": "vcenter",
        "fg_color": "yellow",
    }
)

merge_format = workbook.add_format(
    {
        "border": 1,
        "align": "center",
        "valign": "vcenter",
    }
)


worksheet.merge_range("A1:M1", "A卷任务三模型微调参数机评得分详情", merge_format_title)

worksheet.merge_range("B2:H2", "参数设置", merge_format)
worksheet.merge_range("I2:L2", "其他", merge_format)

worksheet.merge_range("A2:A4", "选手编号", merge_format)
worksheet.merge_range("M2:M4", "总分", merge_format)

worksheet.merge_range("B3:C3", "固定值参数得分", merge_format)
worksheet.write('B4', '拆分验证集比例', merge_format)
worksheet.write('C4', '单次训练样本数', merge_format)

worksheet.merge_range("D3:G3", "组参数得分", merge_format)
worksheet.write('D4', '拆分验证集比例',merge_format)
worksheet.write('E4', '梯度累计步数',merge_format)
worksheet.write('F4', '验证步数',merge_format)
worksheet.write('G4', '训练总步数',merge_format)

worksheet.merge_range("H3:H4", "所有参数设置正确得分", merge_format)

worksheet.merge_range("I3:K3", "Rank排行", merge_format)
worksheet.write('I4', '准确率',merge_format)
worksheet.write('J4', 'Loss值',merge_format)
worksheet.write('K4', '排名',merge_format)

worksheet.merge_range("L3:L4", "提交格式得分", merge_format)



workbook.close()