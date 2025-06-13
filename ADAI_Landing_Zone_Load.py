import logging
import azure.functions as func

app = func.FunctionApp()


@app.function_name(name="ADAI_Landing_Zone_Load")
@app.timer_trigger(schedule="0 4 * * TUE", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def ADAI_Landing_Zone_Load(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
