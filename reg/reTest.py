import re

beginWithHello = re.compile(r'^Hello')
result = beginWithHello.search('Hello world!')
print(result.group())

result = beginWithHello.search('He said Hello')
print(result)

wholeStringIsNum = re.compile(r'^\d+$')
result = wholeStringIsNum.search('12345678')
print(result)

result = wholeStringIsNum.search('123456xy89')
print(result)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())