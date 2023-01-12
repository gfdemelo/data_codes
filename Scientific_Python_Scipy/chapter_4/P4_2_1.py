#!/usr/bin/env python

resistor={'bk':[0,1,'-'],'br':[1,10,1],'rd':[2,1e2,2],'or':[3,1e3,'-'],'yl':[4,1e4,5],'gr':[5,1e5,0.5],'bl':[6,1e6,0.25],'vi':[7,1e7,0.1],'gy':[8,1e8,0.05],'wh':[9,1e9,'-'],'au':['-','-',5],'ag':['-','-',10],'None':['-','-',20]}

def get_resistor_value(a,b,c,d):
	num=str(resistor[a][0])+str(resistor[b][0])
	return int(num)*resistor[c][1],resistor[d][2]

print(get_resistor_value('vi','yl','rd','gr'))
