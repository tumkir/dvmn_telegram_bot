import os
import time
import requests
import telegram
import logging


def make_request(timestamp):
    headers = {'Authorization': os.environ['token']}
    parameters = {'timestamp': timestamp}
    response = requests.get('https://dvmn.org/api/long_polling/', headers=headers, params=parameters)
    response.raise_for_status()
    response_data = response.json()
    return response_data


def compose_message_text(attempts_info):
    if attempts_info['is_negative']:
        message = f'Задачу «{attempts_info["lesson_title"]}» требуется доработать. \n\nСсылка на задачу: https://dvmn.org{attempts_info["lesson_url"]}'
    else:
        message = f'Задача «{attempts_info["lesson_title"]}» успешно проверена. \n\nСсылка на задачу: https://dvmn.org{attempts_info["lesson_url"]}'
    return message


def main():
    telegram_token = os.environ['bot_token']
    chat_id = os.environ['chat_id']
    bot = telegram.Bot(token=telegram_token)
    timestamp = time.time()

    class MyLogsHandler(logging.Handler):
        def emit(self, record):
            log_entry = self.format(record)
            bot.send_message(chat_id=chat_id, text=log_entry)

    logger = logging.getLogger('Bot_loger')
    logger.setLevel(logging.WARNING)
    logger.addHandler(MyLogsHandler())
    logger.warning('Бот запущен')

    while True:
        try:
            response = make_request(timestamp)
            if response['status'] == 'found':
                timestamp = response['last_attempt_timestamp']
                message = compose_message_text(response['new_attempts'][0])
                bot.send_message(chat_id=chat_id, text=message)
            else:
                timestamp = response['timestamp_to_request']
        except (requests.exceptions.HTTPError, requests.exceptions.Timeout):
            logger.exception('Не удалось узнать статус проверки:\n\n')
            time.sleep(3600)
            continue


if __name__ == '__main__':
    main()
