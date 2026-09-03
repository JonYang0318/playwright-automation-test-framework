from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

from pages.parabank_page import ParaBankPage

pytestmark = [pytest.mark.e2e, pytest.mark.functional]


@pytest.mark.describe("ParaBank 登入與登出流程")
@pytest.mark.flaky(reruns=2)
class TestParaBankPage:
    def _login(self, page: Page) -> ParaBankPage:
        parabank_page = ParaBankPage(page)
        parabank_page.open()
        parabank_page.login("john", "demo")
        return parabank_page

    def test_parabank_login_logout(self, page: Page) -> None:
        parabank_page = ParaBankPage(page)

        try:
            parabank_page.open()
            parabank_page.assert_login_form_visible()
            parabank_page.login("john", "demo")

            expect(parabank_page.accounts_overview_heading).to_be_visible(timeout=15000)

            parabank_page.logout()
            parabank_page.assert_login_form_visible()
        except Exception:
            parabank_page.capture_failure_screenshot("parabank_login_logout_failed")
            raise

    @pytest.mark.describe("ParaBank 首頁與登入表單")
    def test_parabank_login_form(self, page: Page) -> None:
        parabank_page = ParaBankPage(page)

        try:
            parabank_page.open()
            parabank_page.assert_login_form_visible()
        except Exception:
            parabank_page.capture_failure_screenshot("parabank_login_form_failed")
            raise

    @pytest.mark.describe("ParaBank 錯誤登入驗證")
    def test_parabank_invalid_login(self, page: Page) -> None:
        parabank_page = ParaBankPage(page)

        try:
            parabank_page.open()
            parabank_page.login_with_invalid_credentials("invalid-user", "invalid-password")
        except Exception:
            parabank_page.capture_failure_screenshot("parabank_invalid_login_failed")
            raise

    @pytest.mark.describe("ParaBank 帳戶總覽")
    def test_parabank_accounts_overview(self, page: Page) -> None:
        try:
            parabank_page = self._login(page)
            expect(parabank_page.accounts_overview_heading).to_contain_text(
                "Accounts Overview", timeout=15000
            )
            expect(page.get_by_role("cell", name="Account")).to_be_visible(timeout=15000)
            expect(page.locator("th").filter(has_text="Balance*")).to_be_visible(timeout=15000)
        except Exception:
            ParaBankPage(page).capture_failure_screenshot("parabank_accounts_overview_failed")
            raise

    @pytest.mark.describe("ParaBank 開立新帳戶頁面")
    def test_parabank_open_new_account_page(self, page: Page) -> None:
        try:
            parabank_page = self._login(page)
            parabank_page.open_new_account()
        except Exception:
            ParaBankPage(page).capture_failure_screenshot("parabank_open_account_failed")
            raise

    @pytest.mark.describe("ParaBank 交易查詢")
    def test_parabank_find_transactions(self, page: Page) -> None:
        try:
            parabank_page = self._login(page)
            parabank_page.open_find_transactions()
            parabank_page.find_transactions()
        except Exception:
            ParaBankPage(page).capture_failure_screenshot("parabank_find_transactions_failed")
            raise

    @pytest.mark.describe("ParaBank 聯絡資料頁面")
    def test_parabank_update_contact_info_page(self, page: Page) -> None:
        try:
            parabank_page = self._login(page)
            parabank_page.open_update_contact_info()
        except Exception:
            ParaBankPage(page).capture_failure_screenshot("parabank_update_contact_failed")
            raise
