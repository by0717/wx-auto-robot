import pyautogui
import time
from dataclasses import dataclass
import PyOfficeRobot
from PyOfficeRobot.core.WeChatType import WeChat, WxParam
from logging_set import logging
from pathlib import Path
from config.path_config import PathConfig
from win32_set import filedialog_handle


@dataclass
class img:
    """Class for keeping track of an item in inventory."""
    img_name: str


@dataclass
class keyWord:
    keyWord_wait: str
    keyWord_receive: str


def img_full_path(img_name) -> str:
    image_path = Path(PathConfig.src_pic_path, img_name).as_posix()
    logging.info("image_path is: {}".format(image_path))
    return image_path


def file_full_path(file_name) -> str:
    file_path = Path(PathConfig.src_file_path, file_name).as_posix()
    logging.info("file_path is: {}".format(file_path))
    return file_path


# 定义img的路径
img_fileTransport_assistant = img_full_path("file_transport_assistant.png")  # 文件传输对话框
img_sendMessage = img_full_path("send_news.png")  # send按钮
img_new_message_1 = img_full_path("new_message_1.png")  # 一条新消息
img_fileTransport = img_full_path("file_transport.png")
img_R3s_pannel = img_full_path("R3s-3.png")
# 定义微信的对象
wx = WeChat()


# keywords 自定义
keywords = {
        "R3s": "请稍等",
        "R3S": "请稍等",
        "R3s-3": "请稍等",
        "r3s": "请稍等",
        "r3": "请稍等"
        }


class img_handle:

    def new_fileTrasport_click(self):
        time.sleep(1)
        file_meeage_xy = pyautogui.locateOnScreen(img_fileTransport, confidence=0.9)
        file_meeage_center = pyautogui.center(file_meeage_xy)
        pyautogui.moveTo(file_meeage_center, duration=1)
        pyautogui.click(file_meeage_center.x, file_meeage_center.y, interval=0.2, duration=0.2, button='left')
        logging.info("new_meeage_click Pass")

    def reply_sendMessage_click(self):
        time.sleep(1)
        send_news_xy = pyautogui.locateOnScreen(img_sendMessage, confidence=0.9)
        send_news_center = pyautogui.center(send_news_xy)
        pyautogui.moveTo(send_news_center, duration=1)
        pyautogui.click(send_news_center.x, send_news_center.y, interval=0.2, duration=0.8)
        logging.info("send_message_click Pass")

    def img_check(self, img_check):
        pyautogui.PAUSE = 1
        img_check_img_xy = pyautogui.locateOnScreen(img_check, confidence=0.9)
        if img_check_img_xy is not None:
            img_check_center = pyautogui.center(img_check_img_xy)
            pyautogui.moveTo(img_check_center, duration=1)
            logging.info("Had found the img :{} on screen".format(img_check))
            return True
        elif isinstance(img_check_img_xy, list):
            logging.info("Had fonud many img {} on screen".format(img_check))
            for i in img_check_img_xy:
                logging.info(i)
                i_center = pyautogui.center(i)
                pyautogui.moveTo(i_center)
                return True
        else:
            logging.info("No img found on screen")
            return False


