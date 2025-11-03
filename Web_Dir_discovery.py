import requests

target_url = input("[*]Enter the target URL: ")
file_name = input("[*]Enter the file name containing Directories: ")

def request(url):
  try:
    response = requests.get("http://" + url)
  except requests.exceptions.ConnectionError:
    pass

file = open(file_name, "r")
for line in file:
  dir = line.strip()
  full_url = target_url + "/" + dir
  response = request(full_url)
  if response:
    print('[*]Discovered Directory At this Path: ' + full_url)