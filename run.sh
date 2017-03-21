#!/bin/bash

hdfs dfs -cat /data/assignments/ex2/part3/webLarge.txt | ./mapper.py > temp
hdfs dfs -copyFromLocal temp /user/$USER/assignment2/task6/part-00000
cat temp | head -20 > output.out
rm temp
