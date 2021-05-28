import csv
f = csv.reader(open('/home/zohaib/Downloads/Document5.csv','r'))
writer = csv.writer(open('outfile.csv','wb'))
emails = set()
from collections import Counter
emails=Counter()
for row in f:
    emails+=Counter([row[0]])
print(emails)