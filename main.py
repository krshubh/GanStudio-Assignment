import sys

def reduce(temp) :
	output = list()	
	while(True) :
		if len(temp) > 1:
			if int(temp[0][4]) >=  int(temp[len(temp) - 1][4]) and  temp[0][2] == 'B' and temp[len(temp) - 1][2] == 'S' :
				output.append([temp[0][0],temp[len(temp) - 1][0],str(temp[0][1]),str(temp[len(temp) - 1][4]),\
							"{:.2f}".format((float(temp[len(temp) - 1][3]) - float(temp[0][3])) * int(temp[len(temp) - 1][4])),  temp[0][2],\
							temp[len(temp) - 1][2], temp[0][3], temp[len(temp) - 1][3]])
				if int(temp[0][4]) - int(temp[len(temp) - 1][4]) == 0 :
					del temp[0]
				else :
					temp[0] = [temp[0][0],temp[0][1],temp[0][2],temp[0][3],int(temp[0][4]) - int(temp[len(temp) - 1][4])]
				del temp[len(temp) - 1]
			elif int(temp[0][4]) <  int(temp[len(temp) - 1][4]) and  temp[0][2] == 'B' and temp[len(temp) - 1][2] == 'S' :
				output.append([temp[0][0],temp[len(temp) - 1][0],str(temp[0][1]),str(temp[0][4]),\
							"{:.2f}".format((float(temp[len(temp) - 1][3]) - float(temp[0][3])) * int(temp[0][4])),  temp[0][2],\
							temp[len(temp) - 1][2], temp[0][3], temp[len(temp) - 1][3]])
				if int(temp[0][4]) - int(temp[len(temp) - 1][4]) == 0 :
					del temp[len(temp) - 1]
				else :
					temp[len(temp) - 1] = [temp[len(temp) - 1][0],temp[len(temp) - 1][1],temp[len(temp) - 1][2],temp[len(temp) - 1][3],int(temp[len(temp) - 1][4]) - int(temp[0][4])]
				del temp[0]
			elif int(temp[0][4]) >=  int(temp[len(temp) - 1][4]) and  temp[0][2] == 'S' and temp[len(temp) - 1][2] == 'B' :
				output.append([temp[0][0],temp[len(temp) - 1][0],str(temp[0][1]),str(temp[len(temp) - 1][4]),\
							"{:.2f}".format((float(temp[0][3]) - float(temp[len(temp) - 1][3])) * int(temp[len(temp) - 1][4])),  temp[0][2],\
							temp[len(temp) - 1][2], temp[0][3], temp[len(temp) - 1][3]])
				if int(temp[0][4]) - int(temp[len(temp) - 1][4]) == 0 :
					del temp[0]
				else :
					temp[0] = [temp[0][0],temp[0][1],temp[0][2],temp[0][3],int(temp[0][4]) - int(temp[len(temp) - 1][4])]
				del temp[len(temp) - 1]
			elif int(temp[0][4]) <  int(temp[len(temp) - 1][4]) and  temp[0][2] == 'S' and temp[len(temp) - 1][2] == 'B' :
				output.append([temp[0][0],temp[len(temp) - 1][0],str(temp[0][1]),str(temp[0][4]),\
							"{:.2f}".format((float(temp[0][3]) - float(temp[len(temp) - 1][3])) * int(temp[0][4])),  temp[0][2],\
							temp[len(temp) - 1][2], temp[0][3], temp[len(temp) - 1][3]])
				if int(temp[0][4]) - int(temp[len(temp) - 1][4]) == 0 :
					del temp[len(temp) - 1]
				else :
					temp[len(temp) - 1] = [temp[len(temp) - 1][0],temp[len(temp) - 1][1],temp[len(temp) - 1][2],temp[len(temp) - 1][3],int(temp[len(temp) - 1][4]) - int(temp[0][4])]
				del temp[0]
			else :
				return temp, output
		else :
			break;
	return temp, output

if __name__ == "__main__" :
	args =  sys.argv
	if len(args) > 1 :
		file = args[1]
	else :
		file = "trades.csv"
	with open(file) as f :
		d = dict()	
		output = list()
		for i,line in enumerate(f) :
			if i != 0 :
				line = line.strip('\n')
				line = line.split(',')
				if line[1] in d :
					temp = d[line[1]]
					temp.append(line)
					d[line[1]], o = reduce(temp)
					output += o
				else :
					temp = list()
					temp.append(line)
					d[line[1]] = temp
		output = sorted(output, key = lambda x: int(x[1]))
		print("OPEN_TIME,CLOSE_TIME,SYMBOL,QUANTITY,PNL,OPEN_SIDE,CLOSE_SIDE,OPEN_PRICE,CLOSE_PRICE")
		for i in output :
			print(','.join(i))
		c_s = sum([float(i[4]) for i in output])
		print("{:.2f}".format(c_s))
		
