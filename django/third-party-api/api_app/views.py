from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
from api_proj.settings import env
import hashlib
import time
import pprint

# MARVEL API REQUIREMENTS
MARVEL_API_KEY = env.get('MARVEL_API_KEY')
MARVEL_SECRET_KEY = env.get('MARVEL_SECRET_KEY')
timestamp = str(int(time.time()))
HASH_STR = f'{timestamp}{MARVEL_SECRET_KEY}{MARVEL_API_KEY}'
MARVEL_SECRET_HASH_KEY = hashlib.md5(HASH_STR.encode()).hexdigest()



# PPRINT
pp = pprint.PrettyPrinter(indent=2, depth=2)
# Create your views here.


class Marvel(APIView):
    def get(self, request):
        search = 'comics'  # can be comics, characters, and more
        auth = OAuth1(MARVEL_API_KEY, MARVEL_SECRET_KEY)
        endpoint = f'http://gateway.marvel.com/v1/public/{search}?ts={timestamp}&apikey={MARVEL_API_KEY}&hash={MARVEL_SECRET_HASH_KEY}'
        response = requests.get(endpoint, auth=auth)
        print('\n\n\n\n\n\n', response.status_code, '\n\n\n\n\n\n\n\n\n')
        if response.status_code == 200:
            responseJSON = response.json()
        else:
            print(f"Error: {response.status_code}")
        display_arr = []
        for x in range(6):
            display_arr.append(responseJSON['data']['results'][x])
        return Response(display_arr)


