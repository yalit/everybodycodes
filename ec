#!/bin/bash

if [[ $1 == "run" || $1 == "test" ]]; then
  PYTHONPATH=$(pwd)/.. python3 main.py ${1} ${2} ${3} ${4}
fi

