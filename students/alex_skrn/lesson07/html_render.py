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
        file_out.write("{}<{}>\n".format(cur_ind, self.tag))
        for elem in self.content:
            try:
                elem.render(file_out, Element.indent + cur_ind)
            except AttributeError:
                file_out.write("{}{}\n".format(Element.indent + cur_ind, str(elem)))
        file_out.write("{}</{}>\n".format(cur_ind, self.tag))


class Html(Element):
    tag = "html"
    def render(self, file_out, cur_ind=""):
        file_out.write("{}<!DOCTYPE html>\n".format(cur_ind))
        file_out.write("{}<{}>\n".format(cur_ind, self.tag))
        for elem in self.content:
            try:
                elem.render(file_out, Element.indent + cur_ind)
            except AttributeError:
                file_out.write("{}{}\n".format(Element.indent + cur_ind, str(elem)))
        file_out.write("{}</{}>".format(cur_ind, self.tag))


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"
