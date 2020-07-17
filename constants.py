# -*- coding: utf-8 -*-
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

from __future__ import unicode_literals, division, absolute_import, print_function

pref_search_type = 'search_type'
pref_output_type = 'output_type'
pref_windowGeometry = 'windowGeometry'
pref_debug = 'debug'
pref_add_notes_mark = 'add_notes_mark'
pref_mix_notes_class = 'mix_notes_class'

search_type_sup = 'sup'
search_type_paragraph = 'paragraph'
search_type_preprocessed = 'preprocessed'
search_type_brackets = 'brackets'

search_type_dict = {
    search_type_sup: '中亚注释：<sup><a/></sup>自动查找',
    search_type_paragraph: '段间注：正文[1]，后续段落<p>[1]</p>',
    search_type_preprocessed: '正则预处理：正文[id:href]；注释<p>[id:href]注释内容</p>',
    search_type_brackets: '原始文本中括号：正文【【注释】】',
}

output_duokan = 'duokan'
output_mix = 'mix'

output_type_dict = {
    output_duokan: '多看兼容弹注',
    output_mix: '夹注',
}

default_mix_notes_class = 'jia-zhu'
