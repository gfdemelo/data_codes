#!/usr/bin/env python3

import time

x = float(time.time())

minutos=(x/60)
horas=(minutos/60)
dias=(horas/24)
anos=dias/365.25
#print('Desde 1970 foram', minutos,'minutos,', horas, 'horas e', dias, 'dias.') 
n = 1970
mes1=mes3=mes5=mes7=mes8=mes10=mes12=31
mes4=mes6=mes9=mes11=30



for i in range(int(anos+1)):	
	if dias<365 and n%4 == 0 and n%100 !=0:
		mes2=29
		if dias < mes1 and dias > 0:
			print('Estamos no mês de Janeiro e o dia é: ', int(dias))
		dias=dias-mes1
		if dias<mes2 and dias > 0:                                               		
			print('Estamos no mês de Fevereiro e o dia é: ', int(dias))
		dias=dias-mes2
		if dias<mes3 and dias > 0:
			print('Estamos no mês de Março e o dia é: ', int(dias))
			hora=(mes3+dias)-int(mes3+dias)
			hour=hora*24
			minuto=(hour-3)-int(hour-3)
			second=(minuto*60)-int(minuto*60)
			segundos=second*60
			print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
		dias=dias-mes3
		if dias<mes4 and dias>0:
                	print('Estamos no mês de Abril e o dia é: ', int(dias))
                	hora=(mes4+dias)-int(mes4+dias)
                	hour=hora*24
                	minuto=(hour-3)-int(hour-3)
                	second=(minuto*60)-int(minuto*60)
                	segundos=second*60
                	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
		dias=dias-mes4
		if dias<mes5 and dias > 0:
                	print('Estamos no mês de Maio e o dia é: ', int(dias))
                	hora=(mes5+dias)-int(mes5+dias)
                	hour=hora*24
                	minuto=(hour-3)-int(hour-3)
                	second=(minuto*60)-int(minuto*60)
                	segundos=second*60
                	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
		dias=dias-mes5
		if dias<mes6 and dias > 0:
                	print('Estamos no mês de Junho e o dia é: ', int(dias))
                	hora=(mes6+dias)-int(mes6+dias)
                	hour=hora*24
                	minuto=(hour-3)-int(hour-3)
                	second=(minuto*60)-int(minuto*60)
                	segundos=second*60
                	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
		dias=dias-mes6
		if dias<mes7 and dias > 0:
                	print('Estamos no mês de Julho e o dia é: ', int(dias))
                	hora=(mes7+dias)-int(mes7+dias)
                	hour=hora*24
                	minuto=(hour-3)-int(hour-3)
                	second=(minuto*60)-int(minuto*60)
                	segundos=second*60
                	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
		dias=dias-mes7
		if dias<mes8 and dias > 0:
                	print('Estamos no mês de Agosto e o dia é: ', int(dias))
                	hora=(mes8+dias)-int(mes8+dias)
                	hour=hora*24
                	minuto=(hour-3)-int(hour-3)
                	second=(minuto*60)-int(minuto*60)
                	segundos=second*60
                	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
		dias=dias-mes8
		if dias<mes9 and dias > 0:
                	print('Estamos no mês de Setembro e o dia é: ', int(dias))
                	hora=(mes9+dias)-int(mes9+dias)
                	hour=hora*24
                	minuto=(hour-3)-int(hour-3)
                	second=(minuto*60)-int(minuto*60)
                	segundos=second*60
                	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
		dias=dias-mes9
		if dias<mes10 and dias > 0:
                	print('Estamos no mês de Outubro e o dia é: ', int(dias))
                	hora=(mes10+dias)-int(mes10+dias)
                	hour=hora*24
                	minuto=(hour-3)-int(hour-3)
                	second=(minuto*60)-int(minuto*60)
                	segundos=second*60
                	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
		dias=dias-mes10
		if dias<mes11 and dias > 0:
                	print('estamos no mês de novembro e o dia é: ', int(dias))
                	hora=(mes11+dias)-int(mes11+dias)
                	hour=hora*24
                	minuto=(hour-3)-int(hour-3)
                	second=(minuto*60)-int(minuto*60)
                	segundos=second*60
                	print('a hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
		dias=dias-mes11
		if dias<mes12 and dias > 0:
                	print('Estamos no mês de Dezembro e o dia é: ', int(dias))
                	hora=(mes12+dias)-int(mes12+dias)
                	hour=hora*24
                	minuto=(hour-3)-int(hour-3)
                	second=(minuto*60)-int(minuto*60)
                	segundos=second*60
                	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
		dias=dias-mes12
	elif dias < 365:
                	mes2=28
                	if dias < mes1:
                		print('Estamos no mês de Janeiro e o dia é: ', int(dias))
                	dias=dias-mes1
                	if dias<mes2:                                               		
                		print('Estamos no mês de Fevereiro e o dia é: ', int(dias))
                	dias=dias-mes2
                	if dias<mes3:
                		print('Estamos no mês de Março e o dia é: ', int(dias))
                		hora=(mes3+dias)-int(mes3+dias)
                		hour=hora*24
                		minuto=(hour-3)-int(hour-3)
                		second=(minuto*60)-int(minuto*60)
                		segundos=second*60
                		print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
                	dias=dias-mes3
                	if dias<mes4 and dias>0:
                        	print('Estamos no mês de Abril e o dia é: ', int(dias))
                        	hora=(mes4+dias)-int(mes4+dias)
                        	hour=hora*24
                        	minuto=(hour-3)-int(hour-3)
                        	second=(minuto*60)-int(minuto*60)
                        	segundos=second*60
                        	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
                	dias=dias-mes4
                	if dias<mes5 and dias > 0:
                        	print('Estamos no mês de Maio e o dia é: ', int(mes5+dias))
                        	hora=(mes5+dias)-int(mes5+dias)
                        	hour=hora*24
                        	minuto=(hour-3)-int(hour-3)
                        	second=(minuto*60)-int(minuto*60)
                        	segundos=second*60
                        	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
                	dias=dias-mes5
                	if dias<mes6 and dias > 0:
                        	print('Estamos no mês de Junho e o dia é: ', int(dias))
                        	hora=(mes6+dias)-int(mes6+dias)
                        	hour=hora*24
                        	minuto=(hour-3)-int(hour-3)
                        	second=(minuto*60)-int(minuto*60)
                        	segundos=second*60
                        	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
                	dias=dias-mes6
                	if dias<mes7 and dias > 0:
                        	print('Estamos no mês de Julho e o dia é: ', int(dias))
                        	hora=(mes7+dias)-int(mes7+dias)
                        	hour=hora*24
                        	minuto=(hour-3)-int(hour-3)
                        	second=(minuto*60)-int(minuto*60)
                        	segundos=second*60
                        	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
                	dias=dias-mes7
                	if dias<mes8 and dias > 0:
                        	print('Estamos no mês de Agosto e o dia é: ', int(dias))
                        	hora=(mes8+dias)-int(mes8+dias)
                        	hour=hora*24
                        	minuto=(hour-3)-int(hour-3)
                        	second=(minuto*60)-int(minuto*60)
                        	segundos=second*60
                        	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
                	dias=dias-mes8
                	if dias<mes9 and dias > 0:
                        	print('Estamos no mês de Setembro e o dia é: ', int(dias))
                        	hora=(mes9+dias)-int(mes9+dias)
                        	hour=hora*24
                        	minuto=(hour-3)-int(hour-3)
                        	second=(minuto*60)-int(minuto*60)
                        	segundos=second*60
                        	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
                	dias=dias-mes9
                	if dias<mes10 and dias > 0:
                        	print('Estamos no mês de Outubro e o dia é: ', int(dias))
                        	hora=(mes10+dias)-int(mes10+dias)
                        	hour=hora*24
                        	minuto=(hour-3)-int(hour-3)
                        	second=(minuto*60)-int(minuto*60)
                        	segundos=second*60
                        	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
                	dias=dias-mes10
                	if dias<mes11 and dias > 0:
                        	print('estamos no mês de novembro e o dia é: ', int(dias))
                        	hora=(mes11+dias)-int(mes11+dias)
                        	hour=hora*24
                        	minuto=(hour-3)-int(hour-3)
                        	second=(minuto*60)-int(minuto*60)
                        	segundos=second*60
                        	print('a hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
                	dias=dias-mes11
                	if dias<mes12 and dias > 0:
                        	print('Estamos no mês de Dezembro e o dia é: ', int(dias))
                        	hora=(mes12+dias)-int(mes12+dias)
                        	hour=hora*24
                        	minuto=(hour-3)-int(hour-3)
                        	second=(minuto*60)-int(minuto*60)
                        	segundos=second*60
                        	print('A hora é', int(hour-3), 'horas', int(minuto*60), 'minutos e', int(segundos), 'segundos')
                	dias=dias-mes12



	if n%4 == 0 and n%100 != 0:# and n%400 == 0:
		year=366
		dias=dias-year
#		print(dias, n)
	else:
		year2=365
		dias=dias-year2	
#		print(dias, n)
	
	
			
	n=n+1
		
print('O ano atual é: ', int(n-1))


