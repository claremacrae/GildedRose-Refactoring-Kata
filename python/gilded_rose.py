# -*- coding: utf-8 -*-

def increment_quality_if_less_than_50(item):
    if item.quality < 50:
        item.quality = item.quality + 1

def decrement_quality_if_greater_than_zero(item, increment):
    if item.quality > 0:
        item.quality = item.quality - increment

    if item.quality < 0:
        item.quality = 0

def handle_sulfuras(item):
    # never changes
    pass

def handle_aged_brie(item):
    increment_quality_if_less_than_50(item)
    item.sell_in = item.sell_in - 1

def handle_backstage_pass(item):
    increment_quality_if_less_than_50( item)
    if item.sell_in < 11:
        increment_quality_if_less_than_50(item)
    if item.sell_in < 6:
        increment_quality_if_less_than_50(item)

    item.sell_in = item.sell_in - 1

    if item.sell_in < 0:
        item.quality = 0

def handle_normal_case(item, increment):
    decrement_quality_if_greater_than_zero(item, increment)

    item.sell_in = item.sell_in - 1

    if item.sell_in < 0:
        decrement_quality_if_greater_than_zero(item, increment)

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name.startswith("Sulfuras, "):
                handle_sulfuras(item)
            elif item.name == "Aged Brie":
                handle_aged_brie(item)
            elif item.name.startswith("Backstage passes "):
                handle_backstage_pass(item)
            elif item.name.startswith("Conjured "):
                handle_normal_case(item, 2)
            else:
                handle_normal_case(item, 1)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
