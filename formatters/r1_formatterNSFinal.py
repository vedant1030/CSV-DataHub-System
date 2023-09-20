import csv

with open('data sets/NS_Top_Twenty_Baby_Names_-_1920-Current.csv') as file1:
    male_frequency = {}
    female_frequency = {}

    # loop through each row of the CSV file and update the male and female counts
    for row in csv.DictReader(file1):
        year = row['YEAR']
        sex = row['SEX']
        name = row['FIRST NAME']
        frequency = int(row['COUNT'])
    
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
       
    with open('formatted files/formatted_NS.csv', 'w', newline='') as format_file:
        csv.writer(format_file).writerow(['First Name', 'Frequency', 'Rank', 'Gender'])

        rank = 1
        prev_count = None

        for name, count in sorted_names:
          
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