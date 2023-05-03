#!/usr/bin/env ruby

regex = /^h.n$/
input_str = ARGV[0]

if input_str.match?(regex)
  puts input_str
end
