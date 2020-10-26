from pyrogram import Client

from messages import message


def main():
    # api_id = 1936059
    # api_hash = "3762e62a9653fdb474e1d1ecc9559571"
    # groupIds = [-431644407, -476219790, -408271358]

    # with Client("my_account", api_id, api_hash) as app:
    #     for id in groupIds:
    #         app.send_message(chat_id=id, text="Hello from user")

    api_id = 1868620
    api_hash = "7cac9b58cb4d8f833183f51a4866c6d0"
    print("I am here")
    with Client("RachelUser", api_id, api_hash) as app:
        for dialog in app.iter_dialogs():
            print(dialog.chat.title or dialog.chat.first_name)
            print(message)


if __name__ == "__main__":
    main()

# +6597755479
# api_id = 1868620
# api_hash = "7cac9b58cb4d8f833183f51a4866c6d0"


# Getting dialogs
# for dialog in app.iter_dialogs():
#     print(dialog.chat.title or dialog.chat.first_name)
