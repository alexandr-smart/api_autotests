# Запуск тестов на Linux
```bash
PYTHONPATH=. pytest /home/test/PycharmProjects/api_autotests/tests --env=prod --alluredir=allure-results 
```

Run allure-reports Linux
```bash
allure serve /home/test/PycharmProjects/api_autotests/allure-results
```

# Запуск тестов на Windows
```bash
$$env:PYTHONPATH = "."
pytest .\tests --alluredir=allure-results
```

Run allure-reports Windows
```bash
allure serve C:\Users\alexandr\PycharmProjects\api_autotests\allure-results
```
