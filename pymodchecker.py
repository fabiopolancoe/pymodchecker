import sys
from subprocess import call
from guizero import App, Text, PushButton, TextBox,info

def search():
    mod = str(packname.value)
    bool = mod in sys.modules
    if bool == True:
        app.info("Success!", "The module have been found in the system")
    elif bool == False:
        install = app.yesno("Fail", "The module haven't been found in the system. Install module?")
        if install == True:
            app.info("Installing...", "Installing the module, please click on 'OK' and wait")
            call(['xterm', '-e', 'pip3', 'install', mod])
        else:
            app.info("Okay!", "Okay, good luck Pythonista!")

app = App(title="PyModChecker", height=200)
label1 = Text(app, text="Welcome to Pythonista, let's check for installed Python modules")
label2 = Text(app, text="Type the name of the module you're searching for")
packname = TextBox(app, width=50)
get = PushButton(app, text="Search module", command=search)

app.display()
