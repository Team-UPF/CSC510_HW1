#!/bin/bash

# Find the PID of infinite.sh
pid=$(pgrep -f infinite.sh)
echo "Task 1 is running on ID $pid"

# If process is found, kill it
if [ -n "$pid" ]; then
    echo "Killing process ID $pid"
    kill $pid
else
    echo "infinite.sh not found"
fi
