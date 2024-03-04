# This script does the following:
#   1. updates packages
#   2. installs Nginx
#   3. sets listening port on 80
#   4. sets `Hello World!` as a default response
#   5. adjusts redirect_me page to 301
#   6. starts/restarts server after everything
#   7. adds custom header of `X-Served-By` for HOSTNAME

exec { 'addheader':
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By $HOSTNAME;/" /etc/nginx/nginx.conf; sudo service nginx restart;',
  provider => shell,
}
