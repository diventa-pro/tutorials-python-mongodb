#!/bin/bash

set -e
set -u
# set -x	# Uncomment for debugging


# The replica set configuration document
#
# mongo1: Primary, since we initiate the replica set on monog0
# mongo2: Secondary
# mongo3: Arbiter, since we set the 'arbiterOnly' option to true
_config=\
'
{
	"_id": "rs0",
	"members": [
		{ "_id": 0, "host": "mongo1" },
		{ "_id": 1, "host": "mongo2" },
		{ "_id": 2, "host": "mongo3", arbiterOnly: true },
	]
}
'

sleep 5;


if [[ -n "${MONGO_INITDB_ROOT_USERNAME:-}" && -n "${MONGO_INITDB_ROOT_PASSWORD:-}" ]]; then
	mongosh --quiet \
	--host mongo1 \
	-u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD \
	--authenticationDatabase admin \
	<<-EOF
		rs.initiate($_config);
	EOF
else
	mongosh --quiet \
	--host mongo1 \
	<<-EOF
		rs.initiate($_config);
	EOF
fi

exec "$@"