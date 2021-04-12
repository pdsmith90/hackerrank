#!/bin/bash

read A
read B
read C

if [ "$A" = "$B" ] && [ "$A" = "$C" ]; then
    echo "EQUILATERAL"
elif [ "$A" = "$B" ] || [ "$A" = "$C" ]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
