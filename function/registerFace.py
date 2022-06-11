import os
import cv2
import time
from facesTrain import faceTrain

def registerFace(args, bot, msg):
    try:
        if  args[1]  != "rahasia":
            bot.send_message(msg.chat.id, "Password salah")
        else:
            try:
                os.mkdir('faces-data')
            except:
                pass
            
            os.mkdir(f'faces-data/{args[2]}')
            os.system('py ampy/cli.py --port COM5 run iot/registerDone.py')
            bot.send_message(msg.chat.id, "Tunggu sebentar...")
            cam = cv2.VideoCapture(0)
            
            face_cascade = cv2.CascadeClassifier('Cascade Classfier/haarcascade_frontalface_alt2.xml')

            total_image = 6
            counter = 1
            
            # looping untuk membaca seluruh frame camera
            while True:
                # read frame
                # ret  tidak dibutuhkan karena kita membaca frame dari kamera
                # ret, frame = cam.read()
                _, frame = cam.read()
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # pencarian wajah
                faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.10, minNeighbors=3)

                for x, y, w, h in faces:
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

                    # menyimpan gambar
                    # fokus pada bagian wajah)
                    face_area = frame_gray[y:y+h, x:x+w]
                    cv2.imwrite(f'faces-data/{args[2]}/{counter}.jpg', face_area)

                    counter += 1
                    os.system('py ampy/cli.py --port COM5 run iot/registerWarn.py')
                    print(f'faces-data/{args[2]}/{counter}.jpg')

                if counter == total_image:
                    break

                time.sleep(1)

            cam.release()
            cv2.destroyAllWindows()
            faceTrain()
            os.system('py ampy/cli.py --port COM5 run iot/registerDone.py')
            bot.send_message(msg.chat.id, "Selamat, anda sudah terdaftar")
    except FileExistsError:
        bot.send_message(msg.chat.id, "Nama sudah terdaftar")
