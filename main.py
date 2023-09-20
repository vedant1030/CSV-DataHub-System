import csv
import pandas as pd
import matplotlib.pyplot as plt

def generate_top_names_graph(filename):
    
    df = pd.read_csv(filename)
    top_names = df.sort_values(by='Frequency', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(top_names['First Name'], top_names['Frequency'])
    ax.set_title('Top 10 Names by Frequency')
    ax.set_xlabel('Name')
    ax.set_ylabel('Frequency')
    ax.tick_params(axis='x', labelrotation=45)
    output_filename1 = f"{filename[:-4]}_Graphs.png"
    fig.savefig(output_filename1)
  
def mostCommonNameInYear(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
          if row[2] == '2':            
            return row[0]

def frequency(filename, name):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
          if row[0] == name:
            return row[1]
    return -1 

def topTen(filename):

    count = 0;
  
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
          print(row[0])
          count += 1
          if count == 10:
            return 0      
    
def main ():

  num = 0
  
  while num != '6':
    
    print("Option 1 - Most popular name in a province/state")
    print("Option 2 - Check if a name is the most common in a year province/state")
    print("Option 3 - Check the number of people with a common name")
    print("Option 4 - Top 10 names in a province/state")
    print("Option 5 - Make a graph of the top 10 names in a province/state")
    print("Option 6 - Exit")
    
  
    num = input("Choose an option:")
    if num == '1':
      countryNum = input("Choose a province/state - 1 for Nova Scotia / 2 for California / 3 for New Brunswick:")
  
      if countryNum == '1':
        country = "formattedFilesAndGraphs/formatted_NS.csv"
      elif countryNum == '3':
        country = "formattedFilesAndGraphs/formatted_NB.csv"
      elif countryNum == '2':
        country = "formattedFilesAndGraphs/formatted_CALI.csv"
      else:
        print("improper option")
  
     
      name  = mostCommonNameInYear(country)
  
      print('The most common name is',name)
          
    elif num == '2':
      countryNum = input("Choose a province/state - 1 for Nova Scotia / 2 for California / 3 for New Brunswick:")
  
      if countryNum == '1':
        country = "formattedFilesAndGraphs/formatted_NS.csv"
      elif countryNum == '3':
        country = "formattedFilesAndGraphs/formatted_NB.csv"
      elif countryNum == '2':
        country = "formattedFilesAndGraphs/formatted_CALI.csv"
      else:
        print("improper option")
    
      name = input("Choose a name in all caps:")
    
      hName  = mostCommonNameInYear(country)
    
      if name == hName:
        print(name,'is the most common name')
      else:
        print(name,'is not the most common name')
        
    elif num == '3':
  
      countryNum = input("Choose a province/state - 1 for Nova Scotia / 2 for California / 3 for New Brunswick:")
  
      if countryNum == '1':
        country = "formattedFilesAndGraphs/formatted_NS.csv"
      elif countryNum == '3':
        country = "formattedFilesAndGraphs/formatted_NB.csv"
      elif countryNum == '2':
        country = "formattedFilesAndGraphs/formatted_CALI.csv"
      else:
        print("Improper Option!")
    
      name = input("Choose a name in all caps:")
  
      amount = frequency(country,name)
  
      if  amount != -1:
        print("There are",amount,"people named",name)
      else:
        print(name,"does not exist in the file")
      
  
    elif num == '4':
      countryNum = input("Choose a province/state - 1 for Nova Scotia / 2 for California / 3 for New Brunswick:")
  
      if countryNum == '1':
        country = "formattedFilesAndGraphs/formatted_NS.csv"
      elif countryNum == '3':
        country = "formattedFilesAndGraphs/formatted_NB.csv"
      elif countryNum == '2':
        country = "formattedFilesAndGraphs/formatted_CALI.csv"
      else:
        print("Improper Option!")
  
      topTen(country)
          
    elif num == '5':
      print("Generating graph for all States/Provinces...\n")
      generate_top_names_graph("formattedFilesAndGraphs/formatted_NB.csv")
      generate_top_names_graph("formattedFilesAndGraphs/formatted_CALI.csv")
      generate_top_names_graph("formattedFilesAndGraphs/formatted_NS.csv")
      print("Please check in /formattedFilesAndGraphs\n")

    elif num == '6':
      print("Thank you for using me, have a good day!")
    else: 
        print("Input Error!")
  
if __name__ == "__main__":
    main()