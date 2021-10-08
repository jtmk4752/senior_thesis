import bottle
import face_recognition
import json
import os

#人の顔ではないとface_recognition.face_encodings(img)[0]が空になる。
def get_EncodingData(e_name,img):
    try:
        loaded_face_encodings = face_recognition.face_encodings(img)[0]
    except:
        bottle.redirect("/error")
    
    encoding_data = loaded_face_encodings.tolist()
    result = {
        "name":e_name,
        "data": encoding_data
    }
    return result

def img_converter(e_name,i_data):
    folder_name="img_data"
    if not os.path.exists(folder_name):
        try:
            os.makedirs(folder_name)
        except Exception as e:
            print(e)
            raise
    file_name=e_name + ".json"
    imageTojson_data = get_EncodingData(e_name,i_data)
    with open(os.path.join(folder_name, file_name),"w") as fp:
        json.dump(imageTojson_data,fp)