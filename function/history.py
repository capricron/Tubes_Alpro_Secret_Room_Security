from database import mycursor

def history(bot,msg):
    mycursor.execute("SELECT * FROM riwayat")
    myresult = mycursor.fetchall() 
    for id,username,nama,jam,tanggal,keterangan in myresult:
        bot.send_message(msg.chat.id, "Id: "+str(id)+"\nUsername: "+username +"\nNama: " + nama + "\nJam: " + jam + "\nTanggal: " + tanggal + "\nKeterangan: " + keterangan)