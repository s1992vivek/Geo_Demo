
'''Clubbing multiple CSV''' 
# from glob import glob

# with open('main.csv', 'a') as singleFile:
#     for csv in glob('*.csv'):
#         if csv == 'main.csv':
#             pass
#         else:
#             for line in open(csv, 'r'):
#                 singleFile.write(line)



''' phonetic search using Soundex'''
# import enchant
# import fuzzy

# d = enchant.Dict("en_US")

# phrase = ['Jack was standing nr the tree' ,
# 'they were abv everything he planned' ,
# 'Just stand opp the counter' ,
# 'Go twrds the gas station']
# soundex = fuzzy.Soundex(4)
# output = []
# for section in phrase:
#     sect = ''
#     for word in section.split():
#         if d.check(word):
#             sect += word + ' '
#         else:
#             for correct_word in d.suggest(word):
#                 if soundex(correct_word) == soundex(word):
#                     sect +=  correct_word + ' '
#     output.append(sect[:-1])

# print output





# import argparse

# # import fuzzy
# from pymongo import Connection

# print Connection.methods 

# ENCODERS = {
#     'soundex':fuzzy.Soundex(4),
#     'nysiis':fuzzy.nysiis,
#     'dmetaphone':fuzzy.DMetaphone(),
#     }

# parser = argparse.ArgumentParser(description='Search for a name in the database')
# parser.add_argument('algorithm', choices=('soundex', 'nysiis', 'dmetaphone'))
# parser.add_argument('name')
# args = parser.parse_args()

# c = Connection()
# db = c.phonetic_search

# encoded_name = ENCODERS[args.algorithm](args.name)
# query = {args.algorithm:encoded_name}

# for person in db.people.find(query):
#     print person['name']

'''
random no generator
'''
# import csv
# import random

# rows_count = 315
# cols_count = 315
# x=y=158

# matrix = [[0 for j in range(cols_count)] for i in range(rows_count)]

# lat1,lon1 = input("Lat Long(seperated with a comma): ")

  
# ncount = 0
# with open('latlong.csv', 'wb') as csvfile:
#     while (ncount < 99225):
#         a= random.randint(0,314)
#         b= random.randint(0,314)
#         if matrix[a][b]==1:
#             continue
#         else:
#             lat=lat1-(a-157)*.001
#             lon=lon1-(b-157)*.001        
#             spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#             spamwriter.writerow([lat] + [lon])
#         matrix[a][b]=1
#         ncount= sum(x.count(1) for x in matrix)
#         print ncount


import csv
import random


Delhi=[]
col_lat=6
col_long=7
included_cols=[6,7]
# city='delhi'
# path='/home/delhivery/Downloads/Cities/'+city+'.csv'
# print path


with open(r'/home/delhivery/Downloads/Cities/Delhi.csv', 'rb') as f:
    reader=csv.reader(f)
    for row in reader:
        temp_r = list(row[i] for i in included_cols)
        Delhi.append(temp_r)
        
curr_row_no=random.randint(1,len(Delhi))
print curr_row_no
lat1= float(Delhi[curr_row_no][1])
lon1= float(Delhi[curr_row_no][2])
lat1=round(lat1,3)
lon1=round(lon1,3)
print lat1,lon1

rows_count = 41
cols_count = 41
x=y=21
matrix = [[0 for j in range(cols_count)] for i in range(rows_count)]
  
ncount = 0
with open('latlong.csv', 'wb') as csvfile:
    while (ncount < 1681):
        a= random.randint(0,40)
        b= random.randint(0,40)
        if matrix[a][b]==1:
            continue
        else:
            lat=lat1-(a-20)*.001
            lon=lon1-(b-20)*.001        
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([lat] + [lon])
        matrix[a][b]=1
        ncount= sum(x.count(1) for x in matrix)