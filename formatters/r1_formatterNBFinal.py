import csv

with open('data sets/NB_Top_20_Popular_Baby_Names_1980-2018___Les_20_noms_de_b_b__populaire_au_N.-B._1980-2018.csv') as file1:
    male_frequency = {}
    female_frequency = {}

    # loop through each row of the CSV file and update the male and female counts
    for row in csv.DictReader(file1):
        year = row['Year / Année']
        sex = row['Sex / Sexe']
        name = row['Name / Nom']
        frequency = int(row['Count / Total'])
    
        if sex == 'M':
            if name in male_frequency:
                male_frequency[name] += frequency
            else:
                male_frequency[name] = frequency
        elif sex == 'F':
            if name in female_frequency:
                female_frequency[name] += frequency
            else:
                female_frequency[name] = frequency

    name_frequency = {}
    for name in male_frequency.keys() | female_frequency.keys():
        name_frequency[name] = male_frequency.get(name, 0) + female_frequency.get(name, 0)
    def get_count(item):
        return item[1]
    sorted_names = sorted(name_frequency.items(), key=get_count, reverse=True)
       
    with open('formatted files/formatted_NB.csv', 'w', newline='') as format_file:
        csv.writer(format_file).writerow(['First Name', 'Frequency', 'Rank', 'Gender'])

        rank = 1
        prev_count = None

        for name, count in sorted_names:
            # Handle ties
            if count != prev_count:
                prev_count = count
                rank = rank + 1

            if name in male_frequency:
                gender = 'M'
            elif name in female_frequency:
                gender = 'F'
            else:
                gender = 'U'

            csv.writer(format_file).writerow([name, count, rank, gender])