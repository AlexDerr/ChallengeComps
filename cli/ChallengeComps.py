# List of all of the champions
allChampList = [ 
	'Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia',
	'Annie', 'Aphelios', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Bel\'Veth',
	'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', 'Cho\'Gath',
	'Corki', 'Darius', 'Diana', 'Dr. Mundo', 'Draven', 'Ekko', 'Elise',
	'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank',
	'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger',
	'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce',
	'Jhin', 'Jinx', 'K\'Sante', 'Kai\'Sa', 'Kalista', 'Karma', 'Karthus', 
	'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', 'Kha\'Zix', 'Kindred', 
	'Kled', 'Kog\'Maw', 'LeBlanc', 'Lee Sin', 'Leona', 'Lillia', 'Lissandra',
	'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi',
	'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Neeko',
	'Nidalee', 'Nilah', 'Nocturne', 'Nunu & Willump', 'Olaf', 'Orianna', 'Ornn',
	'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus',
	'Rek\'Sai', 'Rell', 'Renata Glasc', 'Renekton', 'Rengar', 'Riven', 'Rumble',
	'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco',
	'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona',
	'Soraka', 'Swain', 'Sylas', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon',
	'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate',
	'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'Vel\'Koz',
	'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 
	'Wukong', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick',
	'Yuumi', 'Zac', 'Zed', 'Zeri', 'Ziggs', 'Zilean', 'Zoe',
	'Zyra'
]

