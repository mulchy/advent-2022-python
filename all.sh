#!/bin/bash
i=1
for f in *.py
do
    echo "Day $i"
    echo
    python "$f"
    echo
    ((i++))
done
