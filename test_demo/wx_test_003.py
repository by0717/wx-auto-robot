import pyautogui
import time


pyautogui.PAUSE = 1  # 调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用，建议用time.sleep
pyautogui.FAILSAFE = True  # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常
# 判断(x,y)是否在屏幕上
x, y = 122, 244
pyautogui.onScreen(x, y)  # 结果为true
width, height = pyautogui.size()  # 屏幕的宽度和高度
print(width, height)
currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
print(currentMouseX, currentMouseY)
# 控制鼠标移动,duration为持续时间
for i in range(2):
    pyautogui.moveTo(100, 100, duration=0.25)  # 移动到 (100,100)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
for i in range(2):
    pyautogui.moveRel(50, 0, duration=0.25)  # 从当前位置右移100像素
    pyautogui.moveRel(0, 50, duration=0.25)  # 向下
    pyautogui.moveRel(-50, 0, duration=0.25)  # 向左
    pyautogui.moveRel(0, -50, duration=0.25)  # 向上

# 按住鼠标左键，把鼠标拖拽到(100, 200)位置
pyautogui.dragTo(100, 200, button='left')
# 按住鼠标左键，用2秒钟把鼠标拖拽到(300, 400)位置
pyautogui.dragTo(300, 400, 2, button='left')
# 按住鼠标左键，用0.2秒钟把鼠标向上拖拽
pyautogui.dragRel(0, -60, duration=0.2)

# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
# 其中，button属性可以设置成left，middle和right。
pyautogui.click(10, 20, 2, 0.25, button='left')
pyautogui.click(x=100, y=200, duration=2)  # 先移动到(100, 200)再单击
pyautogui.click()  # 鼠标当前位置点击一下
pyautogui.doubleClick()  # 鼠标当前位置左击两下
pyautogui.doubleClick(x=100, y=150, button="left")  # 鼠标在（100，150）位置左击两下
pyautogui.tripleClick()  # 鼠标当前位置左击三下

pyautogui.mouseDown()  # 鼠标左键按下再松开
pyautogui.mouseUp()
pyautogui.mouseDown(button='right')  # 按下鼠标右键
pyautogui.mouseUp(button='right', x=100, y=200)  # 移动到(100, 200)位置，然后松开鼠标右键

# scroll函数控制鼠标滚轮的滚动，amount_to_scroll参数表示滚动的格数。正数则页面向上滚动，负数则向下滚动
# pyautogui.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)
pyautogui.scroll(5, 20, 2)
pyautogui.scroll(10)  # 向上滚动10格
pyautogui.scroll(-10)  # 向下滚动10格
pyautogui.scroll(10, x=100, y=100)  # 移动到(100, 100)位置再向上滚动10格

# 缓动/渐变函数可以改变光标移动过程的速度和方向。通常鼠标是匀速直线运动，这就是线性缓动/渐变函数。
# PyAutoGUI有30种缓动/渐变函数，可以通过pyautogui.ease*?查看。
# 开始很慢，不断加速
pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)
# 开始很快，不断减速
pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)
# 开始和结束都快，中间比较慢
pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)
# 一步一徘徊前进
pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)
# 徘徊幅度更大，甚至超过起点和终点
pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)
# 案例获取鼠标的位置，方便复制我们定位的鼠标坐标点到代码中


# 获取鼠标位置
def get_mouse_positon():
  time.sleep(5)  # 准备时间
  print('开始获取鼠标位置')
  try:
    for i in range(10):
    # Get and print the mouse coordinates.
    x, y = pyautogui.position()
    positionStr = '鼠标坐标点（X,Y）为：{},{}'.format(str(x).rjust(4), str(y).rjust(4))
    pix = pyautogui.screenshot().getpixel((x, y)) # 获取鼠标所在屏幕点的RGB颜色
    positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
      3) + ')'
    print(positionStr)
    time.sleep(0.5) # 停顿时间
  except:
    print("获取鼠标位置失败")