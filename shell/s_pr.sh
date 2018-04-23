#!/bin/bash
echo $(docker ps -a | grep Sup- | grep Exited | awk '{print $NF}')

