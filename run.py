#! /usr/bin/env python3

import requests
import os
from multiprocessing import Pool

source_path= "/data/feedback/"
key_values= ['title', 'name', 'date', 'feedback']

def sender(filename):
feedbacks_dict= {}
with open(source_path+filename, 'r') as fh:
lines = fh.readlines()
for k, v in zip(key_values, lines):
feedbacks_dict.update({k: v})
response = requests.post("http://<corpweb-external-IP>/feedback/", json=feedbacks_dict)
print(response.raise_for_status())
print(response.status_code)

Files = os.listdir(source_path)
Po = Pool(len(Files))
Po.map(sender, Files)
