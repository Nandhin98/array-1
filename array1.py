def extrema():
            	n=int(input())
                	l=[]
              	c=0
             	for i in range(n):
	             	l.append(int(input()))
                     	if (l[i]<l[i-1] and l[i]<l[i+1] ) or (l[i]>l[i+1] and l[i]>l[i-1]):
	               		c=c+1
                        	print(c)
                try:
                	extrema()
              except:
                          	print('invalid')
