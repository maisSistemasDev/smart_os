import logging
import functools

# Configura o logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_decorator(func):
    """
    Decorator que registra a entrada e saída de uma função, bem como exceções.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Entrando na função {func.__name__} com args: {args} e kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Saindo da função {func.__name__} com resultado: {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção na função {func.__name__}: {e}")
            raise  # Re-lança a exceção para que o comportamento da função não seja alterado
    return wrapper
import logging
import functools

# Configura o logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_decorator(func):
    """
    Decorator que registra a entrada e saída de uma função, bem como exceções.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Entrando na função {func.__name__} com args: {args} e kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Saindo da função {func.__name__} com resultado: {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção na função {func.__name__}: {e}")
            raise  # Re-lança a exceção para que o comportamento da função não seja alterado
    return wrapper
