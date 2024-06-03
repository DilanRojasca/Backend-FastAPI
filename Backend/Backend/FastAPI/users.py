from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad user
class User(BaseModel):
    id: int
    name:str
    surname:str
    gmail:str
    age:int

#Base de datos inventada.
users_list = [User(id = 1, name = "Dilan", surname = "Rojas", gmail = "dilanrojasc6@gmail.com",age = 20),
             User(id = 2, name = "Sara", surname = "Uribe", gmail = "uribesa@gmail.com",age = 21),
             User(id = 3 ,name = "Mariana", surname = "Hernandez", gmail = "Mari.Hernandez@gmail.com", age=23)]

#En Json
@app.get("/usersJson")
async def usersJson():
    return [{"id": 1, "name" : "Dilan", "surname":"Rojas", "gmail" : "dilanrojasc6@gmail.com", "age":20},
            {"id": 2,"name" : "Sara", "surname":"Uribe", "gmail" : "uribesa@gmail.com", "age":21},
            {"id": 3,"name" : "Mariana", "surname":"Hernandez", "gmail" : "Mari.Hernandez@gmail.com", "age":23}]


@app.get("/users")
async def users():
    return users_list

#parametro PATH 
@app.get("/user/{id}")
async def user(id: int):
        return search_user(id)
        
#parametro QUERY
@app.get("/user/")
async def user(id: int):
    return search_user(id)
        

def search_user(id: int):
        users = filter(lambda user: user.id == id, users_list)
        try:   
            return list(users)[0]
        except:
             return {"error":"User not found"}

#POST, DELETE, PUT
#POST/Anadir
@app.post("/user/")
async def create_user(user: User):
     if type(search_user(user.id)) == User:
         return {"error":"User already exists"}
     else:
        users_list.append(user)
        return user

#PUT/actualizar

@app.put("/user/")
async def update_user(user: User):
        
        found = False

        for index, saved_user in enumerate(users_list):
             
             if saved_user.id == user.id:
                users_list[index] = user
                found = True
                return {"message":"User updated"}
             
             if not found:
                  return {"error":"User not found"}
             
             else:
                  return user

#DELETE
@app.delete("/user/{id}")
async def delete_user(id:int):
     
     found = False

     for index,saved_user in enumerate(users_list):
          if saved_user.id == id:
               del users_list[index]
               found = True
          
          if not found:
               return {"error":"User not found"}