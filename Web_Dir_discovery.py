import requests

target_url = input("[*]Enter the target URL: ")
file_name = input("[*]Enter the file name containing Directories: ")

def request(url):
  try:
    response = requests.get("http://" + url)
  except requests.exceptions.ConnectionError:
    pass
