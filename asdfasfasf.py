def get_file_key(file_path):
    file_path = file_path.replace("\\", "/")
    file_path_list = file_path.split("/")
    length = len(file_path_list)
    if length == 1:
        return file_path_list[0]
    if "json_data" not in file_path:
        assert False, "json文件，必须存放于test_case/json_data文件夹及其子文件夹中"
    for i in range(length):
        if file_path_list[i] == "json_data":
            if length - 1 > i:
                file_path_list = file_path_list[i + 1:]
            break
    print(file_path_list)
    return "/".join(file_path_list)


print(get_file_key("test_case/json_data/user/register.json"))
