import paho.mqtt.client as paho
import serial

mesg_length = {b'1': 5,
               b'2': 5}

def get_connection():
    # for windows COM#
    ser = serial.Serial('COM10', timeout = 1)
    return ser

def get_sensor(ser, sensor_byte, tries=3):
    for _ in range(tries):
        ser.write(sensor_byte)
        data = ser.read(mesg_length[sensor_byte]).decode().strip()
        if data =='':
            print('No data, something wrong')
        else:
            break
        return data

ser = get_connection

client = paho.Client('client-isu-002')
client.connect("broker.hivemq.com")

if ser: 
    client.loop_start()
    
for i in range(10):
    sensor_data = get_sensor(ser, b'1')
    if sensor_data:
        client.publish('arduino/data', sensor_data, qos=1)

ser.close()
client.loop_stop()
