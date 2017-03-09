#!/usr/bin/env python

import sys
from io import open
from datetime import datetime
from statistics import mean,stdev
from ascii_graph import Pyasciigraph

def read_speedtest(file):
  line = file.readline()
  if line == '':
    return None
  datetime_line = line.split()
  speedtest = {}
  speedtest['datetime'] = datetime.strptime(datetime_line[4] + ' ' + datetime_line[5], '%d/%m/%Y %H:%M')
  try:
    speedtest['ping'] = float(file.readline().split()[1])
    speedtest['download'] = float(file.readline().split()[1])
    speedtest['upload'] = float(file.readline().split()[1])
  except: # Catches the case where there is an issue reaching speedtest
    speedtest['ping'] = 0.0
    speedtest['download'] = 0.0
    speedtest['upload'] = 0.0
  line = file.readline()
  while '----------' not in line:
    line = file.readline()
    print line;
  return speedtest

def to_graph_input(speedtests, attr):
  "Takes speedtest list and extracts the attribute, suitable for input into Pyasciigraph"
  return map(lambda speedtest: (datetime.strftime(speedtest['datetime'], '%d/%m/%Y %H:%M'), speedtest[attr]), speedtests)

def print_stats(speedtests, attr, title, unit, outliers_greater=False):
  vals = map(lambda speedtest:speedtest[attr], speedtests)
  this_mean = mean(vals)
  this_stdev = stdev(vals)
  print 'Avg %8s: %.02f %s (+/- %.02f)' % (title, this_mean, unit, this_stdev)
  
  vals = to_graph_input(speedtests,attr)
  printed_header = False
  for val in vals:
    if (outliers_greater and val[1] > this_mean+2*this_stdev) or (not outliers_greater and val[1] < this_mean-2*this_stdev):
      if not printed_header:
        print "> Outliers:"
        printed_header = True
      print '  > %s -- %.02f %s' % (val[0], val[1], unit)
  print

def print_graph(speedtests, attr, title, unit):
  graph = Pyasciigraph(line_length=60, min_graph_length=30, graphsymbol='=', float_format='{0:,.2f} ' + unit)
  for line in graph.graph(title, to_graph_input(speedtests,attr)):
    print line
  print

def main():
  if len(sys.argv) < 2:
    sys.stderr.write("Usage: graph.py <input_file.txt>\n")
    exit(1)
  
  filename=sys.argv[1]
  speedtests=[]
  
  with open(filename,'r') as file:
    speedtest = read_speedtest(file)
    while speedtest != None:
      speedtests.append(speedtest)
      speedtest = read_speedtest(file)
  
  #speedtests = sorted(speedtests, key=lambda speedtest: speedtest['datetime'])
  
  print 'Speedtest results for period from ' + datetime.strftime(speedtests[0]['datetime'], '%d/%m/%Y %H:%M') + ' to ' + datetime.strftime(speedtests[-1]['datetime'], '%d/%m/%Y %H:%M')
  print
  print_stats(speedtests, 'ping', 'Ping', 'ms', True)
  print_stats(speedtests, 'download', 'Download', 'Mbps')
  print_stats(speedtests, 'upload', 'Upload', 'Mbps')

  print
  print_graph(speedtests, 'ping', 'Ping (ms)', 'ms')
  print_graph(speedtests, 'download', 'Download (Mbps)', 'Mbps')
  print_graph(speedtests, 'upload', 'Upload (Mbps)', 'Mbps')

# ------ main -------
main()
