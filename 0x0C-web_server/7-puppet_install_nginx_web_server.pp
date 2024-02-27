# This script does the following:
#   1. updates packages
#   2. installs Nginx
#   3. sets listening port on 80
#   4. sets `Hello World!` as a default response
#   5. adjusts redirect_me page to 301
#   6. starts/restarts server after everything

package { 'nginx':
  ensure => 'installed'
}

file_line { 'nginx_redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;'
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=VZrDxD0Za9I permanent;'
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!'
}

service { 'nginx':
  ensure  => 'running';
  require => Package['nginx']
}
