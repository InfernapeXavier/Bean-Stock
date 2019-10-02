import pandas as pd

data=pd.read_csv("Company_Health.csv")

def fetch(symbol):
	comp = symbol
	count=0
	total=0
	for count in range(0,30):
		if(data.iat[count,0]==comp):
			break

	if(float(data.iat[count,1])>=1.5 and float(data.iat[count,1])<=3.2):
		total=total+2
	if(float(data.iat[count,2])>0.0 and data.iat[count,2]<=3.0):
		total=total+1
	if(float(data.iat[count,5])>=25.0):
		total=total+1
	if(float(data.iat[count,6])>=0.3 and float(data.iat[count,6])<=0.6):
		total=total+1
	if(float(data.iat[count,7])>=0.3 and float(data.iat[count,7])<=0.6):
		total=total+2
	if(float(data.iat[count,8])>=11.0 and float(data.iat[count,8])<=14.0):
		total=total+2
	if(float(data.iat[count,9])>=1.0):
		total=total+2
	if(float(data.iat[count,10])>=13.0):
		total=total+1
	if(float(data.iat[count,11])>=5.0):
		total=total+1
	if(float(data.iat[count,12])>=14.0):
		total=total+1

	return total
	# if(total>=0 and total<3):
	# 	return  "Low"
	# elif(total>=3 and total<=5):
	# 	print("Moderate");
	# else:
	# 	print("Investable")
