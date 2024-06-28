# importing Qt widgets
from PyQt5.QtWidgets import * 
import sys
 
# importing pyqtgraph as pg
import pyqtgraph as pg
 
import pandas as pd
from datetime import datetime
import numpy as np

 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("RF MAD Visualizer")
 
        # setting geometry
        self.setGeometry(100, 100, 1024, 768)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()
 
    # method for components
    def UiComponents(self):
 
        # creating a widget object
        widget = QWidget()
 
        # creating a push button object
        self.btn = QPushButton('Load/Plot Data')
        self.btn.clicked.connect(self.btnPressed)
 
        # creating a line edit widget
        self.text = QLineEdit("Ready")
 
        # creating a check box widget
        self.grid = QCheckBox("Grid")
        self.grid.toggle()
        self.grid.toggled.connect(self.gridPressed)
        
 
        # creating a plot window
        #plot = pg.plot()
        date_axis = pg.graphicsItems.DateAxisItem.DateAxisItem(orientation='bottom')
        
        self.plot = pg.PlotWidget(axisItems={'bottom':date_axis})
        self.plot.showGrid(x=True,y=True)
        
        ay = self.plot.getAxis('left')
        cavs = ['R121', 'R122', 'R123', 'R124', 'R125', 'R126', 'R127', 'R128', 'R131', 'R132', 'R133', 'R134', 'R135', 'R136', 'R137', 'R138', 'R141', 'R142', 'R143', 'R144', 'R145', 'R146', 'R147', 'R148', 'R161', 'R162', 'R163', 'R164', 'R165', 'R166', 'R167', 'R168', 'R181', 'R182', 'R183', 'R184', 'R185', 'R186', 'R187', 'R188', 'R1B1', 'R1B2', 'R1B3', 'R1B4', 'R1B5', 'R1B6', 'R1B7', 'R1B8', 'R1C1', 'R1C2', 'R1C3', 'R1C4', 'R1C5', 'R1C6', 'R1C7', 'R1C8', 'R1E1', 'R1E2', 'R1E3', 'R1E4', 'R1E5', 'R1E6', 'R1E7', 'R1E8', 'R1G1', 'R1G2', 'R1G3', 'R1G4', 'R1G5', 'R1G6', 'R1G7', 'R1G8', 'R1H1', 'R1H2', 'R1H3', 'R1H4', 'R1H5', 'R1H6', 'R1H7', 'R1H8', 'R1I1', 'R1I2', 'R1I3', 'R1I4', 'R1I5', 'R1I6', 'R1I7', 'R1I8', 'R1J1', 'R1J2', 'R1J3', 'R1J4', 'R1J5', 'R1J6', 'R1J7', 'R1J8', 'R1L1', 'R1L2', 'R1L3', 'R1L4', 'R1L5', 'R1L6', 'R1L7', 'R1L8']
        ay.setTicks([list(enumerate(cavs))])
        #tick_format = "%Y-%m-%d %H:%M:%S"
        
        #date_axis.setTicks()

        # create list for y-axis
        y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
 
        # create horizontal list i.e x-axis
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
        # create pyqt5graph bar graph item
        # with width = 0.6
        # with bar colors = green
        
        #This code uses a modified ScatterPlotItem.py
        #Either use install.py 
        #or overwrite ./lib/python3.11/site-packages/pyqtgraph/graphicsItems/ScatterPlotItem.py
        #with ./pygtgraphmods/ScatterPlotItem.py
        self.scatter = pg.ScatterPlotItem(cavs=cavs,pen=pg.mkPen(width=1, color='r'), symbol='o', hoverable=True 
           ,tip='{cavs}'.format)


        # add item to plot window
        # adding bargraph item to the plot window
        self.plot.addItem(self.scatter)

        # Creating a grid layout
        layout = QGridLayout()
 
        # setting this layout to the widget
        widget.setLayout(layout)
 
        # adding widgets in the layout in their proper positions
        # button goes in upper-left
        layout.addWidget(self.btn, 0, 3)
        
        # text edit goes in middle-left
        layout.addWidget(self.text, 3, 0)
 
        # check box widget goes in bottom-left
        layout.addWidget(self.grid, 3, 3)
 
        # plot window goes on right side, spanning 3 rows
        layout.addWidget(self.plot, 0, 0, 3, 1)
 
        # setting this widget as central widget of the main window
        self.setCentralWidget(widget)
        
    def btnPressed(self):
        print('test')
        self.scatter.clear()
        dists = []
        
        filenames = QFileDialog.getOpenFileNames(directory=path)
        if filenames:
            print(filenames[0])
        
        
            for fname in filenames[0]:
                self.text.setText('Loading '+fname)
                index,cavs,mad_dist,date_obj = get_data(fname)
                dists.append(mad_dist)
                
                self.scatter.addPoints(x=date_obj.timestamp(),y=index)
                
                #ay = self.scatter.getAxis('left')
                #ay.setTicks([[(i,cavs[i]) for i in index]])
            dists = np.array(dists).flatten()
            self.scatter.setSize(2.0*dists)
            
            self.text.setText('Done.')
        
    
    def gridPressed(self):
        if self.grid.isChecked() == True:
            self.plot.showGrid(x=True,y=True)
        else:
            self.plot.showGrid(x=False,y=False)
            
            
    
def get_data(fname):
    #path = '/cs/prohome/apps/s/smartRAT2/pro/fileio/pca_data/'
    #filename = '2024-02-19_13_18_04'
    print('filename: '+fname)
    df = pd.read_table(fname,delimiter=' ',header=2)
    
    index = df['#index'].values
    
    cavs  = [i.split('_')[-1] for i in df['filename'].values]
    
    mad_dist = df['mad_distance'].values

    date_str = fname.split('/')[-1]
    
    date_format = '%Y-%m-%d_%H_%M_%S'
    date_obj = datetime.strptime(date_str, date_format)
    
    #date_str = time.mktime(date_obj.timetuple())
    #df.close()
    
    return index,cavs,mad_dist,date_obj
 
path = '/cs/prohome/apps/s/smartRAT2/pro/fileio/pca_data/'
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())