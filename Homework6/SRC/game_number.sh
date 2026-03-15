#!/bin/bash

# Простенька гра "Вгадай число"
number=$(( RANDOM % 100 + 1 ))
tries=0
maxtries=5

echo "Вгадайте число від 1 до 100. Є $maxtries спроб."

while [ $tries -lt $maxtries ]; do
    read -p "Спроба $((tries+1)): " guess

    if ! [[ "$guess" =~ ^[0-9]+$ ]]; then
        echo "Введіть число, будь ласка."
        continue
    fi

    tries=$((tries+1))

    if [ "$guess" -eq "$number" ]; then
        echo "Вітаю! Ви вгадали!"
        exit 0
    elif [ "$guess" -gt "$number" ]; then
        echo "Занадто велике."
    else
        echo "Занадто маленьке."
    fi
done

echo "Спроби закінчились. Правильне число було $number."
exit 1
