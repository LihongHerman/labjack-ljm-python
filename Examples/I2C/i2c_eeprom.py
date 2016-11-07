"""
Demonstrates I2C communication using a LabJack. The demonstration uses a
LJTick-DAC connected to FIO0/FIO1 for the T7 or FIO4/FIO5 for the T4, and
configures the I2C settings. Then a read, write and again a read are performed
on the LJTick-DAC EEPROM.

"""
from random import randrange

from labjack import ljm


# Open first found LabJack
handle = ljm.openS("ANY", "ANY", "ANY")  # Any device, Any connection, Any identifier
#handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier
#handle = ljm.openS("T4", "ANY", "ANY")  # T4 device, Any connection, Any identifier
#handle = ljm.open(ljm.constants.dtANY, ljm.constants.ctANY, "ANY")  # Any device, Any connection, Any identifier

info = ljm.getHandleInfo(handle)
print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
      "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
      (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

deviceType = info[0]

# Configure the I2C communication.
if deviceType == ljm.constants.dtT4:
    # For the T4, using FIO4 and FIO5 for SCL and SDA pins. FIO0 to FIO3 are
    # reserved for analog inputs, and digital lines are required.
    ljm.eWriteName(handle, "I2C_SDA_DIONUM", 5)  # SDA pin number = 5 (FIO5)
    ljm.eWriteName(handle, "I2C_SCL_DIONUM", 4)  # SCL pin number = 4 (FIO4)
else:
    # For the T7 and other devices, using FIO0 and FIO1 for the SCL and SDA
    # pins.
    ljm.eWriteName(handle, "I2C_SDA_DIONUM", 1)  # SDA pin number = 1 (FIO1)
    ljm.eWriteName(handle, "I2C_SCL_DIONUM", 0)  # SCL pin number = 0 (FIO0)

# Speed throttle is inversely proportional to clock frequency. 0 = max.
ljm.eWriteName(handle, "I2C_SPEED_THROTTLE", 65516)  # Speed throttle = 65516 (~100 kHz)

# Options bits:
#     bit0: Reset the I2C bus.
#     bit1: Restart w/o stop
#     bit2: Disable clock stretching.
ljm.eWriteName(handle, "I2C_OPTIONS", 0)  # Options = 0

ljm.eWriteName(handle, "I2C_SLAVE_ADDRESS", 80)  # Slave Address of the I2C chip = 80 (0x50)

# Initial read of EEPROM bytes 0-3 in the user memory area. We need a single I2C
# transmission that writes the chip's memory pointer and then reads the data.
ljm.eWriteName(handle, "I2C_NUM_BYTES_TX", 1)  # Set the number of bytes to transmit
ljm.eWriteName(handle, "I2C_NUM_BYTES_RX", 4)  # Set the number of bytes to receive

# Set the TX bytes. We are sending 1 byte for the address.
aNames = ["I2C_DATA_TX"]
aWrites = [ljm.constants.WRITE]  # Indicates we are writing the values.
aNumValues = [1]  # The number of bytes
aValues = [0]  # Byte 0: Memory pointer = 0
ljm.eNames(handle, len(aNames), aNames, aWrites, aNumValues, aValues)

ljm.eWriteName(handle, "I2C_GO", 1)  # Do the I2C communications.

# Read the RX bytes.
aNames = ["I2C_DATA_RX"]
aWrites = [ljm.constants.READ]  # Indicates we are reading the values.
aNumValues = [4]  # The number of bytes
# aValues[0] to aValues[3] will contain the data
aValues = [0]*4
aValues = ljm.eNames(handle, len(aNames), aNames, aWrites, aNumValues, aValues)

print("\nRead User Memory [0-3] = %s" %
      " ".join([("%.0f" % val) for val in aValues]))

# Write EEPROM bytes 0-3 in the user memory area, using the page write
# technique.  Note that page writes are limited to 16 bytes max, and must be
# aligned with the 16-byte page intervals.  For instance, if you start writing
# at address 14, you can only write two bytes because byte 16 is the start of a
# new page.
ljm.eWriteName(handle, "I2C_NUM_BYTES_TX", 5)  # Set the number of bytes to transmit
ljm.eWriteName(handle, "I2C_NUM_BYTES_RX", 0)  # Set the number of bytes to receive

# Set the TX bytes.
aNames = ["I2C_DATA_TX"]
aWrites = [ljm.constants.WRITE]  # Indicates we are writing the values.
aNumValues = [5]  # The number of bytes
aValues = [0]  # Byte 0: Memory pointer = 0
# Create 4 new random numbers to write (aValues[1-4]).
aValues.extend([randrange(0, 256) for _ in range(4)])
ljm.eNames(handle, len(aNames), aNames, aWrites, aNumValues, aValues)

ljm.eWriteName(handle, "I2C_GO", 1)  # Do the I2C communications.

print("Write User Memory [0-3] = %s" %
      " ".join([("%.0f" % val) for val in aValues[1:]]))

# Final read of EEPROM bytes 0-3 in the user memory area. We need a single I2C
# transmission that writes the address and then reads the data.
ljm.eWriteName(handle, "I2C_NUM_BYTES_TX", 1)  # Set the number of bytes to transmit
ljm.eWriteName(handle, "I2C_NUM_BYTES_RX", 4)  # Set the number of bytes to receive

# Set the TX bytes. We are sending 1 byte for the address.
aNames = ["I2C_DATA_TX"]
aWrites = [ljm.constants.WRITE]  # Indicates we are writing the values.
aNumValues = [1]  # The number of bytes
aValues = [0]  # Byte 0: Memory pointer = 0
ljm.eNames(handle, len(aNames), aNames, aWrites, aNumValues, aValues)

ljm.eWriteName(handle, "I2C_GO", 1)  # Do the I2C communications.

# Read the RX bytes.
aNames = ["I2C_DATA_RX"]
aWrites = [ljm.constants.READ]  # Indicates we are reading the values.
aNumValues = [4]  # The number of bytes
# aValues[0] to aValues[3] will contain the data
aValues = [0]*4
aValues = ljm.eNames(handle, 1, aNames, aWrites, aNumValues, aValues)

print("Read User Memory [0-3] = %s" %
      " ".join([("%.0f" % val) for val in aValues]))

# Close handle
ljm.close(handle)
