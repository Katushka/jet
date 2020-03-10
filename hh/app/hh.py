import requests
import logging
from hh.app.core import ApiCore


class ApiHh(ApiCore):
    logging.basicConfig(filename="report_api_test.log", level=logging.INFO)

    def get_list_vacancies(self, params):
        url = f'{ApiCore.BASE_URL}vacancies'
        answer = get(url, params)
        return answer

    def get_vacancy_id(self, vacancy_id):
        url = f'{ApiCore.BASE_URL}vacancies/{vacancy_id}'
        answer = get(url)
        return answer


def get(url, params=None):
    response = requests.get(url, params=params)
    logging.info(f" \n\nGET: {url} \nParams: {params} \nStatus code:{response.status_code}")
    response.raise_for_status()
    answer = response.json()
    logging.info(answer)
    return answer
