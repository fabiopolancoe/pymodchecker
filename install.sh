echo Welcome to PyChecker installer
pip3 install tkinter guizero
cd /usr/bin
sudo wget https://github.com/fabiopolancoe/pychecker/blob/master/pymodchecker.py
sudo wget https://github.com/fabiopolancoe/pychecker/blob/master/pymodchecker.sh
sudo mv pymodchecker.sh pymodchecker
sudo chmod 777 pymodchecker
echo Installed, issue pymodchecker in terminal to run 
