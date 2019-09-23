import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
print("arduino serial readline ")


while True:
    #ser.readline()
    #input_data = input("enter hex code in decimal format ")
    #ser.write(input_data.encode())
    input_data = input()
    print("you entered", input_data)
    if (input_data == '1'):
        ser.write('1')
    if (input_data == '0'):
        ser.write('0') 
