import serial

arduino = serial.Serial(port='COM3',  baudrate=115200, timeout=.1)
try:
	string = arduino.readline().decode('utf-8').strip()
	print(string)
except:
	print("error")