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
            print(text, chat_id)
            
            if text == '/start':
                send_welcome_msg(chat_id)
            elif text == '👍':
                global like
                like += 1
            elif text == '👎':
                global dislike
                dislike += 1
            print(like, dislike)
            last_update_id = current_update_id
            
        time.sleep(1)

main()