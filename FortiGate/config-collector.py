#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import requests
import csv
import datetime

# コンフィグ取得時の文字コード処理対策
reload(sys)
sys.setdefaultencoding('utf-8')

# SSL自己証明書エラー出力の抑止
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 入出力パラメータ
backup_dir = './' # コンフィグファイル出力先
target_file = './fortigate.csv' # コンフィグ取得対象機器リスト

def getConfig(ipaddr, username, password):
    """ コンフィグ取得処理
    """
    
    # REST APIキー取得
    payload = {'username':username, 'secretkey':password}
    url = 'https://' + ipaddr + '/logincheck'
    res_logincheck = requests.post(url, data = payload, verify = False)
    
    # コンフィグ取得
    url = 'https://' + ipaddr + '/api/v2/monitor/system/config/backup/?destination=file&scope=global'
    res_backup = requests.get(url, cookies = res_logincheck.cookies, verify = False)
    
    return res_backup.text.decode('utf-8')


def main():
    with open(target_list, 'r') as in_file:
        rows = csv.reader(in_file, delimiter=',', doublequote=True, lineterminator="\n", quotechar='"', skipinitialspace=True)
        for row in rows:
            hostname = row[0]
            ipaddr = row[1]
            username = row[2]
            password = row[3]
            
            config = getConfig(ipaddr, username, password)
            result_file = backup_dir + hostname + datetime.datetime.now().strftime("_%Y%m%d-%H%M%S") + '.confg'
            with open(result_file, 'w') as out_file:
                out_file.write(config)


if __name__ == "__main__":
    main()
