#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
	
	cleaned_data = []
	data_with_error = [] #guardar os erros
	for i,p in enumerate(predictions):
		residual_error = (p-net_worths[i])**2 #pegando o erro r2, o valor que deu menos o esperado, tudo ao quadrado
		data_with_error.append((ages[i],net_worths[i],residual_error)) #passando da forma pedida
	sorted_data_with_error= sorted(data_with_error,key=lambda x: x[2]) #ordenando a lista de lista pela 3 posicao da tupla
	cleaned_data = sorted_data_with_error[0:81] #pegando so a as 81 primeiras posicoes
	return cleaned_data

