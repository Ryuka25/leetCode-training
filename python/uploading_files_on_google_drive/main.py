from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os

gauth = GoogleAuth
gauth.LocalWebServerAyth()

drive = GoogleDrive(gauth)
path = str(input("Enter the correct path to the folder"))
path= r"{}".format(path)

try:
    for x in os.listdir(path):
        f = drive.createFile({'title':x})
        f.setContentFile(os.path.join(path,x))
        f.Upload()
        f = None

        print(f"[*] Uploading : {os.path.join(path,x)}")
except:
    print("Something wrong Happened")
    exit

print("[*] Upload Finish !")