import csv
import os
import json
from pprint import pprint

os.chdir("./Annexes/fake_quotes")
files = [file for file in os.listdir() if os.path.isfile(file)]
# print(files)
author_sets = {}


def clean_and_split_quote(quote, convertype):
    return convertype(quote.replace(',', '').replace('.', '').replace('?', '').strip().split())


def create_sets_and_return_unique_set(files):
    # Cette variable créée un set global à tous les auteurs.
    global_authors_set = []
    # Cette variable créée un set global pour chaque auteur dans un dictionnaire.
    global_author_sets = {}
    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            for item in data:
                # print(item)
                global_author_sets[item["author"]] = clean_and_split_quote(item['quote'], set)
                if item["author"] in author_sets:
                    author_sets[item["author"]].extend(clean_and_split_quote(item['quote'], list))
                else:
                    author_sets[item["author"]] = clean_and_split_quote(item['quote'], list)
            global_authors_set.append(set.union(*global_author_sets.values()))
    # pprint(global_authors_set)
    return set.intersection(*global_authors_set)


def count_the_desc_by_author(word_to_count: str):
    count_for_author = {}
    for author, words in author_sets.items():
        list_of_words = list(words)
        count_for_author[author] = list_of_words.count(word_to_count)

    return dict(sorted(count_for_author.items(), key=lambda x: x[1], reverse=True))


def write_in_csv(csv_file, data_dictionnary):
    if os.path.exists(csv_file):
        os.remove(csv_file)

    with open(csv_file, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Auteur", "Nombre d'occurences du mote 'the'"])

        for author, count in data_dictionnary.items():
            writer.writerow([author, count])


unique_set = create_sets_and_return_unique_set(files)
print(unique_set)

counter = count_the_desc_by_author('the')
print(counter)

os.chdir("./..")
filename_csv_quotes_counter = './quotes_counter.csv'
write_in_csv(filename_csv_quotes_counter, counter)
