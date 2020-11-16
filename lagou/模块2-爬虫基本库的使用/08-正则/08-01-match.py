# import re
#
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)  # match 方法中，第一个参数传入正则表达式，第二个参数传入要匹配的字符串
# print(result)
# print(result.group())  # 输出匹配的内容
# print(result.span())  # 输出匹配的范围，结果是(0, 25)，这就是匹配到的结果字符串在原字符串中的位置范围。


# 获取字符串中的一部分
# import re
#
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)  # 将数字部分的正则表达式用 () 括起来，然后调用了 group(1) 获取匹配结果。
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())


# 通用匹配  .*  其中 . 可以匹配任意字符（除换行符），* 代表匹配前面的字符无限次，它们组合在一起就可以匹配任意字符了
# import re
#
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())

# 贪婪与非贪婪
## 使用上面的通用匹配 .* 时，有时候匹配到的并不是我们想要的结果
# import re
#
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$', content)
# print(result)
# print(result.group(1))  # 只匹配到了数字7，
# 在贪婪匹配下，.* 会匹配尽可能多的字符。
# 正则表达式中 .* 后面是 \d+，也就是至少一个数字，并没有指定具体多少个数字，
# 因此，.* 就尽可能匹配多的字符，这里就把 123456 匹配了，给 \d+ 留下一个可满足条件的数字 7，最后得到的内容就只有数字 7 了。

## 非贪婪匹配：.*?   --- 匹配字符串中间的字符串时使用非贪婪匹配模式
# import re
#
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
# 此时就可以成功获取 1234567 了。
# 原因可想而知，贪婪匹配是尽可能匹配多的字符，非贪婪匹配就是尽可能匹配少的字符。
# 当 .*? 匹配到 Hello 后面的空白字符时，再往后的字符就是数字了，而 \d+ 恰好可以匹配，
# 那么 .*? 就不再进行匹配，交给 \d+ 去匹配后面的数字。这样 .*? 匹配了尽可能少的字符，\d+ 的结果就是 1234567 了。

## 匹配字符串末尾时使用贪婪匹配
# import re
#
# content = 'http://weibo.com/comment/kEraCN'
# result1 = re.match('http.*?comment/(.*?)', content)
# result2 = re.match('http.*?comment/(.*)', content)
# print('result1', result1.group(1))
# print('result2', result2.group(1))


# 修饰符
# 正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
# import re
#
# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$', content)   # 有换行符，报错
# print(result.group(1))
# 因为我们匹配的是除换行符之外的任意字符，当遇到换行符时，.*? 就不能匹配了，导致匹配失败。只需加一个修饰符 re.S，即可修正这个错误

# result = re.match('^He.*?(\d+).*?Demo$', content, re.S)  # 这个修饰符的作用是匹配包括换行符在内的所有字符。


# 转义匹配
# import re
#
# content = '(百度) www.baidu.com'
# result = re.match('\(百度 \) www\.baidu\.com', content)
# print(result)

# match 方法是从字符串的开头开始匹配的，一旦开头不匹配，那么整个匹配就失败了。
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo', content)
print(result)  # 字符串以 Extra 开头，但是正则表达式以 Hello 开头，整个正则表达式是字符串的一部分，但是这样匹配是失败的。
# match 方法在使用时需要考虑到开头的内容，这在做匹配时并不方便。它更适合用来检测某个字符串是否符合某个正则表达式的规则




