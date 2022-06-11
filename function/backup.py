import os
import cv2
import time
from facesTrain import faceTrain

def registerFace(args, bot, msg):
    if  args[1]  != "rahasia":
        bot.send_message(msg.chat.id, "Password salah")
    else:
        bot.send_message(msg.chat.id, "Tunggu sebentar...")
        cam = cv2.VideoCapture(0)
        
        face_cascades_file = 'Cascade Classfier/face-detect.xml'
        face_cascades = cv2.CascadeClassifier(face_cascades_file)

        total_image = 11
        counter = 1
        
        try:
            os.mkdir('faces-data')
        except:
            pass
        
        os.mkdir(f'faces-data/{args[2]}')
        # looping untuk membaca seluruh frame camera
        while True:
            # read frame
            # ret  tidak dibutuhkan karena kita membaca frame dari kamera
            # ret, frame = cam.read()
            _, frame = cam.read()
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # pencarian wajah
            faces = face_cascades.detectMultiScale(frame_gray, scaleFactor=1.10, minNeighbors=3)

            for x, y, w, h in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

                # menyimpan gambar
                # fokus pada bagian wajah)
                face_area = frame_gray[y:y+h, x:x+w]
                cv2.imwrite(f'faces-data/{args[2]}/{counter}.jpg', face_area)

                counter += 1
                print(f'faces-data/{args[2]}/{counter}.jpg')

            if counter == total_image:
                break

            time.sleep(1)

        cam.release()
        cv2.destroyAllWindows()
        faceTrain()
        bot.send_message(msg.chat.id, "Selamat, anda sudah terdaftar")
