import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet']
cell = sheet['ai']
cell = sheet.cell(1,1)
print(cell.value)
