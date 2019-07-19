import paho.mqtt.client as mqtt
import time
import pyowm

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected 
        Connected = True
        
    else:
        print("Connection failed")

Connected = False

client = mqtt.Client()
client.on_connect = on_connect
client.connect("10.10.3.221", 1883, 60)
client.loop_start()

while Connected != True:
    time.sleep(0.1)

owm = pyowm.OWM("c5ee9c50723ce0c97892e4fd6ef2caef")
observation = owm.weather_at_place("Cape Coast, Ghana")
observation2 = owm.weather_at_place("Koforidua, Ghana")
w = observation.get_weather()
w2 = observation2.get_weather()

try:
    while True:
        message = input('Your message: ')
        message1 = str((message, w))
        client.publish("UCC", message1)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()