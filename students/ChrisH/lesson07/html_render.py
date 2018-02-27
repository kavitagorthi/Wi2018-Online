#!/usr/bin/env python3
# -----------------------------------------------------------
# html_render.py
#  Render an html page in a 'pretty printed' way, indented
#  and human readable.
# -----------------------------------------------------------



class Element(object):

    def __init__(self, content=None, tag='html', indent='    '):
        if content is None:
            self.content = ''
        else:
            self.content = str(content)
        self.tag = tag
        self.indent = indent
        self.sub_elements = []

    def append(self, content):
        """
        Appends another string to the content.
        :return: None
        """
        self.content += content

    def render(self, file_out, cur_ind=''):
        """
        Renders the tag and strings in the content
        :param file_out: any open, writeable file-like object
        :param cur_ind: a string with the current indentation level
                        this is the amount that the element should already be indented
        :return: None
        """
        text_out = \
            cur_ind + '<' + self.tag + '>\n' + \
            cur_ind + self.indent + self.content + '\n' + \
            cur_ind + '</' + self.tag + '>\n'

        file_out.write(text_out)
