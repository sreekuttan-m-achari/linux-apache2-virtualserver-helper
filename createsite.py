#!/usr/bin/env python

import os.path
import commands

# subdirectory =  "etc"
# try:
#     os.mkdir(subdirectory)
# except Exception:
#     pass

# subdirectory =  "etc/sites-available"
# try:
#     os.mkdir(subdirectory)
# except Exception:
#     pass

site_name = raw_input("Enter sitename (in lowercase): ")

site_domain = raw_input("Enter site domain (in lowercase eg : .local , .com , .net .. ): ")

conf_file_name = "/etc/apache2/sites-available/"+site_name+site_domain+".conf"

framework = raw_input("Enter site framework (  default / codeignitor / laravel / lumen / symfony ): ")

file = open(conf_file_name, "w")

file.write("<VirtualHost *:80> \n")

file.write("\t ServerName "+ site_name+site_domain+"\n")


if framework == 'laravel' or framework == 'lumen' :
	file.write("\t \tDocumentRoot /var/www/html/"+site_name+"/public \n")

	file.write("\t \t<Directory /var/www/html/"+site_name+"/public> \n")
elif framework == 'symfony' :
   	file.write("\t \tDocumentIndex app.php \n")

   	file.write("\t \tDocumentRoot /var/www/html/"+site_name+"/app \n")

	file.write("\t \t<Directory /var/www/html/"+site_name+"/app> \n")
else :
	file.write("\t \tDocumentRoot /var/www/html/"+site_name+" \n")

	file.write("\t \t<Directory /var/www/html/"+site_name+"> \n")
	

file.write("\t \t \t AllowOverride All \n \t \t \t Require all granted \n  \t \t </Directory> \n </VirtualHost>")

file.close()

enable_site = commands.getstatusoutput( 'sudo a2ensite '+ site_name+site_domain )
print "\n"
print enable_site[1]

server_reload = commands.getstatusoutput( 'sudo service apache2 reload ' )
print "\n"
print server_reload[1]
print "\n Apache Service Reloaded!" 

with open("/etc/hosts", "r+") as f:
     old = f.read() # read everything in the file
     f.seek(0) # rewind
     f.write("127.0.0.1 	 	" + site_name+site_domain +" \n" + old) # write the new line before

subdirectory =  "/var/www/html/"+ site_name

try:
    os.mkdir(subdirectory)
except Exception:
    pass

site = "\nProject directory created at : " +subdirectory+ "  \nSite enabled! Visit link : http://"+ site_name+site_domain

print site 

# <VirtualHost *:80>
#         ServerName mylara.com
#         DocumentRoot /var/www/html/mylara/public

#         <Directory /var/www/html/mylara/public>
#             AllowOverride All
#             Require all granted
#         </Directory>

# </VirtualHost>

