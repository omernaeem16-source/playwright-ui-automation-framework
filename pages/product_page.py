class ProductPage:
    def __init__ (self, page):
        self.page = page
        self.product_name = page.get_by_test_id("product-detail-name")
        self.product_price = page.get_by_test_id("product-detail-price")
        self.add_to_cart = page.get_by_role("button", name = "Add Bluetooth Speaker to cart")
        self.view_cart = page.get_by_test_id("product-view-cart-button")


    def add_to_cart_button(self):
        self.add_to_cart.click()

    def open_cart(self):
        self.view_cart.click()

    