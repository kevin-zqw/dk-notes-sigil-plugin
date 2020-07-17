# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab

from __future__ import unicode_literals, division, absolute_import, print_function

import os
import sys
import re
from tkdialogs import launch_tk_gui as launch_gui


_DEBUG_ = False
prefs = {}
search_type = 'sup'
output_type = 'duokan'
mix_notes_class = 'jia-zhu'
add_notes_mark = True


def run(bk):
    global _DEBUG_
    global prefs
    global search_type
    global output_type
    global mix_notes_class
    global add_notes_mark

    prefs = bk.getPrefs()

    # set default preference values
    if 'debug' not in prefs:
        prefs['debug'] = _DEBUG_
    if 'search_type' not in prefs:
        prefs['search_type'] = search_type
    if 'output_type' not in prefs:
        prefs['output_type'] = output_type
    if 'mix_notes_class' not in prefs:
        prefs['mix_notes_class'] = mix_notes_class
    if 'add_notes_mark' not in prefs:
        prefs['add_notes_mark'] = add_notes_mark
    if 'windowGeometry' not in prefs:
        prefs['windowGeometry'] = None

    ''' Launch Main Dialog '''
    launch_gui(bk, prefs)

    _DEBUG_ = prefs['debug']
    search_type = prefs['search_type']
    output_type = prefs['output_type']
    mix_notes_class = prefs['mix_notes_class']
    add_notes_mark = prefs['add_notes_mark']

    print('*****************多看注释插件（终结版）*****************\n\n')

    print('Python路径: {}'.format(sys.path))
    print('是否调试模式: {}\n'.format(_DEBUG_))

    print('查找方式: {}'.format(search_type))
    print('输出方式: {}'.format(output_type))
    print('夹注样式: {}'.format(mix_notes_class))
    print('注释是否添加◎字符: {}'.format(add_notes_mark))

    print('\n---------------插件开始运行---------------\n')

    # get all html files

    print('\n---------------插件运行完毕---------------\n')
    return 0


def main():
    print('I reached main when I should not have\n')
    return -1


if __name__ == "__main__":
    sys.exit(main())
