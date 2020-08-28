from gtts import gTTS 
import os 
import PyPDF2 as p2
from time import sleep
from pydub import AudioSegment
import argparse

parser=argparse.ArgumentParser(description='pdf to mp3')
parser.add_argument('-p','--path_to_pdf',type=str,help='Path to the PDF file')
args=parser.parse_args()

pdf_path = args.path_to_pdf

PDFfile = open(pdf_path, 'rb')

PDFreader = p2.PdfFileReader(PDFfile)

language = 'en-us'

num_pages = PDFreader.getNumPages()
i = 1
final, first = None, True

while i <=(num_pages-1):
    print(f'page{i}')
    x = PDFreader.getPage(i)
    myobj = gTTS(text=x.extractText(), lang=language, slow=False)
    mp3_file = f"{pdf_path[:-4]}-{i}.mp3"
    myobj.save(mp3_file)
    if(first):
        final = AudioSegment.from_mp3(mp3_file)
        first = False
    else:
        final += AudioSegment.from_mp3(mp3_file)
    os.remove(mp3_file)
    i += 1
    sleep(4)

print('EXPORTING!')
final.export("complete.mp3", format="mp3")

print('DONE!')

# TO PLAY THE AUDIO
# os.system("start Deep Learning Based Chatbot Models.mp3")
