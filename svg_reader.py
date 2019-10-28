from xml.dom import minidom
class reader(object):

    #Al ser un método estático no es necesario usar el parametro self
    @staticmethod
    def read(svg):
        svg_dom = minidom.parse(svg)
        #svg_dom = minidom.parseString(svg_string)
        titles = svg_dom.getElementsByTagName('title')

        my_list = []

        for title in titles:
            tmp = title.firstChild.nodeValue.split("\n")
            my_list.append(tmp)
        return my_list;