sentence_lines = ""

if 0:
    file_name = "pdf_input.txt"
    with open(file_name,"r",encoding='utf-8') as fin:
        for line in fin.readlines():
            line = line[:-1] # 去掉\n
            if line[-1] == " " and line[-2] == "-":
                sentence_lines += line[:-2] # 去掉 -
            elif line[-1] == " ":
                sentence_lines += line
            elif line[-1] == "-":
                sentence_lines += line[:-1]
            else:
                sentence_lines += line + " "
else:
    import win32clipboard
    import win32con
    def get_text():
        win32clipboard .OpenClipboard()
        text_result = win32clipboard .GetClipboardData(win32con.CF_UNICODETEXT)
        win32clipboard .CloseClipboard()
        return text_result
    lines = get_text()
    lines = lines.split("\r\n")
    # print(lines)
    for line in lines:
        if line[:-1] == "\n":
            line = line[:-1] # 去掉\n
        if line[-1] == " " and line[-2] == "-":
            sentence_lines += line[:-2] # 去掉 -
        elif line[-1] == " ":
            sentence_lines += line
        elif line[-1] == "-":
            sentence_lines += line[:-1]
        else:
            sentence_lines += line + " "


sentence_lines = sentence_lines[:-1]
sentence_lines += "."
print("\n\n",sentence_lines)




import random
import hashlib
import urllib.parse
import json
import http.client


def baidu_translation(content):

    appid = '20220223001091634'  # 你的appid
    secretKey = 'WzgnVDEF671wwZnAh6OM'  # 你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        # print(js)
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return (dst)  # 打印结果
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()


res = baidu_translation(sentence_lines)
print(res,"\n\n")

file_name = "pdf_output.txt"
with open(file_name,"w",encoding='utf-8') as fout:
    fout.write(sentence_lines)
    fout.write("\n")
    fout.write(res)
