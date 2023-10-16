import requests
from tqdm import tqdm

URL = "https://www.ceskyflorbal.cz/team/detail/roster/"
TEAM_FROM = 34496
TEAM_TO = 37379

for number in (pbar := tqdm(range(TEAM_FROM, TEAM_TO))):
    r = requests.get(URL+str(number))

    team = ""
    league = ""
    lines = r.text.splitlines()
    for line in lines:
        line = line.strip()
        if not line.startswith('<h1 class="ProfileClub-header--heading">'):
            if not line.startswith('<h3 class="ProfileClub-header--city">'):
                continue
        if line.startswith('<h1 class="ProfileClub-header--heading">'):
            team = line.replace('<h1 class="ProfileClub-header--heading">', "")
            team = team.replace("</h1>", "")
        if line.startswith('<h3 class="ProfileClub-header--city">'):
            league = line.replace('<h3 class="ProfileClub-header--city">', "")
            league = league.replace("</h3>", "")
    pbar.write(team+" ("+league+")")