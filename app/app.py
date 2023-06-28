from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from models import db, Plant, User
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api =Api(app)

    
        
db.init_app(app)

migrate = Migrate(app, db)
#index
class Index (Resource):
   def get(self):
       response_dict={
           'Status':'success',
           "message": "Welcome to the API"
       }
       response = make_response(
           jsonify(response_dict
        
           ),
           200,
           
       )
       return response
api.add_resource(Index,'/')  





#post-user
class Users(Resource):
    def post(self):
        new_user = User(
            name = request.form['name']
            # updated_at = request.form['updated_at'],
            # created_at =request.form['created_at']
            )
        db.session.add(new_user)
        db.session.commit()
        response_dict = new_user.to_dict()
        response = make_response(
            jsonify(response_dict),
            201,
        )
        return response
    #get-user
    def get(self):
        user = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(user),200)

api.add_resource(Users, '/users')

#delete-user and patch-user
class UserID(Resource):
    def delete(self, id):
        user=User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return "", 204
        else:
            response_dict={
                "message": 'no user'
            }
            response = make_response(
                jsonify(response_dict), 404
            )
            return response

    def patch(self, id):
        user = User.query.get(id)
        

        if user:
                for attr in request.form:
                  setattr(user,attr,request.form.get(attr))
                db.session.add(user)
                db.session.commit()

                user_dict= user.to_dict()

                response = make_response(
                    jsonify(user_dict), 200
                )

                return response
        else:
                response_dict={
                "message": 'no user'
               }
                response = make_response(
                jsonify(response_dict), 404
               )
                return response

api.add_resource(UserID,'/users/<int:id>')    








#post-plant


#post-plant
class Plants(Resource):
    def post(self):
        new_plant=Plant(
        plant_type = request.form['plant_type'],
        user_id= request.form['user_id']
        )
        db.session.add(new_plant)
        db.session.commit()
        response=make_response (jsonify(new_plant.to_dict()), 201)
        return response
    def get(self):
        plants=[plant.to_dict() for plant in Plant.query.all()]
        return make_response(jsonify(plants),200)
    
api.add_resource(Plants, '/plants')

class Plants_by_id(Resource):
    def get(self, id=None):
        if id:
            plant = Plant.query.filter_by(id=id).first().to_dict()
            if plant:
                return make_response(jsonify(plant), 200)
        else:
            response_dict={
                "message": 'Plant not found'
                }   
            abort = make_response(
                jsonify(response_dict), 404
                )
            return abort
    def delete(self, id):
        plant=Plant.query.get(id)
        if plant:
            db.session.delete(plant)
            db.session.commit()
            return "success", 204
        else:
            response_dict={
                "message": 'Plant not found'
                }   
            abort = make_response(
                jsonify(response_dict), 404
                )
            return abort
        
    def patch(self, id):
        plant = Plant.query.get(id)
        
        if plant:
            for attr in request.form:
                setattr(plant, attr, request.form.get(attr))
            db.session.add(plant)
            db.session.commit()
            
            plant_dict = plant.to_dict()
            
            response = make_response(
                jsonify(plant_dict), 200
            )
            return response
        
        else:
            response_dict={
            "message": 'no user'
            }
            response = make_response(
                jsonify(response_dict),404
            )
            return response 
        
    
api.add_resource(Plants_by_id, '/plants/<int:id>')
    
if __name__ =='_main_':
   app.run(port=5000)










































