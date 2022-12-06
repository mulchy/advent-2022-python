#!/bin/bash
i=1
for f in *.py
do
    echo "Day $i"
    echo
    python "$f" "input/day$(printf "%02d" $i).txt"
    echo
    ((i++))
done
