import requests

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAANRnVQEAAAAAEpvugMVEXkQgVnLxTc17zUodsps%3DlzVppzC8l43Mx5FQu38jiwCa2nFiaOY2eoJFwvFb6nZgthfVOK'
#API_KEY_SECRET = 'SItRWmwicXJNdGMWAUUScYjK2c1VsTmxndN5mVT91bRiKpOEwn'
#API_KEY = 'Yy46hSNwCr34a50j4tAiAHhFe'

class TwitterAPI:
    @staticmethod
    def create_twitter_headers():
        headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}
        return headers

    @staticmethod
    def create_twitter_url(keyword, max_results=10):
        search_url = 'https://api.twitter.com/2/tweets/search/recent'

        query_params = {
            'query': keyword,
            'max_results': max_results,
            'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
            'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,'
                            'public_metrics,referenced_tweets,reply_settings,source',
            'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
            'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
            'next_token': {}
        }
        return search_url, query_params

    @staticmethod
    def query_twitter_api(url, headers, params):
        response = requests.request('GET', url, headers=headers, params=params)
        return response.json()



