import bottle
import face_recognition
import json

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
    file_name=e_name + ".json"
    imageTojson_data = get_EncodingData(e_name,i_data)
    with open(file_name,"w") as fp:
        json.dump(imageTojson_data,fp)