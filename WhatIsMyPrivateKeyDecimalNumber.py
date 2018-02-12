
myPrivateKey = "" # put your bitcoin WIF format private key here!


import base58
import hashlib

def WIF2DEC(privatekey):
	privHex = base58.b58decode(privatekey).encode('hex')
	privRawHex = privHex[0: len(privHex)-8]
	privRawHex2 = privHex[2: len(privHex)-8]
	checksum = privHex[len(privHex)-8: len(privHex)]
	decodePrivRawHex = str(privRawHex).decode('hex');
	SHA256a = hashlib.new('sha256',decodePrivRawHex).digest()
	SHA256b = hashlib.new('sha256',SHA256a).digest()
	checksumCompare = SHA256b.encode('hex')[0:8]
	if checksumCompare == checksum : 
		privatekeyDecimal = int(privRawHex2,16)
		return ('Your private key dcimal number is: '+str(privatekeyDecimal))
	else:
		return ('Not valid bitcoin private key! ')

print WIF2DEC(myPrivateKey); 
