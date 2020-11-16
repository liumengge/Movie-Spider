# search，它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果。
# 也就是说，正则表达式可以是字符串的一部分，在匹配时，search 方法会依次扫描字符串，直到找到第一个符合规则的字符串，然后返回匹配内容，
# 如果搜索完了还没有找到，就返回 None

import re

# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)


html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

# 尝试提取 class为 active 的 li 节点内部超链接包含的歌手名和歌名，此时需要提取第三个 li 节点下 a 节点的 singer 属性和文本。
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))










