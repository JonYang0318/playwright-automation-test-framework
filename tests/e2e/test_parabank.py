from __future__ import annotations

from pathlib import Path

import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenarios, then, when

from pages.parabank_page import ParaBankPage

FEATURE_FILE = Path(__file__).resolve().parents[2] / "features" / "parabank.feature"
scenarios(str(FEATURE_FILE))

pytestmark = [pytest.mark.e2e, pytest.mark.functional, pytest.mark.flaky(reruns=2)]


@pytest.fixture
def parabank_page(page: Page) -> ParaBankPage:
    return ParaBankPage(page)


@given("I open the ParaBank home page")
def open_home_page(parabank_page: ParaBankPage) -> None:
    parabank_page.open()


@given("I am logged in to ParaBank")
def logged_in(parabank_page: ParaBankPage) -> None:
    parabank_page.open()
    parabank_page.login("john", "demo")


@when(parsers.parse('I log in with username "{username}" and password "{password}"'))
def login_with_credentials(
    parabank_page: ParaBankPage, username: str, password: str
) -> None:
    if username == "john" and password == "demo":
        parabank_page.login(username, password)
    else:
        parabank_page.login_with_invalid_credentials(username, password)


@then("the login form should be ready")
def login_form_is_ready(parabank_page: ParaBankPage) -> None:
    parabank_page.assert_login_form_visible()


@then("I should see the Accounts Overview page")
def accounts_overview_is_visible(parabank_page: ParaBankPage) -> None:
    expect(parabank_page.accounts_overview_heading).to_be_visible(timeout=15000)


@then("I should see the Customer Login form")
def customer_login_is_visible(parabank_page: ParaBankPage) -> None:
    parabank_page.assert_login_form_visible()


@then("I should see the invalid login message")
def invalid_login_is_visible(parabank_page: ParaBankPage) -> None:
    expect(parabank_page.login_error_message).to_be_visible(timeout=15000)


@then("the account overview should show Account and Balance columns")
def account_columns_are_visible(parabank_page: ParaBankPage) -> None:
    expect(parabank_page.accounts_overview_heading).to_be_visible(timeout=15000)
    expect(parabank_page.page.locator("th").filter(has_text="Account")).to_be_visible(
        timeout=15000
    )
    expect(parabank_page.page.locator("th").filter(has_text="Balance*")).to_be_visible(
        timeout=15000
    )


@when("I log out")
def log_out(parabank_page: ParaBankPage) -> None:
    parabank_page.logout()


@when("I open the new account page")
def open_new_account_page(parabank_page: ParaBankPage) -> None:
    parabank_page.open_new_account()


@then("the new account form should be visible")
def new_account_form_is_visible(parabank_page: ParaBankPage) -> None:
    expect(parabank_page.open_new_account_heading).to_be_visible(timeout=15000)
    expect(parabank_page.account_type_select).to_be_visible(timeout=15000)
    expect(parabank_page.from_account_select).to_be_visible(timeout=15000)


@when("I open the transaction search page")
def open_transaction_search(parabank_page: ParaBankPage) -> None:
    parabank_page.open_find_transactions()


@when("I search transactions by account")
def search_transactions(parabank_page: ParaBankPage) -> None:
    parabank_page.find_transactions()


@then("the transaction search page should remain available")
def transaction_search_is_available(parabank_page: ParaBankPage) -> None:
    expect(parabank_page.find_transactions_heading).to_be_visible(timeout=15000)


@when("I open the update contact information page")
def open_update_contact(parabank_page: ParaBankPage) -> None:
    parabank_page.open_update_contact_info()


@then("the update profile page should be visible")
def update_profile_is_visible(parabank_page: ParaBankPage) -> None:
    expect(parabank_page.update_contact_heading).to_be_visible(timeout=15000)
