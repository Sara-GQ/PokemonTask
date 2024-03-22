from pokemon_model import Pokemon 
from rest_framework.response import Response
import config

session = config.DB_SESSION

# def post(self, request):
      
#        data = request.data
#        result = insert_data(data)
#        if result:
#           return Response ({'data': data, 'message': 'data saved success'})
#        else:
#           return Response("error")

def insert_data(data):

   emp_details = Pokemon(
      pokemon_name= data['name'][:100],
      species= data['species'][:500],
      abilities= data['abilities'][:500],
      moves= data['moves'][:1000],
      weight= data['weight'][:500],
      hieght= data['hieght'][:500],
      forms= data['forms'][:500],
      type=data['type'][:500]
   )
   session.add(emp_details)
   session.commit()
   return True   