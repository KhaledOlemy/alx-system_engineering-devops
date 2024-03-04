#!/usr/bin/puppet
# This script does the following:
#   1. updates packages
#   2. installs Nginx
#   3. sets listening port on 80
#   4. sets `Hello World!` as a default response
#   5. adjusts redirect_me page to 301
#   6. starts/restarts server after everything

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

exec { 'add_header':
  command  => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"${hostname}\";/" /etc/nginx/nginx.conf',
  provider => shell
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
