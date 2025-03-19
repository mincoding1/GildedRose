#include "gmock/gmock.h"
#include "gilded_rose.h"

using std::vector;
using std::string;

TEST(GildedRoseTest, Foo) {
    //Arrange
    vector<Item> items;
    //items.push_back(Item("Foo", 0, 0));
    items.emplace_back("Foo", 0, 0);
    GildedRose app(items);

    //Act
    app.updateQuality();

    //Arrange
    EXPECT_EQ("Foo", app.items[0].name); 
}

