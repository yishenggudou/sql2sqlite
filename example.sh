#!/bin/bash
#Author: timger <yishenggudou@gmail.com>
#weibo <http://t.sina.com/zhanghaibo>
#@yishenggudou http://twitter.com/yishenggudou
sh mysql2sqlite.sh -u timger -p -h 106.186.117.23 apiserver meizitu|sqlite3 apiserver.meizitu.sqlite
