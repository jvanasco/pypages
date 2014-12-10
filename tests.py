import unittest

from pypages import Paginator

import pdb


class PyPagesTestCase(unittest.TestCase):

    def test_object_num(self):
        p = Paginator(100)
        self.assertEquals(p.object_num, 100)
        self.assertEquals(p.per_page, 10)
        self.assertEquals(p.current, 1)
        self.assertEquals(p.start, 1)
        self.assertEquals(p.range_num, 10)
        self.assertEquals(p.end, 10)
        self.assertEquals(p.page_num, 10)
        self.assertEquals(p.pages, range(1, 11))
        self.assertFalse(p.has_previous)
        self.assertTrue(p.has_next)
        self.assertEquals(p.previous, None)
        self.assertEquals(p.next, 2)

        p = Paginator(0)
        self.assertEquals(p.object_num, 0)
        self.assertEquals(p.per_page, 10)
        self.assertEquals(p.current, 0)
        self.assertEquals(p.start, 1)
        self.assertEquals(p.range_num, 10)
        self.assertEquals(p.end, 0)
        self.assertEquals(p.page_num, 0)
        self.assertEquals(p.pages, [])
        self.assertFalse(p.has_previous)
        self.assertFalse(p.has_next)
        self.assertEquals(p.previous, None)
        self.assertEquals(p.next, None)

        p = Paginator(5)
        self.assertEquals(p.object_num, 5)
        self.assertEquals(p.per_page, 10)
        self.assertEquals(p.current, 1)
        self.assertEquals(p.start, 1)
        self.assertEquals(p.range_num, 10)
        self.assertEquals(p.end, 1)
        self.assertEquals(p.page_num, 1)
        self.assertEquals(p.pages, [1])
        self.assertFalse(p.has_previous)
        self.assertFalse(p.has_next)
        self.assertEquals(p.previous, None)
        self.assertEquals(p.next, None)

        p = Paginator(45)
        self.assertEquals(p.object_num, 45)
        self.assertEquals(p.per_page, 10)
        self.assertEquals(p.current, 1)
        self.assertEquals(p.start, 1)
        self.assertEquals(p.range_num, 10)
        self.assertEquals(p.end, 5)
        self.assertEquals(p.page_num, 5)
        self.assertEquals(p.pages, [1, 2, 3, 4, 5])
        self.assertFalse(p.has_previous)
        self.assertTrue(p.has_next)
        self.assertEquals(p.previous, None)
        self.assertEquals(p.next, 2)

        p = Paginator(145)
        self.assertEquals(p.object_num, 145)
        self.assertEquals(p.per_page, 10)
        self.assertEquals(p.current, 1)
        self.assertEquals(p.start, 1)
        self.assertEquals(p.range_num, 10)
        self.assertEquals(p.end, 10)
        self.assertEquals(p.page_num, 15)
        self.assertEquals(p.pages, range(1, 11))
        self.assertFalse(p.has_previous)
        self.assertTrue(p.has_next)
        self.assertEquals(p.previous, None)
        self.assertEquals(p.next, 2)

    def test_per_page(self):
        p = Paginator(145, 1)
        self.assertEquals(p.object_num, 145)
        self.assertEquals(p.per_page, 1)
        self.assertEquals(p.current, 1)
        self.assertEquals(p.start, 1)
        self.assertEquals(p.range_num, 10)
        self.assertEquals(p.end, 10)
        self.assertEquals(p.page_num, 145)
        self.assertEquals(p.pages, range(1, 11))
        self.assertFalse(p.has_previous)
        self.assertTrue(p.has_next)
        self.assertEquals(p.previous, None)
        self.assertEquals(p.next, 2)

    def test_current(self):
        p = Paginator(145, current=5)
        self.assertEquals(p.object_num, 145)
        self.assertEquals(p.per_page, 10)
        self.assertEquals(p.current, 5)
        self.assertEquals(p.start, 1)
        self.assertEquals(p.range_num, 10)
        self.assertEquals(p.end, 10)
        self.assertEquals(p.page_num, 15)
        self.assertEquals(p.pages, range(1, 11))
        self.assertTrue(p.has_previous)
        self.assertTrue(p.has_next)
        self.assertEquals(p.previous, 4)
        self.assertEquals(p.next, 6)

        p = Paginator(145, current=0)
        self.assertEquals(p.current, 1)
        p = Paginator(145, current=-1)
        self.assertEquals(p.current, 1)
        p = Paginator(145, current="hello")
        self.assertEquals(p.current, 1)

    def test_start(self):
        p = Paginator(145, start=6)
        self.assertEquals(p.object_num, 145)
        self.assertEquals(p.per_page, 10)
        self.assertEquals(p.current, 1)
        self.assertEquals(p.start, 6)
        self.assertEquals(p.range_num, 10)
        self.assertEquals(p.end, 15)
        self.assertEquals(p.page_num, 15)
        self.assertEquals(p.pages, range(6, 16))
        self.assertFalse(p.has_previous)
        self.assertTrue(p.has_next)
        self.assertEquals(p.previous, None)
        self.assertEquals(p.next, 2)

        p = Paginator(145, current=10)
        self.assertEquals(p.start, 5)
        p = Paginator(145, start=0)
        self.assertEquals(p.start, 1)
        p = Paginator(145, start=20)
        self.assertEquals(p.start, 20)
        self.assertEquals(p.pages, [])

    def test_range_num(self):
        p = Paginator(145, range_num=50)
        self.assertEquals(p.object_num, 145)
        self.assertEquals(p.per_page, 10)
        self.assertEquals(p.current, 1)
        self.assertEquals(p.start, 1)
        self.assertEquals(p.range_num, 50)
        self.assertEquals(p.end, 15)
        self.assertEquals(p.page_num, 15)
        self.assertEquals(p.pages, range(1, 16))
        self.assertFalse(p.has_previous)
        self.assertTrue(p.has_next)
        self.assertEquals(p.previous, None)
        self.assertEquals(p.next, 2)

    def test_exception(self):
        self.assertRaises(AssertionError, Paginator, -145)
        self.assertRaises((AssertionError, ZeroDivisionError),
                          Paginator, 145, 0)
        self.assertRaises(AssertionError, Paginator, 145, range_num=-1)
        self.assertRaises(ValueError, Paginator, "value")

    def test_pageset(self):
        p = Paginator(100,)
        self.assertEquals(p.pageset_next, None)
        self.assertEquals(p.pageset_previous, None)

        if False:
            for i in range(1, 15):
                p = Paginator(150, start=i)
                print "----= %s" % i
                print p.pages
                if p.pageset_next:
                    pp = Paginator(150, start=p.pageset_next)
                    print ">> %s" % pp.pages
                else:
                    print ">> %s" % []
                if p.pageset_previous:
                    pp = Paginator(150, start=p.pageset_previous)
                    print "<< %s" % pp.pages
                else:
                    print "<< %s" % []

        p = Paginator(150,)
        self.assertEquals(p.pageset_next, 11)
        self.assertEquals(p.pageset_previous, None)

        p = Paginator(150, start=2)
        self.assertEquals(p.pageset_next, 12)
        self.assertEquals(p.pageset_previous, 1)

        p = Paginator(150, start=3)
        self.assertEquals(p.pageset_next, 13)
        self.assertEquals(p.pageset_previous, 1)

        p = Paginator(150, start=4)
        self.assertEquals(p.pageset_next, 14)
        self.assertEquals(p.pageset_previous, 1)

        p = Paginator(150, start=5)
        self.assertEquals(p.pageset_next, 15)
        self.assertEquals(p.pageset_previous, 1)

        p = Paginator(150, start=6)
        self.assertEquals(p.pageset_next, None)
        self.assertEquals(p.pageset_previous, 1)

        # this range is all `None, 1`

        p = Paginator(150, start=11)
        self.assertEquals(p.pageset_next, None)
        self.assertEquals(p.pageset_previous, 1)

        # we finally bump up here

        p = Paginator(150, start=12)
        self.assertEquals(p.pageset_next, None)
        self.assertEquals(p.pageset_previous, 2)

    def test_pageset_centered(self):

        for i in range(1, 86):
            p = Paginator(850, start=i)
            pageset_centered = p.pageset_centered

            # all should have a length of 10
            self.assertEquals(len(pageset_centered), 10)

            # check the first item
            if i <= 5:
                # for the first 5, should be 1
                self.assertEquals(pageset_centered[0], 1)
            elif i >= 80:
                # thereafter, should be 4 items less than the current loop
                self.assertEquals(pageset_centered[0], 76)
            else:
                # thereafter, should be 4 items less than the current loop
                self.assertEquals(pageset_centered[0], i - 4)

            # check the pagination - previous
            if i <= 5:
                # for the first 5, should be None
                self.assertEquals(p.pageset_centered_previous, None)
            elif (i >= 6) and (i <= 11):
                # for the next 5, should be 1
                self.assertEquals(p.pageset_centered_previous, 1)
            else:
                # thereafter, should be 10 items less than i
                self.assertEquals(p.pageset_centered_previous, i - 10)

            # check the pagination - next
            if i <= 5:
                # for the first 5, should be None
                self.assertEquals(p.pageset_centered_next, 15)
            elif (i > 5) and (i < 71):
                self.assertEquals(p.pageset_centered_next, i + 10)
            elif (i >= 71) and (i < 80):
                # for the last 5, should be 81
                self.assertEquals(p.pageset_centered_next, 81)
            else:
                # thereafter, should be 10 items more than i
                self.assertEquals(p.pageset_centered_next, None)

        # ensure we have the right lengths of pages
        test_sets = (
            # items, length
            (9, 1),
            (10, 1),
            (11, 2),
        )
        for test_set in test_sets:
            p = Paginator(test_set[0], start=1)
            self.assertEquals(len(p.pageset_centered), test_set[1])


if __name__ == "__main__":
    unittest.main()
