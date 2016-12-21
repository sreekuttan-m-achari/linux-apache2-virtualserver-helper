# linux-apache2-virtualserver-helper
A simple python script for automating the task of creating virtual server environmsent settings for Linux running Apache2 

Run the following commands 

chmod +x createsite.py

$ sudo cp createsite.py /usr/local/bin/createsite

OR

just copy pase the 'createsite' file ( with out .p extenstion ) to the destination   ' /usr/local/bin/ ' 

then try running the following command 

$ sudo createsite 
$ Enter sitename (in lowercase): mysitename
$ Enter site domain (in lowercase eg : .local , .com , .net .. ):  .local
$ Enter site framework (  default / codeignitor / laravel / lumen  ): default


$ Apache Service Reloaded!
$ Project directory created at :  /var/www/html/mysitename
$ Site enabled! Visit link : http://mysitename.local