require "openssl"
sleep(15) # czasem nie wystarczy 15, warto odpalac troche pozniej po wpisaniu ruby alice.rb
alice_socket = TCPSocket.new 'localhost', 8081
while true
 alice_pk = alice_socket.gets
 puts alice_pk
 dhB = OpenSSL::PKey::DH.new(alice_pk) #alice.pk = alice_pk.to_der
 #pk = dhB.public_key
 dhB.generate_key!
 #xB
 sk = dhB.priv_key
 #yB
 yB = dhB.pub_key
 alice_socket.puts yB
 dhA_public_key = alice_socket.gets
 dhA_public_key_converted = OpenSSL::BN.new(dhA_public_key)
 skB = dhB.compute_key(dhA_public_key_converted)
 puts "Final"
 puts skB
 break
end
#BOB
#generuje (p,g) p = 2q+1, p - safe prime
#w new wrzuca to co dostaje od Alice (pk.to_der)
#dhB = OpenSSL::PKey::DH.new(100)
#klucz publiczy (dostepny)
#pk = dhB.public_key

#p = pk.p
#g = pk.g


#na podstawie (p,g) generuje pare (x,y)

#pk.generate_key!


#xA

#sk = pk.priv_key

#yA = pk.pub_key

#Alice dostaje pk.pem lub der i yA
#Bob dostaje dhA i oblicza skB
#skB = dhB.compute_key(dhA.pub_key)


