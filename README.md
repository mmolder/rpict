# rpict
Code for reading values from up to 40 CT sensors connected to a raspberry pi. It requires a rpi 3 with RPICT8 shields mounted on it.

In order to stack multiple shield on top of eachother, configuration of the serial communication must be done. For one shield this configuration file looks like the following:

```
x
print
zero
format 0
vest 240
addnode 8 10 1 10
addnode 7 10 1 10
addnode 6 10 1 10
addnode 5 10 1 10
addnode 4 10 1 10
addnode 3 10 1 10
addnode 2 10 1 10
addnode 1 10 1 10

addchannel 0 5
addchannel 1 5
addchannel 2 5
addchannel 3 5
addchannel 4 5
addchannel 5 5
addchannel 6 5
addchannel 7 5
print 
x
```

Stacking an additional shield requires the following modifications to be made:

```
x
print
zero
format 0
vest 240
addnode 8 10 1 10
addnode 7 10 1 10
addnode 6 10 1 10
addnode 5 10 1 10
addnode 4 10 1 10
addnode 3 10 1 10
addnode 2 10 1 10
addnode 1 10 1 10
addnode 8 6 1 10
addnode 7 6 1 10
addnode 6 6 1 10
addnode 5 6 1 10
addnode 4 6 1 10
addnode 3 6 1 10
addnode 2 6 1 10
addnode 1 6 1 10

addchannel 0 5
addchannel 1 5
addchannel 2 5
addchannel 3 5
addchannel 4 5
addchannel 5 5
addchannel 6 5
addchannel 7 5
addchannel 8 5
addchannel 9 5
addchannel 10 5
addchannel 11 5
addchannel 12 5
addchannel 13 5
addchannel 14 5
addchannel 15 5
print
x
```

Explanation of the fields;
x: enters interactive mode </br>
print: prints current configuration</br>
format: modifies the output format (0 = CSV (comma separated values))</br>
vest: setup voltage for estimated power</br>
addnode: addnode <current_pin> <slave_pin> <voltage_pin> <slave_pin>, in this case the first eight are the 3,5mm connections on the master board and the last eight are the slave's</br>
addchannel: addchannel <combid> <type>, sets the output channel on the different nodes, in this case all should output the estimated power</br>

Adding additional shields (up to a total of 5 (1 master, 4 slaves)) requires adding another set of eight nodes using the same values as the first slave. The id:s used in the channel will only increase so the third shield for example will have id:s ranging from 16-23.

When the new configuration is done, this is executed by running
```
while read line; do echo $line > /dev/ttyS0; sleep 0.1; done < 1xrpict8.conf
```
in a terminal window.
