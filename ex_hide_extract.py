import patoolib
import os
import uuid
import base64


def extract (filepath:str , extractdir:str ):
   desname = "saw"
   if not os.path.isfile(extractdir + desname):
      os.chdir(extractdir)
      os.mkdir(desname)
      #patoolib.extract_archive(filepath, outdir = extractdir+desname)
      os.system( "tar xvf " + extractdir+desname )
   else:
      os.remove(extractdir + desname)
      extract()

def hide (path:str):
   os.system( "attrib +h " + path) 

def key ():
   message = str(uuid.getnode())
   message_bytes = message.encode('ascii')
   base64_bytes = base64.b64encode(message_bytes)
   base64_message = base64_bytes.decode('ascii')
   return base64_message

