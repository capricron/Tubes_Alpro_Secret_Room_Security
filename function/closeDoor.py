from database import mycursor,mydb

def closeDoor(bot,message):
    sql = "UPDATE door SET status = '0' WHERE status = '1'"
    mycursor.execute(sql)
    mydb.commit()
    bot.send_message(message.chat.id, "Door is closing")