# Ajax，全称为 Asynchronous JavaScript and XML，即异步的 JavaScript 和 XML。

# 传统的网页，如果你想更新其内容，那么必须要刷新整个页面。
# 有了 Ajax，便可以在页面不被全部刷新的情况下更新其内容。
# 在这个过程中，页面实际上在后台与服务器进行了数据交互，获取到数据之后，再利用 JavaScript 改变网页，这样网页内容就会更新了。

# XMLHttpRequest 对象用于和服务器交换数据

# 发送请求
# 以下是JS代码
# var xmlhttp;
# if (window.XMLHttpRequest) {
#     //code for IE7+, Firefox, Chrome, Opera, Safari
#     xmlhttp=new XMLHttpRequest();
# } else {//code for IE6, IE5
#     xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
# }
#
# xmlhttp.onreadystatechange=function() {
#     if (xmlhttp.readyState==4 && xmlhttp.status==200) {
#         document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
#     }
# }
#
# xmlhttp.open("POST","/ajax/",true);
# xmlhttp.send();

# 解析内容
## 得到响应之后，onreadystatechange 属性对应的方法会被触发，此时利用 xmlhttp 的 responseText 属性便可取到响应内容。

# 渲染网页
# JavaScript 有改变网页内容的能力，解析完响应内容之后，就可以调用 JavaScript 针对解析完的内容对网页进行下一步处理。即DOM操作
# 微博的下拉刷新，这其实是 JavaScript 向服务器发送了一个 Ajax 请求，然后获取新的微博数据，将其解析，并将其渲染在网页中的过程

# 真实的数据其实都是通过一次次 Ajax 请求得到的，如果想要抓取这些数据，我们需要知道这些请求到底是怎么发送的，发往哪里，发了哪些参数。
# 如果我们知道了这些，不就可以用 Python 模拟这个发送操作，获取到其中的结果了吗？

# 在一般情况下，页面中的数据都是通过 Ajax 来加载的，
# JavaScript 在后台调用这些 Ajax 数据接口，得到数据之后，
# 再把数据进行解析并渲染呈现出来，得到最终的页面。
# 所以说，要想爬取页面，我们可以通过直接爬取 Ajax 接口获取数据。
