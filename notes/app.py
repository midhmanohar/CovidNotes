from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# db = SQLAlchemy(app)
# ma = Marshmallow(app)


# sample data
NOTES = [
    {
        "id":1,
        "title": "Sample title",
        "body": "Sample body",
        "author": "John",
    },
    {
        "id":2,
        "title": "Sample title",
        "body": "Sample body",
        "author": "John",
    },
    {
        "id":3,
        "title": "Sample title",
        "body": "Sample body",
        "author": "John",
    },
    {
        "id":4,
        "title": "Sample title",
        "body": "Sample body",
        "author": "John",
    }
]


class Note(Resource):
    def get(self, note_id):
        return jsonify(NOTES[note_id])

    def delete(self, note_id):
        del NOTES[note_id]
        return '', 204

    def put(self,note_id):
        new_id = note_id
        new_title = request.form['title']
        new_body = request.form['body']
        new_author = request.form['author']

        new_obj = {
          "id":new_id,
          "title":new_title,
          "body":new_body,
          "author":new_author
        }

        NOTES.append(new_obj)

        return jsonify(NOTES)



class NoteList(Resource):
    def get(self):
        return jsonify(NOTES)

    def post(self):
        new_id = request.form['id']
        new_title = request.form['title']
        new_body = request.form['body']
        new_author = request.form['author']

        new_obj = {
          "id":new_id,
          "title":new_title,
          "body":new_body,
          "author":new_author
        }

        NOTES.append(new_obj)

        return jsonify(NOTES),201



api.add_resource(Note, '/notes/<int:note_id>')
api.add_resource(NoteList, '/notes')


if __name__ == "__main__":
    app.run(debug=True)
