from gilded_rose import *

if __name__ == "__main__":
    print('OMGHAI!')

    items = [
        Item(name='+5 Dexterity Vest', sell_in=10, quality=20),
        Item(name='Aged Brie', sell_in=2, quality=0),
        Item(name='Elixir of the Mongoose', sell_in=5, quality=7),
        Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80),
        Item(name='Sulfuras, Hand of Ragnaros', sell_in=-1, quality=80),
        Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=15, quality=20),
        Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=10, quality=49),
        Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=5, quality=49),
        Item(name='Conjured Mana Cake', sell_in=3, quality=6)
    ]

    days = 2
    for day in range(days):
        print(f'-------- day {day} --------')
        print('name, sellIn, quality')
        for item in items:
            print(item)
        print()

        GildedRose(items).update_quality()
