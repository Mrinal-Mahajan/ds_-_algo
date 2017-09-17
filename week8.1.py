#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     19-03-2017
# Copyright:   (c) DELL 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def best(i):
	if i==0:
		try:
			return ldstable[i]
		except:
			ldstable[i]=1
			return ldstable[i]
	try:
		return ldstable[i]
	except:
		maximum = 1
		for j in range(0,i):
			if l[i]%l[j]==0:
				maximum = max(maximum,best(j)+1)
		ldstable[i] = maximum
		return ldstable[i]
			
l = []
ldstable={}
while True:
    n = raw_input()
    if n=="":
        break
    l.append(int(n))
for i in range(len(l)):
	best(i)
dslen = max(list(ldstable.values()))
# for i in range(len(l)):
# 	dslen = max(dslen,ldstable[i])
if dslen==1:
	dslen =0
print dslen