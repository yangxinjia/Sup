#!/bin/bash
x=$(docker ps -a | awk '{print $NF}' | grep Sup- )
i=1
while (( $i < 5 ))
do
    id_t=$(echo $x | awk '{print $'"$i"'}')
    id_f=${id_t##*-}
    if [[ $id_f == "" ]];then
	echo "1"
	break
    fi
    if [[ $1 == $id_f ]];then
	echo "0"
	break
    fi
    i=$(($i+1))
done
