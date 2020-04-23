#!/bin/sh
cd tmp/workspace/bera/ayehu/automation/google-cloud-audit-automation/dev/
for f in *.csv; do 
mv -- "$f" "${f%.csv}.xlsx"
done
