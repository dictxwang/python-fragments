# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import sys
import argparse
import optparse

'''
使用argparse / optparse解析命令行参数，两种解析方式选其一即可
其中optparse已停止更新
'''


def do_opt_parse():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--type", dest="type", type="string", metavar="t001", help="some tips for type.")
    parser.add_option("-v", "--version", dest="version", type="string", metavar="1.0", help="some tips for version.")
    parser.add_option("-n", "--number", dest="number", type="int", default=1, metavar="10",
                      help="some tips for number.")
    (options, sys.argv[1:]) = parser.parse_args()
    return options


def do_arg_parse():
    aparser = argparse.ArgumentParser()
    aparser.add_argument("-t", "--type", dest="type", metavar="t001", default="t002", help="some tips for type.")
    aparser.add_argument("-v", "--version", dest="version", metavar="1.0", help="some tips for version.")
    args = aparser.parse_args()
    return args


def add(args):
    print("{} + {} = {}".format(args.x, args.y, args.x + args.y))


def sub(args):
    print("{} - {} = {}".format(args.x, args.y, args.x - args.y))


def do_arg_subparse():
    parser = argparse.ArgumentParser(prog="PROG")
    subparsers = parser.add_subparsers(help="sub-command help")
    parser_add = subparsers.add_parser("add", help="add help")
    parser_add.add_argument("-x", type=int, help="give add parameter for x", metavar=0)
    parser_add.add_argument("-y", type=int, help="give add parameter for y", metavar=0)
    parser_add.set_defaults(func=add)

    parser_sub = subparsers.add_parser("sub", help="sub help")
    parser_sub.add_argument("-x", type=int, default=1, help="give sub parameter for x", metavar=1)
    parser_sub.add_argument("-y", type=int, default=1, help="give sub parameter for y", metavar=1)
    parser_sub.set_defaults(func=sub)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":

    # print(do_opt_parse())
    # print(do_arg_parse())
    do_arg_subparse()
