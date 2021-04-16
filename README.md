# bigdata-twstreaming - Streaming de tweets usando Apache Kafka.

## Pasos para la instalación

### Clonar el repositorio

```sh
  git clone https://github.com/gabbraneiro/bigdata-twstreaming.git
```

### Configurar server

En el archivo config/server.properties se debe descomentar la siguiente línea:

#advertised.listeners=PLAINTEXT://your.host.name:9092

Y reemplazar "your.host.name" por el nombre del host en el que va a correr Kafka.

Aclaración: 
    Si utiliza windows, debe modificar la ruta de los logs. Éstas se encuentran en:
    
        config/zookeeper.properties
            Modificar:
                dataDir=/tmp/zookeeper
            Por:
                dataDir=C:/temp/zookeeper

        config/server.properties
            Modificar:
                log.dirs=/tmp/kafka-logs
            Por:
                log.dirs=C:/temp/kafka-logs

### Levantar Kafka

```sh
  ./kafka/bin/zookeeper-server-start.sh ./kafka/config/zookeeper.properties
  ./kafka/bin/kafka-server-start.sh ./kafka/config/server.properties
```

* Es necesario utilizar una consola por comando.

### Ejecutar productor

Las credenciales de de la API de Twitter se encuentran en el archivo tweet-producer/config.py. Le recomendamos que las cambie por sus propias credenciales.

En este archivo también se encuentra la configuración del server. Deberá modificar la información con la correspondiente al server en donde ejecutará Kafka.

Por último ejecutar el tweet-producer/producer.py.

### Funcionamiento del productor

    - Conexión con la API de Twitter.
    - Conexión con el server de Kafka.
    - Leer datos provenientes de la API de Twitter.
    - Enviarlos al server de Kafka por un canal previamente definido.

    Este productor lee y envía tweets cada dos segundos por una cuestión de performance.
