# Основные части проекта


## Бэкенд сайта
- Полноценный API, с которым будет интегрироваться фронтенд(и в теории можно интегрировать любое стороннее решение)
- Блочная структура сайта:
- Аутентификация пользователей app_auth
- Статистика/аналитика app_stat
- Конструктор достижений и скидок app_construct
- Основной модуль для записи покупок и выдачи сертификатов app_shop
- Фильтр игр по каталогу
## Фронтенд


## Считывание NFC карт
По первому взгляду на гугл выяснилось, что в продаже мало дешёвых считывателей, а те, что есть на али, либо имеют неподходящий софт, либо вообще неизвестно, какой там софт.
Проще всего будет зафигачить считыватель самому, купив Arduino и NFC Shield для него, написать прошивку и простую утилиту, которая будет сопоставлять серийник карты с ID пользователя, а затем предлагать автоматически прописать посещение или открыть интерфейс покупки в браузере.
Писать проще всего на C#.