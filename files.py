#test code to generate frequency of nepali and english words in file
import codecs

file=codecs.open(r'nepalii.txt', 'r', 'UTF-8')
nepalii = list(file.read().split())
from collections import Counter
count = Counter(nepalii)
for i,j in count.items():print i,':',j



file = open('english.txt', 'r')
ewords = list(file.read().split())
#print ewords
from collections import Counter
counts = Counter(ewords)
for i,j in counts.items():print i,':',j

