from bs4 import BeautifulSoup
import requests


search = input("Search for ")
params  = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

# Let's look for a order list (ol)
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]  # attrs is to look for any attribute.

    if item_text and item_href:
        print(item_text)
        print(item_href)   

        #children_item = item.children
        #for child in children_item:
        #    print("Child: {}".format(child))
        
        children_item = item.find("h2")
        print("Next sibling: {}".format(children_item.next_sibling))