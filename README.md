# Demo Test

Python + Playwright + Pytest 的 ParaBank E2E 自動化測試範例，採用 BDD、Page Object Model。

## 內容
- `features/parabank.feature`：以 Gherkin 描述使用者情境
- `tests/e2e/test_parabank.py`：pytest-bdd 步驟定義與測試載入
- `pages/parabank_page.py`：頁面操作封裝
- `doc/test/parabank.md`：測試案例清單
- `.github/workflows/e2e.yml`：GitHub Actions CI
- `Jenkinsfile`：Jenkins Pipeline
- `Dockerfile`：Playwright 測試容器

## 本地執行
```bash
pip install -r requirements.txt
python -m playwright install chromium
pytest tests/e2e/test_parabank.py
```

## Jenkins / Docker
```bash
docker build -t demo-bank-e2e .
docker run --rm -v ${PWD}:/app demo-bank-e2e
```

Jenkins、GitHub Actions 與 Docker 都共用 `scripts/run_e2e.py`，因此要回退 CI 行為時，通常只要改一個入口腳本。
Jenkins 版本會先用 `Dockerfile` 建 image，再在容器內跑測試，最後把 JUnit 與 HTML 報表、截圖一起 archive。
目前 `Jenkinsfile` 只依賴基本 Pipeline 能力，不需要另外安裝 HTML Publisher 或 JUnit 外掛。

### Jenkins 建置步驟
1. 安裝必要外掛：`Pipeline`、`Git`、`JUnit`、`HTML Publisher`
2. 在 Jenkins 新增 `Pipeline` Job，來源選 `Pipeline script from SCM`
3. SCM 指向這個 GitHub repo，Branch 填 `main`
4. Jenkins 主機需可執行 `docker build` 與 `docker run`
5. Pipeline 會自動讀取專案根目錄的 `Jenkinsfile`

### Jenkins 產物
- `artifacts/reports/junit.xml`
- `artifacts/reports/pytest-report.html`
- `artifacts/screenshots/`
- 這些檔案會直接作為 build artifacts 保留在 Jenkins

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
- Jenkins pipeline 也能獨立執行
