from pywinauto.application import Application
import os, shutil, tempfile, winshell


temp = tempfile.gettempdir()


def empty_folder(folder):
    for file in os.listdir(folder):
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            shutil.rmtree(file, ignore_errors=True)

empty_folder(temp)
try:
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    
except:
    print("Recycle bin already empty")

app = Application(backend="uia")
app.start("cleanmgr.exe")
app['NettoyageDeDisqueSelectionDuLecteur'].OK.click()
app['NettoyageDeDisquePourC'].wait('exists ready visible active enabled', timeout=9999)
app['NettoyageDeDisquePourC'].OK.click()
app['NettoyageDeDisque']['SupprimerLesFichiers'].click()
app.start("dfrgui.exe")
app['DefragmenteurDeDisque']['DefragmenterLeDisque'].click()
app['DefragmenteurDeDisque'].close()


