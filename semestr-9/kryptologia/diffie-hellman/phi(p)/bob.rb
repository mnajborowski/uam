require "openssl"
sleep(10)
alice_socket = TCPSocket.new '10.100.5.224', 8081
while true
 alice_pk = alice_socket.gets
 dhB = OpenSSL::PKey::DH.new(alice_pk)
 dhB.generate_key!
 yB = dhB.pub_key
 sleep(2)
 alice_socket.puts yB
 dhA_public_key = alice_socket.gets
 dhA_public_key_converted = OpenSSL::BN.new(dhA_public_key)
 skB = dhB.compute_key(dhA_public_key_converted)
 puts "Final"
 puts skB
 break
end


