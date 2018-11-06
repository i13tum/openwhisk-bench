#!/bin/bash

PREV_TOTAL=0
PREV_IDLE=0

cp /dev/null result_statistics

count=0

while [ $count -lt 360 ]
do
    ### 1. get CPU usage
    CPU=(`cat /proc/stat | grep '^cpu '`) # Get the total CPU statistics.
    unset CPU[0]                          # Discard the "cpu" prefix.
    IDLE=${CPU[4]}                        # Get the idle CPU time.

    # Calculate the total CPU time.
    TOTAL=0

    for VALUE in "${CPU[@]:0:4}"; do
      let "TOTAL=$TOTAL+$VALUE"
    done

    # Calculate the CPU usage since we last checked.
    let "DIFF_IDLE=$IDLE-$PREV_IDLE"
    let "DIFF_TOTAL=$TOTAL-$PREV_TOTAL"
    let "DIFF_USAGE=(1000*($DIFF_TOTAL-$DIFF_IDLE)/$DIFF_TOTAL+5)/10"

    # Remember the total and idle CPU times for the next check.
    PREV_TOTAL="$TOTAL"
    PREV_IDLE="$IDLE"

    ### 2. get RAM usage
    ram_use=$(free -m)
    # a. split response by new lines
    IFS=$'\n' read -rd '' -a ram_use_arr <<< "$ram_use"
    # b. remove extra spaces
    ram_use=${ram_use_arr[1]}
    ram_use=$(echo "$ram_use" | tr -s " ")
    # c. split response by spaces
    IFS=' ' read -ra ram_use_arr <<< "$ram_use"
    # d. get variables
    total_ram=${ram_use_arr[1]}
    ram_use=${ram_use_arr[2]}
    # e. create response
    ram_use=$(( 100*ram_use/total_ram ))

    echo -en "$DIFF_USAGE $ram_use\n" >> result_statistics

    count=`expr $count + 1`
    sleep 1
done