import logging
import azure.functions as func

app = func.FunctionApp()


@app.timer_trigger(schedule="0 10 * * * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def ADAI_Func_Landing_Zone_Load(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')


@app.timer_trigger(schedule="0 15 * * * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def ADAI_Func_Data_Refinement(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')


@app.timer_trigger(schedule="0 20 * * * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def ADAI_Func_RDB_Integration(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
