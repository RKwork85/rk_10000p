import string
from typing import List
from  other.XlsxWriter.xlsxwriter import Workbook

class ExcelWriter:
    def __init__(self, filename):
        self.workbook = Workbook(filename)
        self.worksheet = self.workbook.add_worksheet()

        self.base_row = 5

        ## 设置行高、列宽
        self.set_row(0, 20)
        self.set_column(0, 0, 9)
        self.set_column(1, 4, 15)
        self.set_column(5, 6, 12)
        self.set_column(7, 7, 20)
        self.set_column(8, 10, 8)
        self.set_column(11, 12, 12)


        ## 初始化表格
        self.create_title()
        self.create_header()
        self.create_parameters()

    def set_row(self, row, height):
        self.worksheet.set_row(row, height)

    def set_column(self, start_col, end_col, width):
        self.worksheet.set_column(start_col, end_col, width)

    def add_format(self, **kwargs):
        return self.workbook.add_format(kwargs)

    def merge_range(self, range_str, text, format):
        self.worksheet.merge_range(range_str, text, format)

    def write(self, row, col, text, format=None):
        if format:
            self.worksheet.write(row, col, text, format)
        else:
            self.worksheet.write(row, col, text)


    def create_title(self):
        title_format = self.add_format(
            border=1,
            align="center",
            valign="vcenter",
            fg_color="yellow"
        )
        self.merge_range("A1:M1", "A卷任务三模型微调参数机评得分详情", title_format)

    def create_header(self):
        cell_format = self.add_format(
            border=1,
            align="center",
            valign="vcenter"
        )
        self.merge_range("B2:H2", "参数设置", cell_format)
        self.merge_range("I2:L2", "其他", cell_format)
        self.merge_range("A2:A4", "选手编号", cell_format)
        self.merge_range("M2:M4", "总分", cell_format)

    def create_parameters(self):
        cell_format = self.add_format(
            border=1,
            align="center",
            valign="vcenter"
        )
        self.merge_range("B3:C3", "固定值参数得分", cell_format)
        self.write('B4', '拆分验证集比例', cell_format)
        self.write('C4', '单次训练样本数', cell_format)

        self.merge_range("D3:G3", "组参数得分", cell_format)
        self.write('D4', '拆分验证集比例', cell_format)
        self.write('E4', '梯度累计步数', cell_format)
        self.write('F4', '验证步数', cell_format)
        self.write('G4', '训练总步数', cell_format)

        self.merge_range("H3:H4", "所有参数设置正确得分", cell_format)

        self.merge_range("I3:K3", "Rank排行", cell_format)
        self.write('I4', '准确率', cell_format)
        self.write('J4', 'Loss值', cell_format)
        self.write('K4', '排名', cell_format)

        self.merge_range("L3:L4", "提交格式得分", cell_format)

    def parameters_grade(self, score_info: List[str]):
        cell_format = self.add_format(
            border=1,
            align="center",
            valign="vcenter"
        )

        
        letter = string.ascii_uppercase


        if len(score_info) == 12:
            for index, score_item in enumerate(score_info, start=0):

                cell_number = self.base_row 
                cell_position = letter[index] + str(cell_number)    
                print(cell_position)
                score_item = int(score_item)
                if index == 10:
                    self.write(cell_position, '', cell_format)       # 留空等到所有选手文件结束后再来一个 统计类实现
                else:
                    self.write(cell_position, score_item, cell_format)
            
        else:
            print("传入的格式不正确")

        self.base_row += 1 

    def save(self):
        self.workbook.close()


# 使用示例
excel_writer = ExcelWriter("gzc_eval.xlsx")


score_list = [str(i) for i in range(12)]

excel_writer.parameters_grade(score_list)
excel_writer.parameters_grade(score_list)
excel_writer.parameters_grade(score_list)


excel_writer.save()



