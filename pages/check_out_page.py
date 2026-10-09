class CheckOutPage:
    def __init__(self,page):
        self.page = page
        self.first_name = page.get_by_label("First Name")
        self.last_name = page.get_by_label("Last Name")
        self.shipping_address = page.get_by_label("Shipping Address")
        self.address_error = page.get_by_role("alert")
        self.card_number = page.get_by_label("Card Number") 
        self.expiry_date = page.get_by_label("Expiry Date")
        self.cvv = page.get_by_label("CVV")
        self.name_on_card = page.get_by_label("Name on Card")
        self.place_order_button = page.get_by_test_id("place-order-button")
        self.checkout_error = page.get_by_test_id("checkout-error-message")
        

    def shipping_info(self, firstname, lastname, shippingaddress):
        self.first_name.fill(firstname)
        self.last_name.fill(lastname)
        self.shipping_address.fill(shippingaddress)

    def payment_info(self, cardnumber, expirydate, CVV, nameoncard):
        self.card_number.fill(cardnumber)
        self.expiry_date.fill(expirydate)
        self.cvv.fill(CVV)
        self.name_on_card.fill(nameoncard)

    def place_order(self):
        self.place_order_button.click()




