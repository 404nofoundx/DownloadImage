""" Download image according to given urls and automatically rename them in order. """
# -*- coding: utf-8 -*-
# author: Yabin Zheng
# Email: sczhengyabin@hotmail.com

from __future__ import print_function

import hashlib
import shutil
import imghdr
import os
import concurrent.futures
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Proxy-Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, sdch",
}


def download_image(image_url, dst_dir, file_prefix, timeout=20, use_proxy=False):
    proxies = None
    # if proxy_type:
    #     proxies = {
    #         "http": proxy_type + "://" + proxy,
    #         "https": proxy_type + "://" + proxy
    #     }
    response = None
    try_times = 0
    while True:
        try:
            try_times += 1
            response = requests.get(
                image_url, headers=headers, timeout=timeout, proxies=proxies)
            image_name = get_img_name(response.content)
            file_name = file_prefix + "_" + image_name
            file_path = os.path.join(dst_dir, file_name)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            response.close()
            file_type = imghdr.what(file_path)
            if file_type in ["jpg", "jpeg", "png", "bmp"]:
                new_file_name = "{}.{}".format(file_name, file_type)
            else:
                new_file_name = "{}.{}".format(file_name, 'jpg')
            new_file_path = os.path.join(dst_dir, new_file_name)
            shutil.move(file_path, new_file_path)
            print("##下载成功:  {} ".format(new_file_name))
            break
        except Exception as e:
            if try_times < 3:
                continue
            if response:
                response.close()
            print("##下载错误:  {}  {}".format(e.args,image_url))
            break


def download_images(image_urls, folder_dir='./download_images', file_prefix="img", max_workers=50, timeout=20, use_proxy=False):
    """
    图片下载
    :param image_urls:图片列表
    :param folder_dir:文件夹地址
    :param file_prefix:文件来源
    :param max_workers:最大并发
    :param timeout:下载超时
    :param use_proxy:是否使用代理
    :return:
    """

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_list = list()
        count = 0
        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)
        for image_url in image_urls:
            future_list.append(executor.submit(
                download_image, image_url, folder_dir, file_prefix, timeout, use_proxy))
            count += 1
        concurrent.futures.wait(future_list, timeout=180)


def get_img_name(image_url):
    """
    图片name
    :param image_url:
    :return:
    """
    md5 = hashlib.md5()
    md5.update(image_url)
    image_name = md5.hexdigest()
    return image_name