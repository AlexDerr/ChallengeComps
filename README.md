# ChallengeComps

A tool to create a list of the League of Legends team compositions that would count for the largest amount of 5-stack team composition challenges. 

Due to the mostly static nature of the input/output to the program and large run time, output files have been included in the repository. `5+.zip` contains a `.txt` file containing a reduced list that has a list of compositions that count for 5 or more challenges and `3+.zip` contains a `.txt` file with a list of compositions counting for 3 or more.

The output of `ChallengeComps.py` is a text file `output.txt` containing team compositions along with the challenges that they count for. These are provided 1 per line and they are sorted by the number of challenges they count for.
```
('Aurelion Sol', 'Bard', 'Galio', 'Maokai', 'Alistar') : ['aoe', 'heal', 'displacement', 'globals', 'revive', 'immobilizing']
```

5-stack challenges that are considered by this tool and the output that correlates to them
- aoe - It Has "Ultimate In the Name!
- heal - We Protec
- poke - We're Good Over Here
- displacement - Get Over Here
- globals - Nowhere to Hide
- revive - They Just... Don't... DIE!
- immobilizing - Hold That Pose
- stealth - Where'd They Go?
- summon - Summoners on the Rift
- trap - It's a Trap!
- terrain - I'm Helping
- shurima - The Sun Disc Never Sets
- ionia - Everybody was Wuju Fighting
- bandle - 5 under 5'
- bilgewater - All Hands on Deck
- demacia - FOR DEMACIA
- freljord - Ice, Ice, Baby
- ixtal - Elemental, My Dear Watson
- noxus - Strength Above All
- piltover - Calculated
- shadowIsles - Spooky Scary Skeletons
- targon - Peak Performance
- void - (Inhuman Screeching Sounds)
- zaun - Chemtech Comrades
- oneClass - Variety's Overrated

5-stack challenges that are not considered by this tool
- Any not on this list

As new champions are released they will need to be added `allChamplist` and then added into the list of each challenge that they count for.