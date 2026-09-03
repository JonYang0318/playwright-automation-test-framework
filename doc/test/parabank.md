# ParaBank - 銀行網站登入流程測試案例清單

## 測試範圍
- 測試頁面：ParaBank Demo Banking Site
- 官方站點：[https://parabank.parasoft.com/parabank](https://parabank.parasoft.com/parabank)
- 測試帳號：`john` / `demo`
- 自動化框架：Python + Playwright + Pytest + pytest-bdd + POM

## 測試案例
- [x] TC-01 開啟 ParaBank 首頁
- [x] TC-02 驗證登入區塊與欄位可見
- [x] TC-03 使用 `john / demo` 成功登入
- [x] TC-04 驗證登入後顯示 Accounts Overview
- [x] TC-05 驗證 Logout 可返回登入首頁
- [x] TC-06 發生失敗時自動截圖
- [x] TC-07 驗證首頁登入表單
- [x] TC-08 驗證錯誤帳密登入訊息
- [x] TC-09 驗證登入後帳戶總覽欄位
- [x] TC-10 開啟開立新帳戶頁面並驗證表單
- [x] TC-11 查詢帳戶交易紀錄
- [x] TC-12 開啟更新聯絡資料頁面

## 驗證重點
- 不使用 `time.sleep()`
- 優先使用 `role` 與 `id` 做定位
- 使用 `expect(...).to_be_visible()`、`expect(...).to_have_url()`、`expect(...).to_contain_text()` 進行動態等待
- 測試失敗時輸出 screenshot 方便追查
- Gherkin feature 位於 `features/parabank.feature`，步驟定義位於 `tests/e2e/test_parabank.py`

## 備註
- 測試重試標註使用 `@pytest.mark.flaky(reruns=2)`
- 測試完成後，將已通過案例更新為 `- [x]`
