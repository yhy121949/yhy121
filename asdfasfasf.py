import jsonpath


def json_extractor(json_path):
    """
    根据jsonpath提取响应中的数据
    :param send_request: SendRequest对象实例
    :param var_name: 变量名
    :param json_path: jsonpath
    :param match_no: 匹配结果中的第几个，0表示随机取一个
    :param default: 默认值
    :return:
    """

    data = {
  "resultCode": 200,
  "message": "SUCCESS",
  "data": "19a21ebf78f40e6e9e2b28f02add7271"
}
    res = jsonpath.jsonpath(data, json_path)
    print(res)

json_extractor('$.data')