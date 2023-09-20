import sys
import pandas as pd
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print("Usage: python script.py <filename.csv>")
    sys.exit(1)

filename = sys.argv[1]

df = pd.read_csv(filename)

top_names = df.sort_values(by='Frequency', ascending=False).head(10)

plt.bar(top_names['First Name'], top_names['Frequency'])
plt.title('Top 10 Names by Frequency')
plt.xlabel('Name')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
output_filename = f"{filename[:-4]}topNamesGraphs.png"
plt.savefig(output_filename)