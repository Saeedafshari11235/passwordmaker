import patoolib
import os

def extract(fileName , fileDest):
    patoolib.extract_archive(fileName, outdir=fileDest)

def hide(hidedFile):
    os.system("attrib +h " + hidedFile)

