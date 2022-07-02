# List of all of the champions
allChampList = [ 
	'Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia',
	'Annie', 'Aphelios', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Bel\'Veth',
	'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', 'Cho\'Gath',
	'Corki', 'Darius', 'Diana', 'Dr. Mundo', 'Draven', 'Ekko', 'Elise',
	'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank',
	'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger',
	'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce',
	'Jhin', 'Jinx', 'Kai\'Sa', 'Kalista', 'Karma', 'Karthus', 'Kassadin',
	'Katarina', 'Kayle', 'Kayn', 'Kennen', 'Kha\'Zix', 'Kindred', 'Kled', 
	'Kog\'Maw', 'LeBlanc', 'Lee Sin', 'Leona', 'Lillia', 'Lissandra', 'Lucian', 
	'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi', 'Miss Fortune', 
	'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 
	'Nocturne', 'Nunu & Willump', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 
	'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', 'Rek\'Sai', 'Rell', 
	'Renata Glasc', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 
	'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 
	'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 
	'Sylas', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 
	'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 
	'Urgot', 'Varus', 'Vayne', 'Veigar', 'Vel\'Koz', 'Vex', 'Vi', 
	'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 
	'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 
	'Zac', 'Zed', 'Zeri', 'Ziggs', 'Zilean', 'Zoe', 'Zyra'
]

