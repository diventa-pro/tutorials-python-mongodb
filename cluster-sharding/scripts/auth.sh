#!/bin/bash

mongosh <<EOF
use admin;
db.createUser({user: "root", pwd: "root", roles:[{role: "root", db: "admin"}]});
exit;
EOF