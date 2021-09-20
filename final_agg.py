# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 21:43:56 2021

@author: CompuLand
"""
import hashlib
import glob

read_files = glob.glob("*.yml")

with open("result.yml", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
  #this file finalllllllllllllll to eliminate ant duplication          
output_file_path=open(r"C:\Users\CompuLand\Downloads\translations\translations\finalllllll.yml","r")  
#output_file_path="C:\\Users\CompuLand\Downloads\translations\translations\result.yml")
input_file_path=open(r"C:\Users\CompuLand\Downloads\translations\translations\result.yml","r")  
#input_file_path ="C:\\Users\CompuLand\Downloads\translations\translations\all_yml.yml")
completed_lines_hash = set()
output_file=output_file_path
input_file=input_file_path
#output_file = open(output_file_path, "w") 

#4
for line in input_file:
  #5
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  #6
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
#7
output_file.close()