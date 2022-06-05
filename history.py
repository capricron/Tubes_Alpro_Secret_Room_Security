from database import mycursor

def history(bot,msg):
    mycursor.execute("SELECT * FROM riwayat")
    myresult = mycursor.fetchall() 
    for nama,jam,tanggal,keterangan in myresult:
        bot.send_message(msg.chat.id, "Nama: " + nama + "\nJam: " + jam + "\nTanggal: " + tanggal + "\nKeterangan: " + keterangan)