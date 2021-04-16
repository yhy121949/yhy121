def get_json_pre_or_post(data, key):
    """
    字符串解析的形式，获取json文件中pre_process或者post_process的值
    :param send_request:
    :param key: "pre_process" or "post_process"
    :return:
    """
    if key not in ["pre_process", "post_process"]:
        return []
    index = data.find(key)
    if index == -1:
        return []
    data = data[index:]
    data = data[data.find(":") + 1:]

    print(data)


a = '''
{
  "feature": "流程用例",
  "story": "新用户下单流程",
  "title": "登录",
  "service": "mall",
  "method": "POST",
  "url": "/api/v1/user/login",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "loginName": "",
    "passwordMd5": "$MD5(123456)$"
  },
  "files": {
  },
  "post_process": []
}
'''
get_json_pre_or_post(a, "pre_process")
