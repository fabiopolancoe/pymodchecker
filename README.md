# PyModChecker
## No more issuing "pip3 list" to check if a Python module is installed!
Are you tired of issuing pip list or pip3 to check if the Python module that you need is installed or not in your system?
PyChecker is the solution, a **GUI** tool that checks if a Python module is installed an asks you if you want to install it.
### Requirements
- Tkinter (Python module)
- Guizero (Python module)
- Sys (Python module)
- Uxterm/Xterm (Linux application)
### Instalation instructions
#### Install packages manually
```
pip3 install tkinter guizero
```
```
sudo apt-get install xterm
```
Finally download and execute pymodchecker.py
#### Automatic install
```
wget https://github.com/fabiopolancoe/pymodchecker/blob/master/install.sh
sudo bash pymodchecker.sh
```
I will try to fix it so you can call it from a single command with no args
