#!/usr/bin/env python

import os.path
import commands

makeExe = commands.getstatusoutput( 'chmod +x createsite.py ' )
print "\n"
print makeExe[1]
print "\n Make Executable :Success!" 

installGlobal = commands.getstatusoutput( 'chmod +x createsite.py ' )
print "\n"
print installGlobal[1]
print "\n Script Installed Successfully! \n Run command 'sudo createsite' " 
