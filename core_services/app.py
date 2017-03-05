'''*********************************************************************************
TRITONSPARK - TEST - SMART PARKING LOT SYSTEM AUTOMATION SCRIPT
*********************************************************************************'''

from pubnub import Pubnub
import time
from threading import Thread
import sys
from random import randint

pub_key = "pub-c-c7e0db72-117c-4e7b-95ca-5848e2c56a3b"
sub_key = "sub-c-0b137540-0098-11e7-af37-0619f8945a4f"

g_userData = dict()
g_myCar = dict()
g_carNumber = '2'

CAR_PRKING_OCCUPIED = 1
CAR_PARKING_FREE = 0

def callback(message, channel):
	g_userData.update(message)

def caRcallback(message, channel):
	g_myCar.update(message)

def startAutomation():
	# print ("**************************")
	# print ("*TRITONSPARK TEST CONSOLE*")
	# print ("**************************")

	global pubnub 
	pubnub = Pubnub(publish_key=pub_key,subscribe_key=sub_key)
	pubnub.subscribe(channels='parkingapp-resp', callback=callback, error=callback,
					connect=connect, reconnect=reconnect, disconnect=disconnect)

	parking_lots = 6
	r_park_time = randint(5,10)
	r_parking_lot_num = '%03d' % randint(1,6)
	r_parking_status = randint(0,1)
	# run_command = raw_input().split(' ')
	print "Sleeping for : ", r_park_time, " secs\n"
	if(r_parking_status == 1):
		pubnub.publish(channel='parkingapp-req', 
					message={"requester":"APP","lotNumber":str(r_parking_lot_num),
					"requestType":2,"requestValue":g_carNumber})
		time.sleep(2)
	else:
		pubnub.publish(channel='parkingapp-req', 
					message={"requester":"APP","lotNumber":str(r_parking_lot_num),
					"requestType":3,"requestValue":g_carNumber})
		time.sleep(2)
	# time.sleep(r_park_time)
		
def error(message):
    print("ERROR : " + str(message))
  
def connect(message):
    print "CONNECTED"
  
def reconnect(message):
	print("RECONNECTED")
  
def disconnect(message):
	print("DISCONNECTED")


if __name__ == '__main__':
	while True:
		t1 = Thread(target=startAutomation, args=())
		t1.start()
		t1.join()

		
#End of the Script 
##*****************************************************************************************************##
