#!/usr/bin/puppet
# Install flask 2.1.0 pip3
exec { 'installflask':
  command => 'pip3 install flask==2.1.0',
  path    => '/usr/bin'
}
