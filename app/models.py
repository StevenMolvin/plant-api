from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_serializer import SerializerMixin 

db = SQLAlchemy()
class User(db.Model,SerializerMixin):
    __tablename__='users'
    serialize_rules=('-plants.user',)
    id= db.Column('id',db.Integer(),primary_key=True)
    name = db.Column("name",db.String())
    
    plants=db.relationship('Plant', backref= 'user')
    
    created_at = db.Column('created_at', db.DateTime, default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, onupdate=db.func.now())
    
    def __repr__(self):
        return f'<User {self.name}.>'
class Plant(db.Model,SerializerMixin):
    __tablename__="plants"
    serialize_rules=('-user.plants',)
    id = db.Column('id',db.Integer(),primary_key=True)
    user_id = db.Column('user_id',db.Integer(),db.ForeignKey('users.id'))
    plant_type = db.Column('plant_type', db.String())
   
    
    created_at = db.Column('created_at', db.DateTime, default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, onupdate=db.func.now())
    
    
          