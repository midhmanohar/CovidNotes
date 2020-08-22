from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# db = SQLAlchemy(app)
# ma = Marshmallow(app)


# sample data
NOTES = {
    1: {
        "title": "Sample title",
        "body": "Sample body",
        "author": "John",
    }
}


class Note(Resource):
    def get(self, note_id):
        return NOTES[note_id]

    def delete(self, note_id):
        del NOTES[note_id]
        return '', 204


class NoteList(Resource):
    def get(self):
        return NOTES


api.add_resource(Note, '/notes/<int:note_id>')
api.add_resource(NoteList, '/notes')


if __name__ == "__main__":
    app.run(debug=True)
