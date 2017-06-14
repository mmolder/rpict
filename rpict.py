#!/usr/bin/python

import serial, sys, getopt, os.path, subprocess
from subprocess import call

"""
conf_serial
Called upon if the -n flag is given while running the script. This will reconfigure the serial connection 
to listen to n_shileds*8 inputs and calculate the estimated power for all of them. Use only if more shileds 
are added, not each time the script is run.
"""
def conf_serial(n_shields):
	print "Configuring serial port for use with %s shields..." % n_shields
	if n_shields == 1:
		execute = 'while read line; do echo $line > ' + serial_port + '; sleep 0.1; done < rpict8v1.conf'
		call(execute, shell=True)		
	elif n_shields == 2:
		execute = 'while read line; do echo $line > ' + serial_port + '; sleep 0.1; done < rpict8v2.conf'
		call(execute, shell=True)
	elif n_shields == 3:
		execute = 'while read line; do echo $line > ' + serial_port + '; sleep 0.1; done < rpict8v3.conf'
		call(execute, shell=True)
	elif n_shields == 4:
		execute = 'while read line; do echo $line > ' + serial_port + '; sleep 0.1; done < rpict8v4.conf'
		call(execute, shell=True)
	elif n_shields == 5:
		execute = 'while read line; do echo $line > ' + serial_port + '; sleep 0.1; done < rpict8v5.conf'
		call(execute, shell=True)
	else:
		print 'The number of shields is not supported, exiting.'
		sys.exit()
	print "Configuration done!"

def print_help():
	print "usage: %s -i <number of CT:s> [-n <number of shields>]" % sys.argv[0]
	print "only use the -n flag if more shileds are added, not every run"

try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:n:")	# read arguments to variables
except getopt.GetoptError:
	print_help()
	sys.exit(2)

if os.path.exists('/dev/ttyAMA0'):
	serial_port = '/dev/ttyAMA0'
elif os.path.exists('dev/ttyS0'):
	serial_port = '/dev/ttyS0'
else:
	print "Could not detect any supported serial port on device"
	sys.exit()
print "Device detected serial port @ %s" % serial_port

if len(sys.argv) <= 2:
	# default values
	numct = 1
	numshields = 1
else:
	for opt, arg in opts:
		# print help
		if opt == "-h":
			print_help()
			sys.exit()
		# -i flag for the number of CT:s connected
		elif opt in ("-i"):
			numct = arg
		# configure serial for n shields
		elif opt in ("-n"):
			numshields = arg
			# configure serial connection to the correct number of shields, do only if argument is given
			conf_serial(numshields)

ser = serial.Serial(serial_port, 38400)		# port, baud rate
ser.flushInput()							# remove garbage
print "Variables configured and serial port ready for use, starting collecting data..."

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
