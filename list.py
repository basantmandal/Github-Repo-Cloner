"""
Download Public Repositories from Github
pip install requests
You can also use the requirements.txt for Package Installation
"""

import requests
import os

username = input("Enter Github Username:")
request = requests.get('https://api.github.com/users/'+username+'/repos')
json = request.json()
for i in range(0,len(json)):
  print("\nRepository Sr.No :",i+1)
  print("Repository Name:",json[i]['name'])
  print("Cloning Repository - ", json[i]['svn_url'],"\n")
  os.system('git clone ' + json[i]['svn_url'] + '.git')
  print("Cloning Completed \n\n")