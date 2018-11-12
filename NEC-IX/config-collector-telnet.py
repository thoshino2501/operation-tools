#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import telnetlib
import datetime

### account
### ToDo: Configファイルから読み込めるようにする
user = 'dummy'
password = 'dummy'

### set param
### ToDo: 引数のエラー処理を入れる 
host = sys.argv[1]
port = 23
port = sys.argv[2]
timeout = 3
prompt = {
    'general': '> ',
    'enable': '# ',
    'login': 'login: ',
    'password': 'Password: '
}
nl = "\r\n" # new line character

### Telnet接続
### IXの場合はTelnetオプション
tn = telnetlib.Telnet()
# tn.set_debuglevel(3)
tn.set_option_negotiation_callback(lambda x,y,z:None)
tn.open(host, port, timeout)

### ログイン処理
### IXの場合はTelnetオプション送信を無効化する
tn.read_until(prompt['login'], timeout)
tn.write(user + nl)
tn.read_until(prompt['password'], timeout)
tn.write(password + nl)

### 自動実行させたい内容
tn.read_until(prompt['general'], timeout)
tn.write("enable" + nl)
tn.read_until(prompt['enable'], timeout)
tn.write("terminal length 0" + nl)
tn.read_until(prompt['enable'], timeout)
tn.write("show run" + nl)
result =tn.read_until(prompt['enable'], timeout)
tn.write("exit" + nl)
tn.close()

### ファイル書き出し
filename = host + "_" + datetime.now().strftime("%Y%m%d-%H%M%S")
fp=open(filename,"w")
fp.write(output)
fp.close()
