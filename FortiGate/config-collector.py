#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import datetime

# SSL自己証明書エラー出力の抑止
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    # リモートログイン情報
    # コンフィグ取得対象機器の環境に合わせて適宜変更すること
    username = 'testuser'
    password = 'testpass'
    hostname = 'FW01'
    ipaddr = '192.168.0.1'
    
    # REST APIキー取得
    url = 'https://' + ipaddr + '/logincheck'
    res_logincheck = requests.post(url, data = payload, verify = False)
    
    # Config取得
    url = 'https://' + ipaddr + '/api/v2/monitor/system/config/backup/?destination=file&scope=global'
    res_backup = requests.get(url, cookies = res_logincheck.cookies, verify = False)
    
    # ファイル書き込み
    filename = hostname + datetime.now().strftime("%Y%m%d-%H%M%S")
    with open(filename, 'w') as f:
        f.write(res_backup.text.decode('utf-8')

if __name__ == "__main__":
    main()
