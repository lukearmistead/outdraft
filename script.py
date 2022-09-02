from espn_api.football import League
import pandas as pd
from pprint import pprint
import json
import requests
import yaml
import time

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def lookup_yaml(path):
    with open(path, 'r') as stream:
        return yaml.safe_load(stream)

def extract_espn():
    # https://stmorse.github.io/journal/espn-fantasy-v3.html

    creds = lookup_yaml('creds.yml')
    league_id = 156968
    year = 2021

    # This cookie finder might simplify the process of getting these creds moving forward
    # https://chrome.google.com/webstore/detail/espn-cookie-finder/oapfffhnckhffnpiophbcmjnpomjkfcj
    swid = creds['espn']['swid']
    espn_s2 = creds['espn']['espn_s2']
    url = "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/" + \
          str(league_id)
    params = {
        "view": "players_wl",
        "seasonId": str(year),
        }

    r = requests.get(url,
                     params=params,
                     cookies={"SWID": swid, "espn_s2": espn_s2})
    league = League(league_id=league_id, year=2018, espn_s2=espn_s2, swid=swid, fetch_league=True)
    gameweek = 1
    box_scores = league.box_scores(gameweek)
    player = box_scores[0].home_lineup[0]
    pprint(player)

# def download_stats():

def extract_fantasypros(lookup, season, positions,  creds, week=0, scoring='HALF', ranking_type='ROS'):
    params = {
        'position': positions,
        'week': str(week),
        'scoring': scoring,
        'type': 'ROS', # Rest of season
        }

    url = f'https://api.fantasypros.com/public/v2/json/nfl/{season}/{lookup}'
    response = requests.get(url, headers=creds, params=params)

    payload = response.json()
    pprint(payload)
    names, stats = [], []
    for entry in payload['players']:
        names.append(entry['name'])
        stats.append(entry['stats'])
    df = pd.DataFrame(stats)
    df['name'] = names
    df['season'] = season
    return df

def main():
    creds = lookup_yaml('creds.yml')['fantasypros']
    dfs = []
    lookup = 'projections'
    positions = ['QB', 'RB', 'WR', 'TE', 'DST', 'K']
    for season in range(2022, 2014, -1):
        for position in positions:
            try:
                df = extract_fantasypros(
                    lookup, 
                    season, 
                    position,
                    creds,
                    )
            except:
                time.sleep(60)
                df = extract_fantasypros(
                    lookup, 
                    season, 
                    position,
                    creds,
                    )
            df.to_csv(f'data/fantasypros/{season}-{lookup}-{position}.csv', index=False)

    # https://curlconverter.com/
    # https://api.fantasypros.com/public/v2/docs/

if __name__ == '__main__':
    # extract_espn()
    main()
