from __future__ import annotations

import re
from pathlib import Path

from playwright.sync_api import Page, expect


class ParaBankPage:
    URL = "https://parabank.parasoft.com/parabank/index.htm"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator('input[type="submit"][value="Log In"]')
        self.logout_link = page.get_by_role("link", name=re.compile(r"log\s*out", re.I))
        self.customer_login_heading = page.get_by_role("heading", name="Customer Login")
        self.accounts_overview_heading = page.get_by_role("heading", name="Accounts Overview")
        self.register_link = page.get_by_role("link", name="Register")
        self.login_error_message = page.get_by_text(
            "The username and password could not be verified."
        )
        self.open_new_account_link = page.get_by_role("link", name="Open New Account")
        self.open_new_account_heading = page.get_by_role("heading", name="Open New Account")
        self.account_type_select = page.locator("#type")
        self.from_account_select = page.locator("#fromAccountId")
        self.open_account_button = page.get_by_role("button", name="Open New Account")
        self.account_opened_heading = page.get_by_role("heading", name="Account Opened!")
        self.find_transactions_link = page.get_by_role("link", name="Find Transactions")
        self.find_transactions_heading = page.get_by_role("heading", name="Find Transactions")
        self.find_transactions_button = page.locator("#findById")
        self.account_id_select = page.locator("#accountId")
        self.update_contact_link = page.get_by_role("link", name="Update Contact Info")
        self.update_contact_heading = page.get_by_role("heading", name="Update Profile")

    def open(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")
        expect(self.customer_login_heading).to_be_visible(timeout=15000)

    def assert_login_form_visible(self) -> None:
        expect(self.username_input).to_be_visible(timeout=15000)
        expect(self.username_input).to_be_enabled(timeout=15000)
        expect(self.password_input).to_be_visible(timeout=15000)
        expect(self.password_input).to_be_enabled(timeout=15000)
        expect(self.login_button).to_be_visible(timeout=15000)
        expect(self.login_button).to_be_enabled(timeout=15000)
        expect(self.register_link).to_be_visible(timeout=15000)

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        expect(self.page).to_have_url(re.compile(r"/overview\.htm"), timeout=15000)
        expect(self.accounts_overview_heading).to_be_visible(timeout=15000)

    def login_with_invalid_credentials(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        expect(self.login_error_message).to_be_visible(timeout=15000)

    def open_new_account(self) -> None:
        self.open_new_account_link.click()
        expect(self.open_new_account_heading).to_be_visible(timeout=15000)
        expect(self.account_type_select).to_be_visible(timeout=15000)
        expect(self.from_account_select).to_be_visible(timeout=15000)

    def create_savings_account(self) -> None:
        self.account_type_select.select_option("SAVINGS")
        expect(self.open_account_button).to_be_enabled(timeout=15000)
        self.open_account_button.click()

        expect(self.account_opened_heading).to_be_visible(timeout=15000)

    def open_find_transactions(self) -> None:
        self.find_transactions_link.click()
        expect(self.find_transactions_heading).to_be_visible(timeout=15000)
        expect(self.account_id_select).to_be_visible(timeout=15000)

    def find_transactions(self) -> None:
        self.find_transactions_button.click()
        expect(self.page).to_have_url(re.compile(r"/findtrans.htm"), timeout=15000)

    def open_update_contact_info(self) -> None:
        self.update_contact_link.click()
        expect(self.update_contact_heading).to_be_visible(timeout=15000)

    def logout(self) -> None:
        expect(self.logout_link).to_be_visible(timeout=15000)
        self.logout_link.click()

        expect(self.page).to_have_url(re.compile(r"/index\.htm"), timeout=15000)
        expect(self.customer_login_heading).to_be_visible(timeout=15000)

    def capture_failure_screenshot(self, filename: str) -> Path:
        screenshot_dir = Path(__file__).resolve().parents[1] / "artifacts" / "screenshots"
        screenshot_dir.mkdir(parents=True, exist_ok=True)

        screenshot_path = screenshot_dir / f"{filename}.png"
        self.page.screenshot(path=str(screenshot_path), full_page=True)
        return screenshot_path
