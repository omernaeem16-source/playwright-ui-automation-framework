import os

from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.check_out_page import CheckOutPage


def test_laptop_backpack_product_flow(page):
    # Ensure login credentials are configured in the .env file
    username = os.getenv("QA_USERNAME")
    password = os.getenv("QA_PASSWORD")
    assert username and password, (
        "Set QA_USERNAME and QA_PASSWORD in the project .env file."
    )

    # Initialize Page Objects for the complete purchase journey
    login_page = LoginPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    check_out_page = CheckOutPage(page)

    # Step 1: Log in and verify successful navigation
    login_page.open()
    login_page.login(username, password)
    expect(page).to_have_url("https://qademo.com/catalog")

    # Step 2: Open the Laptop Backpack product page
    catalog_page.open_laptop_backpack()

    # Verify the product details before adding it to the cart
    expect(product_page.product_name).to_have_text("Laptop Backpack")
    expect(product_page.product_price).to_have_text("$49.99")
    expect(product_page.add_to_cart).to_be_visible()

    # Step 3: Add the product to the cart and verify its details
    product_page.add_to_cart_button()
    product_page.open_cart()

    expect(cart_page.product_name).to_have_text("Laptop Backpack")
    expect(cart_page.product_price).to_have_text("$49.99")
    expect(cart_page.product_quantity).to_have_text("1")

    # Step 4: Proceed to checkout and enter shipping information
    cart_page.checkout()
    check_out_page.shipping_info(
        "Omer",
        "Naeem",
        "Lumumbastr 21",
    )

    # Enter payment information using demo test data
    check_out_page.payment_info(
        "4242 4242 4242 4242",
        "12/27",
        "123",
        "Omer Naeem",
    )

    # Step 5: Place the order and verify confirmation
    check_out_page.place_order()
    expect(
        page.get_by_test_id("order-confirmation-heading")
    ).to_have_text("Order Confirmed!")

