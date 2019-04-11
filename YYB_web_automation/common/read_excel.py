# -*- coding: utf-8 -*-
import xlrd
class ExcelUtil():
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r
if __name__ == "__main__":
    import os
    propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(propath)
    filepath = os.path.join(propath,"common","data_excel.xlsx")
    print(filepath)
    # filepath = "C:\web_etest\YYB\common\data_excel.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    print (data.dict_data())
    # for i in data.dict_data():
    #     print (i)