import serial
import time

# Set up the serial connection to the Arduino Uno
ser = serial.Serial('COM3', 9600, timeout=1)  # Replace 'COM3' with your Arduino's serial port

while True:
    # Read the serial data from the Arduino Uno
    data = ser.readline().decode().strip()

    # Check if the data is a valid pulse rate reading
    if data.startswith('Pulse:'):
        # Extract the pulse rate value from the data
        pulse_rate_str = data.split(':')[1].strip()
        pulse_rate_value = pulse_rate_str.split(' ')[0]  # Extract the value before the 'BPM' unit
        pulse_rate = int(pulse_rate_value)  # Convert the value to an integer

        # Print the pulse rate in real-time
        print(f'Pulse Rate: {pulse_rate} BPM')

    # Wait for 1 second before reading the next data
    time.sleep(1)