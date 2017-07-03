#!/bin/bash

# top10.bash

# This script should get price history of top10.

export SCRIPT=`realpath $0`
export SCRIPTPATH=`dirname $SCRIPT`
export PATH=${SCRIPTPATH}:$PATH
export YPRICE=${SCRIPTPATH}/..
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=/dev/null # prevents chromedriver 'hang'

cd ${YPRICE}/py/
${HOME}/anaconda3/bin/python top10.py

cd     $YPRICE
date > ${YPRICE}/static/top10.bash.done.txt

exit
