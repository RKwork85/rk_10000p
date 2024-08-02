from  other.XlsxWriter.xlsxwriter import Workbook

class ExcelWriter:
    def __init__(self, filename):
        self.workbook = Workbook(filename)
        self.worksheet = self.workbook.add_worksheet()

    def set_row(self, row, height):
        self.worksheet.set_row(row, height)

    def set_column(self, start_col, end_col, width):
        self.worksheet.set_column(start_col, end_col, width)

    def add_merge_format(self, **kwargs):
        return self.workbook.add_format(kwargs)

    def merge_range(self, range_str, text, format):
        self.worksheet.merge_range(range_str, text, format)

    def write(self, row, col, text, format=None):
        if format:
            self.worksheet.write(row, col, text, format)
        else:
            self.worksheet.write(row, col, text)

    def create_title(self):
        merge_format_title = self.add_merge_format(
            border=1,
            align="center",
            valign="vcenter",
            fg_color="yellow"
        )
        self.merge_range("A1:M1", "A卷任务三模型微调参数机评得分详情", merge_format_title)

    def create_header(self):
        merge_format = self.add_merge_format(
            border=1,
            align="center",
            valign="vcenter"
        )
        self.merge_range("B2:H2", "参数设置", merge_format)
        self.merge_range("I2:L2", "其他", merge_format)
        self.merge_range("A2:A4", "选手编号", merge_format)
        self.merge_range("M2:M4", "总分", merge_format)

    def create_parameters(self):
        merge_format = self.add_merge_format(
            border=1,
            align="center",
            valign="vcenter"
        )
        self.merge_range("B3:C3", "固定值参数得分", merge_format)
        self.write('B4', '拆分验证集比例', merge_format)
        self.write('C4', '单次训练样本数', merge_format)

        self.merge_range("D3:G3", "组参数得分", merge_format)
        self.write('D4', '拆分验证集比例', merge_format)
        self.write('E4', '梯度累计步数', merge_format)
        self.write('F4', '验证步数', merge_format)
        self.write('G4', '训练总步数', merge_format)

        self.merge_range("H3:H4", "所有参数设置正确得分", merge_format)

        self.merge_range("I3:K3", "Rank排行", merge_format)
        self.write('I4', '准确率', merge_format)
        self.write('J4', 'Loss值', merge_format)
        self.write('K4', '排名', merge_format)

        self.merge_range("L3:L4", "提交格式得分", merge_format)

    def save(self):
        self.workbook.close()

# 使用示例
excel_writer = ExcelWriter("gzc_eval.xlsx")
excel_writer.set_row(0, 20)
excel_writer.set_column(7, 7, 15)
excel_writer.create_title()
excel_writer.create_header()
excel_writer.create_parameters()
excel_writer.save()