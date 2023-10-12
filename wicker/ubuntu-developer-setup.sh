#!/bin/bash
CURRENT_DIR=$(pwd)
echo $CURRENT_DIR

echo "=============================================="
echo "Starting dependency installation"
echo "=============================================="

#update repo manager
sudo apt update -y
sudo apt upgrade -y

#get standard development tools
sudo apt install build-essential libtool autoconf git unzip wget -y
sudo apt install clang clang-tidy clang-format lcov -y
sudo apt install doxygen -y

echo "=============================================="
echo "Build catch2 from source"
echo "=============================================="
cd /tmp
git clone https://github.com/catchorg/Catch2.git
cd Catch2
cmake -Bbuild -H. -DBUILD_TESTING=OFF
sudo cmake --build build/ --target install
cd $CURRENT_DIR

echo "=============================================="
echo "Insallation complete"
echo "=============================================="



