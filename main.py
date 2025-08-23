''' this is to create an API using Flask'''

from flask import Flask, request

app=Flask(__name__)

data={
    1: {"name": "Alice", "age": 30}, 
    2: {"name": "Bob", "age": 25}
}


@app.route("/todos", methods=["GET"])
def get_todos():
    response=[]
    for key, value in data.items():
        temp=value
        temp["id"]=key
        response.append(temp)
    return response


@app.route("/todos/<int:id>", methods=["GET"])
def get_todo(id):
    if id in data:
        temp=data[id]
        temp["id"]=id
        return temp
    else:
        return {
            "error": "Todo not found!!"
        }, 404


@app.route("/todos", methods=["POST"])
def post_todos():
    reqdata=request.get_json()
    todo={
        "name": reqdata["name"],
        "age": reqdata["age"]
    }
    data[len(data)+1]=todo
    todo["id"]=len(data)
    return todo, 201


@app.route("/todos/<int:id>", methods=["PUT"])
def put_todos(id):
    reqdata=request.get_json()
    if id in data:
        temp=data[id]
        temp["name"]=reqdata.get("name", temp["name"])
        temp["age"]=reqdata.get("age", temp["age"])
        data[id]=temp
        temp["id"]=id
        return temp
    else:
        return {
            "error": "Todo not found!!"
        }, 404


@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todos(id):
    data.pop(id, None)
    return {
        "message" : "Todo deleted Successfully!!"
    }


if __name__ == "__main__":
    app.run(debug=True)

