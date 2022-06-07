from telebot import TeleBot
import re
import random
from time import sleep
import os
# encoding: utf-8
# version: 0.7.1.alpha.1


app = TeleBot(__name__)


func = ['story', 'help', 'quote', 'source']


@app.route('/forward ?(.*)')
def forward(message, cmd):
    chat_dest = message['chat']['id']
    if cmd != '':
        print('Target user: ', cmd)
        tst_msg = 'Just a test.'
        app.send_message(chat_dest, tst_msg)
        tar_usr = '@' + cmd
        try:
            app.send_message(tar_usr, tst_msg)
        except Exception as e:
            print(e)
    else:
        fmt_msg = 'Format: /forward @[USERNAME] to forward message'
        app.send_message(chat_dest, fmt_msg)


@app.route('/ ?(.*)')
def anyword(message, cmd):
    chat_dest = message['chat']['id']
    any_msg = 'Enter /help to get command list.'
    if cmd not in func and cmd != '':
        app.send_message(chat_dest, any_msg)
    else:
        pass


@app.route('/source ?(.*)')
def source(message, cmd):
    sleep(5)
    chat_dest = message['chat']['id']
    init_msg = "Invalid Xpression."
    # random password
    __pw_list = ['EnergeticBOOM', 'ICEBaby', 'BigTAPPER', 'REASONPlus']
    __pw = __pw_list[random.randint(0, len(__pw_list) - 1)]
    # print(__pw)
    if cmd == '':
        app.send_message(chat_dest, init_msg)
    elif cmd == __pw:
        with open('copy', 'rb') as f:
            data = f.read().decode('UTF-8')
            app.send_message(chat_dest, data)


@app.route('/quote ?(.*)')
def quote(message, cmd):
    chat_dest = message['chat']['id']
    list_msg = 'Jack Ma, Elon Musk, and motivational quote are available.'
    if cmd == 'jack':
        file_dir = 'quotes/jack_quote'
        quote_msg = '马云语录：'
    elif cmd == 'elon':
        file_dir = 'quotes/elon_quote'
        quote_msg = 'Elon Musk quote: '
    elif cmd == 'quote':
        # to get list of directory of motivational quotes
        dir_list = os.listdir(r'quotes\motivation_quotes\for everyone')
        # obtain primary directory of the quote files
        file_dir = 'quotes/motivation_quotes/for everyone' + '/' \
                   + dir_list[random.randint(0, len(dir_list) - 1)].strip('\n')
        quote_msg = 'Motivational quote: '
        print(file_dir)
    else:
        err_msg = "Please enter command by format /quote [NAME], which NAME can be 'jack', 'elon', or 'quote': "
        app.send_message(chat_dest, err_msg)
    # send random quote if enter others
    # else:
    #     file_dir = file_list[random.randint(0, len(file_list) - 1)]
    #     quote_msg = msg_list[random.randint(0, len(file_list) - 1)]
    if cmd == '':
        app.send_message(chat_dest, list_msg)
    else:
        app.send_message(chat_dest, quote_msg)
        with open(file_dir, 'rb') as f:
            words = f.readlines()
            word = words[random.randint(0, len(words) - 1)].decode('UTF-8')
            print(word)
            app.send_message(chat_dest, word)
            print('Message sent.')


@app.route('/help ?(.*)')
def help(message, cmd):
    chat_dest = message['chat']['id']
    print(message)
    help_msg = '/story #NUMBER for story\n' \
               '/help to get command list\n' \
               "/quote [NAME] to get quotes, which NAME can be 'jack' or 'elon'"
    app.send_message(chat_dest, help_msg)


@app.route('/story ?(.*)')
def get_story(message, cmd):
    chat_dest = message['chat']['id']
    if cmd == '':
        with open(r'.\stories\index', 'rb') as f:
            index = f.read().decode('UTF-8')
            app.send_message(chat_dest, index)
        init_msg = "Enter a number with '#' that included in index above to read a story: "
        app.send_message(chat_dest, init_msg)
    if cmd != '':
        dec = re.split('([#])', cmd)        # ([])可以保留分隔符
        try:
            if dec[1] == '#' and int(dec[2]) in range(36, 59):
                with open(rf'.\stories\#{dec[2]}', 'rb') as f:
                    story = f.read().decode('UTF-8')
                    app.send_message(chat_dest, story)
            else:
                err_msg = 'Index out of range.'
                app.send_message(chat_dest, err_msg)
        except:
            err_msg = 'Please enter a valid number.'
            app.send_message(chat_dest, err_msg)


@app.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']
    msg = "Parrot Says: {}".format(user_msg)
    app.send_message(chat_dest, msg)     # send message to where it receives'


if __name__ == '__main__':
    while True:
        app.config['api_key'] = '5188600778:AAEytrMqV_byhnZrcUHx8Kqw8EwN1OoT4aw'
        app.poll(debug=True)
