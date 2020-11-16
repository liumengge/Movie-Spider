## 子节点

# from pyquery import PyQuery as pq
#
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1">
#             <a href="link2.html">second item</a>
#          </li>
#          <li class="item-0 active">
#             <a href="link3.html"><span class="bold">third item</span></a>
#          </li>
#          <li class="item-1 active">
#             <a href="link4.html">fourth item</a>
#          </li>
#          <li class="item-0">
#             <a href="link5.html">fifth item</a>
#          </li>
#      </ul>
#  </div>
# '''
#
# doc = pq(html)
# items = doc('.list')  # 通过 .list  参数选取 class 为 list 的节点，然后调用 find 方法，传入 CSS 选择器，选取其内部的 li 节点，最后打印输出
# print(type(items))
# print(items)
# lis = items.find('li')  # find 的查找范围是节点的所有子孙节点
# print(type(lis))
# print(lis)
#
#
# # 如果我们只想查找子节点，那可以用 children 方法
# lis = items.children()
# print(type(lis))
# print(lis)
#
# # 如果要筛选所有子节点中符合条件的节点，比如想筛选出子节点中 class 为 active 的节点，可以向 children 方法传入 CSS 选择器 .active
# lis = items.children('.active')
# print(lis)



## 父节点
# 用 parent 方法来获取某个节点的父节点
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''

# from pyquery import PyQuery as pq
#
# doc = pq(html)
# items = doc('.list')
# container = items.parent()  # 直接父节点，也就是说，它不会再去查找父节点的父节点，即祖先节点
# print(type(container))
# print(container)
#
# # 想获取某个祖先节点，该怎么办呢？我们可以用 parents 方法
#
# doc = pq(html)
# items = doc('.list')
# parents = items.parents()
# print(type(parents))
# print(parents)


## 兄弟节点：siblings 方法

## 节点遍历
# pyquery 的选择结果既可能是多个节点，也可能是单个节点，类型都是 pyquery 类型，并没有返回列表

# 对于单个节点来说，可以直接打印输出，也可以直接转成字符串

# 对于有多个节点的结果，我们就需要用遍历来获取了。例如，如果要把每一个 li 节点进行遍历，需要调用 items 方法：
# from pyquery import PyQuery as pq
#
# doc = pq(html)
# lis = doc('li').items()  # 调用 items 方法后，会得到一个生成器，遍历一下，就可以逐个得到 li 节点对象了，它的类型也是 pyquery 类型
# print(type(lis))
# for li in lis:
#     print(li, type(li))


## 提取节点中的信息

### 获取属性: attr 方法
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
#
# from pyquery import PyQuery as pq
#
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a))
# print(a.attr('href'))
# # 也可以通过调用 attr 属性来获取属性值，
# print(a.attr.href)

# 当返回结果包含多个节点时，调用 attr 方法，只会得到第 1 个节点的属性，想要获取所有的节点属性就需要遍历

# doc = pq(html)
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))

### 获取文本：text 方法
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

from pyquery import PyQuery as pq

doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text())

# 若想获取全部的html则使用.html方法
