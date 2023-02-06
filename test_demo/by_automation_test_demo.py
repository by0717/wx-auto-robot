import uiautomation as uia

uia.uiautomation.SetGlobalSearchTimeout(15)
win_cal = uia.WindowControl(ClassName="ApplicationFrameWindow", searchDepth=1)
win_cal.SetTopmost(True)
window_main = win_cal.Control(searchDepth=1, ClassName='Windows.UI.Core.CoreWindow')
button_group = window_main.Control(searchDepth=1, ClassName='LandmarkTarget')
number_group = button_group.Control(searchDepth=1, Name='数字键盘')
calc_group = button_group.Control(searchDepth=1, Name='标准运算符')
# 模拟按键
win_cal.SendKeys('1')
#number_group.ButtonControl(Name='一').Click()
calc_group.ButtonControl(Name='加').Click()
number_group.ButtonControl(Name='四').Click()
calc_group.ButtonControl(Name='等于').Click()
result_1 = button_group.TextControl(AutomationId="CalculatorResults").Name
print("111", result_1)
result_2 = button_group.PaneControl(AutomationId="TextContainer", searchDepth=2).Name
print("2222", result_2)
result_f = button_group.TextControl(AutomationId='NormalOutput').Name

'''
win_cal_window = win_cal.WindowControl(className="Windows.UI.Core.CoreWindow", searchDepth=1)
win_cal_group = win_cal_window.Control(ClassName="LandmarkTarget", searchDepth=1)
operator_group = win_cal.Control(searchDepth=3, Name="标准运算符")
number_group = win_cal.Control(searchDepth=3, Name="数字键盘")
number_group.ButtonControl(Name="一").Click()
operator_group.ButtonControl(Name="加").Click()
number_group.ButtonControl(Name="二").Click()
operator_group.ButtonControl(Name="等于").Click()
'''

# 获取结果
# nResult_text = win_cal_group.TextControl(AutomationId="CalculatorResults").Name
print("111:", result_f)
# nResult = win_cal.TextControl(searchDepth=4, AutomationId="TextContainer").Name
# print("计算结果为:", nResult)
