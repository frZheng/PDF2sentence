
import os,time
import PDF2sentence
from hashlib import md5
def check_change():
    f1 = open('pdf_input.txt', 'r')
    # print(f1.read())
    target_str = f1.read()
    f1.close()
    res = md5(target_str.encode(encoding='UTF-8')).hexdigest()
    # print(res)
    return res
# check_change()
# exit()
if __name__ == "__main__":
    # chmod_input()
    # exit()
    code_version = 202111221400
    # print(os.getcwd())
    # print("file name: %s" % (__file__), ", code Version: ", code_version)

    last_line = check_change()
    while True:
        time.sleep(0.1)
        line = check_change()
        # print(line)
        if line is not None and line != last_line:
            last_line = line
            PDF2sentence.get_data(1)
            print("new line:", line)

