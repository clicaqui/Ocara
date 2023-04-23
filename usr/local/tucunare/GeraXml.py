#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
	Criado por Mayron Cachina em 14/07/2008
	Adaptado por Raquel de Souza Silva em 23/05/2011

	Gerador de arquivos XML
	
"""

import psycopg2
from string import *
from datetime import *
import os
 

try:
	conn = psycopg2.connect("\
	dbname='ocara'\
	user='ocara'\
	host='localhost'\
	password='liberdade'\
        ");
except:
	print "Erro ao conectar ao banco de dados"
	exit()

dbCursor = conn.cursor()
dbCursor.execute("SELECT * FROM public.user order by id")

resultSet = dbCursor.fetchall()

dbCursor.execute("SELECT codigo_aps FROM public.versions where id = 2")

resultSet2 = dbCursor.fetchall()

for results in resultSet2:
    codigo_aps = results[0]

codigoTelecentro = codigo_aps
dataArquivo = datetime.now()
nomeArquivo = codigoTelecentro+'-'+dataArquivo.strftime('%d-%m-%Y-%H-%M-%S')+'.xml'
arquivos = open(nomeArquivo,'w')
arquivos.write('<?xml version="1.0" encoding="utf-8"?>\n')
arquivos.write('<ocara>\n')

for results in resultSet:
	id_user = results[0]
	dataEnvio = date.today()
	dbCursor.execute("SELECT * FROM public.history a, public.user b where a.user_id=b.id and a.user_id=%d and day=%d and month=%d and year=%d order by a.id" % (id_user, dataEnvio.day, dataEnvio.month, dataEnvio.year))
	

        resultSet = dbCursor.fetchall()	
	for resultsC in resultSet:
	   arquivos.write('<usuario>\n')
	   arquivos.write('   <codigo-telecentro>%s</codigo-telecentro>\n' % codigoTelecentro)
	   id_user = resultsC[11]
	   item1 = '   <nick>'+ str(resultsC[12]) + '</nick>\n'
	   item2 = '   <nome-completo>'+ str(resultsC[13]) + '</nome-completo>\n'
	   item3 = '   <email>'+ str(resultsC[14]) + '</email>\n'
	   item4 = '   <cpf>'+ str(resultsC[16]) + '</cpf>\n'
	   estadoCivil = ""
	
	   if resultsC[18] != None:
	      dbCursor.execute("SELECT description FROM public.marital_status where id=%s order by id" % results[18])
              resultSet = dbCursor.fetchall()	
	      for resultsE in resultSet:
	          item15 = '   <estado-civil>'+ resultsE[0] + '</estado-civil>\n'
	   else:
	      item15 = '   <estado-civil>Não informado</estado-civil>\n'

	   telefone = str(resultsC[19]) 
	   item5 = '   <telefone>'+ telefone + '</telefone>\n' 

	   escolaridade = ""
	   escl = str(resultsC[21])
	   if escl != 'None':
	      if escl == 1:
	         escolaridade = 'Educacao Infantil'
	      elif escl == 2: 
	         escolaridade = 'Ensino Fundamental'
	      elif escl == 3:
	         escolaridade = 'Ensino Medio'
	      elif escl == 4:
	         escolaridade = 'Ensino Profissionalizante'
	      elif escl == 5:
	         escolaridade = 'Graduacao'
	      elif escl == 6:
	         escolaridade = 'Pos-Graduacao'
	      elif escl == 7:
	         escolaridade = 'Mestrado'
	      elif escl == 8:
	         escolaridade = 'Doutorado'
	      else:
	         escolaridade = 'Analfabeto'
	   else:
	      escolaridade = 'Não informado'	

	   item6 = '   <escolaridade>'+ escolaridade + '</escolaridade>\n'
 
	   item7 = '   <ultimo-login>'+ str(resultsC[23]) + '</ultimo-login>\n' 
	   item8 = '   <data-registro>'+ str(resultsC[26]) + '</data-registro>\n' 

	   sexo = ""
	   sex = str(resultsC[28])
	   if sex != 'None':
	      if sex == 1:
	         sexo = 'Feminino'
	      else:
	         sexo = 'Masculino'
	   else:
	      sexo = 'Não informado' 
	   item9 = '   <sexo>'+ sexo + '</sexo>\n' 
	   ocupacao = ""
	   ocup = str(resultsC[29])
	   if ocup != 'None':
	      if ocup == 1:
	         ocupacao = 'Trabalhando'
	      elif ocup == 2: 
	         ocupacao = 'Desempregado'
	      elif ocup == 3:
	         ocupacao = 'Estudante'
	      elif ocup == 4:
	         ocupacao = 'Aposentado'
	      else:
	         ocupacao = 'Inativo'
	   else:
	      ocupacao = 'Não informado'
	   item10 = '   <ocupacao>'+ ocupacao + '</ocupacao>\n' 
	   situacaoOcupacional = ""
	   situOcup = str(resultsC[30])
	   if situOcup != 'None':
	      if situOcup == 1:
	         situacaoOcupacional = 'Contratado com carteira'
	      elif situOcup == 2: 
	         situacaoOcupacional = 'Contratado sem carteira'
	      elif situOcup == 3:
	         situacaoOcupacional = 'Autonomo'
	      elif situOcup == 4:
	         situacaoOcupacional = 'Temporario (bico)'
	      elif situOcup == 5:
	         situacaoOcupacional = 'Dona(o) de casa'
	      else:
	         situacaoOcupacional = 'Negocio proprio'
	   else:
	      situacaoOcupacional = 'Não informado'
	   item11 = '   <situacao-ocupacional>'+ situacaoOcupacional + '</situacao-ocupacional>\n' 
	   tipoDeficiencia = ""
	   tipoDef = str(resultsC[31])
	   if tipoDef != 'None':
	      if tipoDef == 1:
	         tipoDeficiencia = 'Fisica'
	      elif tipoDef == 2: 
	         tipoDeficiencia = 'Auditiva'
	      elif tipoDef == 3:
	         tipoDeficiencia = 'Visual'
	      elif tipoDef == 4:
	         tipoDeficiencia = 'Mental'
	      elif tipoDef == 5:
	         tipoDeficiencia = 'Autismo'
	      else:
	         tipoDeficiencia = 'Sindrome de Down'
	   else:
	      tipoDeficiencia = 'Não informado'
	   item12 = '   <tipo-deficiencia>'+ tipoDeficiencia + '</tipo-deficiencia>\n' 
	   rendaFamiliar = ""
	   rendaFam = str(resultsC[32])
	   if rendaFam != 'None':
	      if rendaFam == 2:
	         rendaFamiliar = 'menos de 1 salario minimo'
	      elif rendaFam == 3: 
	         rendaFamiliar = 'de 1 a 2 salarios minimos'
	      elif rendaFam == 4:
	         rendaFamiliar = 'de 3 a 5 salarios minimos'
	      elif rendaFam == 5:
	         rendaFamiliar = 'de 6 a 10 salarios minimos'
	      elif rendaFam == 6:
	         rendaFamiliar = 'de 11 a 20 salarios minimos'
	      else:
	         rendaFamiliar = 'mais de 20 salarios minimos'
	   else:
	      rendaFamiliar = 'Não informado'
	   item13 = '   <renda-familiar>'+ rendaFamiliar + '</renda-familiar>\n' 
	   etnia = ""
	   etn = str(resultsC[33])
	   if etn != 'None':
	      if etn == 1:
	         etnia = 'Afrodescendente (Negra)'
	      elif etn == 2: 
	         etnia = 'Indigena'
	      elif etn == 3:
	         etnia = 'Parda'
	      elif etn == 4:
	         etnia = 'Amarela'
	      else:
	         etnia = 'Branca'
	   else:
	      etnia = 'Não informado'
	   item14 = '   <etnia>'+ etnia + '</etnia>\n' 
	
	   item16 = "   <uf>Não informado</uf>\n"
	   item17 = "   <cidade>Não informado</cidade>\n"
	   item18 = "   <bairro>Não informado</bairro>\n"
	   item19 = "   <end>Não informado</end>\n"
	   item20 = "   <cep>Não informado</cep>\n"

	   dbCursor.execute("SELECT * FROM public.address WHERE public.address.user=%d" % id_user)
	   resultSet = dbCursor.fetchall()
	   for results in resultSet:
	      if str(results[4]) != "None":
	         dbCursor.execute("SELECT sigla FROM public.state where id=%s" % str(results[5]))
	      
	         resultSet = dbCursor.fetchall()	
	         for resultsB in resultSet:
	            item16 = '   <uf>'+ str(resultsB[0]) + '</uf>\n'
	  
		
	
	      if str(results[4]) != "None":	   
	         dbCursor.execute("SELECT name FROM public.city where id_state=%s" % str(results[4]))
	      
	         resultSet = dbCursor.fetchall()	
	         for resultsA in resultSet:
	            item17 = '   <cidade>'+ str(resultsA[0]) + '</cidade>\n'
	  
		   
	      item18 = '   <bairro>'+ str(results[2]) + '</bairro>\n'
	      item19 = '   <end>'+ str(results[1]) + '</end>\n' 
	      item20 = '   <cep>'+ str(results[3]) + '</cep>\n' 

	   arquivos.write(item1)
	   arquivos.write(item2)
	   arquivos.write(item3)
	   arquivos.write(item4)
	   arquivos.write(item5)
	   arquivos.write(item6)
	   arquivos.write(item7)
	   arquivos.write(item8)
	   arquivos.write(item9)
	   arquivos.write(item10)
	   arquivos.write(item11)
	   arquivos.write(item12)
	   arquivos.write(item13)
	   arquivos.write(item14)
	   arquivos.write(item15)
	   arquivos.write(item16)
	   arquivos.write(item17)
	   arquivos.write(item18)
	   arquivos.write(item19)
	   arquivos.write(item20)

	   item21 = '   <dia>'+ str(resultsC[1]) + '</dia>\n'
	   arquivos.write(item21)
	   item22 = '   <mes>'+ str(resultsC[2]) + '</mes>\n'
	   arquivos.write(item22)
	   item23 = '   <ano>'+ str(resultsC[3]) + '</ano>\n'
	   arquivos.write(item23)
	   item24 = '   <tempo-inicial>'+ str(resultsC[8]) + '</tempo-inicial>\n' 
	   arquivos.write(item24)
	   item25 = '   <tempo-final>'+ str(resultsC[9]) + '</tempo-final>\n' 
	   arquivos.write(item25)

	   arquivos.write('</usuario>\n') 
	
	#arquivos.write('</usuario>\n')   

arquivos.write('</ocara>')
arquivos.close() 
conn.close()

os.system("curl -F  file=@"+nomeArquivo+" http://www.redetelecentro.com.br/cgi-bin/save_file.py")
os.system("rm +"nomeArquivo+".xml")

