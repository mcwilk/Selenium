import xlrd

from FirstAppTestingWithPOP.utils.search_data import SearchData


class ExcelReader:

    @staticmethod
    def get_data():
        wb = xlrd.open_workbook("../Dane.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []

        for i in range(1, sheet.nrows):
            search_data = SearchData(
                sheet.cell(i, 1).value,
                sheet.cell(i, 2).value
            )
            data.append(search_data)

        return data
