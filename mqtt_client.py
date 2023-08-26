import paho.mqtt.client as pahoClient
import time
from paho import mqtt
import paho.mqtt.client as mqtt_client
import paho.mqtt.properties as properties

client = pahoClient.Client(client_id = "", userdata = None, protocol = mqtt_client.MQTTv5)
client.tls_set(tls_version = mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("pruebajara", "123498765")
connect_properties = properties.Properties(properties.PacketTypes.CONNECT)
connect_properties.SessionExpiryInterval = 5600
client.connect("6cadf8dab28a4327b9ea16c3944ce5b4.s2.eu.hivemq.cloud", 8883, keepalive = 60, clean_start = False, properties=connect_properties)

def on_connect(client, userdata, flags, rc, properties=None):
    print("on_connect CONNACK recibido, código: %s." % rc)

def on_publish(client, userdata, mid, properties=None):
    print("on_publish mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Suscrito: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print("on_message",  msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_message(client, userdata, message):
    print("Mensaje recibido =", str(message.payload.decode("utf-8")))

client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish


