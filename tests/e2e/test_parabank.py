from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

from pages.parabank_page import ParaBankPage

pytestmark = [pytest.mark.e2e, pytest.mark.functional]


@pytest.mark.describe("ParaBank 登入與登出流程")
@pytest.mark.flaky(reruns=2)
class TestParaBankPage:
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
