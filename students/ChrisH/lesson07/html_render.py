#!/usr/bin/env python3
# -----------------------------------------------------------
# html_render.py
#  Render an html page in a 'pretty printed' way, indented
#  and human readable.
# -----------------------------------------------------------



class Element(object):

    def __init__(self, content=None, indent='    '):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.tag = 'html'
        self.indent = indent

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
        html_out = cur_ind + '<' + self.tag + '>\n'

        for item in self.content:
            html_out += cur_ind + self.indent + item + '\n'

        html_out += cur_ind + '</' + self.tag + '>\n'

        file_out.write(html_out)


class Html(Element):

    def __init__(self):
        self.tag = 'html'

