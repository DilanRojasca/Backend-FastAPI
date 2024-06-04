from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user",
                   tags=["user"], 
                   responses={404:{"message":"not found"}})

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
@router.get("/usersJson")
async def usersJson():
    return [{"id": 1, "name" : "Dilan", "surname":"Rojas", "gmail" : "dilanrojasc6@gmail.com", "age":20},
            {"id": 2,"name" : "Sara", "surname":"Uribe", "gmail" : "uribesa@gmail.com", "age":21},
            {"id": 3,"name" : "Mariana", "surname":"Hernandez", "gmail" : "Mari.Hernandez@gmail.com", "age":23}]


@router.get("/users")
async def users():
    return users_list

#parametro PATH 
@router.get("/{id}", response_model=User, status_code=200)
async def user(id: int):
        return search_user(id)
        
#parametro QUERY
@router.get("/", response_model=User, status_code=200)
async def user(id: int):
    return search_user(id)
        

#POST, DELETE, PUT
#POST/Anadir
                    #HTTP STATUS CODE
                    #status_code=(num)
@router.post("/", response_model=User ,status_code=201)
async def create_user(user: User):

     if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="User already exists")
     
     else:
        users_list.append(user)
        return user

#PUT/actualizar

@router.put("/")
async def update_user(user: User):
        
        found = False

        for index, saved_user in enumerate(users_list):
             
             if saved_user.id == user.id:
                users_list[index] = user
                found = True
                raise HTTPException(status_code=200, detail="user update")
             
             if not found:
                  raise HTTPException(status_code=404, detail="User not found")
             
             else:
                  return user

#DELETE
@router.delete("/{id}")
async def delete_user(id:int):
     
     found = False

     for index,saved_user in enumerate(users_list):
          if saved_user.id == id:
               del users_list[index]
               found = True
               raise HTTPException(status_code=200, detail="User has been delete")
          
          if not found:
               raise HTTPException(status_code=404, detail="user not found")
          

def search_user(id: int):
        users = filter(lambda user: user.id == id, users_list)
        try:   
            return list(users)[0]
        except:
             raise HTTPException(status_code=404, detail="user not found")
        


