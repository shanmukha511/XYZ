#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import os
from glob import glob
from xlsxwriter.workbook import Workbook
for csvfile in glob('/tmp/workspace/bera/ayehu/automation/google-cloud-audit-automation/dev/*.csv'):
    name = os.path.basename(csvfile).split('.')[-2]
    print name
    print csvfile
    workbook = Workbook('./' + str(name) + '.xlsx',
                    {'strings_to_numbers': True,
                    'constant_memory': True})
    print "hi"
    print workbook
    worksheet = workbook.add_worksheet()
    print "bi"
    print worksheet
    print "mi"
    print csvfile
    with open(csvfile, 'r') as f:
        print csvfile
        r = csv.reader(f)
        for (row_index, row) in enumerate(r):
             for (col_index, data) in enumerate(row):
                worksheet.write(row_index, col_index, data)
                worksheet.set_column(0, col_index, 100)
        workbook.close()
