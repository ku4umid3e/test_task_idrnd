import face_recognition as rf
import os


def detect_face(img):
    image = rf.load_image_file(img)
    face_img_loc = rf.face_locations(image)
    if len(face_img_loc) == 0:
        os.remove(img)
        return "I did not find people on this photo."
        
    if len(face_img_loc) == 1:
        return "I found 1 face on this photo."
    
    return f"I found {len(face_img_loc)} persons on this photo."