from mqtt_client import client

#client.subscribe("#", qos = 0)
#client.loop_forever()





import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import ssl
from paho import mqtt
import paho.mqtt.client as mqtt_client

"""
single(topic, payload=None, qos=0, retain=False, hostname="localhost",
port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None,
protocol=mqtt.MQTTv311, transport="tcp")

multiple(msgs, hostname="localhost", port=1883, client_id="", keepalive=60,
will=None, auth=None, tls=None, protocol=mqtt.MQTTv311, transport="tcp")

import paho.mqtt.publish as publish

msgs = [{'topic':"paho/test/multiple", 'payload':"multiple 1"},
    ("paho/test/multiple", "multiple 2", 0, False)]
publish.multiple(msgs, hostname="mqtt.eclipseprojects.io")

___________________________________________________________________


simple(topics, qos=0, msg_count=1, retained=False, hostname="localhost", port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None, protocol=mqtt.MQTTv311)

    import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("paho/test/simple", hostname="mqtt.eclipseprojects.io")
print("%s %s" % (msg.topic, msg.payload))

will
a dict containing will parameters for the client:

will = {‘topic’: “<topic>”, ‘payload’:”<payload”>, ‘qos’:<qos>, ‘retain’:<retain>}.
Topic is required, all other parameters are optional and will default to None, 0 and False respectively.
Defaults to None, which indicates no will should be used.

"""

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))

#publish.callback(on_message_print, "paho/test/single", hostname="mqtt.eclipseprojects.io")

sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

auth = {'username': "pruebajara", 'password': "123498765"}
#publish.single("another", "payload", qos = 2, hostname="6cadf8dab28a4327b9ea16c3944ce5b4.s2.eu.hivemq.cloud", port=8883, client_id="", auth = auth, tls = sslSettings,)
msg = subscribe.simple("another", qos = 2, msg_count = 1, hostname="6cadf8dab28a4327b9ea16c3944ce5b4.s2.eu.hivemq.cloud", port=8883, client_id="124334rrer", auth = auth, tls = sslSettings, clean_session = False, )
#print(len(msg))
#print("%s %s" % (msg.topic, msg.payload))

subscribe.callback(on_message_print, "another", qos = 2, hostname = "6cadf8dab28a4327b9ea16c3944ce5b4.s2.eu.hivemq.cloud", port = 8883, client_id = "AndresClient", auth = auth, tls = sslSettings, protocol = mqtt_client.MQTTv311, clean_session = False,)

    

def on_publish(client, userdata, mid, properties=None):
    print("on_publish mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Suscrito: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg) -> str:
    print("Inside on on_message")
   
#publish.on_subscribe = on_subscribe
#publish.on_message = on_message
#publish.single.on_publish = on_publish


#message_callback_add(sub, callback)


