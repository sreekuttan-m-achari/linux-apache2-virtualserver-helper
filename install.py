#!/usr/bin/env python

import os.path
import subprocess

makeExe = subprocess.getstatusoutput( 'chmod +x createsite.py ' )
print ("\n")
print (makeExe[1])
print ("\n Make Executable :Success!")

installGlobal = subprocess.getstatusoutput( 'chmod +x createsite.py ' )
print ("\n")
print (installGlobal[1])
print ("\n Script Installed Successfully! \n Run command 'sudo createsite' ")
