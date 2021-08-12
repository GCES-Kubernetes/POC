print('Start #################################################################');

db = db.getSiblingDB('test');
db.test.insertOne({
    value: "Ola!"
})

