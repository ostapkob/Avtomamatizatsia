import PyPDF2
import os
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())

print('-'*100)
pdfFileObj = open('encrypted.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.isEncrypted)
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())
print('-'*100)


pdf1 = open('meetingminutes.pdf', 'rb')
pdfReader1 = PyPDF2.PdfFileReader(pdf1)

pdf2 = open('meetingminutes2.pdf', 'rb')
pdfReader2 = PyPDF2.PdfFileReader(pdf2)

waterfile = open('watermark.pdf', 'rb')
water_mark = PyPDF2.PdfFileReader(waterfile)

pdfWriter =  PyPDF2.PdfFileWriter()




for page in range(1, pdfReader1.numPages):
    pdfWriter.addPage(pdfReader1.getPage(page))

for page in range(pdfReader2.numPages):
    p = pdfReader2.getPage(page)
    p.mergePage(water_mark.getPage(0))
    pdfWriter.addPage(p.rotateClockwise(90))

# pdfWriter.addPage(pdfReader1.getPage(0).rotateClockwise(90))

with open('merge.pdf', 'wb') as pdf_w:
    pdfWriter.write(pdf_w)

pdf1.close()
pdf2.close()
waterfile.close()
os.system('merge.pdf')



# import PyPDF2
# import os
# pdf1 = open('C:/YandexDisk/Книги/Avtomatizatsia_rutinnykh_zadach_pri_pomoschi_Python_RUS.pdf', 'rb')
# pdfReader1 = PyPDF2.PdfFileReader(pdf1)
# pdfWriter =  PyPDF2.PdfFileWriter()

# for page in range(390, pdfReader1.numPages):
#     pdfWriter.addPage(pdfReader1.getPage(page))

# with open('new.pdf', 'wb') as pdf_w:
#     pdfWriter.write(pdf_w)

# pdf1.close()
