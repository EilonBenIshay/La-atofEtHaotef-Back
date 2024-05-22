import json
import requests
import copy
from base64 import b64encode
from fake_headers import Headers


class InstagramScraper:
    @staticmethod
    def __build_param(username):
        params = {
            'username': username,
        }
        return params

    @staticmethod
    def __build_headers(username):
        return {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'referer': f'https://www.instagram.com/{username}/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': Headers().generate()['User-Agent'],
            'x-asbd-id': '198387',
            'x-csrftoken': 'VUm8uVUz0h2Y2CO1SwGgVAG3jQixNBmg',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }

    @staticmethod
    def __make_request(params, headers):
        INSTAGRAM_API_LINK = 'https://www.instagram.com/api/v1/users/web_profile_info/'
        return requests.get(INSTAGRAM_API_LINK, headers=headers, params=params)

    @staticmethod
    def scrape(username):
        try:
            headers = InstagramScraper.__build_headers(username)
            params = InstagramScraper.__build_param(username)
            response = InstagramScraper.__make_request(headers=headers, params=params)

            HTTP_OK = 200
            if response.status_code == HTTP_OK:
                return response.json()['data']['user']
            else:
                print('Error : ', response.status_code, response.text)
        except Exception as ex:
            print(ex)


class InstagramUser:
    def __init__(self, username):
        self.__username = username
        self.__scraped_data = InstagramScraper.scrape(username)
        self.__posts = [
                        {
                            "imageURL" : post["node"]["display_url"],
                            "description" : b64encode(post["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"].encode("UTF-16")).decode(),
                            "userName" :  "INSTAGRAM__" + username
                        }
                        for post in self.__scraped_data["edge_owner_to_timeline_media"]["edges"]
                        ]

    def get_posts(self):
        return copy.deepcopy(self.__posts)


def get_all_posts(usernames):
    posts = []
    for username in usernames:
        user = InstagramUser(username)
        try:
            posts += user.get_posts()
        except:
            pass

    return posts
