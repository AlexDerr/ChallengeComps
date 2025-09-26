# ChallengeComps

A tool to create a list of the League of Legends team compositions that would count for the largest amount of 5-stack team composition challenges in the Harmony and Globetrotter groups.

Due to the mostly static nature of the input/output to the program and large run time, output files have been included in the repository. `6+.zip` contains a `.txt` file containing a list of compositions that count for 6 or more challenges.

The output of `ChallengeComps.py` is a text file `comps.txt` containing team compositions along with the challenges that they count for. These are provided 1 per line and they are sorted by the number of challenges they count for.
```
('Aurelion Sol', 'Bard', 'Galio', 'Maokai', 'Alistar') : ['aoe', 'heal', 'displacement', 'globals', 'revive', 'immobilizing']
```

5-stack challenges that are considered by this tool and the output that correlates to them
- It Has Ultimate In the Name!
- We Protec
- We're Good Over Here
- Get Over Here
- Nowhere to Hide
- They Just... Don't... DIE!
- Hold That Pose
- Where'd They Go?
- Summoners on the Rift
- It's a Trap!
- I'm Helping
- The Sun Disc Never Sets
- Everybody was Wuju Fighting
- 5 under 5'
- All Hands on Deck
- FOR DEMACIA
- Ice, Ice, Baby
- Elemental, My Dear Watson
- Strength Above All
- Calculated
- Spooky Scary Skeletons
- Peak Performance
- (Inhuman Screeching Sounds)
- Chemtech Comrades
- Variety's Overrated

5-stack challenges that are not considered by this tool
- Any not on this list

## Usage
This project takes advantage of the LCU api (League Client API). `data_update.py` requires the League of Legends Client to be running on the machine in order to update `data/allchamp_list.json` and `data/challenge_list.json`. 

Then after those files are correctly populated, `challenge_comps.py` can be ran to create the compositions. If you create too large of a text file, you can use `remove_extra.py` to filter out some of the compositions to make it a more reasonable sized file.

### Config
Challenges that are completed can be filtered using `config.json`. A value of true means that it will be evaluated and included if the criteria is met, false means that the challenge will not be considered.

## Shoutout
A great tool for building compositions through a web UI can be found at: https://tahm-ken.ch/.

## Known Bugs
- ** Unclear if this is still a bug after CLU API update, but was seen in previous versions ** Output not always sorted properly, the comp `('Bard', 'Maokai', 'Nidalee', 'Renata Glasc', 'Ziggs') : ['aoe', 'heal', 'poke', 'globals', 'revive', 'immobilizing', 'trap', 'oneClass']` shows up among the 7s although it counts for 8 in this current version. 
