import requests

URL = "https://www.ceskyflorbal.cz/team/detail/roster/"
TEAM_NUMBER = 37379

for number in TEAM_NUMBER:
    r = requests.get({https://www.ceskyflorbal.cz/team/detail/roster/}{number})
    print(r)