# PDF2sentence

使用方法:
后台运行`PDF2sentence_auto.py`, 将论文中的一段复制到`pdf_input.txt`里面(文段跨页的情况), 保存文件翻译结果到`pdf_output.txt`.
运行``PDF2sentence.py直接复制到粘贴板, 运行代码即可得到结果.

代码中第三行选择句子从windows粘贴板获取还是从`pdf_input.txt`获取. 然后对两种数据源分别做了分词操作后, 得到一段字符串, 然后放到百度API进行翻译. 最后打印出原文与翻译.
