import time
from handlers import get_last_update, send_like_dislike, send_welcome_msg
from db import DB


db = DB()

def main():
    last_update = get_last_update()
    last_update_id = last_update['update_id']
    
    while True:
        current_update = get_last_update()
        current_update_id = current_update['update_id']

        if last_update_id != current_update_id:
            last_msg = current_update['message']
            chat_id = last_msg['chat']['id']
            User_name1 = last_msg['chat']['first_name']
            User_name2 = last_msg['chat']['last_name']
            Username = last_msg['chat']['username']

            text = last_msg.get('text')
            
            global like
            global dislike

            if text == '/start':
                send_welcome_msg(chat_id,User_name1,User_name2)
                db.add(chat_id,User_name1,User_name2,Username)
            elif text == '👍':
                data = db.increase_like(chat_id)
                send_like_dislike(chat_id, data['like'], data['dislike'])
            elif text == '👎':
                db.increase_dislike(chat_id)
                send_like_dislike(chat_id, data['like'], data['dislike'])


            last_update_id = current_update_id
            
        time.sleep(1)

main()