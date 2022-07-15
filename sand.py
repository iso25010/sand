from openpyxl import Workbook
wb=Workbook()
ws=wb.active
ws.title='abcd'
l=list()
i=[x for x in 'abcdefgh123456']
j=i.copy()
j.reverse()
print(i)
print(j)
ws.append(i)
ws=wb.create_sheet('dcb')
ws.append(j)
wb.save('abcd.xlsx')
wb.close()
