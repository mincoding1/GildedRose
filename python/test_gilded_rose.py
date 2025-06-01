import pytest
from gilded_rose import Item, GildedRose

class test_gilded_rose:
    def test_foo(self):
        items = [Item('foo', 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].name == 'fixme'
