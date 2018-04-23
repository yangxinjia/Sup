#!/bin/bash

echo $(docker ps | grep Sup- | awk '{print $NF}')
