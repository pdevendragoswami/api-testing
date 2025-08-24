from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/devendra/goswami")
def add(a:int,b:int):
    return a+b

def subtract(a:int,b:int):
    return a-b

def subtract_model(BaseModel):
    a: int
    b: int

@app.post("/subtract")
def subtract_number(model:subtract_model):
    subtract(model.a, model.b)

user_db = {
    1:{"name":"Devendra", "age":25},
    2:{"name":"Hardik", "age":20},
    3:{"name":"Vinod", "age":22}
}


class User(BaseModel):
    name:str
    age:int

@app.put("/update_user/{user_id}")
def user_update(user_id:int, user_data:User):
    if user_id in user_db:
        user_db[user_id] = user_data.dict()
        print(user_db)
        return {"message": "User updated successfully", "user":user_db[user_id]}
    else:
        return {"message":"User not found"}
    
@app.delete("/delete_user/{user_id}")
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        print(user_db)
        return {"messsage": "User deleted successfully"}
    else:
        return {"message": "User not found."}