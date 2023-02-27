import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []
for i in ports:
    portList.append(str(i))
    print(str(i))
PORT = "COM5"

serialInst.baudrate = 9600
serialInst.port = PORT
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        reading = packet.decode('utf')
        divided = reading.split(',')
        
        if len(divided) == 4:
            divided[3] = divided[3].replace('\r', '')
            divided[3] = divided[3].replace('\n', '')
            first = float(divided[0])
            second = float(divided[1])
            third = float(divided[2])
            fourth = float(divided[3])
            
        
