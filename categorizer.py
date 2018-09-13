from __future__ import unicode_literals
import os,unicodedata,sys,pyperclip,shutil,subprocess


mypath=""
pathToSave=""
try:
    mypath=sys.argv[2]
except:
    mypath=pyperclip.paste()

if os.path.isdir(mypath):
    pathToSave=os.path.join(mypath,"categories")
    print("so we will categorize files in directory : "+mypath+" and i will be save in directory : "+pathToSave)
    postfix=input("Enter Postfix for directories (example : files) : ")
    if not postfix:
        postfix="files"
    allDirectories=os.listdir(mypath)
    if not os.path.exists(pathToSave):
        os.makedirs(os.path.join(pathToSave))
    
    for d in allDirectories:
        if os.path.isfile(os.path.join(mypath,d)):
            
            # d=unicodedata.normalize('NFKD', d).encode('ascii','ignore')
            filename, file_extension = os.path.splitext(d)
            extentionPath=file_extension.replace(".","")+"_"+postfix
            if not os.path.exists(os.path.join(pathToSave,extentionPath)):
                os.makedirs(os.path.join(pathToSave,extentionPath))
            d=u'{}'.format(d)
            shutil.move(os.path.join(mypath,d),os.path.join(pathToSave,extentionPath))
    subprocess.Popen(r'explorer /open,"'+pathToSave+'"')

else:
    print("the path was invalid")