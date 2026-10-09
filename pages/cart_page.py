class CartPage:
    def __init__(self,page):
        self.page = page
        self.product_name = page.get_by_test_id("cart-item-name-4")
        self.product_price = page.get_by_test_id("cart-item-price-4")
        self.product_quantity = page.get_by_test_id("cart-item-quantity-4")
        self.check_out = page.get_by_role("button" , name ="Proceed to checkout")
        self.remove_product = page.get_by_test_id("cart-item-remove-4")
        self.increase_quantity = page.get_by_test_id("cart-item-increase-4")
        self.decrease_quantity = page.get_by_test_id("cart-item-decrease-4")
        self.product_subtotal = page.get_by_test_id("cart-item-subtotal-4")


    def checkout(self):
        self.check_out.click()

    def remove_product_from_cart(self):
        self.remove_product.click()

    def increase_qty(self):
        self.increase_quantity.click()

    def decrease_qty(self):
        self.decrease_quantity.click()
