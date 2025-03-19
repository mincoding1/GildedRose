#include "gmock/gmock.h"
#include "gilded_rose.h"

TEST(GildedRoseTest, Foo) {
    //Arrange
    vector<Item> items;
    items.push_back(Item("Foo", 0, 0));
    GildedRose app(items);

    //Act
    app.updateQuality();

    //Arrange
    EXPECT_EQ("fixme", app.items[0].name); //코드 이해 후, 수정 필요
}
