#! /bin/bash


install () {

	echo ""
	echo "MADVisualizer Installation Script"
	echo "---------------------------------"
	echo ""

	echo "Installing Python3.11 virtual environment..."
	python3.11 -m venv venv
	echo "Done!"
	echo ""

	echo "Activating virtual environment..."

	source ./venv/bin/activate

	echo "Done!"

	echo ""
	echo "Installing requirements..."
	pip install -r ./src/requirements.txt

	echo ""
	echo "Installing PyQtGraph mods..."
	cp ./src/pyqtgraphmod/ScatterPlotItem.py ./venv/lib64/python3.11/site-packages/pyqtgraph/graphicsItems/
	cp ./src/pyqtgraphmod/ScatterPlotItem.py ./venv/lib/python3.11/site-packages/pyqtgraph/graphicsItems/
	echo "Done!"
	echo ""

	deactivate
	echo ""
	echo "Virtual environment deactivated"
	echo ""
	echo "-----------------------------------"
	echo "Run ./run.sh to start MadVisualizer"
	echo "Installation complete!"
	echo ""
}

PWD=$(pwd)

if [ "$1" = "-r" ]
then
	echo "Installing in same user directory from a different machine..."
	if [[ -n '$2' ]]
	then
		ssh $2 cd $PWD; ./install.sh
		
	else
		echo "Usage: ./install -r remoteserver"
	fi
else
	install
fi

