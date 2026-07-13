#!/bin/bash

echo " Cleaning old reports..."
rm -rf allure-results allure-report

echo " Running tests..."
pytest -v --alluredir=allure-results

echo "Generating Allure report..."
allure serve allure-results