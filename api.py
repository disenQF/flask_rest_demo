import json
import os
import uuid

from flask import jsonify, request, Response, make_response
from flask_restful import Api, Resource, fields, marshal_with, marshal, reqparse
from werkzeug.datastructures import FileStorage

import settings
from models import *
import dao

api = Api()


def init_api(app):
    api.init_app(app)
    dao.init_db(app)




class UserApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=False, help='必须提供一个id')
    parser.add_argument('name', type=str,required=False)

    user_fields = {
        "id": fields.Integer,
        "name":fields.String,
        "phone": fields.String,
        "url": fields.Url(endpoint='upload',absolute=True, scheme='https')
    }
    out_fields = {"status": fields.String(default='fail'),
                 "data": fields.Nested(user_fields)}


    def get(self):
        self.parser.parse_args()

        users = dao.query(User).all()
        respJson = json.dumps(marshal(data={"status": "ok", "data": users}, fields=self.out_fields))
        print(respJson)
        resp = make_response(respJson)
        resp.set_cookie('token', 'aaadd2212333kkdooo')
        return resp

    def put(self):
        id = request.form.get('id')
        user = dao.get(User, int(id))
        user.phone = request.form.get('phone')

        dao.add(user)
        return jsonify({"status":"ok", "msg":"更新手机号成功!"})

    def post(self):
        user = User()
        user.name = request.form.get('name')
        user.phone = request.form.get('phone')

        dao.add(user)

        return jsonify({"status": "ok", "msg": "新增用户成功!"})

class UploadApi(Resource):
    def post(self):
        print(request.files)
        upFile:FileStorage = request.files.get('photo')

        # 获取文件名的扩展名
        extName = "." + upFile.filename.split('.')[-1]
        # extName = upFile.filename[-4:]
        fileName = str(uuid.uuid4()) + extName
        saveFilePath = os.path.join(settings.STATIC_DIR, fileName )

        upFile.save(saveFilePath, 1024)
        upFile.close()
        return jsonify({"msg":"上传文件成功", "path":'/static/'+fileName})

api.add_resource(UserApi, '/user/', endpoint='user')
api.add_resource(UploadApi, '/upload/',endpoint='upload')
