from wxpy import *
import time

USERID = '13038011192'
WXID = '13038011192'
KEYWORD = 'tmp'


def insertWxGroupMessage(userid, wxid, msg_member, msg_group, msg_time, msg):
    '''
    '''

    print([userid, wxid, msg_member, msg_group, msg_time, msg])

    import sqlite3
    con = sqlite3.connect('Jarvis-forChat.db')
    c = con.cursor()
    sg = True
    try:
        c.execute("insert into WX_group_msg (userID,WX_id,source_WX_id,src_WXgrp,msg_time, msg) \
         values (?,?,?,?,?,?)", (userid, wxid, msg_member, msg_group, msg_time, msg))
        con.commit()
        con.close()
    except Exception as e:
        print(e)
        con.rollback()
        sg = False
        print('[-]Error')
        con.close()
    finally:
        return sg


def get_current_time():
    '''
    以字符串形式返回当前时间
    '''
    return str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))


# print(get_current_time())


bot = Bot(cache_path=True)
bot.enable_puid()

for item in bot.__dict__.items():
    print(item)

@bot.register()
def print_others(msg):
    if msg.type == 'Text':
        # 如果是群消息
        if msg.member:
            insertWxGroupMessage(USERID, WXID, msg.member.name, msg.sender.name, msg.create_time.strftime("%Y%m%d%H%M%S"), msg.text)

'''
    print('\n-----------------\n')
    # msg打印 msg属于message类，会包含消息的聊天对象以及消息的类型和内容
    print(msg)

    # local_time打印
    print("local_time is:", get_current_time())

    # receive_time和本地时间是同步的但是后面跟着一串码
    print("msg_receive_time is:", msg.receive_time)

    # create_time会有一定的误差，原因不明
    print("msg_create_time is:", msg.create_time)

    # msg.sender会返回消息发送者，如果消息来自群聊则会指向群聊，系统消息会指向本人
    print("msg_sender is:", msg.sender)

    # msg.chat显示的是当前的聊天对象（可以是群组）
    print("msg_chat is:", msg.chat)

    # msg.member在群聊中指向群内具体人的备注，如为通知指向自己，非群聊则不显示
    print("msg_member is:", msg.member)

    # msg.receiver在接收的时候是本人
    print("msg_receiver is:", msg.receiver)

    # text可以直接获得纯净文本，没有文本则返回None
    print("msg_text_is:", msg.text)

    # msg.is_at在at自己的时候会挂true
    print("msg_is_at:", msg.is_at,)

    # get_file配合file_name可以把收到的图片按照YMD-HMS.jpg格式放到指定路径里
    msg.get_file(save_path="D:\OWF"+"\\"+msg.file_name+".jpg")

    # 回复消息
    # if msg.sender.name == "有意思的群聊":
    #     msg.reply("hello world")
'''

embed()
