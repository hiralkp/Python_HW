#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 12:15:11 2018

@author: hiralpatel
"""
import os
import csv

compbudget = os.path.join("Resources", "budget_data.csv")
with open(compbudget, newline="") as budget_file:
    
 budget_data = csv.reader(budget_file, delimiter=',')
 #file_header = next(budget_data)
 last_row = "Feb-2017"
 total_row = 0
 
print(f"Header : {file_header}")

 
print(f"Financial Analysis")
print(f"--------------------------------------------------")
 
for row in budget_data:
    if (last_row == row[0]):
        total_row += 1
print(total_row)
 










   





