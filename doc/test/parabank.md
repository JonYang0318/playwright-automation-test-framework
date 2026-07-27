# ParaBank - 銀行網站登入流程測試案例清單

## 測試範圍
- 測試頁面：ParaBank Demo Banking Site
- 官方站點：[https://parabank.parasoft.com/parabank](https://parabank.parasoft.com/parabank)
- 測試帳號：`john` / `demo`
- 自動化框架：Python + Playwright + Pytest + POM

## 測試案例
- [x] TC-01 開啟 ParaBank 首頁
- [x] TC-02 驗證登入區塊與欄位可見
- [x] TC-03 使用 `john / demo` 成功登入
- [x] TC-04 驗證登入後顯示 Accounts Overview
- [x] TC-05 驗證 Logout 可返回登入首頁
- [x] TC-06 發生失敗時自動截圖

## 驗證重點
- 不使用 `time.sleep()`
- 優先使用 `role` 與 `id` 做定位
- 使用 `expect(...).to_be_visible()`、`expect(...).to_have_url()`、`expect(...).to_contain_text()` 進行動態等待
- 測試失敗時輸出 screenshot 方便追查

## 備註
- 測試重試標註使用 `@pytest.mark.flaky(reruns=2)`
- 測試完成後，將已通過案例更新為 `- [x]`
