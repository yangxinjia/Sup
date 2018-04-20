#!/bin/bash

echo $(docker ps | grep ise-face | awk '{print $NF}')
