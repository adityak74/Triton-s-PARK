'''*********************************************************************************
TRITONSPARK - TEST - SMART PARKING LOT SYSTEM
*********************************************************************************'''
from pubnub import Pubnub
from threading import Thread
import sys

pub_key = "pub-c-c7e0db72-117c-4e7b-95ca-5848e2c56a3b"
sub_key = "sub-c-0b137540-0098-11e7-af37-0619f8945a4f"

g_userData = dict()
g_myCar = dict()
g_carNumber = '2'

def init():
	#Pubnub Key Initialization
	global pubnub 
	pubnub = Pubnub(publish_key=pub_key,subscribe_key=sub_key)
	pubnub.subscribe(channels='parkingapp-resp', callback=callback, error=callback,
					connect=connect, reconnect=reconnect, disconnect=disconnect)

def callback(message, channel):
	g_userData.update(message)

def caRcallback(message, channel):
	g_myCar.update(message)

def dataHandling(parking_lot_num, parking_car_num, parking_status):
		init()
		if(parking_status == 1):
			pubnub.publish(channel='parkingapp-req', 
					message={"requester":"APP","lotNumber":str(parking_lot_num),
					"requestType":2,"requestValue":str(parking_car_num)})
		else:
			pubnub.publish(channel='parkingapp-req', 
					message={"requester":"APP","lotNumber":str(parking_lot_num),
					"requestType":3,"requestValue":str(parking_car_num)})
		
			
def error(message):
    print("ERROR : " + str(message))
  
def connect(message):
    print "CONNECTED"
  
def reconnect(message):
	print("RECONNECTED")
  
def disconnect(message):
	print("DISCONNECTED")

# if __name__ == '__main__':
	
# 	while True:
# 		t1 = Thread(target=dataHandling, args=(sys.stdin,))
# 		t1.start()
# 		t1.join()

		
#End of the Script 
##*****************************************************************************************************##
