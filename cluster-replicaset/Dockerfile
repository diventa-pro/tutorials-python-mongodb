FROM mongodb/mongodb-community-server:5.0.26-ubuntu2004

# Esegue i seguenti comandi come utente 'root'
USER root



# Prepara la chiave
# ==========================================

RUN mkdir -p /data/pki

# usa openssl per generare 756 byte casuali da usare come chiave
# -base64 è la codifica. 756 perché un file codificato base64 aumenta di dimensioni di circa 4/3, 
# quindi 756 byte risulteranno in un file di 1024 byte quando codificato in base64. 
# MongoDB richiede che il keyfile sia tra 6 e 1024 byte dopo la decodifica base64.
RUN openssl rand -base64 756 > /data/pki/m103-keyfile
RUN chmod 400 /data/pki/m103-keyfile

RUN chown mongodb:mongodb /data/pki/m103-keyfile



# Prepara le cartelle
# ==========================================

RUN mkdir -p /data/db/node1 /data/db/node2 /data/db/node3
RUN chmod -R 777 /data/db/node1 /data/db/node2 /data/db/node3
