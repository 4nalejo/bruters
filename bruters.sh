#!/bin/bash

trap ctrl_c INT
ctrl_c(){ home; }

home(){
clear
figlet bruters
echo "    by 4n.alejo"
echo
echo -e "\e[31m[1]\e[0m Facebook"
echo -e "\e[31m[2]\e[0m Instagram"
echo -e "\e[31m[0]\e[0m exit"
echo
echo -en "choose option \e[91m?\e[0m "
read opc
if [[ $opc == "1" ]];
then
cd bt-facebook
python bt-facebook.py
cd ..
home
elif [[ $opc == "2" ]];
then
cd bt-instagram
echo -en "username \e[91m?\e[0m "
read u
echo -en "worldlist \e[91m?\e[0m "
read w
python instagram.py $u $w -m 0
echo -en "enter to continue \e[91m?\e[0m "
cd .. 
home
elif [[ $opc == "0" ]];
then
exit
else
home
fi

}
home
