#!/usr/bin/env ruby

regex = /\A\d{10}\z/
arg = ARGV[0]

if arg && arg.match(regex)
  puts arg
end
