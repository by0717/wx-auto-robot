import uiautomation as uia
import time
from logging_set import logging


class wx_image_ocr:
    @classmethod
    def minimize_image(cls):
        uia.uiautomation.SetGlobalSearchTimeout(15)
        try:
            image_preview_window = uia.WindowControl(ClassName="ImagePreviewWnd", searchDepth=1)
            image_preview_window.SetTopmost(True)
            image_preview_window.ButtonControl(Name="最小化", searchDepth=5).Click()
            logging.info("minimize image Pass")
        except Exception:
            logging.info("minimize image Fail")

    @classmethod
    def maximize_image_window(cls):
        uia.uiautomation.SetGlobalSearchTimeout(15)
        try:
            image_preview_window = uia.WindowControl(ClassName="ImagePreviewWnd", searchDepth=1)
            image_preview_window.SetTopmost(True)
            image_preview_window.ButtonControl(Name="最大化", searchDepth=5).Click()
            logging.info("maximize image Pass")
            return True
        except Exception:
            logging.info("maximize image Fail")
            return False

    @classmethod
    def minimize_image_window(cls):
        uia.uiautomation.SetGlobalSearchTimeout(15)
        try:
            image_preview_window = uia.WindowControl(ClassName="ImagePreviewWnd", searchDepth=1)
            image_preview_window.SetTopmost(True)
            image_preview_window.ButtonControl(Name="最大化", searchDepth=5).Click()
            logging.info("minimize image Pass")
            return True
        except Exception:
            logging.info("minimize image Fail")
            return False

    @classmethod
    def close_image_window(cls):
        uia.uiautomation.SetGlobalSearchTimeout(15)
        try:
            image_preview_window = uia.WindowControl(ClassName="ImagePreviewWnd", searchDepth=1)
            image_preview_window.SetTopmost(True)
            image_preview_window.ButtonControl(Name="关闭", searchDepth=5).Click()
            logging.info("minimize image Pass")
            return True
        except Exception:
            logging.info("minimize image Fail")
            return False

    @classmethod
    def get_image_text(cls):
        uia.uiautomation.SetGlobalSearchTimeout(15)
        try:
            image_preview_window = uia.WindowControl(ClassName="ImagePreviewWnd", searchDepth=1)
            image_preview_window.SetTopmost(True)
            image_preview_window.ButtonControl(Name="提取文字", searchDepth=7).Click()
            time.sleep(1)
            text_result = image_preview_window.EditControl(ControlType="UIA_EditControlTypeId", searchDepth=5).Name
            logging.info(type(text_result))
            logging.info(text_result)
            logging.info("get image_text Pass")
            return text_result
        except Exception:
            logging.info("get image_text Fail")
            return text_result

    @classmethod
    def imag_click_handle(cls):
        uia.uiautomation.SetGlobalSearchTimeout(15)
        try:
            UiaAPI = uia.WindowControl(ClassName='WeChatMainWndForPC')
            MsgList = UiaAPI.ListControl(Name='消息')
            MsgItem = MsgList.GetChildren()[-1]
            MsgItem.ButtonControl(ControlType="UIA_ButtonControlTypeId", searchDepth=7).Click()
            logging.info("Click image Pass")
        except Exception:
            logging.info("Click image Fail")


if __name__ == "__main__":
    wx_image_ocr.imag_click_handle()
