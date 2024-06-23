Avviare il cluster:

	$ docker compose up -d
	
Eseguire mongosh nella rete di Docker compose per potersi collegare al cluster

	$ docker run -it --network "mongo-net" mongo mongosh "mongodb://root:root@mongo1,mongo2,mongo3?replicaSet=rs0"
	

