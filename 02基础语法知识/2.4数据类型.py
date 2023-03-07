# 转义字符
print("自强不息\n止于至善")

# 数据类型转换
x = 27.8555
y = str(x)
z = int(x) 
print(type(x))

x = input("请输入")

# 输出不换行
print("自强不息",end='')
print("止于至善")

# 八进制输出
print(' %o ' %27 )

# 字符串输出
print('%s'% 'hello,world' )
print('%-20.3s'% 'hello,world' )

# 使用 “f-字符串”进行格式化输出
name = 'disheng'
age = 14
print(f'姓名：{name},年龄:{age}')

# format（） 函数格式化
print('{},{}'.format('hello','world'))
print('{1},{0}'.format('hello','world'))
print('{b},{a}'.format(a='hello',b='world'))