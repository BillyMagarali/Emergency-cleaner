#Importing the pywinauto module for automation
from pywinauto.application import Application
#Importing OS commands, tempfile (to get the temp dir) and winshell (to empty the recycle bin)
import os, shutil, tempfile, winshell

#getting the temp directory
temp = tempfile.gettempdir()

#function for emptying a folder
def empty_folder(folder):
    for file in os.listdir(folder):
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            shutil.rmtree(file, ignore_errors=True)

#Using it on the temp folder
empty_folder(temp)

#Try to empty recycle bin
try:
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

#If already empty do this to avoid crash        
except:
    print("Recycle bin already empty")

#Initialize pywinauto
app = Application(backend="uia")

#Start disk cleanup
app.start("cleanmgr.exe")
#Select the main disk
app['NettoyageDeDisqueSelectionDuLecteur'].OK.click()
#Wait for the scan to be done
app['NettoyageDeDisquePourC'].wait('exists ready visible active enabled', timeout=9999)
#Click on 'delete files'
app['NettoyageDeDisquePourC'].OK.click()
#Confirm
app['NettoyageDeDisque']['SupprimerLesFichiers'].click()
#Start disk defrag
app.start("dfrgui.exe")
#Click on defrag disk
app['DefragmenteurDeDisque']['DefragmenterLeDisque'].click()
#Close the window until it's done
app['DefragmenteurDeDisque'].close()


