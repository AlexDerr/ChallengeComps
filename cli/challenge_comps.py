import json
import sys
import time
import itertools
from collections import Counter

MIN_CHALLENGES = 5

if __name__ == "__main__":
	with open("data/all_champ_list.json", "r") as f:
		all_champ_list = json.load(f)["all_champ_list"]

	with open("data/challenge_lists.json", "r") as f:
		challenge_lists = json.load(f)

	with open("config.json", "r") as f:
		config = json.load(f)

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

		if(config["It Has Ultimate In the Name!"] and counts["It Has Ultimate In the Name!"] >= 3):
			challenges.append("It Has Ultimate In the Name!")
		if(config["We Protec"] and counts["We Protec"] >= 3):
			challenges.append("We Protec")
		if(config["We're Good Over Here"] and counts["We're Good Over Here"] >= 3):
			challenges.append("We're Good Over Here")
		if(config["Get Over Here"] and counts["Get Over Here"] >= 3):
			challenges.append("Get Over Here")
		if(config["Nowhere to Hide"] and counts["Nowhere to Hide"] >= 3):
			challenges.append("Nowhere to Hide")
		if(config["They Just... Don't... DIE!"] and counts["They Just... Don't... DIE!"] >= 3):
			challenges.append("They Just... Don't... DIE!")
		if(config["Hold That Pose"] and counts["Hold That Pose"] >= 3):
			challenges.append("Hold That Pose")
		if(config["Where'd They Go?"] and counts["Where'd They Go?"] >= 3):
			challenges.append("Where'd They Go?")
		if(config["Summoners on the Rift"] and counts["Summoners on the Rift"] >= 5):
			challenges.append("Summoners on the Rift")
		if(config["It's a Trap!"] and counts["It's a Trap!"] >= 3):
			challenges.append("It's a Trap!")
		if(config["I'm Helping"] and counts["I'm Helping"] >= 3):
			challenges.append("I'm Helping")
		if(config["Variety's Overrated"] and (
			counts["assassin"] >= 5 
			or counts["mage"] >= 5
			or counts["marksman"] >= 5
			or counts["tank"] >= 5
			or counts["support"] >= 5
			or counts["figher"] >= 5
			)
		):
			challenges.append("Variety's Overrated")
		if(config["The Sun Disc Never Sets"] and counts["The Sun Disc Never Sets"] >= 5):
			challenges.append("The Sun Disc Never Sets")
		if(config["Everybody was Wuju Fighting"] and counts["Everybody was Wuju Fighting"] >= 5):
			challenges.append("Everybody was Wuju Fighting")
		if(config["5 Under 5'"] and counts["5 Under 5'"] >= 5):
			challenges.append("5 Under 5'")
		if(config["All Hands on Deck"] and counts["All Hands on Deck"] >= 5):
			challenges.append("All Hands on Deck")
		if(config["FOR DEMACIA"] and counts["FOR DEMACIA"] >= 5):
			challenges.append("FOR DEMACIA")
		if(config["Ice, Ice, Baby"] and counts["Ice, Ice, Baby"] >= 5):
			challenges.append("Ice, Ice, Baby")
		if(config["Elemental, My Dear Watson"] and counts["Elemental, My Dear Watson"] >= 5):
			challenges.append("Elemental, My Dear Watson")
		if(config["Strength Above All"] and counts["Strength Above All"] >= 5):
			challenges.append("Strength Above All")
		if(config["Calculated"] and counts["Calculated"] >= 5):
			challenges.append("Calculated")
		if(config["Spooky Scary Skeletons"] and counts["Spooky Scary Skeletons"] >= 5):
			challenges.append("Spooky Scary Skeletons")
		if(config["Peak Performance"] and counts["Peak Performance"] >= 5):
			challenges.append("Peak Performance")
		if(config["(Inhuman Screeching Sounds)"] and counts["(Inhuman Screeching Sounds)"] >= 5):
			challenges.append("(Inhuman Screeching Sounds)")
		if(config["Chemtech Comrades"] and counts["Chemtech Comrades"] >= 5):
			challenges.append("Chemtech Comrades")

		# Only saving the compositions that counts for x or more challenges to save on memory and storage requirements if needed
		# TOOD : Make this CLI input
		if(len(challenges) >= MIN_CHALLENGES):
			compsDict[str(comp)] = challenges

		compsChecked += 1
		if(compsChecked % 1000000 == 0):
			print("Comps Checked: " + str(compsChecked))

	print("List gen time: ", time.time() - list_gen_start)
	sort_start = time.time()

	# Sorting the list of compositions by the number of challenges they count for and printing that list to a file
	with open("comps.txt", "w") as f:
		sys.stdout = f
		for k in sorted(compsDict, key=lambda k: len(compsDict[k]), reverse=True):
			print(str(len(compsDict[k])) + ": " + k + " : " + str(compsDict[k]))

	sys.stdout = sys.__stdout__
	print("Sort time: ", time.time() - sort_start)