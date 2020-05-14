import xml.etree.ElementTree as ET

def parsing(file_path):
    clear_text = ''
    xml_text = []
    paragraph = 0
    tree = ET.parse(file_path)
    root = tree.getroot()

    for child in root:
        if child.tag != 'body':
            root.remove(child)

    member = root.getchildren()[0]
    appointments = member.getchildren()

    for appointment in appointments:
        if appointment.text != 'None':
            appt_children = appointment.getchildren()
            for appt_child in appt_children:
                xml_text.append(appt_child.text)
        else:
            xml_text.append(appointment.text)

    for i in xml_text:
        clear_text = clear_text + ' ' + str(i)

    return clear_text, xml_text[1], len(xml_text)









