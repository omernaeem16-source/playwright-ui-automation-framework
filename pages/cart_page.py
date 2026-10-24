class CartPage:
    def __init__(self, page):
        self.page = page
        self.product_name = page.get_by_test_id("cart-item-name-3")
        self.product_price = page.get_by_test_id("cart-item-price-3")
        self.product_quantity = page.get_by_test_id("cart-item-quantity-3")
        self.check_out = page.get_by_role("button", name="Proceed to checkout")
        self.remove_product = page.get_by_test_id("cart-item-remove-3")
        self.increase_quantity = page.get_by_test_id("cart-item-increase-3")
        self.decrease_quantity = page.get_by_test_id("cart-item-decrease-3")
        self.product_subtotal = page.get_by_test_id("cart-item-subtotal-3")

    def checkout(self):
        self.check_out.click()

    def remove_product_from_cart(self):
        self.remove_product.click()

    def increase_qty(self):
        self.increase_quantity.click()

    def decrease_qty(self):
        self.decrease_quantity.click()