from flask import Flask, send_file, send_from_directory
from flask_restful import Resource, Api
from flask_restful import reqparse
from twittervideo import *

app = Flask(__name__)
api = Api(app)


class twittervid(Resource):
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('handle', required=True, help="Name cannot be blank!")
		args = parser.parse_args()
		handle = args['handle']
		zipfile = twittervideo(handle)

		if(zipfile=='user does not exist'):
			return {'Error': 'User does not exist!'}
		else:
			
			return send_file(zipfile,as_attachment=True)

api.add_resource(twittervid, '/twittervideo') 

if __name__ == '__main__':
	app.run(debug=True)