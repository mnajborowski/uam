require 'openssl'

ecA = OpenSSL::PKey::EC.new('prime256v1')

ecA.generate_key!
ecA.public_key?
ecA.private_key?

alice = TCPServer.new 'localhost', 8081
bob = alice.accept

bob.puts ecA.public_key.to_bn
pkB_bn = OpenSSL::BN.new(bob.gets)
pkB = OpenSSL::PKey::EC::Point.new(ecA.group, pkB_bn)

skA = ecA.dh_compute_key(pkB)

puts "Alice's secret key: #{skA}"
