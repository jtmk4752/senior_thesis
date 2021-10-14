import bottle
import lmdb
import json
import datetime
import face_recognition
import os.path
from convert_module import img_converter


env = lmdb.Environment("./dbbook")


def get_id(txn):
    cur = txn.cursor()
    ite = cur.iterprev()
    try:
        k, v = next(ite)
        last_id = int(k.decode("utf8"))
    except StopIteration:
        last_id = 0
    id = last_id+1
    return format(id)





@bottle.route("/")
@bottle.view("list")
def list():
    data = []
    KEY = []
    with env.begin() as txn:
        cur = txn.cursor()
        for key, value in cur:
            key = key.decode("utf8")
            d = json.loads(value.decode("utf8"))
            KEY.append(key)
            data.append(d)
    for (d, k) in zip(data, KEY):
        print(k, d)
    return {"data": data, "KEY": KEY}

@bottle.route("/entry")
def root():
    return bottle.static_file("entry.html", root="./static")

@bottle.route("/error")
@bottle.view("error")
def Error():
    print("ファイルエラー")

@bottle.post("/submit")
@bottle.view("submit")
def submit():

    Name = bottle.request.params.Name
    author = bottle.request.params.author
    publisher = bottle.request.params.publisher
    files = bottle.request.files.get('file')

    if files:
        data = {"Name": Name, "author": author, "publisher": publisher}
        try:
            image = face_recognition.load_image_file(files.file)
        except:
            bottle.redirect("/error")
        e_name,_ = os.path.splitext(files.filename)
        img_converter(e_name,image)
        with env.begin(write=True) as txn:
            id = get_id(txn)
            txn.put(id.encode("utf8"), json.dumps(data).encode("utf8"))
        return data
    else:
        bottle.redirect("/error")


@bottle.route("/list")
@bottle.view("list")
def list():
    data = []
    KEY = []
    with env.begin() as txn:
        cur = txn.cursor()
        for key, value in cur:
            key = key.decode("utf8")
            d = json.loads(value.decode("utf8"))
            KEY.append(key)
            data.append(d)
    for (d, k) in zip(data, KEY):
        print(k, d)
    return {"data": data, "KEY": KEY}


@bottle.route("/delete/<message>")
def delete(message):
    with env.begin(write=True) as txn:
        txn.delete(message.encode("utf8"))
    bottle.redirect("/list")




bottle.run()
