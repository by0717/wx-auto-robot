import pyautogui
import time
from dataclasses import dataclass
import PyOfficeRobot
from PyOfficeRobot.core.WeChatType import WeChat
from config.path_config import PathConfig
frim pathlib import Path

@dataclass
class img:
    """Class for keeping track of an item in inventory."""
    img_name: str


@dataclass
class keyWord:
    keyWord_wait: str
    keyWord_receive: str


img_fileTransport = img("file_transport.png")  # 文件传输对话框
img_sendMessage = img("send_news.png")  # send按钮
img_new_message_1 = img("new_message_1.png")  # 一条新消息


def new_fileTrasport_click():
    time.sleep(1)
    new_meeage_xy = pyautogui.locateOnScreen(img_fileTransport, confidence=0.9)
    new_meeage_center = pyautogui.center(new_meeage_xy)
    pyautogui.moveTo(new_meeage_center, duration=1)
    pyautogui.click(new_meeage_center.x, new_meeage_center.y, interval=0.2, duration=0.2, button='left')
    print("new_meeage_click Pass")


def reply_sendMessage_click():
    time.sleep(1)
    send_news_xy = pyautogui.locateAllOnScreen()
    send_news_center = pyautogui.center(send_news_xy)
    pyautogui.moveTo(send_news_center, duration=1)
    pyautogui.click(send_news_center.x, send_news_center.y, interval=0.2, duration=0.8)


def keyWord_reply(who):
    print("begin")
    keywords = {
               "R3s": "请稍等",
               "R3S": "请稍等",
               "R3s-3": "请稍等",
               "r3s": "请稍等"
               }
    wx = WeChat()
    wx.ChatWith(who)  # 打开`who`聊天窗口
    session_list = wx.GetSessionList()  # 当前界面
    print(session_list)
    wx.ChatWith(who)  # 打开`who`聊天窗口
    temp_msg = ''
    friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
    print(friend_name)
    print(receive_msg)
    print(keywords.keys())
    print(list(keywords.keys()))
    while True:
        try:
            if (friend_name == who) and (receive_msg != temp_msg) and (receive_msg in list(keywords.keys())):
                """
                条件：
                朋友名字正确:(friend_name == who)
                不是上次的对话:(receive_msg != temp_msg)
                对方内容在自己的预设里:(receive_msg in kv.keys())
                """
                temp_msg = receive_msg
                print(temp_msg)
                wx.SendMsg(keywords[receive_msg])  # 向`who`发送消息
                print("pass----ok")
                break
            else:
                print("no message")
                continue
        except Exception as error:
            print(error)


def send_message(who):
    print("Begin send")
    PyOfficeRobot.chat.send_message(who=who, message="这个是机器人自动发送消息，不用回复")


def get_wx_session():
    keywords = {
               "R3s": "请稍等",
               "R3S": "请稍等",
               "R3s-3": "请稍等"
               }
    wx = WeChat()
    session_list = wx.GetSessionList()  # 当前界面
    print(session_list)
    wx.ChatWith("DW-Robot")
    friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]
    print(friend_name)
    print(receive_msg)
    print(keywords.keys())
    if receive_msg in keywords.keys():
        send_message("DW-Robot")
    else:
        print("no reply")


def key_words():
    keywords = {
               "R3s": "请稍等",
               "R3S": "请稍等",
               "R3s-3": "请稍等"
               }
    print(keywords.keys())
    print(list((keywords.keys())))
    print(keywords.values())
    print(list(keywords.values()))


if __name__ == '__main__':
    keyWord_reply("DW-Robot")
