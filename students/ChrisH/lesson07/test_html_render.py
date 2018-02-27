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


if __name__ == "__main__":
    unittest.main()
