#!/bin/bash

cd /usr/local/share
mkdir ypp
cd ypp
wget https://github.com/schorrm/ypp/archive/master.zip
unzip master.zip
rm master.zip
mv ypp-master/* .
rm ypp-master -r
chmod +x y++
cd /usr/local/bin
ln -s /usr/share/local/ypp/y++ y++
echo setup complete
