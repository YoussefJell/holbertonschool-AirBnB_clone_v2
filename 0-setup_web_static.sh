#!/usr/bin/env bash
# this sets up the webserver directories
my_config="root\ /var/www/html;\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"

sudo apt-get update -y
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo $'<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>' | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/


sudo sed -i "s@root\ /var/www/html;@${my_config}@g" /etc/nginx/sites-enabled/default
sudo service nginx restart
