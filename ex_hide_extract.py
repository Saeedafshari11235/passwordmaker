import patoolib
import os

def extract (filepath:str , extractdir:str ):
   desname = "saw"
   if not os.path.isdir(extractdir + "/"+ desname):
      os.chdir(extractdir)
      os.mkdir(desname)
      patoolib.extract_archive(filepath, outdir = extractdir + "/"+ desname)
      #os.system( "tar xvf " + filepath +" -C "+ extractdir + "/"+ desname)
      hide()
   else:
      os.remove(extractdir +"/"+ desname)
      extract(extractdir + "/"+ desname)

def hide (path:str):
   os.system( "attrib +h " + path) 


print("!Hider,extracter!")
print("Enter the path of file that you wanna extract:(exm:C:/my/folder/zip.zip)")
z = input()
print("Enter the path that you wanna extract the file into:(exm:C:/my/folder/)")
y = input()
extract(z,y)
