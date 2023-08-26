import mqtt_client


try:
    while(input("Otro topico y/n: ") == "y"):
        mqtt_client.client.publish("verificacion", "Mensaje 1112 4" , 2)
        mqtt_client.client.publish("verificacion", "Mensaje 11224 " , 2)
        mqtt_client.client.publish("verificacion", "Mensaje 11324 " , 2)
        mqtt_client.client.publish("another", "Mensaje 11424 " , 2)
        mqtt_client.client.publish("another", "Mensaje 11524 " , 2)
        mqtt_client.client.publish("another", "Mensaje 11624 " , 2)
        mqtt_client.client.publish("another", "Mensaje 11724 " , 2)
        mqtt_client.client.publish("prueba", "Mensaje 11824 " , 2)
        mqtt_client.client.publish("prueba", "Mensaje 11924 " , 2)
except Exception as ex:
    print("Se ha generado un error intentando conectar", ex)

