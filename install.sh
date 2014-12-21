#!/bin/sh

python setupFiles/get-pip.py

pip install virtualenv

virtualenv venv_biblio

source venv_biblio/bin/activate

pip install requests

pip install xmltodict

pip install pymongo

pip install py2neo

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list

sudo apt-get update

sudo apt-get install -y mongodb-org

sudo service mongod start

setupFiles/neo4j/bin/neo4j start

