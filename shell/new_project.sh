#!/bin/bash
id=$1
project=$2
if [ ! -d ../Sup-project/$2/ ];then
    echo "$project file not exsit"
else
    cd ../Sup-project/$2/
    /bin/bash run_image.sh config.json Sup-$1
    if [ ! $? -ne 0 ]; then
        echo "ok"
    fi
fi
#### id=$1  name=$2  sub-name=$3  port=$4
