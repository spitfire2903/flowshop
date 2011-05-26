#!/bin/bash

count=1
for file in $(ls)
do
    if [ $file = $0 ]
    then
        continue
    fi

    JOBS=`echo $file | cut -d"_" -f1`
    MACHINES=`echo $file | cut -d"_" -f2 | cut -d"." -f1`

    sed 's/^[ \t]*//' $file > f && mv f $file
    sed 's/\ \ /\ /g' $file > f && mv f $file

    for i in {1..10}
    do
        if [ $count -le 9 ]
        then
            NEW_FILE="ta00$count"
        elif [ $count -le 99 ]
        then
            NEW_FILE="ta0$count"
        else
            NEW_FILE="ta$count"
        fi

        echo "$JOBS $MACHINES" > $NEW_FILE

        awk "NR > 3" $file > f
        head -n$MACHINES f >> $NEW_FILE
        awk "NR > $MACHINES" f > $file
        sed 's///g' $NEW_FILE > f && mv f $NEW_FILE

        count=`expr $count + 1`
        echo "created $NEW_FILE"
    done
done
