import PyOfficeRobot


def test_001():
    print("1222222")
    keywords = {
              "R3s": "您好，请稍等，马上安排工程师对接",
              "r3s": "您好，请稍等,马上安排工程师对接",
              "r3s-3": "您好，请稍等，马上安排工程师对接",
              "r3": "您好，请稍等，马上安排工程师对接",
              "R3": "您好，请稍等，马上安排工程师对接"
               }
    PyOfficeRobot.chat.chat_by_keywords(who='运维团队', keywords=keywords)
    print("33333333333333333")


def test_002():
    PyOfficeRobot.chat.send_message(who="文件传输助手", message="你好")


if __name__ == "__main__":
    test_001()
