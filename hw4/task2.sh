#!/bin/bash

# List files containing 'sample' and at least 3 occurrences of 'CSC510', sort by occurrences and file size, and rename files

grep -rl "sample" ./dataset1/ | xargs grep -o "CSC510" | uniq -c | awk '$1 >= 3' | sort -k1,1nr -k5,5nr | sed 's/file_/filtered_/g'
