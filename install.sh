#!/bin/bash

cd /usr/share
sudo mkdir ypp
cd ypp
sudo wget https://github.com/schorrm/ypp/archive/master.zip
sudo unzip master.zip
sudo rm master.zip
sudo mv ypp-master/* .
sudo rm ypp-master -r
cd /usr/bin
sudo ln -s /usr/share/ypp/y++ y++
echo setup complete
