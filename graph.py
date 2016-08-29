#!/usr/bin/env python

from glob import glob
from io import open
from datetime import datetime
from ascii_graph import Pyasciigraph

def to_graph_input(speedtests, attr):
  "Takes speedtest list and extracts the attribute, suitable for input into Pyasciigraph"
  return map(lambda speedtest: (datetime.strftime(speedtest['datetime'], '%d/%m/%Y %H:%M'), speedtest[attr]), speedtests)

# ------ main -------

filenames = glob("./*speedtest.txt")

speedtests=[]

for filename in filenames:
  with open(filename,'r') as file:
    datetime_line = file.readline().split()
    speedtest = {}
    speedtest['datetime'] = datetime.strptime(datetime_line[4] + ' ' + datetime_line[5], '%d/%m/%Y %H:%M')
    speedtest['ping'] = float(file.readline().split()[1])
    speedtest['download'] = float(file.readline().split()[1])
    speedtest['upload'] = float(file.readline().split()[1])
    speedtests.append(speedtest)

speedtests = sorted(speedtests, key=lambda speedtest: speedtest['datetime'])

graph = Pyasciigraph(float_format='{0:,.2f} ms')
for line in graph.graph('Ping (ms)', to_graph_input(speedtests,'ping')):
  print line
print

graph = Pyasciigraph(float_format='{0:,.2f} Mbps')
for line in graph.graph('Download (Mbps)', to_graph_input(speedtests,'download')):
  print line
print

for line in graph.graph('Upload (Mbps)', to_graph_input(speedtests,'upload')):
  print line
print
