import os, shutil
import os.path
from paths import Paths

p1 = Paths('C:/Users/lpzam/Downloads', 'D:/My_Files/Pdf', 'D:/My_Files/Zip', 'D:/My_Files/Doc', 'D:/My_Files/Exe', 'D:/My_Files/Img', 'D:/My_Files/Folder') 

def moveFiles():
    for i in os.listdir(p1.source):
        try:
            if i.endswith('.pdf'):
                currently_pdf = p1.source + '/' + i
                p1.moveFile(currently_pdf, p1.pdf)

            elif i.endswith(('.zip', '.rar')):
                currently_rar = p1.source + '/' + i
                p1.moveFile(currently_rar, p1.rar)

            elif i.endswith(('.doc', '.docx', '.txt', '.csv', '.xls', '.pptx')):
                currently_doc = p1.source + '/' + i
                p1.moveFile(currently_doc, p1.doc)

            elif i.endswith('.exe'):
                currently_exe = p1.source + '/' + i
                p1.moveFile(currently_exe, p1.exe)

            elif i.endswith(('.jpg', '.png', '.tif')):
                currently_img = p1.source + '/' + i
                p1.moveFile(currently_img, p1.img)

            else:
                folderSource = p1.source + '/' + i
                p1.moveFile(folderSource, p1.folder)

        except:
            pass

if __name__ == '__main__':
    moveFiles()