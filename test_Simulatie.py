from unittest import TestCase

import Basicstrategy
import Count


class Test(TestCase):
    def test_basicstrategy(self):
        self.assertEqual(Basicstrategy.basicstrategy([2, 3], 5, 10, False, True,True), "h")
        self.assertEqual(Basicstrategy.basicstrategy(["A11", "V"], 21, 11, False, True, False), "s")
        self.assertEqual(Basicstrategy.basicstrategy(["A11", "A11"], 22, 10, False, True, False), "p")
        self.assertEqual(Basicstrategy.basicstrategy([9, 9], 18,  7, False, True, True), "s")
        self.assertEqual(Basicstrategy.basicstrategy([5, 5], 10, 6, False, True, True), "d")
        self.assertEqual(Basicstrategy.basicstrategy(["V", "B"], 20, 2, False, True,True), "s")
        self.assertEqual(Basicstrategy.basicstrategy([5, 5], 10, 3, False, False,True), "h")
        self.assertEqual(Basicstrategy.basicstrategy([8, 3], 11,  10, False, True,True), "d")
        self.assertEqual(Basicstrategy.basicstrategy([4, 8], 12, 3, False, True,True), "h")
        self.assertEqual(Basicstrategy.basicstrategy([2, 2], 4,  7, False, True, True), "p")
        self.assertEqual(Basicstrategy.basicstrategy([2, 2], 4,  7, True, True, True), "h")
        self.assertEqual(Basicstrategy.basicstrategy([2], 2,  10, True, True, True), "h")
        self.assertEqual(Basicstrategy.basicstrategy(["V", "V"], 20,  11, False, True, True), "s")


    def test_checkrunningcount(self):
        self.assertEqual(Count.checkrunningcount([2, 3, 5, 8, 9]), 3)
        self.assertEqual(Count.checkrunningcount([5, 8, 9, "A11", "V"]), -1)
        self.assertEqual(Count.checkrunningcount([5, 7, "H", "B", "A11", "V"]), -3)
        self.assertEqual(Count.checkrunningcount([5, 7, "H", "B", "A11", "V", "A11", 2, 4, 5, 2, 6, 5, "V"]), 1)




