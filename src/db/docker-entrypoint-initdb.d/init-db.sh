#!/bin/bash

set -e

echo "Inserindo dados em DB"

mongo --username $MONGO_INITDB_ROOT_USERNAME --password $MONGO_INITDB_ROOT_PASSWORD mongodb://localhost:27017/test <<EOF
db.test.insert({
    value: "Bom tarde turma de GCES",
})
EOF