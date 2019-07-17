from flask import jsonify, abort
from flask_restful import Resource, reqparse, fields, marshal
from .models import People, db, IntegrityError
import json

people_fields = {
    'id':   fields.Integer,
    'name': fields.String,
    'is_alive': fields.Boolean,
    'place_id': fields.Integer
}

class Person(Resource):
    def get(self):
        json = [marshal(people, people_fields) for people in People.query.order_by(People.id).all()]
        return jsonify(json)
    
    def post(self):      
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required = True)
        parser.add_argument('is_alive', location='json', required = True)
        parser.add_argument('place_id', location='json', required = True)

        args = parser.parse_args()
        
        create_people = People(name = args['name'], is_alive = args['is_alive'], place_id = args['place_id'])
        
        try:
            db.session.add(create_people)
            db.session.commit()
        except IntegrityError:
                abort(409, 'Conflict')
        
        if create_people:
            return json.dumps({'success':True}), 201, {'ContentType':'application/json'} 
        else:
            abort(400, 'Bad Request')
    
class PeopleById(Resource):
    def get(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('id', location='view_args', required = True)
        args = parser.parse_args()
        json = [marshal(people, people_fields) for people in People.query.filter(People.id == args['id'])]
       
        if json:
            return jsonify(json)
        else:
            abort(404, 'Not Found')

    def put(self, id):        
        get_parser = reqparse.RequestParser()
        get_parser.add_argument('id', location='view_args', required = True)
        get_parser.add_argument('name', location='json', required = True)
        get_args = get_parser.parse_args()
        
        get_people_id = db.session.query(People.id).filter(People.id == get_args['id'])
        people_id = get_people_id.first()

        get_people_name = db.session.query(People.name).filter(People.name == get_args['name'])
        people_name = get_people_name.first()

        if people_id:
            person_parser = reqparse.RequestParser()
            person_parser.add_argument('name', location='json', required = True)
            person_parser.add_argument('is_alive', location='json', required = True)
            person_parser.add_argument('place_id', location='json', required = True)
            person_args = person_parser.parse_args()        
            
            update_person = People.query.get(get_args['id'])
            update_person.name = person_args['name']
            update_person.is_alive = person_args['is_alive']
            update_person.place_id = person_args['place_id']

            try:
                db.session.commit()
            except IntegrityError:
                abort(409, 'Conflict')
                
            if update_person:
                return json.dumps({'success':True}), 201, {'ContentType':'application/json'} 
            else:
                abort(400, 'Bad Request')
        else:
            abort(404, 'Not Found')
        
            
    def delete(self, id):
        id_parser = reqparse.RequestParser()
        id_parser.add_argument('id', location='view_args', required = True)
        id_args = id_parser.parse_args()

        delete_people = People.query.filter_by(id = id_args['id']).delete()
        db.session.commit()
       
        if delete_people:
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        else:
            abort(404, 'Not Found')