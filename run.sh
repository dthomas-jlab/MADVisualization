#! /bin/bash

run () {
	source ./venv/bin/activate
	python ./src/MADVisualizer.py
}

PWD=$(pwd)

if [ "$1" = "-r" ]
then
	echo "Running MADVisualizer on remote machine"
	if [[ -n '$2' ]]
	then
		ssh $2 cd $PWD; ./run.sh
		
	else
		echo "Usage: ./run.sh -r remoteserver"
	fi
else
	run
fi
