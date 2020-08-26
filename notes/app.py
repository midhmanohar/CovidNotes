from flask import Flask, jsonify, request
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
    },
    2: {
        "title": "Sample title",
        "body": "Sample body",
        "author": "John",
    },
    3: {
        "title": "Sample title",
        "body": "Sample body",
        "author": "John",
    },
    4: {
        "title": "Sample title",
        "body": "Sample body",
        "author": "John",
    }
}


class Note(Resource):
    # Get a note by id
    def get(self, note_id):
        note = NOTES[note_id]
        # If note doesn't exists
        if not note:
            return {"message": "Note with the given id doesn't exist"}
        return jsonify(note)

    # Delete a note by id
    def delete(self, note_id):
        if not NOTES[note_id]:
            return {"message": "Note with the given id doesn't exist"}
        del NOTES[note_id]
        return {"message": "The note deleted successfully"}, 204

    # Update a note by id
    def put(self, note_id):
        note = NOTES[note_id]
        # If note doesn't exists
        if not note:
            return {"message": "Note with the given id doesn't exist"}

        # get data through json
        data = request.get_json()
        new_title = data['title']
        new_body = data['body']
        new_author = data['author']

        NOTES[note_id] = {
            "title": new_title,
            "body": new_body,
            "author": new_author
        }

        return jsonify(NOTES)


class NoteList(Resource):
    # Get all notes
    def get(self):
        return jsonify(NOTES)

    # To create a new note
    def post(self):
        # get data through json
        data = request.get_json()
        new_title = data['title']
        new_body = data['body']
        new_author = data['author']
        new_id = len(NOTES) + 1
        new_obj = {
            "title": new_title,
            "body": new_body,
            "author": new_author
        }

        NOTES[new_id] = new_obj

        return jsonify(NOTES)


api.add_resource(Note, '/notes/<int:note_id>')
api.add_resource(NoteList, '/notes')

if __name__ == "__main__":
    app.run(debug=True)
