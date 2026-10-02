# 查找
# find：检测某个子字符串是否包含在字符串里，如果在就返回第一个字符串的开始位置的下标，否则就返回-1
# find（子字符串，开始位置的下标，结束位置的下标）
# 开始和结束位置的下标可以省略，表示在整个字符串里找.也可以只设置开始位置或结束位置。包前不包后
# name="陈树涵是我亲爱的孩子"
# print(name.find('陈树涵'))#该处则返回0

# index：检测某个子字符串是否包含在字符串里，如果在就返回第一个字符串的开始位置的下标，否则就会报错
# index（字字符串，开始下标的位置，结束位置下标）
# 开始和结束位置下标可以省略，表示在整个字符串里查找。也可以只设置开始位置或结束位置。同样遵循包前不包后
# name='陈树涵是我亲爱的孩子'
# print(name.index("涵"))#2

# count():返回某个子字符串在整个字符串中出现的次数，没有就返回0
# count（子字符串，开始位置下标，结束位置下标）
# 开始和结束位置下标可以省略，表示在整个字符串里查找。也可以只设置开始位置或结束位置。同样遵循包前不包后
# name='陈树涵'
# print(name.count('树')) #1

#判断
# startswith():是否以某个子字符串开头，是的话就返回True，不是的话就返回False.设置开始和结束下标则在指定范围内检查
# startswith(子字符串，开始下标的位置，结束下标的位置)
# 开始和结束位置下标可以省略，表示在整个字符串里查找。也可以只设置开始位置或结束位置。
# name='陈树涵是我亲爱的孩子'
# print(name.startswith('陈'))#True
# print(name.startswith('树'))#False

# endswith():是否以某个子字符串结尾，是的话就返回True，不是的话就返回False.设置开始和结束下标则在指定范围内检查
# endswith(子字符串，开始下标的位置，结束下标的位置)
# 开始和结束位置下标可以省略，表示在整个字符串里查找。也可以只设置开始位置或结束位置。

# isupper判断字符串是否全为大写，是就输出True，不是就输出False
# islower判断字符串是否全为小写，是就输出True，不是就输出False
# name='asdff'
# print(name.isupper())
# print(name.islower())

#修改
# replace():替换
# repiace(旧内容，新内容，替换次数)
# 替换次数可以省略，默认全部替换
# name='树涵是我亲爱的孩子'
# print(name.replace('孩','儿'))#树涵是我亲爱的儿子

# split():指定分隔符来切割字符串
# split(分割内容，分割次数)
# 如果字符串不含分割内容，就不进行分割，会作为一个整体
# 如果不指定分割次数，则会对整体进行分割
# 会以列表形式返回
# name='chenshuhan'
# print(name.split('n',1))#['che', 'shuhan']

# # capitalize():第一个字母大写，其他都小写
# name='maJIAqi'
# print(name.capitalize())#Majiaqi
#
# # lower():大写字母转化为小写
# name='MAJIAqi'
# print(name.lower())#majiaqi
#
# # upper():小写字母转化为大写
# name='MAJIAqi'
# print(name.upper())#MAJIAQI




