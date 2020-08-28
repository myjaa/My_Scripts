import PyPDF2 as p2

PDFfile = open('audiobook\Deep Learning Based Chatbot Models.pdf','rb')

PDFreader=p2.PdfFileReader(PDFfile)

# x=PDFreader.getPage(1)
# print(x.extractText())
num_pages=PDFreader.getNumPages()
i=1

while i<=(num_pages-1):
    x=PDFreader.getPage(i)
    print(x.extractText())
    i+=1
