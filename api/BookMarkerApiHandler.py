import json

from flask_restful import Api, Resource, reqparse

def _check_platform(url) : 
    if url[:32] == "https://www.youtube.com/watch?v=" : 
        return 1, url[32:]
    if url[:29] == "https://www.twitch.tv/videos/" : 
        return 2, url[29:]
    return 0, None

class BookMarkerApiHandler(Resource):
    def get(self):
        return {
            'status' : '200',
            'message' : 'This is get method'
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('markers', type=dict)
        parser.add_argument('url', type=str)

        args = parser.parse_args()
        request_markers = args['markers']['list']
        request_url = args['url']


        _, url_id = _check_platform(request_url)
        path = './bookmarker_storage/'+url_id+'.json'

        with open(path, 'w', encoding="UTF-8") as f:
            json.dump(request_markers, f, ensure_ascii=False)

        return {
            'status': '200',
            'message': 'Save bookmarker',
            'markers' : request_markers,
        }