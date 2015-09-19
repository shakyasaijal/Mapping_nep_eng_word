#This code counts the frequency of words in the file and update it in the database table.
import MySQLdb
conn = MySQLdb.connect (host = "localhost",user = "root", db = "pcorpora")
c = conn.cursor()
file = open('neplii.txt', 'r')
eword = list(file.read().split())
#print ewords
from collections import Counter
counts = Counter(eword);
print counts;
"""for i,j in counts.items():
   array= [i,j]   
   c.execute("INSERT INTO fnep (ewords,efrequency) VALUES('%s','%s')" % (i,j))
conn.commit()"""
