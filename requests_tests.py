import requests


params = {"#q":"pizza"}
r = requests.get('http://google.com',params=params)

# 200 means it's working.
# 300 means redirecting.
# 400 means client error (computer error).
# 500 means server error (webpage error).

print("Status {}".format(r.status_code))
print("url: {}".format(r.url))

#print("Test: {}".format(r.text))

file = open('./test_page.html','w+')
file.write(r.text)