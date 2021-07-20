# -*- coding: utf-8 -*-
# author: Yabin Zheng
# Email: sczhengyabin@hotmail.com

from __future__ import print_function

import argparse

import crawler
import downloader
import sys


def main(argv):
    parser = argparse.ArgumentParser(description="Image Downloader")
    parser.add_argument("keywords", type=str,
                        help='搜索关键词')
    parser.add_argument("--engine", "-e", type=str, default="baidu",
                        help="抓取网站.", choices=["baidu", "bing", "360"])
    parser.add_argument("--max-number", "-n", type=int, default=100,
                        help="下载图片数量")
    parser.add_argument("--num-threads", "-j", type=int, default=50,
                        help="进程数")
    parser.add_argument("--timeout", "-t", type=int, default=20,
                        help="下载超时")
    parser.add_argument("--output", "-o", type=str, default="./download_images",
                        help="输出文件夹")
    parser.add_argument("--user-proxy", "-p", type=str, default=False,
                        help="是否使用代理(默认不使用)")

    args = parser.parse_args(args=argv)
    # 默认不加代理
    use_proxy = False
    crawled_urls = crawler.crawl_image_urls(args.keywords,
                                            engine=args.engine, max_number=args.max_number,
                                            use_proxy=use_proxy)
    downloader.download_images(image_urls=crawled_urls, folder_dir=args.output,
                               max_workers=args.num_threads, timeout=args.timeout,
                               use_proxy=use_proxy, file_prefix=args.engine)

    print("Finished.")


if __name__ == '__main__':
    main(sys.argv[1:])
