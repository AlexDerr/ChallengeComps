import json
import sys
import time
import itertools
from collections import Counter

MIN_CHALLENGES = 7

if __name__ == "__main__":
	with open("data/all_champ_list.json", "r") as f:
		all_champ_list = json.load(f)["all_champ_list"]

	with open("data/challenge_lists.json", "r") as f:
		challenge_lists = json.load(f)

	list_gen_start = time.time()
	all_champ_dict = {}

	# Creating a dict with each key being a champion name and a list that will contain the challenges that champion counts for
	for champ in all_champ_list:
		all_champ_dict[champ] = []

	# Populating each champion entry in allChampDict with the list of challenges that champion counts for
	for key in challenge_lists:
		list = challenge_lists[key]
		for champ in list:
			all_champ_dict[champ].append(key)

	compsDict = {}
	compsChecked = 0

	# Looping through every 5 champion composition possible and checking whether or not that composition counts for each challenge
	for comp in itertools.combinations(all_champ_list, 5):
		counts = Counter(all_champ_dict[comp[0]] + all_champ_dict[comp[1]] + all_champ_dict[comp[2]] + all_champ_dict[comp[3]] + all_champ_dict[comp[4]])
		challenges = []

		if(counts["It Has Ultimate In the Name!"] >= 3):
			challenges.append("It Has Ultimate In the Name!")
		if(counts["We Protec"] >= 3):
			challenges.append("We Protec")
		if(counts["We're Good Over Here"] >= 3):
			challenges.append("We're Good Over Here")
		if(counts["Get Over Here"] >= 3):
			challenges.append("Get Over Here")
		if(counts["Nowhere to Hide"] >= 3):
			challenges.append("Nowhere to Hide")
		if(counts["They Just... Don't... DIE!"] >= 3):
			challenges.append("They Just... Don't... DIE!")
		if(counts["Hold That Pose"] >= 3):
			challenges.append("Hold That Pose")
		if(counts["Where'd They Go?"] >= 3):
			challenges.append("Where'd They Go?")
		if(counts["Summoners on the Rift"] >= 5):
			challenges.append("Summoners on the Rift")
		if(counts["It's a Trap!"] >= 3):
			challenges.append("It's a Trap!")
		if(counts["I'm Helping"] >= 3):
			challenges.append("I'm Helping")
		if(counts["The Sun Disc Never Sets"] >= 5):
			challenges.append("The Sun Disc Never Sets")
		if(counts["Everybody was Wuju Fighting"] >= 5):
			challenges.append("Everybody was Wuju Fighting")
		if(counts["5 Under 5'"] >= 5):
			challenges.append("5 Under 5'")
		if(counts["All Hands on Deck"] >= 5):
			challenges.append("All Hands on Deck")
		if(counts["FOR DEMACIA"] >= 5):
			challenges.append("FOR DEMACIA")
		if(counts["Ice, Ice, Baby"] >= 5):
			challenges.append("Ice, Ice, Baby")
		if(counts["Elemental, My Dear Watson"] >= 5):
			challenges.append("Elemental, My Dear Watson")
		if(counts["Strength Above All"] >= 5):
			challenges.append("Strength Above All")
		if(counts["Calculated"] >= 5):
			challenges.append("Calculated")
		if(counts["Spooky Scary Skeletons"] >= 5):
			challenges.append("Spooky Scary Skeletons")
		if(counts["Peak Performance"] >= 5):
			challenges.append("Peak Performance")
		if(counts["(Inhuman Screeching Sounds)"] >= 5):
			challenges.append("(Inhuman Screeching Sounds)")
		if(counts["Chemtech Comrades"] >= 5):
			challenges.append("Chemtech Comrades")
		if(counts["assassin"] >= 5 or counts["mage"] >= 5 or counts["marksman"] >= 5 or counts["tank"] >= 5
			or counts["support"] >= 5 or counts["figher"] >= 5):
			challenges.append("oneClass")

		# Only saving the compositions that counts for x or more challenges to save on memory and storage requirements if needed
		# Make this CLI input
		if(len(challenges) > 3):
			compsDict[str(comp)] = challenges

		compsChecked += 1
		if(compsChecked % 1000000 == 0):
			print("Comps Checked: " + str(compsChecked))

	print("List gen time: ", time.time() - list_gen_start)
	sort_start = time.time()

	# Sorting the list of compositions by the number of challenges they count for and printing that list to a file
	with open("data/comps.txt", "w") as f:
		sys.stdout = f
		for k in sorted(compsDict, key=lambda k: len(compsDict[k]), reverse=True):
			print(str(len(compsDict[k])) + ": " + k + " : " + str(compsDict[k]))

	sys.stdout = sys.__stdout__
	print("Sort time: ", time.time() - sort_start)