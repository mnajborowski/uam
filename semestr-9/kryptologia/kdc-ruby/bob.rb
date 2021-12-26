require 'socket'
require 'openssl'
require 'pdf-reader'

decipher = OpenSSL::Cipher.new('AES-128-ECB')
decipher.decrypt
 decipher.key = File.read('bob_private_key.txt')
cipher = OpenSSL::Cipher.new('AES-128-ECB')
cipher.encrypt
kdc_socket = TCPSocket.new '10.100.5.224', 8080
pdfFlag = 0

encrypted_session_key = kdc_socket.gets

puts 'encrypted session key: ' + encrypted_session_key

session_key = decipher.update(encrypted_session_key)

puts 'session key: ' + session_key

kdc_socket.close


cipher.key = session_key



alice_socket = TCPSocket.new '10.100.5.224', 8081
while true
 cipher.key = session_key
 decipher.key = session_key
 message = alice_socket.gets
 puts message
 decrypted = decipher.update(message)
 print "Decrypted message: " + decrypted + "\n"
 if pdfFlag < 1
 	puts "Sending parsed PDF - press ENTER to send"
 	reader = PDF::Reader.open('testpdf.pdf') do |reader|
   		txt = reader.pages.each do |page|
   		end
   	File.write 'temp.txt', txt.join("\n")
 	end
 	message = File.read('temp.txt')
 	# delete file:
 	File.delete('temp.txt') if File.exist?('temp.txt')
 	confirm = gets
 	# message = gets
 	encrypted= cipher.update(message) + cipher.final
 	pdfFlag = 1
 else
 	puts "Type message >> "
 	message = gets
 	encrypted = cipher.update(message) + cipher.final
 end
 puts "Encrypted " + encrypted
 alice_socket.puts encrypted
end

