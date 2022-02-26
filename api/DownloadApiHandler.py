from flask_restful import Api, Resource, reqparse

from api.download_logic.do_logic import create_cutTool, delete_cutTool


class DownloadApiHandler(Resource) :
    def get(self):
        return {
            'status' : '200',
            'message' : 'Success'
        }

    def post(self):
        # axios 주소는 /flask/download
        # 다운로드받을 파일 위치는 /HIGHLIGHTING.zip
        # 1. POST로 'status':'download_start'랑 'bookmarks' 보내면 파일이 생성됨
        # 2. 위 위치에 있는 파일 다운로드 받고나서 POST로 'status':'download_end'랑 'bookmarks' 보내면 파일 삭제됨
        parser = reqparse.RequestParser()
        parser.add_argument('status', type=str)
        parser.add_argument('bookmarks', type=str)
        args = parser.parse_args()

        if args['status'] == 'download_start' : 
            bookmarks = args['bookmarks']
            # need to parse bookmarks
            create_cutTool([[0,100]])
        elif args['status'] == 'download_done' : 
            delete_cutTool()
        final_ret = {
            "type" : "POST",
            "status" : "success"
        }
        return final_ret
