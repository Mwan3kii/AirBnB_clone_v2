#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
nginx_config="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" "$nginx_config"; then
    sudo sed -i "/listen 80 default_server;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" "$nginx_config"
fi
sudo service nginx restart
exit 0
