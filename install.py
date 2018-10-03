import os
os.system("echo Create_AP & Nginx & Config By Legendary!!")

#获取运行目录
basedir=os.getcwd()+"/"

#解压数据包
os.system("sudo unzip "+basedir+"dat.zip")

#更换源，更新apt表
os.system("sudo cp -f -p "+basedir+"sources.list /etc/apt/sources.list")
os.system("sudo apt-get update")

#安装依赖soft
os.system("sudo apt-get install -y nginx gcc php7.0-zip ntfs-3g exfat-fuse ttf-wqy-zenhei chkconfig php7.0 php7.0-fpm php7.0-common util-linux procps hostapd iproute2 iw haveged dnsmasq")

#编译安装Create_ap From github
os.system("cd create_ap-master&&sudo make install")

#返回运行目录
os.system("cd "+basedir)

#开始拷贝配置文件
#PHP
os.system("sudo cp -f -p php.ini /etc/php/7.0/fpm/php.ini")
#dnsmasq
os.system("sudo cp -f -p dnsmasq.conf /etc/dnsmasq.conf")
#nginx
os.system("sudo cp -f -p -a -r html /var/www/")
os.system("sudo chown -R www-data /var/www/html")
os.system("sudo chown -R www-data /var/www/html/usb")
#调整权限
os.system("sudo chmod 777 /var/www/html/usb")
os.system("sudo chmod 777 /var/www/html")
os.system("sudo chmod 777 /var/www/html/fuck/filemanager.php")
os.system("sudo chown -R root /var/www/html/fuck/filemanager.php")
#nginx
os.system("sudo cp -f -p nginx/default /etc/nginx/sites-available/default")
os.system("sudo cp -f -p nginx.conf /etc/nginx/nginx.conf")
os.system("sudo service nginx restart")
os.system("sudo service nginx start")
#自启
os.system("sudo cp -f -p autoap /etc/init.d/autoap")
os.system("sudo chmod 755 /etc/init.d/autoap")
os.system("sudo chkconfig autoap on")
os.system("sudo mkdir -p /home/pi/autostart")
os.system("sudo chmod 777 /home/pi/autostart")
os.system("sudo cp -f -p create_ap-master/auto.py /home/pi/autostart/auto.py")
os.system("sudo chmod 777 /home/pi/autostart/auto.py")
os.system("sudo cp -f -p create_ap-master/fs.py /home/pi/autostart/fs.py")
os.system("sudo chmod 777 /home/pi/autostart/fs.py")
#################################################################
#                       Extension                               #                      
#################################################################








