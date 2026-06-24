# Learning MongoDB

MongoDb is a database server. 

1. You need to download the Database it's self
2. MongoDB default port is 27017

## What needs to be installed 
1. MonogoDB Server
```mongod```
2. Mongo shell
```mongosh```
3. PyMongo 
The python driver for python.
```
pip install pymongo
```

Installtion depends on the version of the OS


## Add MongoDB Repository

Because MongoDB is a third party software , so it is not included in the default software repositories. Manually add **MongoDB repo** to your system before installing it 

```
sudo apt update
sudo apt install gnupg curl -y

```
Import the official MonogoDB GPG key
Run this command to download and add the secure cryptographic key used by MongoDB to sign its packages

```
curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
--dearmor
```
add to **pop os jammy**

```
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/8.0 multiverse"
```
add to **ubuntu**
```
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
```

## Install MongoDB

```
sudo apt install update 
sudo apt install mongodb-org -y 
```

## Start and Endable the Service
use systenctl, it's a commandline tool used to control and manage the systemd init system and service manager .
it controls services, manages system states and check system health.

```
sudo systemctl start mongod
sudo systemctl enbale mongod 
```

verify if the data base service is running

```
sudo systemctl satus mongod 
```

To talk to your database through shell.
```
mongosh
```
