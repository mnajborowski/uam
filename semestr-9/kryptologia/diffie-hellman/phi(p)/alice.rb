require "openssl"

#ALICE
#generuje (p,g) p = 2q+1, p - safe prime
dhA = OpenSSL::PKey::DH.new(1024)
#klucz publiczy (dostepny)
pk = dhA.public_key

p = pk.p
g = pk.g


#na podstawie (p,g) generuje pare (x,y)

pk.generate_key!


#xA

sk = pk.priv_key

yA = pk.pub_key

#Bob dostaje pk.pem lub der i yA
#alice dostaje dhB i oblicza skA
#skA = dhA.compute_key(dhB.pub_key)

alice_server = TCPServer.new 'localhost', 8081
bob = alice_server.accept

while true
 bob.puts pk.to_der
 sleep(2)
 dhB_public_key = bob.gets
 dhb_public_key_converted = OpenSSL::BN.new(dhB_public_key)
 skA = dhA.compute_key(dhb_public_key_converted)
 puts "Final"
 puts skA
 bob.puts dhA.pub_key
 break
end
