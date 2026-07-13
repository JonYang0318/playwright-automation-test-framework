# 使用官方 Playwright Python 基礎鏡像
FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy

# 設定工作目錄
WORKDIR /app

# 複製專案進 container
COPY . /app

# 安裝系統依賴（Playwright 必要）
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libpangocairo-1.0-0 \
    libxss1 \
    libgbm1 \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Python 套件
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 安裝 Playwright browser
RUN playwright install --with-deps

# 預設執行 pytest
CMD ["pytest"]