# List of champions that count for each challenge
challengeLists = {
	'aoe' : [
		'Amumu', 'Annie', 'Aurelion Sol', 'Azir', 'Bard', 'Bel\'Veth', 'Blitzcrank',
		'Braum', 'Cassiopeia', 'Corki', 'Diana', 'Draven', 'Ekko', 'Ezreal',
		'Fiddlesticks', 'Fizz', 'Galio', 'Gangplank', 'Gnar', 'Gragas', 'Graves',
		'Hecarim', 'Heimerdinger', 'Illaoi', 'Janna', 'Jarvan IV', 'Jinx', 'Karthus',
		'Katarina', 'Kayle', 'Kennen', 'Leona', 'Lissandra', 'Lux', 'Malphite',
		'Maokai', 'Miss Fortune', 'Morgana', 'Nami', 'Neeko', 'Nunu & Willump', 'Orianna',
		'Ornn', 'Pantheon', 'Qiyana', 'Rakan', 'Rammus', 'Rell', 'Renata Glasc',
		'Riven', 'Rumble', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett',
		'Sona', 'Swain', 'Talon', 'Twitch', 'Vel\'Koz', 'Viktor', 'Vladimir',
		'Volibear', 'Xayah', 'Xin Zhao', 'Yone', 'Yuumi', 'Zac', 'Ziggs',
		'Zyra'
	],

	'heal' : [
		'Alistar', 'Annie', 'Bard', 'Fiora', 'Galio', 'Ivern', 'Janna',
		'Karma', 'Kayle', 'Kindred', 'Lee Sin', 'Lulu', 'Lux', 'Morgana',
		'Nami', 'Nidalee', 'Orianna', 'Rakan', 'Rell', 'Renata Glasc', 'Senna',
		'Seraphine', 'Shen', 'Sona', 'Soraka', 'Tahm Kench', 'Taric', 'Thresh',
		'Yuumi', 'Zilean'
	],

	'poke' : [
		'Akshan', 'Ashe', 'Azir', 'Caitlyn', 'Cho\'Gath', 'Corki', 'Dr. Mundo',
		'Ezreal', 'Gangplank', 'Jayce', 'Jhin', 'Jinx', 'Kai\'Sa', 'Karma',
		'Kled', 'Kog\'Maw', 'Lux', 'Maokai', 'Nidalee', 'Pantheon', 'Senna',
		'Seraphine', 'Shyvana', 'Sivir', 'Taliyah', 'Twisted Fate', 'Varus', 'Vel\'Koz',
		'Vex', 'Viktor', 'Xayah', 'Xerath', 'Yuumi', 'Ziggs', 'Zoe'
	],

	'displacement' : [
		'Alistar', 'Aurelion Sol', 'Azir', 'Blitzcrank', 'Darius', 'Gnar', 'Gragas',
		'Hecarim', 'Janna', 'Jayce', 'Kled', 'Lee Sin', 'Maokai', 'Mordekaiser',
		'Nautilus', 'Orianna', 'Poppy', 'Pyke', 'Rell', 'Sett', 'Singed',
		'Skarner', 'Swain', 'Tahm Kench', 'Taliyah', 'Thresh', 'Tristana', 'Urgot',
		'Vayne', 'Xin Zhao', 'Yone', 'Zac', 'Ziggs'
	],

	'globals' : [
		'Akshan', 'Ashe', 'Bard', 'Caitlyn', 'Draven', 'Ezreal', 'Galio',
		'Gangplank', 'Jhin', 'Jinx', 'Kai\'Sa', 'Karthus', 'Kled', 'Lillia',
		'Lux', 'Maokai', 'Nocturne', 'Pantheon', 'Ryze', 'Senna', 'Shen',
		'Sion', 'Soraka', 'Swain', 'Taliyah', 'Twisted Fate', 'Vex', 'Xerath',
		'Ziggs'
	],

	'revive' : [
		'Akshan', 'Alistar', 'Anivia', 'Bard', 'Bel\'Veth', 'Braum', 'Ekko', 
		'Elise', 'Evelynn', 'Fiora', 'Fizz', 'Gwen', 'Jax', 'Kalista', 
		'Karthus', 'Kayle', 'Kayn', 'Kindred', 'Kled', 'Kog\'Maw', 'Lissandra', 
		'Malzahar', 'Maokai', 'Master Yi', 'Olaf', 'Pantheon', 'Rakan', 'Renata Glasc', 
		'Sion', 'Tahm Kench', 'Taric', 'Tryndamere', 'Vladimir', 'Xin Zhao', 'Yuumi', 
		'Zac', 'Zed', 'Zilean'
	],

	'immobilizing' : [
		'Aatrox', 'Alistar', 'Amumu', 'Anivia', 'Aurelion Sol', 'Bard', 'Blitzcrank', 
		'Braum', 'Camille', 'Galio', 'Gnar', 'Gragas', 'Hecarim', 'Ivern',
		'Janna', 'Jarvan IV'
	],

	'stealth' : [
		'Akali', 'Akshan', 'Evelynn', 'Kai\'Sa', 'Kha\'Zix', 'LeBlanc', 'Neeko', 
		'Nocturne', 'Pyke', 'Qiyana', 'Rengar', 'Senna', 'Shaco', 'Talon', 
		'Teemo', 'Twitch', 'Vayne', 'Viego'
	],

	'summon' : [
		'Annie', 'Azir', 'Elise', 'Fiddlesticks', 'Heimerdinger', 'Illaoi', 'Ivern',
		'Kalista', 'Kindred', 'Lissandra', 'Malzahar', 'Maokai', 'Neeko', 'Orianna',
		'Shaco', 'Yorick', 'Zed', 'Zyra'
	],

	'trap' : [
		'Caitlyn', 'Gangplank', 'Jhin', 'Jinx', 'Maokai', 'Nidalee', 'Shaco', 
		'Teemo', 'Ziggs', 'Zyra'
	],

	'terrain' : [
		'Anivia', 'Azir', 'Irelia', 'Ivern', 'Jarvan IV', 'Ornn', 'Taliyah', 
		'Trundle', 'Veigar', 'Yorick'
	],

	'shurima' : [
		'Akshan', 'Amumu', 'Azir', 'Nasus', 'Rammus', 'Renekton', 'Sivir',
		'Skarner', 'Taliyah', 'Xerath', 'Zilean'
	],

	'ionia' : [
		'Ahri', 'Akali', 'Irelia', 'Ivern', 'Jhin', 'Karma', 'Kayn',
		'Kennen', 'Lee Sin', 'Lillia', 'Master Yi', 'Rakan', 'Sett', 'Shen',
		'Syndra', 'Varus', 'Wukong', 'Xayah', 'Yasuo', 'Yone', 'Zed'
	],

	'bandle' : [
		'Corki', 'Fizz', 'Gnar', 'Heimerdinger', 'Kennen', 'Kled', 'Lulu',
		'Poppy', 'Rumble', 'Teemo', 'Tristana', 'Veigar', 'Vex', 'Yuumi',
		'Ziggs'
	],

	'bilgewater' : [
		'Fizz', 'Gangplank', 'Graves', 'Illaoi', 'Miss Fortune', 'Nautilus', 'Pyke', 
		'Tahm Kench', 'Twisted Fate'
	],

	'demacia' : [
		'Fiora', 'Galio', 'Garen', 'Jarvan IV', 'Kayle', 'Lucian', 'Lux',
		'Morgana', 'Poppy', 'Quinn', 'Shyvana', 'Sona', 'Sylas', 'Vayne',
		'Xin Zhao'
	],

	'freljord' : [
		'Anivia', 'Ashe', 'Braum', 'Gnar', 'Gragas', 'Lissandra', 'Nunu & Willump',
		'Olaf', 'Ornn', 'Sejuani', 'Trundle', 'Tryndamere', 'Udyr', 'Volibear'
	],

	'ixtal' : [
		'Malphite', 'Neeko', 'Nidalee', 'Qiyana', 'Rengar', 'Zyra'
	],

	'noxus' : [
		'Cassiopeia', 'Darius', 'Draven', 'Katarina', 'Kled', 'LeBlanc', 'Rell',
		'Riven', 'Samira', 'Sion', 'Swain', 'Talon', 'Vladimir'
	],

	'piltover' : [
		'Caitlyn', 'Camille', 'Corki', 'Ezreal', 'Heimerdinger', 'Jayce', 'Orianna',
		'Seraphine', 'Vi'
	],

	'shadowIsles' : [
		'Elise', 'Evelynn', 'Fiddlesticks', 'Gwen', 'Hecarim', 'Kalista', 'Karthus', 
		'Maokai', 'Senna', 'Thresh', 'Viego', 'Yorick'
	],

	'targon' : [
		'Aphelios', 'Aurelion Sol', 'Diana', 'Leona', 'Pantheon', 'Soraka', 'Taric', 
		'Zoe'
	],

	'void' : [
		'Bel\'Veth', 'Cho\'Gath', 'Kai\'Sa', 'Kassadin', 'Kha\'Zix', 'Kog\'Maw', 'Malzahar', 
		'Rek\'Sai', 'Vel\'Koz'
	],

	'zaun' : [
		'Blitzcrank', 'Dr. Mundo', 'Ekko', 'Janna', 'Jinx', 'Renata Glasc', 'Singed', 
		'Twitch', 'Urgot', 'Viktor', 'Warwick', 'Zac', 'Zeri', 'Ziggs'
	]
}

