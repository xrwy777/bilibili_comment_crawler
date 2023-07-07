# B站评论爬虫

<!-- TOC -->
- [B站评论爬虫](#b站评论爬虫)
  - [使用说明](#使用说明)
  - [现有功能](#现有功能)
  - [TODO](#todo)
<!-- /TOC -->

## 使用说明

<details>
<summary>安装</summary>

克隆 repo，在 Python 环境中安装 requirements.txt

```bash
git clone https://github.com/ultralytics/yolov5  # clone
cd bilibili_comment_crawler
pip install -r requirements.txt  # install
```

</details>

<details>
<summary>使用方式</summary>
运行mian.py，输入要爬取的b站视频网址
</details>

<details>
<summary>输出</summary>
输出在当前目录下的output文件夹，包含xls文件和txt文件
</details>

## 现有功能

- 输入要爬取评论的b站视频网址，将爬取的评论输出到excel和txt文件中

## TODO

- 引入图形化界面，对已经爬取的视频记录输出
