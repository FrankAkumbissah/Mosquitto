import paho.mqtt.publish as publish

publish.single("paho/test/single", "boo!", hostname="localhost", port=4000)