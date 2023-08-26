import openpyxl

wb=openpyxl.Workbook()
file=open('header.h','r')
counter=1
text=file.read()
sheet=wb.create_sheet(title='sheet')
for i in text.splitlines():
    if(i.find('(')!=-1):#then this line contains a prototype
        sheet[f'A{counter}']=i
        sheet[f'B{counter}']=f"IDX{counter-1}"
    counter=counter+1
wb.save("prototypes.xlsx")
file.close()