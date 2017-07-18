#!/usr/bin/env ruby
require 'wav-file'
wav = open("1.wav")
format = WavFile::readFormat(wav)
# puts format
chunk = WavFile::readDataChunk(wav)
wav.close
wavs = chunk.data.unpack('s*')
lsb = wavs.map{|sample| sample[0]}.join
flag = lsb[(lsb.index('1'))..-1]
puts [flag].pack('b*')
