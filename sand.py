from openpyxl import Workbook
wb=Workbook()
ws=wb.active
ws.title='abcd'
l=list()
i=[x for x in 'abcdefgh']
print(i)
ws.append(i)
wb.save('abcd.xlsx')
wb.close()
