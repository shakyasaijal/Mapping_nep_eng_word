import MySQLdb
conn = MySQLdb.connect (host = "localhost",user = "root", db = "pcorpora")
c = conn.cursor()
file = open('C:\Users\Admin\Desktop\english.txt', 'r')
ewords = list(file.read().split())
#print ewords
from collections import Counter
counts = Counter(ewords);
#print counts;
for i,j in counts.items():
   array= [i,j]   
   c.execute("INSERT INTO feng (eword,efrequency) VALUES('%s','%s')" % (i,j))
conn.commit()
