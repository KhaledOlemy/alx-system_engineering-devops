#!/usr/bin/env ruby
a = ARGV[0].scan(/\[from:.*?\] \[to:.*?\] \[flags:.*?\]/).join
a.sub! '[from:', ''
a.sub! 'flags:', ''
a.sub! '] [', ','
a.sub! '] [', ','
a.sub! 'to:', ''
a.sub! ']', ''
puts a
