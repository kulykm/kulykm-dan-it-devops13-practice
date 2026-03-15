#!/bin/bash

# Перевірка кількості аргументів
if [ $# -ne 2 ]; then
    echo "Usage: $0 source destination"
    exit 1
fi

# Перевірка чи існує файл-джерело
if [ ! -f "$1" ]; then
    echo "Error: Source file '$1' does not exist."
    exit 2
fi

# Копіювання
cp "$1" "$2"
echo "File copied from $1 to $2"
