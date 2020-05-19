import hashlib
import json
from time import time

import requests
from django.shortcuts import render

# Create your views here.


def get_h5_html(request):
    """点播h5"""
    vid = request.GET.get("vid")
    if not vid:
        vid = ''  # 视频对应vid
    ts = int(time() * 1000)
    userId = ''
    secretkey = ''
    viewerIp = get_client_ip(request)
    viewerId = '12345'
    viewerName = 'testUser'
    extraParams = 'HTML5'
    concated = 'extraParams{}ts{}userId{}videoId{}viewerId{}viewerIp{}viewerName{}'.format(extraParams,ts,userId,
                                                                                                   vid,viewerId,viewerIp,viewerName)
    plain = secretkey+concated+secretkey
    sign = get_md5(plain).upper()  #  取大写MD5
    token_data = {
        'userId': userId, 'videoId': vid,
        'ts': ts, "viewerIp": viewerIp,
        'viewerName': viewerName, 'extraParams': extraParams,
        'viewerId': viewerId, 'sign': sign
    }
    token = get_token(token_data)
    hash_sign = get_md5(secretkey+vid+str(ts))
    context = {
        "type": type,
        "vid": vid,
        "playsafe": token,
        "ts": ts,
        "sign": hash_sign
    }
    return render(request, 'h5_player_test.html', context)


def get_client_ip(request):
    """获取ip"""
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_md5(str):
    """md5加密"""
    hash_md5 = hashlib.md5()
    b = str.encode(encoding='utf-8')
    hash_md5.update(b)
    str_md5 = hash_md5.hexdigest()
    return str_md5


def get_token(data):
    """获取token"""
    url = ''
    result = json.loads(requests.post(url,data).content)
    token = result.get("data").get("token")
    return token