Avviare docker:

    docker compose up -d

Eseguire

    docker-compose exec shard01-a bash "/scripts/init-shard01.sh"
    docker-compose exec shard02-a bash "/scripts/init-shard02.sh"    

```bash
docker-compose exec router01 sh -c "mongosh < /scripts/init-router.sh"
```    

```bash
docker-compose exec configsvr01 bash "/scripts/auth.sh"

docker-compose exec shard01-a bash "/scripts/auth.sh"
docker-compose exec shard02-a bash "/scripts/auth.sh"
```

```bash
docker-compose exec router01 mongosh --port 27017 -u "root" --authenticationDatabase admin
```
pwd: root

```
// Enable sharding for database `MyDatabase`
sh.enableSharding("MyDatabase")

// Setup shardingKey for collection `MyCollection`**
db.adminCommand( { shardCollection: "MyDatabase.MyCollection", key: { oemNumber: "hashed", zipCode: 1, supplierId: 1 } } )

```

verifica:
```
docker exec -it router-01 bash -c "echo 'sh.status()' | mongosh --port 27017 -u 'root' -p 'root' --authenticationDatabase admin"
```

collegarsi con Compass e creare alcuni documenti:

```
use MyDatabase

db.MyCollection.insertMany([
{ oemNumber: "AAAAAAA", zipCode: 11111, supplierId: "02e1e275-6aa4-43ff-bfb3-39c48ac918b0" },
{ oemNumber: "BBBBBBB", zipCode: 22222, supplierId: "5f55b8b3-43b2-4e02-a1b6-49a12eefc845" },
{ oemNumber: "CCCCCCC", zipCode: 33333, supplierId: "916e2fa8-74a8-40fa-a034-8497278031c3" },
{ oemNumber: "DDDDDDD", zipCode: 44444, supplierId: "70ffe46d-91cd-4552-812c-6c3395d52fcd" },
{ oemNumber: "EEEEEEE", zipCode: 11111, supplierId: "695d786c-3254-477d-a9af-9b628cec51e5" },
{ oemNumber: "AAAAAAA", zipCode: 11111, supplierId: "a589e2e1-6206-43a4-a948-617f3e26524d" }
]);
```