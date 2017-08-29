#!/usr/bin/python
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import subprocess
import shlex

subprocess.call(shlex.split('/home/pi/speedtest-cron/speedtest2.sh'))

#fig = plt.figure()
x = 0
with open('graph.txt') as f:
    lines = f.readlines()
    y = [line.split()[0] for line in lines]
    #x = [x++1 for line in lines]

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Speed Test")
ax1.plot(y, c='r', label='Speed')
leg = ax1.legend()
fig.set_size_inches(3, 2)
fig.savefig('temp.png', dpi=88)

subprocess.call(shlex.split('/home/pi/speedtest-cron/ImageDemo.py temp.png'))
