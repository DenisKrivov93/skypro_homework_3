# SkyBank — анализ банковских операций
Приложение способное проанализировать блок данных и получить сумму по транзакции 
с попутной конвертацией в рубли, если она совершена в другой валюте.
Способно при получениии номера счёта или карты обработать его и возвратить с маской.

## Работа с API
Смотри .env.exemple

### Тесты
pytest --cov=. --cov-report=html - сгенерирует отчет по тестам

#### Логгирование
Программа, в ходе выполнения работы, ведёт логгирование проццесса 
и сохраняет информацию в папке "logs", в корне проекта
