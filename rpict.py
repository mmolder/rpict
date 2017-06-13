#!/usr/bin/python

import serial, sys, getopt, os.path

try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:")	# read arguments to variables
except getopt.GetoptError:
	print "usage: %s -i <number of CT:s>" % sys.argv[0]
	sys.exit(2)

if len(sys.argv) < 2:
	print "usage: %s -i <number of CT:s>" % sys.argv[0]
	sys.exit()

for opt, arg in opts:
	# print help
	if opt == "-h":
		print "usage: %s -i <number of CT:s>" % sys.argv[0]
		sys.exit()
	# -i flag for the number of CT:s connected
	elif opt in ("-i"):
		numct = arg

if os.path.exists('/dev/ttyAMA0'):
	serial_port = '/dev/ttyAMA0'
elif os.path.exists('dev/ttyS0'):
	serial_port = '/dev/ttyS0'
else:
	print "Could not detect any supported serial port on device"
	sys.exit()

ser = serial.Serial(serial_port, 38400)		# port, baud rate
ser.flushInput()				# remove garbage

try:
	while 1:
		response = ser.readline()	# read serial input
		z = response.split(",")		# separate values
		for x in range(0, int(numct)):
			print "CT %s: %s Watts" % (x+1, z[x])
		print ""

except KeyboardInterrupt:
	ser.close()
