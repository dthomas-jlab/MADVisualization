# MADVisualizer 
#### by Dillon Thomas (dthomas@jlab.org) 2024


## Install MADVisualizer depencies:

### Run ./install.sh

Or if you want to install in the same directory but from a different machine like devll/accbrowse
### Run ./install -r remotemachinename
	
	What it does:

	1. A Python3.11 virtual environment will be installed
	 to ./venv.
	
	2. The venv will be activated.

	3. PyQt5, pyqtgraph, and a few other libraries will
	 installed to the venv using "pip install -r ./src/requirements.txt.
	
	4. For MADVis to work modifications had to be made to some of pyqtgraph's libraries.
	 The original libraries will be overwritten with the contents of ./src/pyqtgraphmod/.

	5. The venv will be deactivated and you are now ready to use MADVis.

## Running MADVisualizer:
	
### Run ./run.sh on opsrfdaqnl1

Or if you aren't on opsrfdaqnl1
### Run ./run.sh -r opsrfdaqnl1

	What it does:

	1. Activates the venv
	2. Launches ./src/MADVisualizer.py
	

	
