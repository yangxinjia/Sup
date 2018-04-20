#!/bin/bash
echo $(docker ps -a | grep ise-face- | grep Exited | awk '{print $NF}')

