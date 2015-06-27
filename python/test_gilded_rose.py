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

    def check_one_item(self, item, expected_values):
        items = []
        items.append(item)
        GildedRose(items).update_quality()

        self.assertEqual(expected_values[0], item.name)
        self.assertEqual(expected_values[1], item.sell_in)
        self.assertEqual(expected_values[2], item.quality)


    # At the end of each day our system lowers both values for every item
    def test_quality_and_sell_in_lowers_each_day(self):
        self.check_one_item(
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            ["+5 Dexterity Vest", 9, 19])

        self.check_one_item(
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            ["Elixir of the Mongoose", 4, 6])

    # TODO Once the sell by date has passed, Quality degrades twice as fast

    # TODO The Quality of an item is never negative

    # "Aged Brie" actually increases in Quality the older it gets
    def test_aged_brie_quality_increases_with_age(self):
        self.check_one_item(
            Item(name="Aged Brie", sell_in=2, quality=0),
            ["Aged Brie", 1, 1])
        pass

    # TODO The Quality of an item is never more than 50

    # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    def test_sulfuras_never_has_to_be_sold_and_never_increases_in_Value(self):
        self.check_one_item(
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            ["Sulfuras, Hand of Ragnaros", 0, 80])

        self.check_one_item(
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            ["Sulfuras, Hand of Ragnaros", -1, 80])

    # "Backstage passes", like aged brie, increases in Quality as it's SellIn value approaches;

    # Quality increases by 1 when there are more than 10 days
    def test_backstage_passes_increase_by_one_when_more_than_ten_days(self):
        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            ["Backstage passes to a TAFKAL80ETC concert", 14, 21])

    # Quality increases by 2 when there are 10 days or less
    def test_backstage_passes_increase_by_two_when_ten_days_or_less(self):
        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            ["Backstage passes to a TAFKAL80ETC concert", 9, 50]) # TODO should increase by 2

    # and by 3 when there are 5 days or less
    def test_backstage_passes_increase_by_five_when_ten_days_or_less(self):
        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            ["Backstage passes to a TAFKAL80ETC concert", 4, 50]) # TODO should increase by 2

    # TODO but Quality drops to 0 after the concert

    # Conjured items initially behave normally
    def test_conjured_items_degrade_normally(self):
        self.check_one_item(
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ["Conjured Mana Cake", 2, 5])

    # TODO Just for clarification, an item can never have its Quality increase above 50
    # TODO however "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.


if __name__ == '__main__':
    unittest.main()

