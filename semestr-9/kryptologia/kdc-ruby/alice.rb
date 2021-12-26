#!/usr/bin/env ruby
require 'rubygems'
require 'socket'
require 'openssl'
require 'pdf-reader'

decipher = OpenSSL::Cipher.new('AES-128-ECB')
decipher.decrypt
cipher = OpenSSL::Cipher.new('AES-128-ECB')
cipher.encrypt
pdfFlag = 0


decipher.key = File.read('alice_private_key.txt')

kdc_socket = TCPSocket.new 'localhost', 8080

encrypted_session_key = kdc_socket.gets

puts 'encrypted session key: ' + encrypted_session_key 

session_key = decipher.update(encrypted_session_key)

puts 'session key: ' + session_key

kdc_socket.close



alice_server = TCPServer.new 'localhost', 8081

bob = alice_server.accept
while true
  cipher.key = session_key
  decipher.key = session_key
  # message = gets
  if pdfFlag < 1
  	puts "Sending parsed PDF - press ENTER to send"
  	reader = PDF::Reader.open('testpdf2.pdf') do |reader|
    	txt = reader.pages.each do |page|
    	end
    	File.write 'temp.txt', txt.join("\n")
  	end
  	message = File.read('temp.txt')
  	# delete file:
  	File.delete('temp.txt') if File.exist?('temp.txt')
  	confirm = gets 
  	encrypted = cipher.update(message) + cipher.final
  	pdfFlag = 1
  else
  	puts "Type message >> "
  	message = gets
  	encrypted = cipher.update(message) + cipher.final
  end
  puts "Encrypted " + encrypted
  bob.puts encrypted
  message = bob.gets
  decrypted = decipher.update(message)
  print "Decrypted message: " + decrypted + "\n"
end
