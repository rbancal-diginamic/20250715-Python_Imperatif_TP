import csv


def calculate_passengers_average(reader):
    total_passengers = 0
    total_passengers_age = 0

    for row in reader:
        name = row.get('name', '').strip()
        age_str = row.get('age', '').strip()

        if name == '' or age_str == '':
            continue
        try:
            age = float(age_str)
        except ValueError:
            continue

        total_passengers += 1
        total_passengers_age += age

    return total_passengers_age / total_passengers


def survive_percentage_by_passengers_class(reader):
    total_passengers_class_1 = total_passengers_class_2 = total_passengers_class_3 = 0
    alive_passengers_class_1 = alive_passengers_class_2 = alive_passengers_class_3 = 0

    for row in reader:
        class_passenger = row.get('pclass', '').strip()
        name = row.get('name', '').strip()
        survived = row.get('survived', '').strip()

        if name == '' or class_passenger == '' or survived == '':
            continue
        try:
            if class_passenger == '1':
                total_passengers_class_1 += 1
                if survived == '1':
                    alive_passengers_class_1 += 1
            elif class_passenger == '2':
                total_passengers_class_2 += 1
                if survived == '1':
                    alive_passengers_class_2 += 1
            elif class_passenger == '3':
                total_passengers_class_3 += 1
                if survived == '1':
                    alive_passengers_class_3 += 1
            else:
                continue
        except ValueError:
            continue

    survived_percetange_passengers_class_1 = alive_passengers_class_1 * 100 / total_passengers_class_1
    survived_percetange_passengers_class_2 = alive_passengers_class_2 * 100 / total_passengers_class_2
    survived_percetange_passengers_class_3 = alive_passengers_class_3 * 100 / total_passengers_class_3

    return (survived_percetange_passengers_class_1, survived_percetange_passengers_class_2,
            survived_percetange_passengers_class_3)


def most_passengers_saved_by_boat(reader):
    passengers_by_boat = {}
    for row in reader:
        boat = row.get('boat', '').strip()

        if boat == '':
            continue
        try:
            if boat in passengers_by_boat.keys():
                passengers_by_boat[boat] += 1
            else:
                passengers_by_boat[boat] = 1
        except ValueError:
            continue

    return sorted(passengers_by_boat.items(), key=lambda x: x[1], reverse=True)


# Ouverture et récupération des données dans un dictionnaire transformé en liste.
with open("./Annexes/titanic_survival.csv", newline='') as csvfile:
    reader = list(csv.DictReader(csvfile))

# Execution de la première fonction
average_passengers = calculate_passengers_average(reader)
print(f"La moyenne d'âge des passagers est {round(average_passengers, 2)}")

# Exection de la deuxième fonction
survived_passengers = survive_percentage_by_passengers_class(reader)
print(f"""Le pourcentage de survie pour la première classe est de {survived_passengers[0]}
Le pourcentage de survie pour la première classe est de {survived_passengers[1]}
Le pourcentage de survie pour la première classe est de {survived_passengers[2]}""")

# Exceution de la troisième fonction
passengers_saved_by_boat = most_passengers_saved_by_boat(reader)
print(
    f"Le bateau de sauvetage ayant sauvé le plus de passagers est le bateau {passengers_saved_by_boat[0][0]} avec {passengers_saved_by_boat[0][1]} passagers sauvés.")
