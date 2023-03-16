import time
from handlers import get_last_update, send_like_dislike, send_welcome_msg


like = 0
dislike = 0



def main():
    last_update = get_last_update()
    last_update_id = last_update['update_id']
    
    while True:
        current_update = get_last_update()
        current_update_id = current_update['update_id']

        if last_update_id != current_update_id:
            last_msg = current_update['message']
            chat_id = last_msg['chat']['id']

            text = last_msg.get('text')
            
            global like
            global dislike

            if text == '/start':
                send_welcome_msg(chat_id)
            elif text == '👍':
                like += 1
                send_like_dislike(chat_id, like, dislike)
            elif text == '👎':
                dislike += 1
                send_like_dislike(chat_id, like, dislike)

            print(chat_id, text, like, dislike)
            last_update_id = current_update_id
            
        time.sleep(1)

main()