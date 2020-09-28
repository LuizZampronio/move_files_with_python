import shutil, os

class Paths:
    def __init__(self, source, pdf, rar, doc, exe, img, folder):
        self.source = source
        self.pdf = pdf
        self.rar = rar
        self.doc = doc
        self.exe = exe
        self.img = img
        self.folder = folder

    def moveFile(self, source, dest):
        return shutil.move(source, dest)