import wikipedia
import requests
import webbrowser
from bs4 import BeautifulSoup
from os import environ as env
from flask_restful import Resource
from api.common.flask_ease.request_validation import validate_request


class Wiki_Search(Resource):
    def post(self):
        try:
            det = validate_request('query')
            quer = det['query'].replace("wikipedia", "")
            results = wikipedia.summary(f"{quer}", sentences=5)
            return {"status": True, "type": "wikipedia", "data": results}
        except Exception as er:
            return {"status": False, "type": "wikipedia", "data": f"{er}"}


class Google_search(Resource):
    def post(self):
        try:
            det = validate_request('query')
            query = det['query'].replace("google", "")
            google_search = webbrowser.get(f"{env['BROWSER_PATH']} %s").open(
                "https://www.google.com/search?q=" + query)
            if google_search is True:
                return {"status": True, "type": "google_search", "data": "Here is your search result sir"}
            else:
                return {"status": False, "type": "google_search", "data": "Something went wrong, sir could you please "
                                                                          "check your browser path"}
        except Exception as er:
            return {"status": False, "type": "google_search", "data": f"{er}"}


class Open_youtube(Resource):
    def post(self):
        try:
            det = validate_request('query')
            query = det['query']
            if query is not None:
                query = query.replace("youtube", "")
                you_search = webbrowser.get(f"{env['BROWSER_PATH']} %s").open(
                    "https://www.youtube.com/results?search_query=" + query)
            else:
                you_search = webbrowser.get(f"{env['BROWSER_PATH']} %s").open(
                    "https://www.youtube.com/")
            if you_search is True:
                return {"status": True, "type": "youtube_search", "data": "Here is your youtube search result sir"}
            else:
                return {"status": False, "type": "youtube_search", "data": "Something went wrong, sir could you please "
                                                                          "check your browser path"}
        except Exception as er:
            return {"status": False, "type": "youtube_search", "data": f"{er}"}
