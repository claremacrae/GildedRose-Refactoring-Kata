# -*- coding: utf-8 -*-

def adjust_quality_if_less_than_50(item):
    if item.quality < 50:
        item.quality = item.quality + 1

def handle_sulfuras(item):
    # never changes
    pass

def handle_aged_brie(item):
    adjust_quality_if_less_than_50(item)
    item.sell_in = item.sell_in - 1

def handle_backstage_pass(item):
    adjust_quality_if_less_than_50( item)
    if item.sell_in < 11:
        adjust_quality_if_less_than_50(item)
    if item.sell_in < 6:
        adjust_quality_if_less_than_50(item)

    item.sell_in = item.sell_in - 1

    if item.sell_in < 0:
        item.quality = 0

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                handle_sulfuras(item)
                continue

            if item.name == "Aged Brie":
                handle_aged_brie(item)
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                handle_backstage_pass(item)
                continue

            if item.quality > 0:
                item.quality = item.quality - 1

            item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.quality > 0:
                    item.quality = item.quality - 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
