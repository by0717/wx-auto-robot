import uiautomation as uia
import win32gui
import win32con
import win32clipboard as wc
import time
import os



class WxParam:
    SYS_TEXT_HEIGHT = 33
    TIME_TEXT_HEIGHT = 34
    RECALL_TEXT_HEIGHT = 45
    CHAT_TEXT_HEIGHT = 52
    CHAT_IMG_HEIGHT = 117
    SpecialTypes = ['[文件]', '[图片]', '[视频]', '[音乐]', '[链接]']


UiaAPI = uia.WindowControl(ClassName='WeChatMainWndForPC')
EditMsg = UiaAPI.EditControl(Name='输入')


class WxUtils:
    def SplitMessage(MsgItem):
        uia.SetGlobalSearchTimeout(0)
        MsgItemName = MsgItem.Name
        if MsgItem.BoundingRectangle.height() == WxParam.SYS_TEXT_HEIGHT:
            Msg = ('SYS', MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
        elif MsgItem.BoundingRectangle.height() == WxParam.TIME_TEXT_HEIGHT:
            Msg = ('Time', MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
        elif MsgItem.BoundingRectangle.height() == WxParam.RECALL_TEXT_HEIGHT:
            if '撤回' in MsgItemName:
                Msg = ('Recall', MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
            else:
                Msg = ('SYS', MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
        else:
            Index = 1
            User = MsgItem.ButtonControl(foundIndex=Index)
            try:
                while True:
                    if User.Name == '':
                        Index += 1
                        User = MsgItem.ButtonControl(foundIndex=Index)
                    else:
                        break
                Msg = (User.Name, MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
            except:
                Msg = ('SYS', MsgItemName, ''.join([str(i) for i in MsgItem.GetRuntimeId()]))
        uia.SetGlobalSearchTimeout(10.0)
        return Msg

    def SetClipboard(data, dtype='text'):
        '''复制文本信息或图片到剪贴板
        data : 要复制的内容，str 或 Image 图像'''
        if dtype.upper() == 'TEXT':
            type_data = win32con.CF_UNICODETEXT
        elif dtype.upper() == 'IMAGE':
            from io import BytesIO
            type_data = win32con.CF_DIB
            output = BytesIO()
            data.save(output, 'BMP')
            data = output.getvalue()[14:]
        else:
            raise ValueError('param (dtype) only "text" or "image" supported')
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(type_data, data)
        wc.CloseClipboard()

    def Screenshot(hwnd, to_clipboard=True):
        '''为句柄为hwnd的窗口程序截图
        hwnd : 句柄
        to_clipboard : 是否复制到剪贴板
        '''
        import pyscreenshot as shot
        bbox = win32gui.GetWindowRect(hwnd)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, \
                              win32con.SWP_SHOWWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, \
                              win32con.SWP_SHOWWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        win32gui.BringWindowToTop(hwnd)
        im = shot.grab(bbox)
        if to_clipboard:
            WxUtils.SetClipboard(im, 'image')
        return im

    def SavePic(savepath=None, filename=None):
        Pic = uia.WindowControl(ClassName='ImagePreviewWnd', Name='图片查看')
        Pic.SendKeys('{Ctrl}s')
        SaveAs = Pic.WindowControl(ClassName='#32770', Name='另存为...')
        SaveAsEdit = SaveAs.EditControl(ClassName='Edit', Name='文件名:')
        SaveButton = Pic.ButtonControl(ClassName='Button', Name='保存(S)')
        PicName, Ex = os.path.splitext(SaveAsEdit.GetValuePattern().Value)
        if not savepath:
            savepath = os.getcwd()
        if not filename:
            filename = PicName
        FilePath = os.path.realpath(os.path.join(savepath, filename + Ex))
        SaveAsEdit.SendKeys(FilePath)
        SaveButton.Click()
        Pic.SendKeys('{Esc}')

    def ControlSize(control):
        locate = control.BoundingRectangle
        size = (locate.width(), locate.height())
        return size

    def ClipboardFormats(unit=0, *units):
        units = list(units)
        wc.OpenClipboard()
        u = wc.EnumClipboardFormats(unit)
        wc.CloseClipboard()
        units.append(u)
        if u:
            units = WxUtils.ClipboardFormats(u, *units)
        return units

    def CopyDict():
        Dict = {}
        for i in WxUtils.ClipboardFormats():
            if i == 0:
                continue
            wc.OpenClipboard()
            try:
                content = wc.GetClipboardData(i)
                wc.CloseClipboard()
            except:
                wc.CloseClipboard()
                raise ValueError
            if len(str(i)) >= 4:
                Dict[str(i)] = content
        return Dict


def SendMsg(msg, clear=True):
        '''
        向当前窗口发送消息
        msg : 要发送的消息
        clear : 是否清除当前已编辑内容
        '''
        UiaAPI.SwitchToThisWindow()
        if clear:
            EditMsg.SendKeys('{Ctrl}a', waitTime=0)
        EditMsg.SendKeys(msg, waitTime=0)
        EditMsg.SendKeys('{Enter}', waitTime=0)


def SendClipboard():
        '''向当前聊天页面发送剪贴板复制的内容'''
        SendMsg('{Ctrl}v')


def send_file(*filepath, not_exists='ignore'):
    COPYDICT = {}
    key = ""
    for file in filepath:
        file = os.path.realpath(file)
        if not os.path.exists(file):
            if not_exists.upper() == 'IGNORE':
                print('File not exists:', file)
                continue
            elif not_exists.upper() == 'RAISE':
                raise FileExistsError('File Not Exists: %s' % file)
            else:
                raise ValueError('param not_exists only "ignore" or "raise" supported')
        key += '<EditElement type="3" filepath="%s" shortcut="" />' % file
        if not key:
            return 0
        if not COPYDICT:
            EditMsg.SendKeys(' ', waitTime=0)
            EditMsg.SendKeys('{Ctrl}a', waitTime=0)
            EditMsg.SendKeys('{Ctrl}c', waitTime=0)
            EditMsg.SendKeys('{Delete}', waitTime=0)
            while True:
                try:
                    COPYDICT = WxUtils.CopyDict()
                    break
                except:
                    pass
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(13, '')
        wc.SetClipboardData(16, b'\x04\x08\x00\x00')
        wc.SetClipboardData(1, b'')
        wc.SetClipboardData(7, b'')
        for i in COPYDICT:
            copydata = COPYDICT[i].replace(b'<EditElement type="0" pasteType="0"><![CDATA[ ]]></EditElement>',
                                           key.encode()).replace(b'type="0"', b'type="3"')
            wc.SetClipboardData(int(i), copydata)
        wc.CloseClipboard()
        SendClipboard()
        return 1


def sendf(*args):
    pass


if __name__ == "__main__":
    send_file(r"d:\barry_git\Python\by_wechat\src_file\love.txt")
