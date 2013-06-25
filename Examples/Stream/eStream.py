"""
Demonstrates how to stream using the eStream functions.

"""

from labjack import ljm
import time
from datetime import datetime

ljm.writeLibraryConfigS(ljm.constants.LOG_LEVEL, 1); # 1 is stream packets, 2 is trace log level
ljm.writeLibraryConfigS(ljm.constants.LOG_MODE, 2); # 2 is continuous log, 3 is log on error

# Open first found LabJack
handle = ljm.open(ljm.constants.dtT7, ljm.constants.ctETHERNET, "192.168.1.175")
#handle = ljm.openS("ANY", "ETHERNET", "192.168.1.192")

info = ljm.getHandleInfo(handle)
print "Opened a LabJack with Device type: %i, Connection type: %i,\n" \
    "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" % \
    (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5])

numChannels = 2
scansPerRead = int(252/numChannels) #252 is the max reliable # samples per packet
aScanList_Pos = [0, 2] #[AIN0, AIN1]
aScanList_Neg = [ljm.constants.GND, ljm.constants.GND]
scanRate = 25000

#unknown error
#numChannels = 2
#scansPerRead = int(252/numChannels) #252 is the max reliable # samples per packet
#aScanList_Pos = [0, 2] #[AIN0, AIN1]
#aScanList_Neg = [ljm.constants.GND, ljm.constants.GND]
#scanRate = 50000

scanRate = ljm.eStreamStart(handle, scansPerRead, numChannels, aScanList_Pos, scanRate)
print "Start Stream"

print "Start Read"
try:
    loop = 100
    start = datetime.now()
    totScans = 0
    for i in range(loop):
        ret = ljm.eStreamRead(handle)
        data = ret[0]
        scans = len(data)/numChannels
        totScans += scans
        #totScans -= ret[1]
        print "\neStreamRead", i+1
        print "  First scan out of", scans, " AIN0 =", data[0], "AIN1 =", data[1]
        print "  numSkippedScans:", ret[1], ", deviceScanBacklog:", ret[2], ", ljmScanBacklog:", ret[2]
    end = datetime.now()

    print "\nTotal scans: ", totScans
    time = (end-start).seconds + float((end-start).microseconds)/1000000
    print "Time taken:", time, "seconds"
    print "LJM Scan Rate:", scanRate, "scans/second"
    print "Timed Scan Rate:", totScans/time, "scans/second"
    print "Sample Rate:", totScans*numChannels/time, "samples/second"
except ljm.LJMError, ljme:
    print ljme
except Exception, e:
    print e

print "Stop Stream"
ljm.eStreamStop(handle)

# Close handle
ljm.close(handle)