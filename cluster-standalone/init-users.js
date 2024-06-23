print("Started Adding the Users Roles and Collections.");

db = db.getSiblingDB("admin");
db.createUser({
  user: "userx",
  pwd: "userx",
  roles: [
    { role: "readWrite", db: "ifoadb" },
    { role: "dbAdmin", db: "ifoadb" }
  ],
});

db = db.getSiblingDB("ifoadb");
db.createCollection("testcollection");

print("End Adding the User Roles and Collections.");