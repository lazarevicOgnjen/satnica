import requests
from bs4 import BeautifulSoup
import yearRI
import subjectMD



url = input('url: ')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')



rows = soup.find_all('tr')
header = soup.find('tr')
columns = len(header.find_all('td'))



clean_header = header.get_text(separator=' | ', strip=True)
h = f"| {clean_header} |\n"



subjectMD.writeToMD(f'**url: [{url}]({url})**')



year = ['year1', 'year2', 'year3', 'year4']
tableName = ['I godina', 'II godina', 'III godina', 'IV godina']
i = 0
while i < 4:
	subjectMD.appendToMD(f'\n\n\n**{tableName[i]}**\n\n')
	subjectMD.appendToMD(h)
	subjectMD.appendToMD('|')
	c = 0
	while c < columns:
		subjectMD.appendToMD(':-:|')
		c += 1
	subjectMD.appendToMD('\n')

	for subject in yearRI.year(i+1):
		for row in rows:
			clean_row = row.get_text(separator=' | ', strip=True)
			if subject in clean_row:
				s = f"| {clean_row} |\n"
				subjectMD.appendToMD(s)
				break
		
	i += 1



