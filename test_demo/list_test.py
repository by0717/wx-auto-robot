# keywords 定义
keywords = {
        "R3s": "请稍等",
        "R3S": "请稍等",
        "R3s-3": "请稍等",
        "r3s": "请稍等"
        }
str_test_1 = "R3s怎么这么垃圾"
str_test_2 = "R 怎么3 这么垃圾 s"

bool_p = any(word if word in str_test_2 else False for word in keywords.keys())

print(bool_p)