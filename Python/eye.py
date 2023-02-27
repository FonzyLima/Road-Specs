import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []
for i in ports:
    portList.append(str(i))
PORT = "COM5"

end_time = 10
serialInst.baudrate = 9600
serialInst.port = PORT
serialInst.open()
init_read = []
blink_count = 0
total_count = 0
drowsy = False
while True:
    
    if time.time() < end_time:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            reading = int(packet.decode('utf'))
            init_read.append(reading)

    average = sum(init_read)/len(init_read)
    if not drowsy:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            reading = int(packet.decode('utf'))
            total_count+=1
            if reading > average+50:
                blink_count+=1
            if (blink_count / total_count) * 100 >= 60:
                drowsy = True
    else:
        #Pin's code
        #when done
        drowsy = False
        blink_count = 0
        total_count = 0
        
