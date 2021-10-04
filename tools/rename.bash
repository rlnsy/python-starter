#!/bin/bash

old=$1
new=$2

stat=0

if [[ -z "$old" ]]; then
		echo "need old name" && stat+=1
fi

if [[ -z "$new" ]]; then
		echo "need new name" && stat+=1
fi

if [[ $stat != 0 ]]; then
		echo "error"
		exit $stat
fi

files=( "setup.py" "main.py" "__tests__.py" "tox.ini" )

for f in "${files[@]}"
do
		echo "$f"
		sed -i "" -e "s/$old/$new/" "$f"
done

mv -v "$old" "$new"
