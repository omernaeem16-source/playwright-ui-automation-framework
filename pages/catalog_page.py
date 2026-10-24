class CatalogPage:
    def __init__(self, page):
        self.page = page
        self.laptop_backpack = page.get_by_test_id("product-name-3")

    def open_laptop_backpack(self):
        self.laptop_backpack.click()

        