#!/bin/bash

cp ./depp_completo-temp/depp_completo-temp_1_1.arp ./
python missin_2.py
mv -f new_file.txt ./depp_completo-temp/depp_completo-temp_1_1.arp 
echo "2.5% of missing data added!"
