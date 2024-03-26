from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
from api_proj.settings import env
import pprint


TMDB_KEY = env.get("TMDB_KEY")

# PPRINT
pp = pprint.PrettyPrinter(indent=2, depth=2)


class Comic_Vine(APIView):
    def get(self, request):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_KEY}&with_companies=420&language=en-US&sort_by=popularity.desc"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_KEY}"
        }

        response = requests.get(url, headers=headers)
        responseJSON = response.json()
        print(response.text)
        return Response(responseJSON)
