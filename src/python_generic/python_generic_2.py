# from IPython import display
from ensure import ensure_annotations
from python_generic.custom_exception import GenericException
from utils.logger import logger


@ensure_annotations
def do_work_2(arg1: int, arg2: int) -> dict:

    # Perform your tasks here! #
    try:
        pass
    except Exception as e:
        raise GenericException(str(e))
    logger.info(f"Ran do_work_2 with {arg1}, {arg2}")
    return {}
