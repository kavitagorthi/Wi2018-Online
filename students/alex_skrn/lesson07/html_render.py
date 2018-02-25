#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "
    def __init__(self, content=None):
        if content is not None:
            self.content = [content]
        else:
            self.content = []

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=""):
        file_out.write("<{}>\n".format(self.tag))
        for elem in self.content:
            try:
                elem.render(file_out)
            except AttributeError:
                file_out.write(str(elem))
                file_out.write(" ")
        file_out.write("\n</{}>".format(self.tag))


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"
