#!/bin/sh
for f in *.csv; do 
mv -- "$f" "${f%.csv}.xlsx"
done
