#...........................................................................................................................
#Connect mysql with python
import MySQLdb
import sys
conn = MySQLdb.connect( "localhost","root", "root", "pcorpora")
cursor = conn.cursor()



#get input from user
x=(raw_input('enter an english string to translate '))


#fetch frequency of english word
cursor.execute("Select eword, efrequency from feng where eword='%s'"%(x))
data = cursor.fetchall()
if len(data)>0:
    for row in data:
        eword=row[0]
        efrequency=row[1]


#Data extraction from the relationaldb
    cursor.execute("Select en_text, ne_text from relationtbl where en_text='%s'"%(x))
    datas = list(cursor.fetchall())
    for row in datas:
        rows=list(row)
        eng_word=row[0]
        nep_word=row[1]
        

#Extract frequenct of nepali words appearing with the user input word:
        cursor.execute("Select ewords, efrequency from fnep where ewords='%s'"%(nep_word))
        dataz = list(cursor.fetchall())
        for d in dataz:
            nword=d[0]
            nfreq=d[1]

            

#finding relational frequency of each words in db:
    from collections import Counter
    counts =(Counter(datas))
    for i,j in counts.items():
        cp = j*efrequency * nfreq / float(total_nep)
        print cp
        

#if data not available on database:
else:
    print 'no data available'

