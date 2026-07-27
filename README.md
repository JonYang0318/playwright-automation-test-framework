# Demo Test

Python + Playwright + Pytest 的 ParaBank E2E 自動化測試範例，採用 Page Object Model。

## 內容
- `tests/e2e/test_parabank.py`：登入 / 登出主測試
- `pages/parabank_page.py`：頁面操作封裝
- `doc/test/parabank.md`：測試案例清單
- `.github/workflows/e2e.yml`：GitHub Actions CI

## 本地執行
```bash
pip install -r requirements.txt
python -m playwright install chromium
pytest tests/e2e/test_parabank.py
```

## 報表輸出
- GitHub Actions 會產生：
  - `artifacts/reports/pytest-report.html`
  - `artifacts/reports/junit.xml`
  - `artifacts/screenshots/` 失敗截圖
- Workflow 結束後可在 Actions 頁面下載 artifacts

## CI 觸發條件
- 推送到 `main`
- Pull Request
- 手動執行 `workflow_dispatch`
