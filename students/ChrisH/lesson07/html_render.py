#!/usr/bin/env python3
# -----------------------------------------------------------
# html_render.py
#  Render an html page in a 'pretty printed' way, indented
#  and human readable.
# -----------------------------------------------------------


class Element(object):
    """
    Base Class for elements in an HTML document.
    """

    tag = 'html'

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.indent = '    '

    def append(self, new_content):
        """
        Appends another string to the content.
        :return: None
        """
        self.content.append(new_content)

    def render(self, file_out, cur_ind=''):
        """
        Renders the tag and strings in the content.
        :param file_out: any open, writeable file-like object
        :param cur_ind: a string with the current indentation level
                        this is the amount that the element should already be indented
        :return: None
        """
        if type(self) is Html:
            file_out.write(cur_ind + '<!DOCTYPE html>\n')

        file_out.write(cur_ind + '<' + self.tag + '>\n')

        for item in self.content:
            try:
                item.render(file_out, cur_ind + self.indent)
            except AttributeError:
                file_out.write(cur_ind + self.indent + str(item) + '\n')

        file_out.write(cur_ind + '</' + self.tag + '>\n')


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    """
    Subclass of Element, overrides Element.render to print html text on one line.
    """
    def render(self, file_out, cur_ind=''):
        """
        Renders the tag and strings in the content of the object ON ONE LINE.
        :param file_out: any open, writeable file-like object
        :param cur_ind: a string with the current indentation level
        :return: None, writes output to a given file
        """
        file_out.write(cur_ind + '<' + self.tag + '>')
        for item in self.content:
            try:
                item.render(file_out, '')
            except AttributeError:
                file_out.write(str(item))
        file_out.write('</' + self.tag + '>\n')


class Title(OneLineTag):
    tag = 'title'
