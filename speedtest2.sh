#!/bin/bash

OUTPUT=`cat speedtest.txt`
DOWNLOAD=`echo "$OUTPUT" | grep Download | sed 's/[a-zA-Z:]* \([0-9]*\.[0-9]*\) [a-zA-Z/]*/\1/'`
UPLOAD=`echo "$OUTPUT" | grep Upload | sed 's/[a-zA-Z:]* \([0-9]*\.[0-9]*\) [a-zA-Z/]*/\1/'`
#TIME=`echo "$OUTPUT" | grep at | sed 's/[a-zA-Z:]* \([0-9]*\.[0-9]*\) [a-zA-Z/]*/\1/'`

echo "$DOWNLOAD" > graph.txt
echo "$UPLOAD" > graph2.txt
#echo "up.value $UPLOAD"
