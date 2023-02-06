import os
from pathlib import Path, PurePath


'''
Pathlib 或者os path进行，根据个人喜好进行
'''


class Path_Config:
    full_path_windows = Path(__file__)
    full_path = PurePath(full_path_windows).as_posix()
    root_path_windows = Path(__file__).parent.parent
    root_path = PurePath(root_path_windows).as_posix()
    log_path_windows = Path(root_path, "Log")
    log_path = PurePath(log_path_windows).as_posix()


class PathConfig:
    """
    框架路径配置
    """
    _SLASH = '/'
    # 项目路径
    root_path_windows = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 返回脚本上两层目录路径
    root_path = root_path_windows.replace('\\', '/')
    # 用例路径
    case_path = os.path.join(root_path, 'Cases' + _SLASH)
    # 缓存路径
    cache_path = os.path.join(root_path, 'Cache' + _SLASH)
    # 日志路径
    log_path_windows = os.path.join(root_path, 'Log' + _SLASH)
    log_path = log_path_windows.replace('\\', '/')
    # 测试报告路径
    report_path_allure = os.path.join(root_path, 'Allure_report' + _SLASH)
    # html报告
    report_path_html = os.path.join(root_path, 'HTML_report')
    # 公共配置路径
    common_path = os.path.join(root_path, 'Common' + _SLASH)
    # yaml数据路径
    yaml_data_path = os.path.join(root_path, 'Yaml_data' + _SLASH)
    # picture 源图片路径
    src_pic_path = os.path.join(root_path, 'src_picture' + _SLASH)
    # picture 目标图片路径，存储截图等
    des_pic_path = os.path.join(root_path, 'dec_picture' + _SLASH)
    # 文件源路径
    src_file_path = os.path.join(root_path, 'src_file' + _SLASH)
    # 文件目标路径，用来保存收到文件
    des_file_path = os.path.join(root_path, 'des_file' + _SLASH)


if __name__ == '__main__':
    test = Path_Config()
    print(test.root_path)
    print(test.log_path)
