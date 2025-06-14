import logging
import azure.functions as func


def Landing_Zone_Load(myTimer: func.TimerRequest) -> None:
    logging.info('Python timer trigger function started.')
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
