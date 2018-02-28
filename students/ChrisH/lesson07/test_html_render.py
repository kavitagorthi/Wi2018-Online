#!/usr/bin/env python3
# -----------------------------------------------------------
# test_html_render.py
#  uses unittest module to test html_render.py module
# -----------------------------------------------------------


import unittest
from io import StringIO
# from contextlib import redirect_stdout
import html_render as hr


class htmlrenderTest(unittest.TestCase):

    def test_element_init(self):                # default init
        page = hr.Element()
        self.assertEqual(page.content, [])

        page = hr.Element('test content')       # init with content
        self.assertEqual(page.content, ['test content'])

    def test_element_render(self):
        page = hr.Element()
        f = StringIO()
        page.render(f, '')
        self.assertIn('<html>', f.getvalue())

        page = hr.Element('test content')
        page.render(f, '')
        self.assertIn('test content', f.getvalue())

    def test_SelfClosingTag_init(self):
        el = hr.SelfClosingTag()
        self.assertIsNone(el.content)

    def test_SelfClosingTag_append(self):
        el = hr.SelfClosingTag()
        with self.assertRaises(TypeError):
            el.append('new content')

    def test_hr(self):
        hzr = hr.Hr()
        f = StringIO()
        hzr.render(f, '')
        self.assertEqual(f.getvalue(), '<hr />\n')

        hzr = hr.Hr('',style='text-align: center;')
        f = StringIO()
        hzr.render(f, '')
        self.assertEqual(f.getvalue(), '<hr style="text-align: center;" />\n')

    def test_br(self):
        br = hr.Br('',style='text-align: center;')
        f = StringIO()
        br.render(f, '')
        self.assertEqual(f.getvalue(), '<br style="text-align: center;" />\n')

    def test_A(self):
        a = hr.A('http://www.google.com', 'Google')
        f = StringIO()
        a.render(f, '')
        self.assertEqual(f.getvalue(), '<a href="http://www.google.com">Google</a>\n')

    def test_Ul_empty(self):
        ul = hr.Ul(id="TheList", style="line-height:200%")
        f = StringIO()
        ul.render(f, '')
        self.assertEqual(f.getvalue(), '<ul id="TheList" style="line-height:200%">\n</ul>\n')

    def test_Li_single(self):
        li = hr.Li("Single item", style="color: green")
        f = StringIO()
        li.render(f, '')
        self.assertEqual(f.getvalue(), '<li style="color: green">\n    Single item\n</li>\n')

    def test_Header(self):
        h = hr.H(6, "This is a header.")
        f = StringIO()
        h.render(f, '')
        self.assertEqual(f.getvalue(), '<h6>This is a header.</h6>\n')

if __name__ == "__main__":
    unittest.main()
