#!/usr/bin/python

import serial, sys, getopt

try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:")	# read arguments to variables
except getopt.GetoptError:
	print "usage: %s -i <number of CT:s>" % sys.argv[0]
	sys.exit(2)
for opt, arg in opts:
	# print help
	if opt == "-h":
		print "usage: %s -i <number of CT:s>" % sys.argv[0]
		sys.exit()
	# -i flag for the number of CT:s connected
	elif opt in ("-i"):
		numct = arg

ser = serial.Serial('/dev/ttyAMA0', 38400)	# device, baud-rate
ser.flushInput()				# remove garbage

try:
	while 1:
		response = ser.readline()	# read serial input
		z = response.split(",")		# sepparate values
		for x in range(0, int(numct)):
			print "CT %s: %s Watts" % (x+1, z[x])
		print ""

except KeyboardInterrupt:
	ser.close()
