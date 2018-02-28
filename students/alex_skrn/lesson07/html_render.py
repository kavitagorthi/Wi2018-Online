#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "
    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        self.attrs = self.kwargs_to_str(**kwargs)

    def append(self, new_content):
        self.content.append(new_content)

    def kwargs_to_str(self, **kwargs):
        """Convert kwargs to string."""
        a_list = []
        for k, v in zip(kwargs.keys(), kwargs.values()):
            a_list.append(k)
            a_list.append(v)
        return " ".join(['{}="{}"'] * len(kwargs)).format(*tuple(a_list))

    def render(self, file_out, cur_ind=""):
        if not self.attrs:
            file_out.write("{}<{}>\n".format(cur_ind, self.tag))
        else:
            file_out.write("{}<{} {}>\n".format(cur_ind, self.tag, self.attrs))
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
        if not self.attrs:
            file_out.write("{}<{}>\n".format(cur_ind, self.tag))
        else:
            file_out.write("{}<{} {}>\n".format(cur_ind, self.tag, self.attrs))
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


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    tag = "title"

    def render(self, file_out, cur_ind=""):
        if not self.attrs:
            file_out.write("{}<{}>".format(cur_ind, self.tag))
        else:
            file_out.write("{}<{} {}>".format(cur_ind, self.tag, self.attrs))
        for elem in self.content:
            try:
                elem.render(file_out, Element.indent + cur_ind)
            except AttributeError:
                file_out.write("{}".format(str(elem)))
        file_out.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    tag = "hr"
    try:
        def __init__(self, **kwargs):
            self.attrs = self.kwargs_to_str(**kwargs)
    except TypeError:
        print("SelfClosingTag accepts no content")
        raise

    def append(self):
        print("SelfClosingTag accepts no content")
        raise TypeError

    def render(self, file_out, cur_ind=""):
        if not self.attrs:
            file_out.write("{}<{} />\n".format(cur_ind, self.tag))
        else:
            file_out.write("{}<{} {} />\n".format(cur_ind, self.tag, self.attrs))


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"
