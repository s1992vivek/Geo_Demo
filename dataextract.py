import random
import csv
City={}
included_cols=[1]
j=1
with open(r'/home/delhivery/Downloads/Cities/Delhi.csv', 'rb') as f:
    next(f, None)
    reader=csv.reader(f)
    for row in reader:
        City[j]=round(float(row[6]),3),round(float(row[7]),3)
        # print City[j]
        j=j+1
print len(City)
print City[2800][0], City[2800][1]
D={}

for g in range(1,len(City)+1):
	
	lat_c=City[g][0]
	long_c=City[g][1]
	F=[]
	for i in range(41):
		lat=lat_c-(i-20)*.001
		for j in range(41):
			lon=long_c-(j-20)*.001
			tup=(round(lat,3),round(lon,3))
			F.append(tup)       
	F1=[F,1681]
	D[g]=F1
checked=[]
total=len(City)*1681
print D[2400][0][1500][0]
len_city=len(City)
'''apply geocode'''

while (total>0):
	loc_rand= random.randint(1,len_city)
	if len(checked)==len_city:
		break
	if loc_rand in checked:
		continue

	if D[loc_rand][1]>1:
		grid_rand=random.randint(1,D[loc_rand][1])
	elif D[loc_rand][1]==1:
		grid_rand=1

	else:
		checked.append(loc_rand)
		del D[loc_rand]
		print 'qwertyuiopasdfghjklxcvbnm,xcvbnm,fghjk'
		continue
	# pt=D[loc_rand][0][grid_rand]
	'apply geocode on rand_lat rand_long'
	rand_lat=D[loc_rand][0][grid_rand][0]
	rand_long=D[loc_rand][0][grid_rand][1]

	del D[loc_rand][0][grid_rand]
	D[loc_rand][1]=D[loc_rand][1]-1
	total=total-1
	print total








