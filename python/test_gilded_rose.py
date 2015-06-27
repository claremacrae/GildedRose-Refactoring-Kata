# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

class GildedRoseRegressionTest(unittest.TestCase):
    def test_foo(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]

        new_items = [
            ["+5 Dexterity Vest", 9, 19],
            ["Aged Brie", 1, 1],
            ["Elixir of the Mongoose", 4, 6],
            ["Sulfuras, Hand of Ragnaros", 0, 80],
            ["Sulfuras, Hand of Ragnaros", -1, 80],
            ["Backstage passes to a TAFKAL80ETC concert", 14, 21],
            ["Backstage passes to a TAFKAL80ETC concert", 9, 50],
            ["Backstage passes to a TAFKAL80ETC concert", 4, 50],
            ["Conjured Mana Cake", 2, 5]
        ]

        GildedRose(items).update_quality()

        nitems = len(items)
        for i in range(nitems):
            self.assertEqual(new_items[i][0], items[i].name)
            self.assertEqual(new_items[i][1], items[i].sell_in)
            self.assertEqual(new_items[i][2], items[i].quality)

if __name__ == '__main__':
    unittest.main()

