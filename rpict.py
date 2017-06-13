#!/usr/bin/python

import serial, sys, getopt, os.path
from subprocess import call

def conf_serial(n_shileds):
	if n_shileds == 1:
		execute = 'while read line; do echo $line > ' + serial_port + '; sleep 0.1; done < rpict8v1.conf'
		call(execute)		
	elif n_shields == 2:
		execute = 'while read line; do echo $line > ' + serial_port + '; sleep 0.1; done < rpict8v2.conf'
		call(execute)
	elif n_shileds == 3:
		execute = 'while read line; do echo $line > ' + serial_port + '; sleep 0.1; done < rpict8v3.conf'
		call(execute)
	elif n_shields == 4:
		execute = 'while read line; do echo $line > ' + serial_port + '; sleep 0.1; done < rpict8v4.conf'
		call(execute)
	else:
		execute = 'while read line; do echo $line > ' + serial_port + '; slepp 0.1; done < rpict8v5.conf'
		call(execute)

try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:n:")	# read arguments to variables
except getopt.GetoptError:
	print "usage: %s -i <number of CT:s> -n <number of shields>" % sys.argv[0]
	sys.exit(2)

if os.path.exists('/dev/ttyAMA0'):
	serial_port = '/dev/ttyAMA0'
elif os.path.exists('dev/ttyS0'):
	serial_port = '/dev/ttyS0'
else:
	print "Could not detect any supported serial port on device"
	sys.exit()


if len(sys.argv) < 2:
	# default values
	numct = 1
	numshields = 1
else:
	for opt, arg in opts:
		# print help
		if opt == "-h":
			print "usage: %s -i <number of CT:s> -n <number of shields>" % sys.argv[0]
			sys.exit()
		# -i flag for the number of CT:s connected
		elif opt in ("-i"):
			numct = arg
		# configure serial for n shields
		elif opt in ("-n"):
			numshileds = arg
			# configure serial connection to the correct number of shields, do only if argument is given
			conf_serial(numshields)

ser = serial.Serial(serial_port, 38400)		# port, baud rate
ser.flushInput()							# remove garbage

try:
	# do forever
	while 1:
		response = ser.readline()	# read serial input
		z = response.split(",")		# separate values
		for x in range(0, int(numct)):
			print "CT %s: %s Watts" % (x+1, z[x])	# print results
		print ""

except KeyboardInterrupt:
	ser.close()
