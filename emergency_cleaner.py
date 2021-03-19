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
print("Deleting temp files/Suppression des fichiers temporaires")
#Try to empty recycle bin
try:
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    print("Emptying recycle bin/Vidage de la corbeille")

#If already empty do this to avoid crash        
except:
    print("Recycle bin already empty/Corbeille déjà vide")

#Initialize pywinauto
app = Application(backend="uia")

#Start disk cleanup
app.start("cleanmgr.exe")
#Wait for the window to appear
print("Opening disk cleaner/Ouverture du nettoyeur de disque")
app['NettoyageDeDisqueSelectionDuLecteur'].wait('exists enabled visible active', timeout=99999)
#Select the main disk
app['NettoyageDeDisqueSelectionDuLecteur'].OK.click()
#Wait for the scan to be done
print("Scanning main disk/Scan du disque principal en cours")
app['NettoyageDeDisquePourC'].wait('exists enabled visible active', timeout=99999)
#Click on 'delete files'
app['NettoyageDeDisquePourC'].OK.click()
#Confirm
app['NettoyageDeDisque']['SupprimerLesFichiers'].click()
print("Disk cleaning in progress/Nettoyage de disque en cours")
#Start disk defrag
app.start("dfrgui.exe")
#Wait for the defrag window to appear
print("Opening disk defrag/Ouverture du défragmenteur de disque")
app['DefragmenteurDeDisque'].wait('exists enabled visible active', timeout=99999)
#Click on defrag disk
app['DefragmenteurDeDisque']['DefragmenterLeDisque'].click()
print("Défragmentation du disque en cours")
#Close the window until it's done
app['DefragmenteurDeDisque'].close()
#Finishing
print("Finished/Terminé")