# List of champions that count for each challenge
challengeLists = {
	'aoe': [
		'Amumu', 'Anivia', 'Annie', 'Aurelion Sol', 'Azir', 'Bard', 'Bel\'Veth', 
		'Blitzcrank', 'Braum', 'Cassiopeia', 'Corki', 'Diana', 'Draven', 'Ekko',
		'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fizz', 'Galio', 'Gangplank', 'Gnar',
		'Gragas', 'Graves', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Janna', 'Jarvan IV',
		'Jinx', 'Karthus', 'Katarina', 'Kayle', 'Kennen', 'Leona', 'Lissandra',
		'Lux', 'Malphite', 'Maokai', 'Miss Fortune', 'Morgana', 'Nami', 'Neeko',
		'Nilah', 'Nunu & Willump', 'Orianna', 'Ornn', 'Pantheon', 'Qiyana', 'Rakan',
		'Rammus', 'Rell', 'Renata Glasc', 'Riven', 'Rumble', 'Samira', 'Sejuani',
		'Senna', 'Seraphine', 'Sett', 'Sona', 'Swain', 'Talon', 'Twitch',
		'Vel\'Koz', 'Viktor', 'Vladimir', 'Volibear', 'Xayah', 'Xin Zhao', 'Yone',
		'Yuumi', 'Zac', 'Ziggs', 'Zyra'
	],

	'heal': [
		'Alistar', 'Annie', 'Bard', 'Fiora', 'Galio', 'Ivern', 'Janna',
		'K\'Sante', 'Karma', 'Kayle', 'Kindred', 'Lee Sin', 'Lulu', 'Lux',
		'Morgana', 'Nami', 'Nidalee', 'Nilah', 'Orianna', 'Rakan', 'Rell',
		'Renata Glasc', 'Senna', 'Seraphine', 'Shen', 'Sona', 'Soraka', 'Tahm Kench',
		'Taric', 'Thresh', 'Yuumi', 'Zilean'
	],

	'poke': [
		'Akshan', 'Ashe', 'Azir', 'Caitlyn', 'Cho\'Gath', 'Corki', 'Dr. Mundo',
		'Ezreal', 'Gangplank', 'Jayce', 'Jhin', 'Jinx', 'Kai\'Sa', 'Karma',
		'Kled', 'Kog\'Maw', 'Lux', 'Maokai', 'Nidalee', 'Pantheon', 'Senna',
		'Seraphine', 'Shyvana', 'Sivir', 'Taliyah', 'Twisted Fate', 'Varus', 'Vel\'Koz',
		'Vex', 'Viktor', 'Xayah', 'Xerath', 'Yuumi', 'Zeri', 'Ziggs',
		'Zoe'
	],

	'displacement': [
		'Alistar', 'Aurelion Sol', 'Azir', 'Blitzcrank', 'Darius', 'Gnar', 'Gragas',
		'Hecarim', 'Janna', 'Jayce', 'K\'Sante', 'Kled', 'Lee Sin', 'Maokai', 
		'Mordekaiser', 'Nautilus', 'Nilah', 'Orianna', 'Poppy', 'Pyke', 'Rell',
		'Sett', 'Singed', 'Skarner', 'Swain', 'Tahm Kench', 'Taliyah', 'Thresh',
		'Tristana', 'Urgot', 'Vayne', 'Xin Zhao', 'Yone', 'Zac', 'Ziggs'
	],

	'globals': [
		'Akshan', 'Ashe', 'Bard', 'Caitlyn', 'Draven', 'Ezreal', 'Galio',
		'Gangplank', 'Jhin', 'Jinx', 'Kai\'Sa', 'Karthus', 'Kled', 'Lillia',
		'Lux', 'Maokai', 'Nocturne', 'Pantheon', 'Ryze', 'Senna', 'Shen',
		'Sion', 'Soraka', 'Swain', 'Taliyah', 'Twisted Fate', 'Vex', 'Xerath',
		'Ziggs'
	],

	'revive': [
		'Akshan', 'Alistar', 'Anivia', 'Bard', 'Bel\'Veth', 'Braum', 'Ekko', 
		'Elise', 'Evelynn', 'Fiora', 'Fizz', 'Gwen', 'Jax', 'K\'Sante', 
		'Kalista', 'Karthus', 'Kayle', 'Kayn', 'Kindred', 'Kled', 'Kog\'Maw',
		'Lissandra', 'Malzahar', 'Maokai', 'Master Yi', 'Olaf', 'Pantheon', 'Rakan',
		'Renata Glasc', 'Sion', 'Tahm Kench', 'Taric', 'Tryndamere', 'Vladimir', 'Xin Zhao',
		'Yuumi', 'Zac', 'Zed', 'Zilean'
	],

	'immobilizing': [
		'Aatrox', 'Alistar', 'Amumu', 'Anivia', 'Aurelion Sol', 'Bard', 'Blitzcrank', 
		'Braum', 'Camille', 'Galio', 'Gnar', 'Gragas', 'Hecarim', 'Ivern',
		'Janna', 'Jarvan IV', 'K\'Sante', 'Kled', 'LeBlanc', 'Leona', 'Lissandra',
		'Lulu', 'Maokai', 'Morgana', 'Nami', 'Nautilus', 'Neeko', 'Nunu & Willump',
		'Ornn', 'Poppy', 'Pyke', 'Qiyana', 'Rammus', 'Rell', 'Renata Glasc', 
		'Riven', 'Sejuani', 'Seraphine', 'Sett', 'Shaco', 'Singed', 'Sion',
		'Skarner', 'Tahm Kench', 'Thresh', 'Urgot', 'Vi', 'Warwick', 'Xin Zhao',
		'Yasuo', 'Yone', 'Zac', 'Zyra'
	],

	'stealth': [
		'Akali', 'Akshan', 'Evelynn', 'Kai\'Sa', 'Kha\'Zix', 'LeBlanc', 'Neeko', 
		'Nocturne', 'Pyke', 'Qiyana', 'Rengar', 'Senna', 'Shaco', 'Talon', 
		'Teemo', 'Twitch', 'Vayne', 'Viego'
	],

	'summon': [
		'Annie', 'Azir', 'Elise', 'Fiddlesticks', 'Heimerdinger', 'Illaoi', 'Ivern',
		'Kalista', 'Kindred', 'Lissandra', 'Malzahar', 'Maokai', 'Neeko', 'Orianna',
		'Shaco', 'Yorick', 'Zed', 'Zyra'
	],

	'trap': [
		'Caitlyn', 'Gangplank', 'Jhin', 'Jinx', 'Maokai', 'Nidalee', 'Shaco', 
		'Teemo', 'Ziggs', 'Zyra'
	],

	'terrain': [
		'Anivia', 'Azir', 'Irelia', 'Ivern', 'Jarvan IV', 'Ornn', 'Taliyah', 
		'Trundle', 'Veigar', 'Yorick'
	],

	# K'Sante not currently listed
	'shurima': [
		'Akshan', 'Amumu', 'Azir', 'K\'Sante', 'Nasus', 'Rammus', 'Renekton',
		'Sivir', 'Skarner', 'Taliyah', 'Xerath', 'Zilean'
	],

	'ionia': [
		'Ahri', 'Akali', 'Irelia', 'Ivern', 'Jhin', 'Karma', 'Kayn',
		'Kennen', 'Lee Sin', 'Lillia', 'Master Yi', 'Rakan', 'Sett', 'Shen',
		'Syndra', 'Varus', 'Wukong', 'Xayah', 'Yasuo', 'Yone', 'Zed'
	],

	'bandle': [
		'Corki', 'Fizz', 'Gnar', 'Heimerdinger', 'Kennen', 'Kled', 'Lulu',
		'Poppy', 'Rumble', 'Teemo', 'Tristana', 'Veigar', 'Vex', 'Yuumi',
		'Ziggs'
	],

	'bilgewater': [
		'Fizz', 'Gangplank', 'Graves', 'Illaoi', 'Miss Fortune', 'Nautilus', 'Nilah',
		'Pyke', 'Tahm Kench', 'Twisted Fate'
	],

	'demacia': [
		'Fiora', 'Galio', 'Garen', 'Jarvan IV', 'Kayle', 'Lucian', 'Lux',
		'Morgana', 'Poppy', 'Quinn', 'Shyvana', 'Sona', 'Sylas', 'Vayne',
		'Xin Zhao'
	],

	'freljord': [
		'Anivia', 'Ashe', 'Braum', 'Gnar', 'Gragas', 'Lissandra', 'Nunu & Willump',
		'Olaf', 'Ornn', 'Sejuani', 'Trundle', 'Tryndamere', 'Udyr', 'Volibear'
	],

	'ixtal': [
		'Malphite', 'Neeko', 'Nidalee', 'Qiyana', 'Rengar', 'Zyra'
	],

	'noxus': [
		'Cassiopeia', 'Darius', 'Draven', 'Katarina', 'Kled', 'LeBlanc', 'Rell',
		'Riven', 'Samira', 'Sion', 'Swain', 'Talon', 'Vladimir'
	],

	'piltover': [
		'Caitlyn', 'Camille', 'Corki', 'Ezreal', 'Heimerdinger', 'Jayce', 'Orianna',
		'Seraphine', 'Vi'
	],

	'shadowIsles': [
		'Elise', 'Evelynn', 'Fiddlesticks', 'Gwen', 'Hecarim', 'Kalista', 'Karthus', 
		'Maokai', 'Senna', 'Thresh', 'Viego', 'Yorick'
	],

	'targon': [
		'Aphelios', 'Aurelion Sol', 'Diana', 'Leona', 'Pantheon', 'Soraka', 'Taric', 
		'Zoe'
	],

	'void': [
		'Bel\'Veth', 'Cho\'Gath', 'Kai\'Sa', 'Kassadin', 'Kha\'Zix', 'Kog\'Maw', 'Malzahar', 
		'Rek\'Sai', 'Vel\'Koz'
	],

	'zaun': [
		'Blitzcrank', 'Dr. Mundo', 'Ekko', 'Janna', 'Jinx', 'Renata Glasc', 'Singed', 
		'Twitch', 'Urgot', 'Viktor', 'Warwick', 'Zac', 'Zeri', 'Ziggs'
	],

	'assassin': [
		'Ahri', 'Akali', 'Akshan', 'Ekko', 'Evelynn', 'Fiora', 'Fizz',
		'Gwen', 'Irelia', 'Jax', 'Kassadin', 'Katarina', 'Kayn', 'Kha\'Zix',
		'LeBlanc', 'Lee Sin', 'Malzahar', 'Master Yi', 'Nidalee', 'Nilah', 'Nocturne',
		'Pantheon', 'Pyke', 'Qiyana', 'Quinn', 'Rengar', 'Riven', 'Shaco',
		'Sylas', 'Talon', 'Teemo', 'Tristana', 'Tryndamere', 'Twitch', 'Vayne',
		'Vi', 'Viego', 'Xin Zhao', 'Yasuo', 'Yone', 'Zed'
	],

	'mage': [
		'Ahri', 'Amumu', 'Anivia', 'Annie', 'Aurelion Sol', 'Azir', 'Bard',
		'Brand', 'Cassiopeia', 'Cho\'Gath', 'Diana', 'Elise', 'Evelynn', 'Ezreal',
		'Fiddlesticks', 'Galio', 'Gragas', 'Heimerdinger', 'Ivern', 'Janna', 'Jhin',
		'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kennen', 'Kog\'Maw', 'LeBlanc',
		'Lillia', 'Lissandra', 'Lulu', 'Lux', 'Malzahar', 'Maokai', 'Morgana',
		'Nami', 'Neeko', 'Nidalee', 'Orianna', 'Renata Glasc', 'Rumble', 'Ryze',
		'Seraphine', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'Taliyah',
		'Twisted Fate', 'Varus', 'Veigar', 'Vel\'Koz', 'Vex', 'Viktor', 'Vladimir',
		'Xerath', 'Yuumi', 'Ziggs', 'Zilean', 'Zoe', 'Zyra'
	],

	'marksman': [
		'Akshan', 'Aphelios', 'Ashe', 'Azir', 'Caitlyn', 'Corki', 'Draven',
		'Ezreal', 'Graves', 'Jayce', 'Jhin', 'Jinx', 'Kai\'Sa', 'Kalista',
		'Kennen', 'Kindred', 'Kog\'Maw', 'Lucian', 'Miss Fortune', 'Quinn', 'Samira',
		'Senna', 'Sivir', 'Teemo', 'Tristana', 'Twitch', 'Varus', 'Vayne',
		'Xayah', 'Zeri'
	],

	'tank': [
		'Aatrox', 'Alistar', 'Amumu', 'Blitzcrank', 'Braum', 'Camille', 'Cho\'Gath',
		'Darius', 'Dr. Mundo', 'Galio', 'Garen', 'Gnar', 'Hecarim', 'Illaoi',
		'Jarvan IV', 'K\'Sante', 'Kled', 'Leona', 'Malphite', 'Maokai', 'Nasus',
		'Nautilus', 'Nunu & Willump', 'Olaf', 'Ornn', 'Poppy', 'Rammus', 'Rell',
		'Renekton', 'Sejuani', 'Sett', 'Shen', 'Shyvana', 'Singed', 'Sion',
		'Skarner', 'Tahm Kench', 'Trundle', 'Udyr', 'Urgot', 'Volibear', 'Warwick',
		'Wukong', 'Yorick', 'Zac'
	],

	'support': [
		'Alistar', 'Anivia', 'Ashe', 'Bard', 'Braum', 'Fiddlesticks', 'Heimerdinger',
		'Ivern', 'Janna', 'Karma', 'Kayle', 'Leona', 'Lulu', 'Lux',
		'Morgana', 'Nami', 'Nautilus', 'Neeko', 'Orianna', 'Pyke', 'Rakan',
		'Rell', 'Renata Glasc', 'Senna', 'Seraphine', 'Sona', 'Soraka', 'Tahm Kench',
		'Taliyah', 'Taric', 'Thresh', 'Yuumi', 'Zilean', 'Zoe', 'Zyra'
	],

	'fighter': [
		'Aatrox', 'Bel\'Veth', 'Blitzcrank', 'Camille', 'Darius', 'Diana', 'Dr. Mundo',
		'Ekko', 'Elise', 'Fiora', 'Fizz', 'Gangplank', 'Garen', 'Gnar',
		'Gragas', 'Gwen', 'Hecarim', 'Illaoi', 'Irelia', 'Jarvan IV', 'Jax',
		'Jayce', 'K\'Sante', 'Kayle', 'Kayn', 'Kled', 'Lee Sin', 'Lillia',
		'Malphite', 'Master Yi', 'Mordekaiser', 'Nasus', 'Nilah', 'Nocturne', 'Nunu & Willump',
		'Olaf', 'Ornn', 'Pantheon', 'Poppy', 'Qiyana', 'Rammus', 'Rek\'Sai',
		'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sejuani', 'Sett',
		'Shyvana', 'Singed', 'Sion', 'Skarner', 'Swain', 'Taric', 'Thresh',
		'Trundle', 'Tryndamere', 'Udyr', 'Urgot', 'Vi', 'Viego', 'Volibear',
		'Warwick', 'Wukong', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Zac'
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
	if(counts['assassin'] >= 5 or counts['mage'] >= 5 or counts['marksman'] >= 5 or counts['tank'] >= 5
		or counts['support'] >= 5 or counts['figher'] >= 5):
		challenges.append('oneClass')

	# Only saving the compositions that counts for x or more challenges to save on memory and storage requirements if needed
	if(len(challenges) > 3):
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