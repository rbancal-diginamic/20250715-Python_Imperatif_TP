import json
from pprint import pprint


def create_inventory(citations: any):
    inventory = {}
    for citation in citations:
        if citation["book"] in inventory.keys():
            inventory[citation["book"]] += 1
        else:
            inventory[citation["book"]] = 1
    return sorted(inventory.items(), key=lambda x: x[1], reverse=True)

def classed_words_inventory(citations: any):
    inventory = {}
    for citation in citations:
        details_quote = citation["quote"].replace(',', '').replace('.', '').strip().split(' ')
        for word in details_quote:
            if word in inventory.keys():
                inventory[word] += 1
            else:
                inventory[word] = 1
    filtered_inventory = filter(lambda item: item[1] >= 5, sorted(inventory.items(), key=lambda x: x[1], reverse=True))
    return dict(filtered_inventory)

# read json file
with open("./Annexes/fake_quotes/edgar_allan_poe.json", "r") as json_file:
    citation_edgar = json.load(json_file)

books_inventory = create_inventory(citation_edgar)
pprint(books_inventory)

words_inventory = classed_words_inventory(citation_edgar)
print(words_inventory)