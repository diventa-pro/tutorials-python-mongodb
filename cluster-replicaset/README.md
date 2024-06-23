Assicurarsi che Docker sia in funzione

Avviare il cluster:

	$ docker compose up -d
	
Eseguire mongosh nella rete di Docker compose per potersi collegare al cluster:

	$ docker run -it --network "cluster-replicaset_mongo-net" mongo mongosh "mongodb://root:root@mongo1,mongo2,mongo3?replicaSet=rs0"

Verificare lo stato del cluster, dovrebbero apparire: 
* un MASTER 
* un SECONDARY
* un ARBITRER

```javascript
rs.status();
```	

Creare una collection, inserire dei dati, verificare che siano inseriti:

```javascript
db = db.getSiblingDB('myDb');
db.createCollection('persone');
db.persone.insertMany([
	{nome: 'Mario', cognome: 'Rossi', eta: 30},
	{nome: 'Gianna', cognome: 'Bianchi', eta: 40}
]);
db.persone.find({});
```

Stopare il nodo #1:

	$ docker compose down mongo1
	
Verificare che lo stato del cluster sia cambiato, dovrebebro apparire tre nodi:
* un nodo non raggiungibile
* un PRIMARY
* un ARBITRER

```javascript
rs.status();
```

verificare che i dati siano ancora raggiungibili:

```javascript
db = db.getSiblingDB('myDb');
c = db['persone'];
c.find({});
```

Stopare il nodo #2:

	$ docker compose down mongo2

Verificare lo stato del cluster:

```javascript
rs.status();
```

La richiesta termina con un errore perchè non esiste più nessun nodo del cluster.

	rs0 [secondary] myDb> rs.status();
	Uncaught:
	MongoServerSelectionError: getaddrinfo ENOTFOUND mongo1
	Caused by:
	MongoNetworkError: getaddrinfo ENOTFOUND mongo1
	Caused by:
	Error: getaddrinfo ENOTFOUND mongo1

Riavviare i due nodi 

	$ docker compose up -d

Verificare lo stato del cluster:

```javascript
rs.status();
```	

Può capitare che i due nodi mongo1 e mongo2 abbiamo modificato il loro ruolo di primary e secondary

Verificare che i dati siano nuovamente disponibili.