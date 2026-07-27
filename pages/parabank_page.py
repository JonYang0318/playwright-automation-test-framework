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
