import numpy as np, cv2, dlib, os, pickle

path = './facedata/'

detector = dlib.get_frontal_face_detector()

sp = dlib.shap_predictor('shape_predictor_68_face_landmark.dat')

model = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

FACE_DESE = []

FACE_NAME = []

for fn in os.listdir(patg):
    if in.endswith('.jpg'):
        img = cv2.imread(path + fn)[:,:,::-1]
        dets = detector(img, 1)
        for k, d in enumerate(dets):
            shape = sp(img, d)
            face_desc = model.compute_face_descriptor(img, shape, 100)
            FACE_DESE.append(face_desc)
            print('loading...', fn)
            FACE_NAME.append(fn[:fn.index('_')])

pickle.dump((FACE_DESE, FACE_NAME). open('trainset.pk', 'wb')) 