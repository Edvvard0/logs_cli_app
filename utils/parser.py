
def pars_log_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        logs = f.readlines()

    return logs

# print(pars_log_file("../app1.log"))