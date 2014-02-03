#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright 2011 timger
#    +Author timger
#    +Gtalk&Email yishenggudou@gmail.com
#    +Msn yishenggudou@msn.cn
#    +Weibo @timger http://t.sina.com/zhanghaibo
#    +twitter @yishenggudou http://twitter.com/yishenggudou
#    Licensed under the MIT License, Version 2.0 (the "License");


import os

DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
NAME_FILE = os.path.relpath(__file__)
from sqlalchemy import create_engine
from sqlalchemy import text

__author__ = 'timger & yishenggudou@gmail.com'
__license__ = 'MIT'
__version__ = (0, 0, 0)


def table2sqlite(uri, path, table=None):
    dbpath = os.path.abspath(path)
    sql_engine = create_engine(uri, echo=True, echo_pool=True)
    sql = "SHOW CREATE TABLE `{table}`".format(table=table)
    table_sql = sql_engine.execute(text(sql)).fetchone()[1]
    print '>>>' * 10
    print table_sql
    print '>>>' * 10
    sqlite_uri = "sqlite:///{p}".format(p=dbpath)
    sqlite_engine = create_engine(sqlite_uri, echo=True, echo_pool=True)
    sqlite_engine.execute(text(table_sql))
    sql = "SELECT * FROM `{table}`".format(table=table)
    rows = sql_engine.execute(text(sql)).fetchall()
    for row in rows:
        sql = """INSERT INTO `{table}` VALUES ({vals});"""
        sql = sql.format(table=table, vals=','.join(list(row)))
        sqlite_engine.execute(text(sql))


def main():
    import argparse
    parser = argparse.ArgumentParser(description='sqltable 2 sqlite')
    parser.add_argument('--dburl', type=str,
                        help="""sqlalchemy db url like:\
                        mysql+mysqldb://timger:timger@127.0.0.1:3306/sitespider
                        """)
    parser.add_argument('table', type=str,
                        help='db table name')
    parser.add_argument('name', type=str,
                        help='sqlite database name')
    args = parser.parse_args()
    table2sqlite(args.dburl, args.name, args.table)

if __name__ == "__main__":
    main()
