import os

name = input()
fileF = name+".ui"
fileName = name+".py"
c = 'cmd /k "pyuic5 -x "'+fileF+'" -o "'+fileName

os.system(c)