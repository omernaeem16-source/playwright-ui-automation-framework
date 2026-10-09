import os

from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.check_out_page import CheckOutPage


def test_checkout_with_invalid_cardnumber(page):
    # Ensure login credentials are configured
    username = os.getenv("QA_USERNAME")
    password = os.getenv("QA_PASSWORD")
    assert username and password, (
        "Set QA_USERNAME and QA_PASSWORD in the project .env file."
    )

    # Initialize Page Objects for the checkout journey
    login_page = LoginPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    check_out_page = CheckOutPage(page)

    # Log in and verify successful navigation
    login_page.open()
    login_page.login(username, password)
    expect(page).to_have_url("https://qademo.com/catalog")

    # Select the Bluetooth Speaker and verify its details
    catalog_page.open_bluetooth_speaker()
    expect(product_page.product_name).to_have_text("Bluetooth Speaker")
    expect(product_page.product_price).to_have_text("$159.99")

    # Add the product to the cart and verify its contents
    expect(product_page.add_to_cart).to_be_visible()
    product_page.add_to_cart_button()
    product_page.open_cart()

    expect(cart_page.product_name).to_have_text("Bluetooth Speaker")
    expect(cart_page.product_price).to_have_text("$159.99")
    expect(cart_page.product_quantity).to_have_text("1")

    # Proceed to checkout and enter shipping information
    cart_page.checkout()
    check_out_page.shipping_info(
        "Omer",
        "Naeem",
        "Lumumbastr 21",
    )

    # Submit an invalid card number to exercise payment validation
    check_out_page.payment_info(
        "1234 1234 1234 1234",
        "12/27",
        "123",
        "Omer Naeem",
    )
    check_out_page.place_order()

    # Verify the error appears and no confirmation is visible
    expect(check_out_page.checkout_error).to_have_text(
        "Invalid card number. Please check and try again."
    )
    expect(
        page.get_by_test_id("order-confirmation-heading")
    ).not_to_be_visible()


def test_checkout_with_missing_shipping_address(page):
    # Ensure login credentials are configured
    username = os.getenv("QA_USERNAME")
    password = os.getenv("QA_PASSWORD")
    assert username and password, (
        "Set QA_USERNAME and QA_PASSWORD in the project .env file."
    )

    # Initialize Page Objects for the checkout journey
    login_page = LoginPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    check_out_page = CheckOutPage(page)

    # Log in and verify successful navigation
    login_page.open()
    login_page.login(username, password)
    expect(page).to_have_url("https://qademo.com/catalog")

    # Add the Bluetooth Speaker to the cart
    catalog_page.open_bluetooth_speaker()
    product_page.add_to_cart_button()
    product_page.open_cart()

    # Proceed to checkout
    cart_page.checkout()

    # Fill the other shipping fields but leave the address empty
    check_out_page.first_name.fill("Omer")
    check_out_page.last_name.fill("Naeem")

    # Enter valid-format demo payment data
    check_out_page.payment_info(
        "4242 4242 4242 4242",
        "12/27",
        "123",
        "Omer Naeem",
    )

    # Submit without a shipping address
    check_out_page.place_order()

    # Verify that the required-address validation is displayed
    expect(check_out_page.address_error).to_have_text(
        "Address is required"
    )

