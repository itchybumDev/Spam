import datetime

from pyrogram import Client

from messages import message
import time

def main():
    api_id = 1868620
    api_hash = "7cac9b58cb4d8f833183f51a4866c6d0"
    print("Starting pyro.py")

    #[[Title, id, frequency, lastSent], [Title, id, frequency, lastSent]]
    chatGroups = []

    with Client("RachelUser", api_id, api_hash) as app:
        for dialog in app.iter_dialogs():
            print(dialog.chat.title or dialog.chat.first_name)
            print(dialog.chat.id)
            # print(message)

        startGroup(app, chatGroups)


def startGroup(app, chatGroups):
    while True:
        for g in chatGroups:
            keepSending(app, g)

        time.sleep(30)


def keepSending(app, group):
    #[Title, id, frequency, lastSent]
    if (isinstance(group[3], int)
            or (datetime.today() - group[3].lastSent).total_seconds() > group[3].frequency):
        print("sent to {} - {} -{}".format(group[0], group[1], group[2]))
        app.send_message(group[2], message, parse_mode="markdown")


if __name__ == "__main__":
    main()

# +6597755479
# api_id = 1868620
# api_hash = "7cac9b58cb4d8f833183f51a4866c6d0"


# Getting dialogs
# for dialog in app.iter_dialogs():
#     print(dialog.chat.title or dialog.chat.first_name)
