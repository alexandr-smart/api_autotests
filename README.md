# Запуск всех тестов
```bash
PYTHONPATH=. pytest /home/test/PycharmProjects/api_autotests/tests --alluredir=allure-results 
```

Run allure-reports
```bash
allure serve /home/test/PycharmProjects/api_autotests/allure-results
```
