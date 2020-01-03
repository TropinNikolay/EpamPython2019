"""
Написать тесты(pytest or unittest) к предыдущим 2 заданиям, запустив которые, я бы смог бы проверить их корректность
Обязательно проверить всю критическую функциональность
"""
import unittest
import time
from task1 import SiamObj
from task2 import Message


class MetaTest(unittest.TestCase):
    def setUp(self) -> None:
        self.unit1 = SiamObj("1", "2", a=1)
        self.unit2 = SiamObj("1", "2", a=1)
        self.unit3 = SiamObj("2", "2", a=1)
        self.pool = self.unit3.pool

    def test_equality(self):
        self.assertEqual(self.unit1, self.unit2)
        self.assertNotEqual(self.unit1, self.unit3)

    def test_connection_method(self):
        self.unit3.connect("1", "2", 1).a = 2
        self.assertTrue(self.unit2.a == 2)
        self.assertTrue(self.unit1.a == 2)

    def test_pool_attribute(self):
        self.assertTrue(len(self.pool) == 2)

    def test_deletion(self):
        del self.unit3
        self.assertTrue(len(self.pool) == 1)


class PropertyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.m = Message()
        self.initial = self.m.msg

    def test_equality(self):
        self.assertEqual(self.initial, self.m.msg)

    def test_updating_cache(self):
        time.sleep(1)
        self.assertNotEqual(self.m, self.initial)

    def test_setter(self):
        self.m.msg = 239
        self.assertEqual(self.m.msg, 239)


if __name__ == "__main__":
    unittest.main()
