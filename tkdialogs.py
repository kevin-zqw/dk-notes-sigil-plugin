# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab

from __future__ import unicode_literals, division, absolute_import, print_function

import sys
import os

import tkinter


def launch_tk_gui(bk, prefs):
    root = tkinter.Tk()
    root.withdraw()
    root.title('')
    root.resizable(True, True)
    root.minsize(440, 420)
    if not sys.platform.startswith('darwin'):
        img = tkinter.Image('photo', file=os.path.join(bk._w.plugin_dir, bk._w.plugin_name, 'images/icon.png'))
        root.tk.call('wm','iconphoto',root._w,img)
    guiMain(root, bk, prefs).pack(fill=tkinter.constants.BOTH, expand=True)
    root.mainloop()


class guiMain(tkinter.Frame):
    def __init__(self, parent, bk, prefs):
        tkinter.Frame.__init__(self, parent, border=5)
        self.parent = parent
        # Edit Plugin container object
        self.bk = bk
        self.prefs = prefs

        if self.prefs['windowGeometry'] is None:
            # Sane geometry defaults
            w = self.parent.winfo_screenwidth()
            h = self.parent.winfo_screenheight()
            rootsize = (440, 420)
            x = w/2 - rootsize[0]/2
            y = h/2 - rootsize[1]/2
            self.prefs['windowGeometry'] = ('%dx%d+%d+%d' % (rootsize + (x, y)))

        self.initUI()
        parent.protocol('WM_DELETE_WINDOW', self.quitApp)

    def initUI(self):
        ''' Build the GUI and assign variables and handler functions to elements. '''
        self.parent.title(self.bk._w.plugin_name)
        body = tkinter.Frame(self)

        title_label_frame = tkinter.Frame(body)
        dash_label = tkinter.Label(title_label_frame, text='多看注释插件（终结版）', pady=3)
        dash_label.pack(fill=tkinter.constants.BOTH)
        title_label_frame.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        tkinter.Label(body, pady=0).pack()

        search_type_label_frame = tkinter.Frame(body)
        search_type_label = tkinter.Label(search_type_label_frame, text='注释查找和匹配方式')
        search_type_label.pack(side=tkinter.constants.LEFT)
        search_type_label_frame.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        # search types
        search_frame = tkinter.Frame(body, bd=1, relief=tkinter.constants.GROOVE)
        self.searchType = tkinter.StringVar()

        # sup
        radio_frame_sup = tkinter.Frame(search_frame)
        radio_search_sup = tkinter.Radiobutton(radio_frame_sup, text='中亚注释：<sup><a/></sup>自动查找',
                                               var=self.searchType, value='sup')
        radio_search_sup.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.BOTH)
        radio_frame_sup.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        # paragraph
        radio_frame_paragraph = tkinter.Frame(search_frame)
        radio_search_paragraph = tkinter.Radiobutton(radio_frame_paragraph, text='段间注：正文[1]，后续段落<p>[1]</p>',
                                                     var=self.searchType, value='paragraph')
        radio_search_paragraph.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.BOTH)
        radio_frame_paragraph.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        # preprocessed
        radio_frame_preprocessed = tkinter.Frame(search_frame)
        radio_search_preprocessed = tkinter.Radiobutton(radio_frame_preprocessed, text='正则预处理：正文[id:href]；注释<p>[id:href]注释内容</p>',
                                                        var=self.searchType, value='preprocessed')
        radio_search_preprocessed.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.BOTH)
        radio_frame_preprocessed.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        # brackets
        radio_frame_brackets = tkinter.Frame(search_frame)
        radio_search_brackets = tkinter.Radiobutton(radio_frame_brackets, text='原始文本中括号：正文【【注释】】',
                                                    var=self.searchType, value='brackets')
        radio_search_brackets.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.BOTH)
        radio_frame_brackets.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        search_frame.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        search_type = self.prefs['search_type']
        if search_type == 'sup':
            radio_search_sup.select()
        elif search_type == 'paragraph':
            radio_search_paragraph.select()
        elif search_type == 'preprocessed':
            radio_search_preprocessed.select()
        else:
            radio_search_brackets.select()

        tkinter.Label(body, pady=0).pack()

        output_type_label_frame = tkinter.Frame(body)
        output_type_label = tkinter.Label(output_type_label_frame, text='输出类型')
        output_type_label.pack(side=tkinter.constants.LEFT)
        output_type_label_frame.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        # output types
        output_frame = tkinter.Frame(body, bd=1, relief=tkinter.constants.GROOVE)
        self.outputType = tkinter.StringVar()

        # DuoKan notes
        radio_frame_duokan = tkinter.Frame(output_frame)
        radio_output_duokan = tkinter.Radiobutton(radio_frame_duokan, text='多看兼容弹注',
                                                  var=self.outputType, value='duokan')
        radio_output_duokan.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.BOTH)
        radio_frame_duokan.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        # add mark char before notes
        self.add_notes_mark = tkinter.BooleanVar()
        checkbox_add_notes_mark_frame = tkinter.Frame(output_frame)
        checkbox_add_notes_mark = tkinter.Checkbutton(checkbox_add_notes_mark_frame, text='注释内容前添加◎字符',
                                                        variable=self.add_notes_mark)
        checkbox_add_notes_mark.pack(side=tkinter.constants.LEFT, padx=20, fill=tkinter.constants.BOTH)
        checkbox_add_notes_mark_frame.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)
        if self.prefs['add_notes_mark']:
            checkbox_add_notes_mark.select()

        # Mix notes
        radio_frame_mix = tkinter.Frame(output_frame)
        radio_output_mix = tkinter.Radiobutton(radio_frame_mix, text='夹注',
                                                   var=self.outputType, value='mix')
        radio_output_mix.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.BOTH)
        radio_frame_mix.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        # Mix span class
        mix_span_class_frame = tkinter.Frame(output_frame)
        mix_span_class_label = tkinter.Label(mix_span_class_frame, text='span样式名:')
        mix_span_class_label.pack(side=tkinter.constants.LEFT, padx=20)

        self.mix_notes_class_entry = tkinter.Entry(mix_span_class_frame)
        self.mix_notes_class_entry.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.BOTH, expand=1)
        self.mix_notes_class_entry.insert(0, self.prefs['mix_notes_class'])

        mix_span_class_frame.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        output_type = self.prefs['output_type']
        if output_type == 'duokan':
            radio_output_duokan.select()
        else:
            radio_output_mix.select()

        output_frame.pack(side=tkinter.constants.TOP, fill=tkinter.constants.BOTH)

        self.debug = tkinter.BooleanVar()
        checkbox_debug = tkinter.Checkbutton(body, text='调试模式（不修改文本，仅查找并报告不匹配的注释项）',
                                             variable=self.debug)
        checkbox_debug.pack(side=tkinter.constants.BOTTOM, pady=10, anchor=tkinter.constants.W)
        if self.prefs['debug']:
            checkbox_debug.select()

        # Dialog buttonbox (three buttons)
        buttons = tkinter.Frame()
        self.gbutton = tkinter.Button(buttons, text='运行插件', command=self.cmdDo)
        self.gbutton.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.BOTH, expand=True)
        self.qbutton = tkinter.Button(buttons, text='取消', command=self.cmdCancel)
        self.qbutton.pack(side=tkinter.constants.LEFT, fill=tkinter.constants.BOTH, expand=True)
        buttons.pack(side=tkinter.constants.BOTTOM, pady=5, padx=5, fill=tkinter.constants.BOTH)

        body.pack(fill=tkinter.constants.BOTH)

        # Get the saved window geometry settings
        self.parent.geometry(self.prefs['windowGeometry'])
        self.parent.deiconify()
        self.parent.lift()


    def cmdDo(self):
        self.prefs['search_type'] = self.searchType.get()
        self.prefs['output_type'] = self.outputType.get()
        self.prefs['windowGeometry'] = self.parent.geometry()
        self.prefs['debug'] = self.debug.get()
        self.prefs['add_notes_mark'] = self.add_notes_mark.get()
        if len(self.mix_notes_class_entry.get()):
            self.prefs['mix_notes_class'] = self.mix_notes_class_entry.get()

        self.bk.savePrefs(self.prefs)
        self.quitApp()

    def cmdCancel(self):
        '''Close aborting any changes'''
        self.prefs['windowGeometry'] = self.parent.geometry()
        self.prefs['debug'] = self.debug.get()
        self.bk.savePrefs(self.prefs)
        self.quitApp()

    def quitApp(self):
        '''Clean up and close Widget'''
        try:
            self.parent.destroy()
            self.parent.quit()
        except:
            pass


def main():
    ''' For debugging the tkinter dialog outside of the sigil plugin '''
    from datetime import datetime, timedelta
    prefs = {}

    # Fake book container object
    class w(object):
        def __init__(self):
            w.plugin_name = 'dk-notes-sigil-plugin'
            w.plugin_dir = '/Users/kevin/GitHub'

    class bk(object):
        def __init__(self):
            bk._w = w()

        def savePrefs(self, dummy):
            return
    sim_bk = bk()

    prefs['search_type'] = 'sup'
    prefs['output_type'] = 'duokan'
    prefs['windowGeometry'] = None
    prefs['debug'] = False
    prefs['add_notes_mark'] = True
    prefs['mix_notes_class'] = 'jia-zhu'

    launch_tk_gui(sim_bk, prefs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
