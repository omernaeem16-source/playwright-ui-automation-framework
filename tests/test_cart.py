import os

from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_remove_product_from_cart(page):
    # Initialize page objects for the cart removal flow
    login_page = LoginPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Load credentials from environment variables
    username = os.getenv("QA_USERNAME")
    password = os.getenv("QA_PASSWORD")
    assert username and password, (
        "Set QA_USERNAME and QA_PASSWORD in the project .env file."
    )

    # Log in and verify successful navigation
    login_page.open()
    login_page.login(username, password)
    expect(page).to_have_url("https://qademo.com/catalog")

    # Open the Bluetooth Speaker product page
    catalog_page.open_bluetooth_speaker()

    # Verify product details before adding it to the cart
    expect(product_page.product_name).to_have_text("Bluetooth Speaker")
    expect(product_page.product_price).to_have_text("$159.99")
    expect(product_page.add_to_cart).to_be_visible()

    # Add the product and navigate to the cart
    product_page.add_to_cart_button()
    product_page.open_cart()

    # Verify the product and its initial quantity
    expect(cart_page.product_name).to_have_text("Bluetooth Speaker")
    expect(cart_page.product_price).to_have_text("$159.99")
    expect(cart_page.product_quantity).to_have_text("1")

    # Remove the product and verify that the cart becomes empty
    cart_page.remove_product_from_cart()
    expect(page.get_by_test_id("cart-empty-heading")).to_have_text(
        "Your cart is empty"
    )


def test_increase_product_quantity(page):
    # Initialize page objects
    login_page = LoginPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Load credentials from environment variables
    username = os.getenv("QA_USERNAME")
    password = os.getenv("QA_PASSWORD")
    assert username and password, (
        "Set QA_USERNAME and QA_PASSWORD in the project .env file."
    )

    # Log in and verify successful navigation
    login_page.open()
    login_page.login(username, password)
    expect(page).to_have_url("https://qademo.com/catalog")

    # Open the Bluetooth Speaker product page
    catalog_page.open_bluetooth_speaker()

    # Add the product and open the cart
    expect(product_page.product_name).to_have_text("Bluetooth Speaker")
    product_page.add_to_cart_button()
    product_page.open_cart()

    # Verify the initial quantity
    expect(cart_page.product_quantity).to_have_text("1")

    # Increase quantity from 1 to 2
    cart_page.increase_qty()
    expect(cart_page.product_quantity).to_have_text("2")


def test_decrease_product_quantity(page):
    # Initialize page objects
    login_page = LoginPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Load credentials from environment variables
    username = os.getenv("QA_USERNAME")
    password = os.getenv("QA_PASSWORD")
    assert username and password, (
        "Set QA_USERNAME and QA_PASSWORD in the project .env file."
    )

    # Log in and verify successful navigation
    login_page.open()
    login_page.login(username, password)
    expect(page).to_have_url("https://qademo.com/catalog")

    # Add the Bluetooth Speaker to the cart
    catalog_page.open_bluetooth_speaker()
    expect(product_page.product_name).to_have_text("Bluetooth Speaker")
    product_page.add_to_cart_button()
    product_page.open_cart()

    # Increase quantity from 1 to 2
    cart_page.increase_qty()
    expect(cart_page.product_quantity).to_have_text("2")

    # Decrease quantity from 2 to 1
    cart_page.decrease_qty()
    expect(cart_page.product_quantity).to_have_text("1")


def test_cart_subtotal_updates_when_quantity_increases(page):
    # Initialize page objects
    login_page = LoginPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Load credentials from environment variables
    username = os.getenv("QA_USERNAME")
    password = os.getenv("QA_PASSWORD")
    assert username and password, (
        "Set QA_USERNAME and QA_PASSWORD in the project .env file."
    )

    # Log in and verify successful navigation
    login_page.open()
    login_page.login(username, password)
    expect(page).to_have_url("https://qademo.com/catalog")

    # Add the Bluetooth Speaker to the cart
    catalog_page.open_bluetooth_speaker()
    expect(product_page.product_name).to_have_text("Bluetooth Speaker")
    product_page.add_to_cart_button()
    product_page.open_cart()

    # Verify the initial quantity and subtotal
    expect(cart_page.product_quantity).to_have_text("1")
    expect(cart_page.product_subtotal).to_have_text("$159.99")

    # Increase quantity from 1 to 2
    cart_page.increase_qty()

    # Verify that the subtotal doubles when quantity doubles
    expect(cart_page.product_quantity).to_have_text("2")
    expect(cart_page.product_subtotal).to_have_text("$319.98")

