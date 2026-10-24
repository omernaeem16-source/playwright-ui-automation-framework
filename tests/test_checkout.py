
import os

from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.check_out_page import CheckOutPage


def test_checkout_with_invalid_cardnumber(page):
    # Get login credentials from environment variables
    username = os.getenv("QA_USERNAME")
    password = os.getenv("QA_PASSWORD")

    # Ensure both credentials are configured before running the test
    assert username and password, (
        "Set QA_USERNAME and QA_PASSWORD in the project .env file."
    )

    # Initialize Page Objects for the checkout journey
    login_page = LoginPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    check_out_page = CheckOutPage(page)

    # Step 1: Log in and verify successful navigation to the catalog
    login_page.open()
    login_page.login(username, password)
    expect(page).to_have_url("https://qademo.com/catalog")

    # Step 2: Open the in-stock Laptop Backpack product
    catalog_page.open_laptop_backpack()

    # Verify the product name and price
    expect(product_page.product_name).to_have_text("Laptop Backpack")
    expect(product_page.product_price).to_have_text("$49.99")

    # Step 3: Add the product to the cart
    expect(product_page.add_to_cart).to_be_visible()
    product_page.add_to_cart_button()
    product_page.open_cart()

    # Verify the product details and quantity in the cart
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

    # Step 5: Enter an invalid card number to test payment validation
    check_out_page.payment_info(
        "1234 1234 1234 1234",
        "12/27",
        "123",
        "Omer Naeem",
    )
    check_out_page.place_order()

    # Verify the invalid-card error is displayed
    expect(check_out_page.checkout_error).to_have_text(
        "Invalid card number. Please check and try again."
    )

    # Verify that no order confirmation is displayed
    expect(
        page.get_by_test_id("order-confirmation-heading")
    ).not_to_be_visible()


def test_checkout_with_missing_shipping_address(page):
    # Get login credentials from environment variables
    username = os.getenv("QA_USERNAME")
    password = os.getenv("QA_PASSWORD")

    # Ensure both credentials are configured before running the test
    assert username and password, (
        "Set QA_USERNAME and QA_PASSWORD in the project .env file."
    )

    # Initialize Page Objects for the checkout journey
    login_page = LoginPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    check_out_page = CheckOutPage(page)

    # Step 1: Log in and verify successful navigation to the catalog
    login_page.open()
    login_page.login(username, password)
    expect(page).to_have_url("https://qademo.com/catalog")

    # Step 2: Open the in-stock Laptop Backpack product
    catalog_page.open_laptop_backpack()

    # Add the product to the cart and open the cart
    product_page.add_to_cart_button()
    product_page.open_cart()

    # Step 3: Proceed to checkout
    cart_page.checkout()

    # Fill in the first and last names, but leave the address empty
    check_out_page.first_name.fill("Omer")
    check_out_page.last_name.fill("Naeem")

    # Enter valid-format demo payment data
    check_out_page.payment_info(
        "4242 4242 4242 4242",
        "12/27",
        "123",
        "Omer Naeem",
    )

    # Submit the order without a shipping address
    check_out_page.place_order()

    # Verify that the required-address validation is displayed
    expect(check_out_page.address_error).to_have_text(
        "Address is required"
    )
