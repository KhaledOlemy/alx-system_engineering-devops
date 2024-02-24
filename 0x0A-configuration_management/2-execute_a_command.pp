# create manifest kills process named killmenow
exec { 'killmenow':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
