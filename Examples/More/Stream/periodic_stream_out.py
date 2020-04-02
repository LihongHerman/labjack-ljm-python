"""
Demonstrates usage of the periodic stream-out functions

Streams out arbitrary values. These arbitrary values act on DAC0 to cyclically
increase the voltage from 0 to 2.5.

Relevant Documentation:
 
LJM Library:
    LJM Library Installer:
        https://labjack.com/support/software/installers/ljm
    LJM Users Guide:
        https://labjack.com/support/software/api/ljm
    Opening and Closing:
        https://labjack.com/support/software/api/ljm/function-reference/opening-and-closing
    LJM Single Value Functions (like eReadName, eReadAddress): 
        https://labjack.com/support/software/api/ljm/function-reference/single-value-functions
    Stream Functions (eStreamRead, eStreamStart, etc.):
        https://labjack.com/support/software/api/ljm/function-reference/stream-functions
 
T-Series and I/O:
    Modbus Map:
        https://labjack.com/support/software/api/modbus/modbus-map
    Stream Mode:
        https://labjack.com/support/datasheets/t-series/communication/stream-mode
    Stream-Out:
        https://labjack.com/support/datasheets/t-series/communication/stream-mode/stream-out
    Digital I/O:
        https://labjack.com/support/datasheets/t-series/digital-io
    DAC:
        https://labjack.com/support/datasheets/t-series/dac

"""
import sys

from time import sleep

from labjack import ljm

import ljm_stream_util

def open_ljm_device(device_type, connection_type, identifier):
    try:
        handle = ljm.open(device_type, connection_type, identifier)
    except ljm.LJMError:
        print(
            "Error calling ljm.open(" +
            "device_type=" + str(device_type) + ", " +
            "connection_type=" + str(connection_type) + ", " +
            "identifier=" + identifier + ")"
        )
        raise

    return handle


def print_device_info(handle):
    info = ljm.getHandleInfo(handle)
    print(
        "Opened a LabJack with Device type: %i, Connection type: %i,\n"
        "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i\n" %
        (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5])
    )

def main():
    scan_rate = 1000
    scans_per_read = int(scan_rate / 2)
    # Number of seconds to stream out waveforms
    run_time = 5
    # The desired stream channels
    # Up to 4 out-streams can be ran at once
    scan_list_names = ["STREAM_OUT0"]
    scan_list = ljm.namesToAddresses(len(scan_list_names), scan_list_names)[0]
    # Only stream out to DAC0
    target_addr = 1000
    # Stream out index can only be a number between 0-3
    stream_out_index = 0
    samples_to_write = 512
    # Make an arbitrary waveform that increases voltage linearly from 0-2.5V
    write_data = []
    for i in range(samples_to_write):
        sample = 2.5*i/samples_to_write
        write_data.append(sample)

    print("Beginning...\n")
    handle = open_ljm_device(ljm.constants.dtANY, ljm.constants.ctANY, "ANY")
    print_device_info(handle)

    try :
        print("\nInitializing stream out... \n")
        ljm.periodicStreamOut(handle, stream_out_index, target_addr, scan_rate, len(write_data), write_data)
        actual_scan_rate = ljm.eStreamStart(handle, scans_per_read, len(scan_list), scan_list, scan_rate)
        print("Stream started with scan rate of %f Hz\n Running for %d seconds\n" % (scan_rate, run_time))
        sleep(run_time)

    except ljm.LJMError:
        ljm_stream_util.prepare_for_exit(handle)
        raise
    except Exception:
        ljm_stream_util.prepare_for_exit(handle)
        raise

    ljm_stream_util.prepare_for_exit(handle)


if __name__ == "__main__":
    main()