require 'openssl'

ecB = OpenSSL::PKey::EC.new('prime256v1')

ecB.generate_key!
ecB.public_key?
ecB.private_key?

alice = TCPSocket.new '10.100.5.224', 8081

pkA_bn = OpenSSL::BN.new(alice.gets)
pkA = OpenSSL::PKey::EC::Point.new(ecB.group, pkA_bn)
alice.puts ecB.public_key.to_bn

skB = ecB.dh_compute_key(pkA)

puts "Bob's secret key: #{skB}"