import sys
import time
import itertools
from collections import Counter

list_gen_start = time.time()
allChampDict = {}

# Creating a dict with each key being a champion name and a list that will contain the challenges that champion counts for
for champ in allChampList:
	allChampDict[champ] = []

# Populating each champion entry in allChampDict with the list of challenges that champion counts for
for key in challengeLists:
	list = challengeLists[key]
	for champ in list:
		allChampDict[champ].append(key)

compsDict = {}
compsChecked = 0

# Looping through every 5 champion composition possible and checking whether or not that composition counts for each challenge
for comp in itertools.combinations(allChampList, 5):
	counts = Counter(allChampDict[comp[0]] + allChampDict[comp[1]] + allChampDict[comp[2]] + allChampDict[comp[3]] + allChampDict[comp[4]])
	challenges = []

	if(counts['aoe'] >= 3):
		challenges.append('aoe')
	if(counts['heal'] >= 3):
		challenges.append('heal')
	if(counts['poke'] >= 3):
		challenges.append('poke')
	if(counts['displacement'] >= 3):
		challenges.append('displacement')
	if(counts['globals'] >= 3):
		challenges.append('globals')
	if(counts['revive'] >= 3):
		challenges.append('revive')
	if(counts['immobilizing'] >= 3):
		challenges.append('immobilizing')
	if(counts['stealth'] >= 3):
		challenges.append('stealth')
	if(counts['summon'] >= 5):
		challenges.append('summon')
	if(counts['trap'] >= 3):
		challenges.append('trap')
	if(counts['terrain'] >= 3):
		challenges.append('terrain')
	if(counts['shurima'] >= 5):
		challenges.append('shurima')
	if(counts['ionia'] >= 5):
		challenges.append('ionia')
	if(counts['bandle'] >= 5):
		challenges.append('bandle')
	if(counts['bilgewater'] >= 5):
		challenges.append('bilgewater')
	if(counts['demacia'] >= 5):
		challenges.append('demacia')
	if(counts['freljord'] >= 5):
		challenges.append('freljord')
	if(counts['ixtal'] >= 5):
		challenges.append('ixtal')
	if(counts['noxus'] >= 5):
		challenges.append('noxus')
	if(counts['piltover'] >= 5):
		challenges.append('piltover')
	if(counts['shadowIsles'] >= 5):
		challenges.append('shadowIsles')
	if(counts['targon'] >= 5):
		challenges.append('targon')
	if(counts['void'] >= 5):
		challenges.append('void')
	if(counts['zaun'] >= 5):
		challenges.append('zaun')

	# Only saving the compositions that counts for 2 or more challenges to save on memory and storage requirements
	if(len(challenges) > 2):
		compsDict[str(comp)] = str(challenges)

	compsChecked += 1
	if(compsChecked % 1000000 == 0):
		print('Comps Checked: ' + str(compsChecked))

print('List gen time: ', time.time() - list_gen_start)
sort_start = time.time()

# Sorting the list of compositions by the number of challenges they count for and printing that list to a file
with open('output.txt', 'w') as f:
	sys.stdout = f
	for k in sorted(compsDict, key=lambda k: len(compsDict[k]), reverse=True):
		print(k + ' : ' + str(compsDict[k]))

sys.stdout = sys.__stdout__
print('Sort time: ', time.time() - sort_start)