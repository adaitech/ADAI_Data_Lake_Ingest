import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('O timer estava atrasado, executando agora!')

    logging.info('Executando função Azure no horário: %s', utc_timestamp)
