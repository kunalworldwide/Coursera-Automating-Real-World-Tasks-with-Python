#! /usr/bin/env python3

import os
import requests
import csv
import glob

path = 'data/feedback'

def final_file_list(path):
    return glob.glob(os.path.join(path, '*'))

files = final_file_list(path)
print(files)

def make_feedback_dict(list):

    for file in list:
        with open(file, 'r') as fb:
            counter = 0
            data = fb.read().split('\n')
            dict = {"title": data[0], "name": data[1], "date": data[2], "feedback": data[3]}
            dict.update({"title": data[0], "name": data[1], "date": data[2], "feedback": data[3]})
    counter += 1
    return dict

feedback_dict = make_feedback_dict(files)
print(feedback_dict)
