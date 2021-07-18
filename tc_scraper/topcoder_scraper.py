#Note the contest names are case-senstive
from bs4 import BeautifulSoup
import requests
import math
import sys
base = 'https://competitiveprogramming.info'
source = requests.get(base + '/topcoder/srm/').text

print('Enter the contest to analyse:(Note, Name is case sensitive)')
contest_name = input()

soup = BeautifulSoup(source, 'lxml')
table =  soup.find_all('tr')
for i in range(125):
	print('~',end='')
print()
for row in table:
	contest = row.find_all('td')
	
	if len(contest) == 5 and contest_name == contest[2].text:
		div1_status = (contest[3].a.text)[-1] != "*"
		div2_status = (contest[4].a.text)[-1] != "*"

		div1_link = base + contest[3].a['href']
		div2_link = base + contest[4].a['href']
		
		sourcediv1 = requests.get(div1_link).text
		soup1 = BeautifulSoup(sourcediv1, 'lxml')
		
		sourcediv2 = requests.get(div2_link).text
		soup2 = BeautifulSoup(sourcediv2, 'lxml');
		
		print(contest[2].text,end=' ') 
		print('Div1')

		ProblemSet = soup1.find_all('p')[1]
		Problems = ProblemSet.find_all('a')
		div1problemcnt = 0
		for Problem in Problems:
			print(f'{Problem.text:40}', end = ' ')
			print(Problem['href'])
			div1problemcnt += 1
		print()

		data1 = soup1.find_all('tr')
		Solvedby = [0] * div1problemcnt
		Rating = [0] * div1problemcnt
		Outoff = [0] * div1problemcnt
		
		if div1problemcnt == 0:
			div1_status = 0
		if div1_status:
			for row in data1:
				data = row.find_all('td')
				if len(data):
					for i in range(div1problemcnt):
						temp = (data[3 + i].text)
						afterrating = (data[-2].text)
						if len(temp) == 0:
							temp = 0.0
						else:
							temp = float(temp)
						if (len(afterrating) != 0):
							Outoff[i] += 1
							if temp > 0:
								Solvedby[i] += 1
								Rating[i] += int(data[-2].text)
			if len(Outoff) and Outoff[0] != 0:
				print('Solvedby(Rated Partcipants):' + " "*12, end = ' ')
				print(Solvedby)
				print('TriedBy(Rated Partcipants):' +  " "*13, end = ' ')
				print(Outoff)
				print('Expected Problem Ratings:' + " "*15, end = ' ')
				for i in range(div1problemcnt):
					if Solvedby[i]:
						Rating[i] = math.ceil(Rating[i] / Solvedby[i])
					else:
						Rating[i] = 'INF'
				print(Rating)
				print()
		else:
			print('The contest in unrated or invalid! No stats available!!')
		
		for i in range(125):
			print('-',end='')
		print()
		print(contest[2].text,end=' ') 
		print('Div2')
		ProblemSet = soup2.find_all('p')[1]
		Problems = ProblemSet.find_all('a')
		div2problemcnt = 0
		for Problem in Problems:
			print(f'{Problem.text:40}', end = ' ')
			print(Problem['href'])
			div2problemcnt += 1
		print()
		data2 = soup2.find_all('tr')
		Solvedby = [0] * div2problemcnt
		Rating = [0] * div2problemcnt
		Outoff = [0] * div2problemcnt

		if div2problemcnt == 0:
			div2_status = 0
		if div2_status:
			for row in data2:
				data = row.find_all('td')
				if len(data):
					for i in range(div1problemcnt):
						temp = (data[3 + i].text)
						afterrating = (data[-2].text)
						if len(temp) == 0:
							temp = 0.0
						else:
							temp = float(temp)
						if (len(afterrating) != 0):
							Outoff[i] += 1
							if temp > 0:
								Solvedby[i] += 1
								Rating[i] += int(data[-2].text)
			if len(Outoff) and Outoff[0] != 0:
				print('Solvedby(Rated Partcipants):' + " "*12, end = ' ')
				print(Solvedby)
				print('TriedBy(Rated Partcipants):' +  " "*13, end = ' ')
				print(Outoff)
				print('Expected Problem Ratings:' + " "*15, end = ' ')
				for i in range(div2problemcnt):
					if Solvedby[i]:
						Rating[i] = math.ceil(Rating[i] / Solvedby[i])
					else:
						Rating[i] ='INF'
				print(Rating)
				print()
		else:
			print('The contest in unrated or invalid! No stats available !!')
for i in range(125):
	print('~',end='')
print()
