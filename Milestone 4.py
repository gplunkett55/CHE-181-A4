import pyfirmata as pf
from jupyterplot import ProgressPlot
from time import sleep

#Set up arduino (only needs to be run once)
board = pf.Arduino("COM5")
it = pf.util.Iterator(board)
it.start()

#Defines the a0 pin on the arduino
a0 = board.get_pin('a:0:i')
a1 = board.get_pin('a:1:i')
a2 = board.get_pin('a:2:i')
a3 = board.get_pin('a:3:i')

#Calculates the voltage in thee a0 pin
voltage = a0.read() * 5

#Creates the plot and also records data to a .txt file
with open('temperature.txt', 'w') as f:
    pp = ProgressPlot(x_label='Time(10 seconds)',  line_names=['voltage'])
    time=0
    temperature = 0
    for i in range(1000000):
        time += 1
        voltage = a0.read() * 5
        voltage2 = a1.read() * 5
        voltage3 = a2.read() * 5
        current = (voltage-voltage2)/3806
        resistance = (voltage2/current)
        temperature = ((resistance/1000)-1)/0.00383
        pp.update(temperature)
        #Pauses for the specified amount of time (seconds) before taking a new point
        sleep(10)
        #sends data to new file
        f.write(str(time)+'\t'+str(temperature)+'\n')
    pp.finalize()
        
