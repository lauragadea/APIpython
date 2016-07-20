import mercadopago
import json
import sys
import socket
import binascii
import struct
import errno
import shlex

client_id = "8345175340580712"
client_secret = "4BZspfgSwHIcopc3dbPlr2cmHXZMgeLS"
user_id = "43203111"

mp = mercadopago.MP("8345175340580712", "4BZspfgSwHIcopc3dbPlr2cmHXZMgeLS")
#access_token = mp.get_access_token()
#print 'Number of args: ', len(sys.argv)
#print 'Argument list', str(sys.argv[1])




if str(sys.argv[1]) == "user":
	#DATOS DEL USUARIO
	user = mp.get("/users/me")
	print user
elif str(sys.argv[1]) == "balance":
	balance = mp.get("/users/43203111/mercadopago_account/balance")
	print balance
elif str(sys.argv[1]) == 'currencies':
	#MONEDAS DISPONIBLES
	questions = mp.get("/currencies")
	print questions
else:
	print 'no es un comando valido'




#mp = mercadopago.MP("TEST-8345175340580712-041908-ce8fc1a3b875a4224c2ca9b97f46b26d__LC_LA__-43203111")







#ULTIMOS MOVIMIENTOS
#balance = mp.get("/mercadopago_account/movements/search")
#print balance

#FORMAS DE PAGO
#way_of_pay = mp.get("/v1/payment_methods")
#print way_of_pay

#print access_token


#print mp.get("https://api.mercadopago.com/collections/:id")
