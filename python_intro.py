def ciao(cosabuffa):
    print('Ciao ' + cosabuffa + '!')

cose_buffe = ['prima_cosa_buffa','un_gatto','ultima_cosa_buffa']
k=0
for cosabuffa in cose_buffe:
	ciao(cosabuffa)
	k=k+1
	if k < 3:
		print('Ecco la prossima cosa buffa:')
	else:
		print('Le cose buffe sono finite :(')


cosa_a_caso={'nome_cosa':'Roborbio', 'tipo_cosa':'cosa buffa!'}
print(cosa_a_caso['nome_cosa'])
print('Cosa è Roborbio? Naturalmente è una ' + cosa_a_caso['tipo_cosa'])