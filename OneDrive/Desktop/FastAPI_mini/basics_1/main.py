from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def read_root():
    return("helo","world")
##creating
@app.post('/items/')
def create_items(name:str,price:float):
    return {"name":name,"price":price}
##updating 
@app.put('/items/{item_id}')
def update_items(item_id:int,name:str,price:float):
    return {"item_id":item_id,"name":name,"price":price}

##deleting request are used to delete resources on server
@app.delete('/items/{item_id}')
def delete_items(item_id:int):
    return f"{item_id} deleted succesfully"

@app.get('/item/')
def getti_items(item_id:int,name:str):
    return {"item_id":item_id,"name":name}   ##127.0.0.1:8000/item/1  url path parametrs
