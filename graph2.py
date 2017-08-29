import matplotlib.pyplot as plt
import numpy as np
import time 

x = np.linspace(0, 1, 20)
y = np.random.rand(1, 20)[0]


plt.ion()
fig = plt.figure()
ay = fig.add_subplot(111)
line1, = ay.plot(x, y, 'b-') 

for i in range(0,100):
    y = np.random.rand(1, 20)[0]
    line1.set_ydata(y)
    fig.canvas.draw()
    time.sleep(0.1)