class message_handle(img_handle):
    # keywords 回复进入循环
    def keyWord_reply_cycle(self, who):
        while True:
            logging.info("kewWord reply begin")
            session_list = wx.GetSessionList()  # 当前界面
            logging.info(session_list)
            temp_msg = ''
            wx.ChatWith(who)  # 打开`who`聊天窗口
            friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
            logging.info(friend_name)
            logging.info(receive_msg)
            logging.info(keywords.keys())
            logging.info(list(keywords.keys()))
            receive_msg_bool = any(keyWord_in_list if keyWord_in_list in receive_msg else False for keyWord_in_list in keywords.keys())
            try:
                if (friend_name == who) and (receive_msg != temp_msg) and receive_msg_bool is True:
                    """
                    条件：
                    朋友名字正确:(friend_name == who)
                    不是上次的对话:(receive_msg != temp_msg)
                    对方内容在自己的预设里:(receive_msg in kv.keys())
                    """
                    temp_msg = receive_msg
                    logging.info(temp_msg)
                    wx.SendMsg(keywords[receive_msg])  # 向`who`发送消息
                    logging.info("send message to {} pass".format(who))
                else:
                    logging.info("no message")
                    time.sleep(2)
            except Exception as error:
                logging.info(error)
                break

    def keyWord_reply_single(self, who):
        logging.info("kewWord reply begin")
        session_list = wx.GetSessionList()  # 当前界面
        logging.info(session_list)
        temp_msg = ''
        wx.ChatWith(who)  # 打开`who`聊天窗口
        friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
        logging.info(friend_name)
        logging.info(receive_msg)
        logging.info(keywords.keys())
        logging.info(list(keywords.keys()))
        receive_msg_bool = any(keyWord_in_list if keyWord_in_list in receive_msg else False for keyWord_in_list in keywords.keys())
        try:
            if (friend_name == who) and (receive_msg != temp_msg) and receive_msg_bool is True:
                """
                条件：
                朋友名字正确:(friend_name == who)
                不是上次的对话:(receive_msg != temp_msg)
                对方内容在自己的预设里:(receive_msg in kv.keys())
                """
                temp_msg = receive_msg
                logging.info(temp_msg)
                wx.SendMsg(keywords[receive_msg])  # 向`who`发送消息
                logging.info("send message to {} pass".format(who))
            else:
                logging.info("no message")
                time.sleep(2)
        except Exception as error:
            logging.info(error)

    def send_message(self, who, send_message):
        logging.info("This is a message to send")
        PyOfficeRobot.chat.send_message(who=who, message=send_message)

    def get_wx_session(self):
        session_list = wx.GetSessionList()  # 当前界面
        logging.info(session_list)

    def key_words(self):  # just for test
        keywords = {
                "R3s": "请稍等",
                "R3S": "请稍等",
                "R3s-3": "请稍等"
                }
        logging.info(keywords.keys())
        logging.info(list((keywords.keys())))
        logging.info(keywords.values())
        logging.info(list(keywords.values()))

    def message_forward(self, f_who, f_message):
        logging.info("This is a messge  forward to :{}".format(f_who))
        PyOfficeRobot.chat.send_message(who=f_who, message=f_message)

    def file_send(self, f_who, f_file):
        logging.info("This is a file send  to {}".format(f_who))
        wx.ChatWith(f_who)
        time.sleep(1)
        self.new_fileTrasport_click()
        logging.info("Send file is: {}".format(f_file))
        filedialog_handle(f_file)
        time.sleep(1)
        self.reply_sendMessage_click()

    def get_last_session(self):
        session_list = wx.GetSessionList()
        logging.info(session_list)
        last_seesion = session_list[0]
        logging.info(last_seesion)
        return last_seesion

    def get_message_type(self):
        session_message_last = wx.GetLastMessage
        print(session_message_last)
        session_message_sender = session_message_last[0]
        session_message_type = session_message_last[1]
        print(session_message_sender)
        print(session_message_type)
        if WxParam.SpecialTypes[0] in session_message_type:
            print("sesstion message type is file")
        elif WxParam.SpecialTypes[1] in session_message_type:
            print("sesstion message type is picture")
        elif WxParam.SpecialTypes[2] in session_message_type:
            print("session message type is video")
        elif WxParam.SpecialTypes[3] in session_message_type:
            print("session message tyep is music")
        elif WxParam.SpecialTypes[4] in session_message_type:
            print("session message type is link")
        else:
            print("session message type is words")
        return session_message_type


if __name__ == '__main__':
    mh = message_handle()
    wx.ChatWith("DW-Robot")
    mh.get_message_type()
