import logging
# import ADAI_Data_Acquisition
# import ADAI_Landing_Zone_Load
# import ADAI_Data_Refinement
# import ADAI_RDB_Integration
import azure.functions as func

app = func.FunctionApp()


@app.timer_trigger(schedule="0 5 * * * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')


# @app.timer_trigger(schedule="0 5 * * * *", arg_name="ADAI_Func_Data_Acquisition", run_on_startup=False,
#                    use_monitor=False)
# def timer_trigger(myTimer: func.TimerRequest) -> None:

#     logging.info('Python timer trigger function started.')
#     if myTimer.past_due:
#         logging.info('The timer is past due!')

#     # ADAI_Data_Acquisition.Data_Acquisition(myTimer)

#     logging.info('Python timer trigger function executed.')


# @app.timer_trigger(schedule="0 10 * * * *", arg_name="ADAI_Func_Landing_Zone_Load", run_on_startup=False,
#                    use_monitor=False)
# def timer_trigger(myTimer: func.TimerRequest) -> None:
#     if myTimer.past_due:
#         logging.info('The timer is past due!')

#     ADAI_Landing_Zone_Load.Landing_Zone_Load(myTimer)

#     logging.info('Python timer trigger function executed.')


# @app.timer_trigger(schedule="0 15 * * * *", arg_name="ADAI_Func_RDB_Integration", run_on_startup=False,
#                    use_monitor=False)
# def timer_trigger(myTimer: func.TimerRequest) -> None:
#     if myTimer.past_due:
#         logging.info('The timer is past due!')

#     ADAI_Data_Refinement.Data_Refinement(myTimer)

#     logging.info('Python timer trigger function executed.')


# @app.timer_trigger(schedule="0 20 * * * *", arg_name="ADAI_Func_Landing_Zone_Load", run_on_startup=False,
#                    use_monitor=False)
# def timer_trigger(myTimer: func.TimerRequest) -> None:
#     if myTimer.past_due:
#         logging.info('The timer is past due!')

#     ADAI_RDB_Integration.RDB_Integration(myTimer)

#     logging.info('Python timer trigger function executed.')
