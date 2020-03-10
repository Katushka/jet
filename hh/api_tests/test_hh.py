import pytest
import random
from hh.app.core import ApiCore


class TestHh(ApiCore):

    list_params = [
        ('noExperience', 'part', 'fullDay', 'direct', '14.205'),
        ('noExperience', 'part', 'flexible', 'anonymous', '18.246'),
        ('between1And3', 'part', 'fullDay', 'open', '18.249'),
        ('between1And3', 'part', 'fullDay', 'open', '18.249'),
        ('between1And3', 'part', 'flexible', 'closed', '16.228'),
        ('between1And3', 'part', 'fullDay', 'closed', '16.228')
    ]

    @pytest.mark.parametrize("experience, employment, schedule, vacancy_type, metro", list_params)
    def test_params_list_vacancies(self, hh, experience, employment, schedule, vacancy_type, metro):
        params = {'experience': experience, 'employment': employment, 'schedule': schedule,
                  'vacancy_type': vacancy_type, 'metro': metro}
        answer = hh.get_list_vacancies(params)
        vacancies = answer['items']
        if len(answer['items']) != 0:
            vacancy = random.choice(vacancies)
            vacancy_id = vacancy['id']
            city_name = vacancy['area']['name']
            city_id = vacancy['area']['id']
            station_id = vacancy['address']['metro']['station_id']
            assert station_id == metro
            assert city_name == self.CITY_SPB['name']
            assert city_id == self.CITY_SPB['id']
        else:
            assert len(vacancies) == 0
            vacancy_id = None

        return vacancy_id

    @pytest.mark.parametrize("experience, employment, schedule, vacancy_type, metro", list_params)
    def test_params_in_vacancy(self, hh, experience, employment, schedule, vacancy_type, metro):
        vacancy_id = self.test_params_list_vacancies(hh, experience, employment, schedule, vacancy_type, metro)
        if vacancy_id:
            vacancy = hh.get_vacancy_id(vacancy_id)
            vacancy_experience = vacancy['experience']['id']
            vacancy_employment = vacancy['employment']['id']
            vacancy_schedule = vacancy['schedule']['id']
            vacancy_metro = vacancy['address']['metro']['station_id']
            assert vacancy_experience == experience
            assert vacancy_employment == employment
            assert vacancy_schedule == schedule
            assert vacancy_metro == metro
        else:
            print('No vacancy for testing!!!')
