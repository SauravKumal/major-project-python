import serial

ser = serial.Serial(
    port='COM4',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0)

print("connected to: " + ser.portstr)
count=1

# ser.write("hello".encode('ascii'))
while True:
    for line in ser.read():
        print(line)
        print(str(count) + str(': ') + chr(line) )
        count = count+1

ser.close()