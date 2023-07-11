import requests
import json


def search(heroes_list, url):
    intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
    for hero in heroes_list:
        hero_dict = json.loads(requests.get(url + hero).content)
        intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])
    return intelligence_dict


if __name__ == '__main__':
    url = 'https://www.superheroapi.com/api/2619421814940190/search/'
    heroes_list = ['Hulk', 'Captain america', 'Thanos']
    result = search(heroes_list, url)
    print(result)

