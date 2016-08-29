#!/usr/bin/env python

from io import open
from datetime import datetime
from ascii_graph import Pyasciigraph

def read_speedtest(file):
  line = file.readline()
  if line == '':
    return None
  datetime_line = line.split()
  speedtest = {}
  speedtest['datetime'] = datetime.strptime(datetime_line[4] + ' ' + datetime_line[5], '%d/%m/%Y %H:%M')
  speedtest['ping'] = float(file.readline().split()[1])
  speedtest['download'] = float(file.readline().split()[1])
  speedtest['upload'] = float(file.readline().split()[1])
  file.readline() # to consume the '----------' separator
  return speedtest

def to_graph_input(speedtests, attr):
  "Takes speedtest list and extracts the attribute, suitable for input into Pyasciigraph"
  return map(lambda speedtest: (datetime.strftime(speedtest['datetime'], '%d/%m/%Y %H:%M'), speedtest[attr]), speedtests)

def print_graph(speedtests, dict_entry, title, unit):
  graph = Pyasciigraph(line_length=60, min_graph_length=30, graphsymbol='=', float_format='{0:,.2f} ' + unit)
  for line in graph.graph(title, to_graph_input(speedtests,dict_entry)):
    print line
  print
# ------ main -------

speedtests=[]

with open('speedtest.txt','r') as file:
  speedtest = read_speedtest(file)
  while speedtest != None:
    speedtests.append(speedtest)
    speedtest = read_speedtest(file)

#speedtests = sorted(speedtests, key=lambda speedtest: speedtest['datetime'])

print 'Speedtest results for period from ' + datetime.strftime(speedtests[0]['datetime'], '%d/%m/%Y %H:%M') + ' to ' + datetime.strftime(speedtests[-1]['datetime'], '%d/%m/%Y %H:%M')
print
print

print_graph(speedtests, 'ping', 'Ping (ms)', 'ms')
print_graph(speedtests, 'download', 'Download (Mbps)', 'Mbps')
print_graph(speedtests, 'upload', 'Upload (Mbps)', 'Mbps')
