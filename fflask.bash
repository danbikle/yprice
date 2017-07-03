#!/bin/bash

# fflask.bash

# This script should start a Flask server.
# I usually run this script on my laptop rather than heroku.

export SCRIPT=`realpath $0`
export SCRIPTPATH=`dirname $SCRIPT`
cd    $SCRIPTPATH
export FLASK_DEBUG=1
python fflask.py

exit
