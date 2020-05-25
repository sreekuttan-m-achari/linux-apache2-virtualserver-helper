#!/usr/bin/env python

import os.path
import subprocess

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

site_name = input("Enter sitename (in lowercase): ")

site_domain = input("Enter site domain (in lowercase eg : .local , .com , .net .. ): ")

www_support = input("Enable www." + site_name + site_domain + " (y/N): ")

conf_file_name = "/etc/apache2/sites-available/" + site_name + site_domain + ".conf"

framework = input("Enter site framework (  default / laravel / lumen / symfony ): ")

file = open(conf_file_name, "w")

# Added to mitigate CVE-2017-8295 vulnerability
file.write("UseCanonicalName On \n")

file.write("<VirtualHost *:80> \n")

file.write("\t ServerName " + site_name + site_domain + "\n")
if www_support == 'y' or www_support == 'Y':
    file.write("\t ServerAlias www." + site_name + site_domain + "\n")

if framework == 'laravel' or framework == 'lumen':
    file.write("\t \tDocumentRoot /var/www/html/" + site_name + "/public \n")

    file.write("\t \t<Directory /var/www/html/" + site_name + "/public> \n")
elif framework == 'symfony':
    file.write("\t \tDirectoryIndex app.php \n")

    file.write("\t \tDocumentRoot /var/www/html/" + site_name + "/web/app \n")

    file.write("\t \t<Directory /var/www/html/" + site_name + "/web/app> \n")
else:
    file.write("\t \tDocumentRoot /var/www/html/" + site_name + " \n")

    file.write("\t \t<Directory /var/www/html/" + site_name + "> \n")

file.write("\t \t \t AllowOverride All \n \t \t \t Require all granted \n  \t \t </Directory> \n")

file.write("\t CustomLog /var/log/apache2/" + site_name + site_domain + "-access.log combined \n")
file.write("\t ErrorLog /var/log/apache2/" + site_name + site_domain + "-error.log \n")

file.write("</VirtualHost>")

file.close()

enable_site = subprocess.getstatusoutput('sudo a2ensite ' + site_name + site_domain)
print("\n")
print(enable_site[1])

server_reload = subprocess.getstatusoutput('sudo service apache2 reload ')
print("\n")
print(server_reload[1])
print("\n Apache Service Reloaded!")

with open("/etc/hosts", "r+") as f:
    old = f.read()  # read everything in the file
    f.seek(0)  # rewind
    www_host = ""
    if www_support == 'y' or www_support == 'Y':
        www_host = "  www." + site_name + site_domain
    f.write("127.0.0.1 	 	" + site_name + site_domain + www_host + " \n" + old)  # write the new line before

subdirectory = "/var/www/html/" + site_name

if framework == 'default':
    try:
        os.mkdir(subdirectory)
    except Exception:
        pass
    permissons = subprocess.getstatusoutput('sudo chmod -R 777 ' + subdirectory)
    print("\n")
    print(permissons[1])
    print("\n Directory Permissions Updated")
    site = "\nProject directory created at : " + subdirectory + "  \nSite enabled! Visit link : http://" + site_name + site_domain
else:
    site = "\nCreate your project in : " + subdirectory + "  \n Site enabled! After creating project, visit link : http://" + site_name + site_domain

print(site)

# <VirtualHost *:80>
#         ServerName mylara.com
#         DocumentRoot /var/www/html/mylara/public

#         <Directory /var/www/html/mylara/public>
#             AllowOverride All
#             Require all granted
#         </Directory>

# </VirtualHost>
