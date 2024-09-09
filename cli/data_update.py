import base64
import json
import re
import requests
import subprocess
import sys
import urllib3

urllib3.disable_warnings()

HARMONY_CHALLENGE_ID = "303400"
GLOBETROTTER_CHALLENGE_ID = "303500"
ENTRY_PER_LINE = 7


def pretty_str(data):
    out_str = "{\n"
    for key in data:
        data[key].sort()
        out_str += f"\t\"{key}\": ["
        for entry in data[key]:
            if (data[key].index(entry) % ENTRY_PER_LINE == 0
                and data[key].index(entry) != len(data[key]) - 1
            ):
                out_str += "\n\t\t"

            out_str += f"\"{entry}\""

            if data[key].index(entry) != len(data[key]) - 1:
                out_str += ", "

            if data[key].index(entry) == len(data[key]) - 1:
                out_str += "\n"

                
        out_str += "\t],\n"
    out_str += "}"
    out_str = out_str[:-3]
    out_str += "\n}"

    return out_str


if __name__ == "__main__":
    cmd_out = str(subprocess.check_output(["wmic", "PROCESS", "WHERE", "name='LeagueClientUx.exe'", "GET", "commandline"]))
    app_port = re.search("--app-port=([0-9]*)", cmd_out)[0][11:]
    auth_token = re.search("--remoting-auth-token=([\\w-]*)", cmd_out)[0][22:]
    encoded_token = base64.b64encode(f'riot:{auth_token}'.encode()).decode()

    champion_response = requests.get(
        f"https://127.0.0.1:{app_port}/lol-champions/v1/owned-champions-minimal",
        headers={
            "Accept": "application/json",
            "Authorization": f"Basic {encoded_token}",
            "Content-Type": "application/json"
        },
        verify=False
    )
    
    champion_id_dict = {}
    champion_data_response = json.loads(champion_response.text)
    for champion in champion_data_response:
          champion_id_dict[champion["id"]] = champion["name"]

    # with open("data/raw_champion_data.json", "w") as f:
    #         f.write(json.dumps(champion_data_response, indent=4))
    # with open("data/champion_dict.json", "w") as f:
    #         f.write(json.dumps(champion_id_dict, indent=4))

    challenge_response = requests.get(
        f"https://127.0.0.1:{app_port}/lol-challenges/v1/challenges/local-player",
        headers={
            "Accept": "application/json",
            "Authorization": f"Basic {encoded_token}",
            "Content-Type": "application/json"
        },
        verify=False
    )

    raw_challenge_dict = json.loads(challenge_response.text)
    # with open("data/challenge_data.json", "w") as f:
    #         f.write(json.dumps(challenge_data_dict, indent=4))

    if (HARMONY_CHALLENGE_ID not in raw_challenge_dict 
        or GLOBETROTTER_CHALLENGE_ID not in raw_challenge_dict
    ):
        print("Harmony or Globetrotter ID not found. Exiting.")
        sys.exit()

    processed_challenge_dict = {}
    for challenge_id in raw_challenge_dict[HARMONY_CHALLENGE_ID]["childrenIds"] + raw_challenge_dict[GLOBETROTTER_CHALLENGE_ID]["childrenIds"]:
        champion_ids = raw_challenge_dict[str(challenge_id)]["availableIds"]
        champion_names = [champion_id_dict[champion_id] for champion_id in champion_ids if champion_id < 3000]
        processed_challenge_dict[raw_challenge_dict[str(challenge_id)]["name"]] = champion_names

    # It has ultimate in the name has double quotes in the name so adjust it to work in json
    processed_challenge_dict["It Has Ultimate In the Name!"] = processed_challenge_dict.pop('It Has "Ultimate" In the Name!')

    # Get all the list of champions per class
    for challenge_id in CLASS_CHALLENGE_IDS:
        champion_ids = raw_challenge_dict[str(challenge_id)]["availableIds"]
        champion_names = [champion_id_dict[champion_id] for champion_id in champion_ids if champion_id < 3000]
        class_name = raw_challenge_dict[str(challenge_id)]["name"][:-11].lower()
        processed_challenge_dict[class_name] = champion_names

    pretty_challenge_list_str = pretty_str(processed_challenge_dict)

    with open("data/challenge_lists.json", "w") as f:
        f.write(pretty_challenge_list_str)

    all_champ_list = [champion_id_dict[key] for key in champion_id_dict]
    all_champ_list.sort()
    pretty_all_champ_list_str = pretty_str({"all_champ_list": all_champ_list})

    with open("data/all_champ_list.json", "w") as f:
        f.write(pretty_all_champ_list_str)
