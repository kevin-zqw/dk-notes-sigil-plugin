# 查找注释和链接
1. `<sup><a href>与<p><a id>自动匹配`
2. `正文编号[1]，与后续段落注释<p>[1]对应`
3. `正则预先处理成统一格式，比如[id_href]，与<p>[id_href]注释内容</p>`
4. `OCR文本，注释直接插入正文中：xxxxxxxx【这是注释】`

# 输出类型
1. 弹注（多看，兼容中亚）
2. 夹注（`<span class="xxx"></span>`）

# 实现思路
1. 无论是哪种方式来查找和匹配注释，也无论是 章后注，段间注，行间注，篇后注（跨HTML）。第一步是把注释的位置与注释内容一一对应起来，100%匹配上，才会进行下一步
2. 把注释内容全部提取出来，删除原有的注释行；插入注释内容到相应的注释编号的位置，这里会使用一个中间格式（待定）
3. 根据用户选择输出类型，生成多看注释，夹注

# TODO
1. 连续四个以上的空行（\n\s）正则删除：`re.sub(r'\n\s*\n','\n',a,re.MULTILINE)`
2. 提供弹注选项，是否包含`◎`字符
3. ePub3标准，需要改命名空间，参考第10章
4. 注中注如何匹配？如何替换？

# 备忘
1. `soup.select('sup > a[id]')`
2. `span.unwrap()`取出文本
3. `span.extract()`删除tag
