import sys, os
from subprocess import call
from guizero import App, Text, PushButton, TextBox

def search():
    mod = str(packname.value)
    bool = mod in sys.modules
    if bool == True:
        app.info("Success!", "The module have been found in the system")
    elif bool == False:
        install = app.yesno("Fail", "The module haven't been found in the system. Install module?")
        if install == True:
            app.info("Installing...", "Installing the module, please click on 'OK' and wait")
            call(['sudo', 'pip', 'install', mod])
        else:
            app.info("Okay!", "Okay, good luck Pythonista!")
            
def direct_install():
    mod1 = app.question("Specify package", "Please type the name of the package that you want to install", initial_value=None)
    if mod1 is not None:
        app.info("Installing...", "Installing the module, please click on 'OK' and wait")
        call(['sudo', 'pip', 'install', mod1])
    else:
        app.info("Okay!", "Okay, good luck Pythonista!")
    
def listmods():
    modlist = os.popen('pip list').read()
    app.info("Modules", modlist)

app = App(title="PyModChecker", height=250)
label1 = Text(app, text="Welcome to Pythonista, let's check for installed Python modules")
label2 = Text(app, text="Type the name of the module you're searching for")
packname = TextBox(app, width=50)
get = PushButton(app, text="Search module", command=search)
label3 = Text(app, text="Other tools and options")
list = PushButton(app, text="List all modules (Note:The list could be incomplete)", command=listmods)
install = PushButton(app, text="Directly install a module", command=direct_install)

app.display()
