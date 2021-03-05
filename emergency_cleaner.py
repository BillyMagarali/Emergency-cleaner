#Importing the sleep function to wait between two actions
from time import sleep
#Importing the pywinauto module for automation
from pywinauto.application import Application

#Importing the OS, tempfile (to delete temp files) and winshell (to empty the recycle bin)
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
            
#Emptying the temp folder
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
app.start("cleanmgr.exe", timeout=100)
#Select the main disk
app['NettoyageDeDisqueSelectionDuLecteur'].OK.click()
#Wait for the delete files window to appear
app['NettoyageDeDisquePourC'].wait('exists ready visible active enabled', timeout=100)
#Order to delete files
app['NettoyageDeDisquePourC'].OK.click()
#Confirm
app['NettoyageDeDisque']['SupprimerLesFichiers'].click()
#Wait for it to be done (had to use the sleep function because the confirm prompt and the deleting files prompt are called the same)
sleep(2)
app['NettoyageDeDisque'].wait_not('exists ready visible active enabled', timeout=100)
#Start disk defrag
app.start("dfrgui.exe", timeout=100)
#Click on defrag disk
app['DefragmenteurDeDisque']['DefragmenterLeDisque'].click()
#Close window while it's being done
app['DefragmenteurDeDisque'].close()

