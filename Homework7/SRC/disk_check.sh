#!/bin/bash

# Порогове значення використання диска (передається як параметр)
THRESHOLD=$1

# Отримати використання кореневого розділу /
USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

# Якщо перевищено поріг — записати попередження у лог
if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "$(date): WARNING - Disk usage is ${USAGE}% (threshold ${THRESHOLD}%)" >> /var/log/disk.log
fi
