#!/bin/bash

cd /usr/share
mkdir ypp
cd ypp
wget https://github.com/schorrm/ypp/archive/master.zip
unzip master.zip
rm master.zip
mv ypp-master/* .
rm ypp-master -r
cd /usr/bin
ln -s /usr/share/ypp/y++ y++
echo setup complete
