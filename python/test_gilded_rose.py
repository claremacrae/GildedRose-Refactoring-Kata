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
        self.assertEqual(2, len(expected_values))

        expected_name = item.name
        original_item_text = str(item)

        items = []
        items.append(item)
        GildedRose(items).update_quality()

        self.assertEqual(expected_name, item.name, original_item_text)
        self.assertEqual(expected_values[0], item.sell_in, original_item_text)
        self.assertEqual(expected_values[1], item.quality, original_item_text)
        # The Quality of an item is never negative
        self.assertGreaterEqual(item.quality, 0, original_item_text)

    # ===========================================================================================
    # At the end of each day our system lowers both values for every item
    def test_quality_and_sell_in_lowers_each_day(self):
        self.check_one_item(
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            [9, 19])

        self.check_one_item(
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            [4, 6])

    # Once the sell by date has passed, Quality degrades twice as fast
    def test_quality_drops_twice_as_fast_after_sell_by(self):
        self.check_one_item(
            Item(name="Elixir of the Mongoose", sell_in=0, quality=7),
            [-1, 5])

    # The Quality of an item is never negative
    def test_quality_never_negative(self):
        self.check_one_item(
            Item(name="Elixir of the Mongoose", sell_in=5, quality=1),
            [4, 0])

        self.check_one_item(
            Item(name="Elixir of the Mongoose", sell_in=5, quality=0),
            [4, 0])

    # ===========================================================================================
    # "Aged Brie" actually increases in Quality the older it gets
    def test_aged_brie_quality_increases_with_age(self):
        self.check_one_item(
            Item(name="Aged Brie", sell_in=2, quality=0),
            [1, 1])
        pass

    # The Quality of an item is never more than 50 - Aged Brie
    def test_aged_brie_quality_does_not_increase_above_50(self):
        self.check_one_item(
            Item(name="Aged Brie", sell_in=30, quality=49),
            [29, 50])

        self.check_one_item(
            Item(name="Aged Brie", sell_in=30, quality=50),
            [29, 50])

    # ===========================================================================================
    # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    # "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.
    def test_sulfuras_never_has_to_be_sold_and_never_increases_in_Value(self):
        self.check_one_item(
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            [0, 80])

        self.check_one_item(
            Item(name="Sulfuras, Foot of Troy", sell_in=-1, quality=80),
            [-1, 80])

    # ===========================================================================================
    # "Backstage passes", like aged brie, increases in Quality as it's SellIn value approaches;

    # Quality increases by 1 when there are more than 10 days
    def test_backstage_passes_increase_by_one_when_more_than_ten_days(self):
        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            [14, 21])

    # The Quality of an item is never more than 50 - Backstage passes
    def test_backstage_pass_quality_does_not_increase_above_50_when_more_than_ten_days(self):
        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=49),
            [14, 50])

        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=50),
            [14, 50])

    # ===========================================================================================
    # Quality increases by 2 when there are 10 days or less
    def test_backstage_passes_increase_by_two_when_ten_days_or_less(self):
        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20),
            [9, 22])

    # The Quality of an item is never more than 50 - Backstage passes
    def test_backstage_pass_quality_does_not_increase_above_50_when_ten_days_or_less(self):
        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            [9, 50])

        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=50),
            [9, 50])

    # ===========================================================================================
    # and by 3 when there are 5 days or less
    def test_backstage_passes_increase_by_three_when_five_days_or_less(self):
        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20),
            [4, 23])

    # The Quality of an item is never more than 50 - Backstage passes
    def test_backstage_pass_quality_does_not_increase_above_50_when_more_five_days_or_less(self):
        self.check_one_item(
            Item(name="Backstage passes to a Meatloaf concert", sell_in=5, quality=49),
            [4, 50])

        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50),
            [4, 50])

    # ===========================================================================================
    # "Backstage pass" Quality drops to 0 after the concert
    def test_backstage_passes_increase_by_five_when_ten_days_or_less(self):
        self.check_one_item(
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=49),
            [-1, 0])

    # ===========================================================================================
    # Conjured items degrade in Quality twice as fast as normal items
    def test_conjured_items_degrade_twice_as_fast(self):
        self.check_one_item(
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),
            [2, 4])

    def test_conjured_items_degrade_twice_as_fast_after_sell_by(self):
        self.check_one_item(
            Item(name="Conjured Moon Cake", sell_in=0, quality=6),
            [-1, 2])

        self.check_one_item(
            Item(name="Conjured Apple Cake", sell_in=0, quality=1),
            [-1, 0])


if __name__ == '__main__':
    unittest.main()
