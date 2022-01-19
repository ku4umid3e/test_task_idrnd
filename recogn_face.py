import face_recognition as rf
import os


def detect_face(img):
    image = rf.load_image_file(img)
    face_img_loc = rf.face_locations(image)
    if len(face_img_loc) > 0:
        pass
    else:
        os.remove(img)