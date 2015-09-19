#for listing nepali files 
import codecs
file=codecs.open(r'C:\Users\Admin\Desktop\nepalii.txt', 'r', 'UTF-8')
nepalii = list(file.read().split())
from collections import Counter
count = Counter(nepalii)
for i,j in count.items():print i,':',j
#..............................................................
file = open('C:\Users\Admin\Desktop\english.txt', 'r')
ewords = list(file.read().split())
#print ewords
from collections import Counter
counts = Counter(ewords)
for i,j in counts.items():print i,':',j
#.........................................
