import pandas as pd

def main():
    excelname = 'sample.xlsx'
    excel = pd.ExcelFile(excelname)
    print(excel.sheet_names)


if __name__ == "__main__":
    main()