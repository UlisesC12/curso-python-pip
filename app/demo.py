import csv

def read_csv(path):
 with open(path, 'r') as csvfile:
   reader = csv.reader(csvfile, delimiter=',')
   for row in reader:
      print(row)

read_csv('./app/data.csv')