import logging as logger
import random
import string


def generate_string(company_prefix=None):
    logger.info('Generate random string')
    if not company_prefix:
        company_prefix = 'Pharmateksol'

    random_string_length = 5
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_string_length))
    company_name = company_prefix + ' ' + random_string
    random_info = {'company_name': company_name}
    return random_info
