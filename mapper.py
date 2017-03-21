#!/usr/bin/python

'''
TASK 6 Reservoir sampling multiple lines

'''


import sys
import random

counts = 0
sample_lines = []
sample_count = 100

for line in sys.stdin:
	line = line.strip()
	if counts < sample_count:
		sample_lines.append(line)
	else:
		random_idx = random.randint(0, counts)
		if random_idx < sample_count:
			sample_lines[random_idx] = line
	counts += 1

for each in sample_lines:
	print(each)
