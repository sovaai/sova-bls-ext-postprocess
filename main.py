import logging


async def postprocess_event(message):
    if message['technical_info'].get('not_send_engine'):
        message['text'] = {"value": message['technical_info']['technical_context']['last_response']['text']}
    return message


async def main(message):
    logging.debug(f"Данные которые пришли в постпроцессор {message}")
    if message['type'] == 'event':
        message = await postprocess_event(message)
    return message