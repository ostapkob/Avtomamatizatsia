import openpyxl

wb = openpyxl.Workbook()
# print(wb.get_active_sheet())
sheet = wb.get_active_sheet()
sheet.title = 'Ostap'
print(wb.get_active_sheet())
for i in range(1, 10):
    sheet['B' + str(i)] = i

wb.create_sheet('Potap')
sheet = wb.get_sheet_by_name('Potap')
print(sheet)
for i in range(1, 10):
    sheet['B' + str(i)] = i**2


wb.save('text_xl.xlsx')
