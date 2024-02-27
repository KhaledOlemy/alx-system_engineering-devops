# This script does the following:
#   1. updates packages
#   2. installs Nginx
#   3. sets listening port on 80
#   4. sets `Hello World!` as a default response
#   5. adjusts redirect_me page to 301
#   6. starts/restarts server after everything
exec {'install-nginx':
      provider => shell,
      command  =>"""
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo chmod -R 777 /var/www
sudo echo 'Hello World!' > /var/www/html/index.nginx-debian.html
sudo echo "Ceci n'est pas une page" > /var/www/html/404.html
new_server_config=\
"server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name olemy.tech;

	location / {
		try_files \$uri \$uri/ =404;
	}
	if (\$request_filename ~ redirect_me)
	{
		rewrite ^ https://www.youtube.com/watch?v=VZrDxD0Za9I permanent;
	}
	error_page 404 /404.html;
}"

sudo chmod -R 777 /etc/nginx/
bash -c "echo -e '$new_server_config' > /etc/nginx/sites-enabled/default"

if [ "$(pgrep -c nginx)" -le 0 ];
then
	sudo service nginx start
else
	sudo service nginx restart
fi
"""
