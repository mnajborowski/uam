require 'openssl'
require 'socket'

cipher = OpenSSL::Cipher.new('AES-128-ECB')
cipher.encrypt

session_key = cipher.random_key
puts 'session key: ' + session_key

server = TCPServer.new 8080

loop do
  alice = server.accept
  cipher.key = File.read('alice_private_key.txt')
  
  alice.puts cipher.update(session_key)
  alice.close
  bob = server.accept
  cipher.key = File.read('bob_private_key.txt')
  bob.puts cipher.update(session_key)
  bob.close
  server.close
end
