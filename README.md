# PyModChecker
## No more issuing "pip3 list" to check if a Python module is installed! :+1:
Are you tired of issuing pip list or pip3 to check if the Python module that you need is installed or not in your system?
PyChecker is the solution, a **GUI** tool that checks if a Python module is installed an asks you if you want to install it. **Note:** Run pymodchecker from a terminal.
### Requirements :computer:
- Tkinter (Python module)
- Guizero (Python module)
- Sys (Python module)
### Instalation instructions
#### Install packages manually :wrench:
```
pip3 install tkinter guizero
```
Finally download and execute pymodchecker.py
#### Automatic install :robot:
```
wget https://github.com/fabiopolancoe/pymodchecker/blob/master/install.sh
```
```
sudo bash install.sh
```
```
pymodchecker
```
This sould now run from a direct command

### **Note:** Please delete the pymodchecker and pymodchecker.py files from /usr/bin after upgrading to a new release or the upgrade will not work.
