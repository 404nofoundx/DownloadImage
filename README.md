# DownloaderImage

## 1. 简介

输入一组关键词，指定所需图片个数，在常见搜索引擎中检索，记录图片url地址，并将图片保存在指定目录下。
+ 百度图片：https://image.baidu.com/
+ 360搜图：https://image.so.com/
+ 微软：https://cn.bing.com/images/trending?FORM=ILPTRD）


## 2. 功能

+ 支持的搜索引擎: 360, 必应, 百度
+ 可配置线程数及代理

## 3. 安装

### 3.1 安装相关python库


```bash
pip3 install -r requirements.txt
```

## 4. 如何使用

### 4.1 命令行

```bash
usage: image_downloader.py [-h] [--engine {baidu,bing,360}]
                           [--max-number MAX_NUMBER]
                           [--num-threads NUM_THREADS] [--timeout TIMEOUT]
                           [--output OUTPUT] [--user-proxy USER_PROXY]
                           keywords
```
help
```bash
usage: image_downloader.py [-h] [--engine {baidu,bing,360}] [--max-number MAX_NUMBER] [--num-threads NUM_THREADS] [--timeout TIMEOUT] [--output OUTPUT] [--user-proxy USER_PROXY]
                           keywords

Image Downloader

positional arguments:
  keywords              搜索关键词

optional arguments:
  -h, --help            show this help message and exit
  --engine {baidu,bing,360}, -e {baidu,bing,360}
                        抓取网站.
  --max-number MAX_NUMBER, -n MAX_NUMBER
                        下载图片数量
  --num-threads NUM_THREADS, -j NUM_THREADS
                        进程数
  --timeout TIMEOUT, -t TIMEOUT
                        下载超时
  --output OUTPUT, -o OUTPUT
                        输出文件夹
  --user-proxy USER_PROXY, -p USER_PROXY
                        是否使用代理(默认不使用)
```

关注公众号是对我开源最大的支持！
![公众号](https://github.com/404SpiderMan/DownloadImage/blob/main/biz.jpg)



参考项目:https://github.com/sczhengyabin/Image-Downloader
