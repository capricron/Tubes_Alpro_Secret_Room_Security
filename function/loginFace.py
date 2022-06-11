import numpy as numpy
import cv2
import pickle
import time
from database import mycursor,mydb
from iot import openGate
from datetime import datetime
import pytz

def simpanDatabase(id,username,keterangan, nama):
    sekarang = datetime.now(pytz.timezone('Asia/Jakarta'))
    tanggal = sekarang.strftime("%d-%m-%Y")
    jam = sekarang.strftime("%H:%M:%S")

    if nama != "unknown":
        sql = "UPDATE door SET status = '1'"
        mycursor.execute(sql)
        mydb.commit()
    
    sql = "INSERT INTO riwayat (id,username, nama, jam, tanggal, keterangan) VALUES (%s, %s,%s, %s ,%s, %s)"
    val = (id, username, nama, jam, tanggal, keterangan)
    mycursor.execute(sql, val)
    mydb.commit()


def deteksiWajah(bot,message):

    face_cascade = cv2.CascadeClassifier('Cascade Classfier/haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")

    labels = {"person_name": 1}
    with open("labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    cap = cv2.VideoCapture(0)
    tunggu = 0
    try:
        while tunggu < 10:
            # cv2.imgs
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in faces:
                # print(x,y,w,h)
                roi_gray = gray[y:y+h, x:x+w]
                id_, conf = recognizer.predict(roi_gray) 
                if conf >= 45 and conf <= 85:
                    keterangan = "Berhasil Masuk"
                    simpanDatabase(message.from_user.id, message.from_user.username,keterangan, labels[id_])
                    bot.send_message(message.chat.id, "Selamat Datang \n" + labels[id_])
                    cap.release()
                    cv2.destroyAllWindows()
                    openGate()

            time.sleep(0.5)
            tunggu += 1
            
        if tunggu == 10:
            bot.send_message(message.chat.id, "Tidak ada wajah terdeteksi")
            cap.release()
            cv2.destroyAllWindows()
            simpanDatabase(message.from_user.id, message.from_user.username,"Tidak ada wajah terdeteksi", "unknown")
    except:
        pass

