#Note the contest names are case-senstive
from bs4 import BeautifulSoup
from statistics import NormalDist
import requests
import argparse
import math
import sys


def analysis(contest_name, l, div):
	base = 'https://competitiveprogramming.info'
	source = requests.get(base + '/topcoder/srm/').text
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
			break
	if (div == 1):
		div_status = div1_status 
		div_link = div1_link
		sourcediv = sourcediv1
		soup = soup1

	else:
		div_status = div2_status 
		div_link = div2_link
		sourcediv = sourcediv2
		soup = soup2
		
	print(f'{ contest_name } ANALYSIS')
	print()

	ProblemSet = soup.find_all('p')[1]
	Problems = ProblemSet.find_all('a')
	divproblemcnt = 0
	for Problem in Problems:
		print(f'{Problem.text:40}', end = ' ')
		if l:
			print(Problem['href'])
		else:
			print()
		divproblemcnt += 1

	print()
	print('COMPUTING PROBLEM RATINGS!! WAIT A MINUTE')
	print()
	table = soup.find_all('tr')
	Solvedby = [0] * divproblemcnt
	
	
	if divproblemcnt == 0:
		div_status = 0

	AveRating = 0 
	cnt_OldCoders = 0
	Rating = []
	volatility = []
	PerfAs = []
	SolvedStatus = []
	
	if div_status:
		for row in table:
			data = row.find_all('td')
			
			if len(data):
				afterrating = data[-2].text
				
				if len(afterrating) != 0:
					st = []
					for i in range(divproblemcnt):
						score = data[3 + i].text
						if len(score) == 0:
							st.append(0)
							score = 0
						else:
							score = float(score)
							if score > 0:
								st.append(1)
							else:
								st.append(0)
					
					coder_link = base + '/topcoder/srm/history/' + data[1].text
					codersource = requests.get(coder_link).text
					codersoup = BeautifulSoup(codersource, 'lxml')
					history = codersoup.find_all('tr')
					
					isOldParticipant = -1
					for contest in history:
						contest_data = contest.find_all('td')
						
						if len(contest_data):
							if isOldParticipant == 0:
								isOldParticipant += 1
								volatility.append(int(contest_data[-4].text))
								break
							else:
								isOldParticipant += 1
					
					if isOldParticipant == 0:
						PerfAs.append(int(data[-2].text))
						Rating.append(-1)
						volatility.append(0)
					else:
						PerfAs.append(-1) #tobecalculated
						Rating.append(int(data[-3].text))
						cnt_OldCoders += 1
						AveRating += int(data[-3].text)

					SolvedStatus.append(st)
						
		n = len(Rating)

		if (n == 0):
			div_status = 0

		Outoff = [n] * divproblemcnt				
		
		if cnt_OldCoders >= 1:				
			AveRating /= cnt_OldCoders
			num1 = 0
			num2 = 0
			for i in range(n):
				if (Rating[i] != -1):
					num1 += volatility[i] ** 2
					num2 += (Rating[i] - AveRating) ** 2

			CF = math.sqrt(num1 / cnt_OldCoders + num2 / (cnt_OldCoders - 1))

			ERanks = []
			for i in range(n):
				if Rating[i] != -1:
					exp = 0.5
					for j in range(n):
						if i == j:
							continue
						if Rating[j] != -1:
							num = Rating[j] - Rating[i]
							den = 2 * ((volatility[j] ** 2) + (volatility[i] ** 2))
							den = math.sqrt(den)
							exp += 0.5 * (math.erf(num / den) + 1)
					ERanks.append(exp)
				else:
					ERanks.append(-1)

			EPerf = []
			APerf = []

			OldCoderRank = 0
			for i in range(n):
				if ERanks[i] != -1:
					OldCoderRank += 1
					if (ERanks[i] <= 5) or (OldCoderRank <= 5):
						num1 = sys.float_info.epsilon 
						num2 = sys.float_info.epsilon 
					else:
						num1 = ERanks[i] - 5
						num2 = OldCoderRank - 5
				
					EPerf.append(-1 * NormalDist().inv_cdf(num1 / cnt_OldCoders))
					APerf.append(-1 * NormalDist().inv_cdf(num2 / cnt_OldCoders))
				else:
					EPerf.append(0)
					APerf.append(0)
			

			for i in range(n):
				if ERanks[i] != -1:
					PerfAs[i] = Rating[i] + CF * (APerf[i] - EPerf[i])


		ProblemRatings = [0] * divproblemcnt
		

		for i in range(n):
			st = SolvedStatus[i]
			for j in range(len(st)):
				if st[j]:
					ProblemRatings[j] += PerfAs[i]
					Solvedby[j] += 1


		for i in range(divproblemcnt):
			if Solvedby[i] == 0:
				ProblemRatings[i] = 'INF'
			else:
				ProblemRatings[i] = math.ceil(ProblemRatings[i] / Solvedby[i])

		if div_status:
			print('Solvedby(Rated Partcipants):' + " "*12, end = ' ')
			print(Solvedby)
					
			print('TriedBy(Rated Partcipants):' +  " "*13, end = ' ')
			print(Outoff)
					
			print('Expected Problem Ratings:' + " "*15, end = ' ')
			print(ProblemRatings)
		else:
			print('The contest in unrated or invalid! No stats available !!')
	else:
		print('The contest in unrated or invalid! No stats available !!')

	for i in range(125):
		print('~',end='')
	print()
