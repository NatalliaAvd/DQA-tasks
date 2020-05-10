import xml.etree.ElementTree as Et

file = Et.parse("Example.fb2")

#tags = file.find('body')
title = file.findall('title')

temp1 = []

for item in title:
    text = item.firstChild.nodeValue
    #text = item.findall('p').text
    print(text)
    temp1.append(text)
print(temp1)





for item in items:
    temp2 = []
    color = item.get('color')
    temp2.append(color)
    name = item.find('name').text
    temp2.append(name)
    count = item.find('count').text
    temp2.count(count)
    infos = item.find('subtag').findall('Info')

    temp3 = []
    for info in infos:
        name = info.get('name')
        value = info.text
        temp3.append(name)
        temp3.append(value)
    temp3 = [';'.join(temp3)]
    result = temp1 + temp2 + temp3
    result = '|'.join(result)
    print(result)







from xml.dom.minidom import parse

dom = parse("Example.fb2")
print(dom)
for node in dom.getElementsByTagName('book-title'):
    print(node.firstChild.nodeValue)







