Lanciare Docker:

	$ docker compose up -d
	
Connettersi da Compose con la seguente stringa, come utente root:

	mongodb://root:root@localhost:27017/
	
Verificare che gli utenti siano stati creati:
	
	db.getUsers( { showCredentials: true } )	
	
https://www.mongodb.com/docs/v5.0/reference/method/db.getUsers/	

Ci si dovrebbe poter collegare con l'utente appena creato:
	
	mongodb://userx:userx@localhost:27017/