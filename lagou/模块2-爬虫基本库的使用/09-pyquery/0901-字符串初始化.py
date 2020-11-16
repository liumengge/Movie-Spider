html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq

doc = pq(html)
# 这里首先引入 pyquery 这个对象，取别名为 pq，然后声明了一个长 HTML 字符串，
# 并将其当作参数传递给 pyquery 类，这样就成功完成了初始化
print(doc('li'))  # 将初始化的对象传入 CSS 选择器





