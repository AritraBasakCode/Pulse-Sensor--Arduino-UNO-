import serial

ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the correct serial port
while True:
    try:
        data = ser.readline().decode().strip()
        if data.startswith("Heart Rate"):
            print(data)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")
ser.close()
