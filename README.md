# Бот-монитор проверки на сайте dvmn.org

Бот для телеграм оповещает о проверке заданий на сайте [dvmn.org](https://dvmn.org/)

## Как запустить на Heroku

* Зарегистрируйтесь на [heroku.com](https://www.heroku.com/) и создайте [новое приложение](https://dashboard.heroku.com/new-app)
* Форкните данный репозиторий

В разделе **Config Vars** на вкладке **Settings** вашего приложения пропишите:
- Токен бота. Необходимо создать бота и получить токен у [@botfather](https://t-do.ru/botfather)
- Ваш chat_id в телеграме. Можно узнать у бота [@userinfobot](https://t-do.ru/userinfobot)
- [Токен от dvmn](https://dvmn.org/api/docs/)

![config vars](https://raw.githubusercontent.com/tumkir/dvmn_telegram_bot/master/image/config_vars.png)

- Напишите личное сообщение вашему боту, иначе он не сможет отправить сообщение вам.
- Привяжите аккаунт GitHub на вкладке **Deploy** вашего приложения на Heroku и выберите нужный репозиторий
- Нажмите на кнопку **Deploy Branch** (позже можете включите автоматический деплой кнопкой выше)
- На вкладке **Resources** включите Dynos

![dynos](https://raw.githubusercontent.com/tumkir/dvmn_telegram_bot/master/image/dynos.png)

Бот должен успешно запуститься и написать об этом вам в телеграм.

Если сообщение от бота не пришло, то нужно поставить [консольный клиент Heroku](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) и прочитать логи

```bash
heroku logs --app APP_NAME
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).