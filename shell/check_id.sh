#!/bin/bash
echo $(docker ps -a | grep Sup-$1)
