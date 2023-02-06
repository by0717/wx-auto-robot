import win32gui
import win32con
from pathlib import Path


def filedialog_handle(file_full_path):
    file_full_path_windows = str(Path(file_full_path))
    print(file_full_path_windows)
    dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, file_full_path_windows)  # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button


if __name__ == "__main__":
    filedialog_handle('d:/barry_git/Python/by_wechat/src_file/love.txt')
