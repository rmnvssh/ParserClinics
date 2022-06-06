import requests
from bs4 import BeautifulSoup as BS
import random_info
import pandas as pd

page = 1
id = 0
filteredClinics = []

while True:
    if page == 1:
        r = requests.get("https://prodoctorov.ru/nnovgorod/top/medcentr/")
    else:
        r = requests.get("https://prodoctorov.ru/nnovgorod/top/medcentr/" + "?page=" + str(page))
    html = BS(r.text, "html.parser")
    allClinics = html.findAll('div', class_='b-card__top')

    if len(allClinics):
        for clinic in allClinics:
            id += 1
            isName = clinic.find('div', class_='b-card__name').\
                find('a', class_='b-card__name-link b-link ui-text ui-text_h5 ui-text_color_primary-blue')
            name = next(isName.stripped_strings)
            address = clinic.find('div', class_='b-card__address-container').find('div', class_='b-card__address').text
            isPhone = clinic.find('div', class_='d-flex').find('div', class_='b-card__lpu-phone-container')
            if (isPhone is not None):
                phone = isPhone.find('div', class_='b-card__lpu-phone').\
                    find('span', class_='b-card__lpu-phone-num').text
            else:
                phone = random_info.number()

            mail = random_info.email_clinic(8)
            passClinic = random_info.generate_password()

            link = clinic.find('div', class_='b-card__name').\
                find('a', class_='b-card__name-link b-link ui-text ui-text_h5 ui-text_color_primary-blue').get('href')
            clinicUrl = "https://prodoctorov.ru" + str(link)
            clinicR = requests.get(clinicUrl)
            title = BS(clinicR.text, "html.parser")
            infoClinic = title.find('div', class_='b-clinic-profile__content b-text-unit b-text-unit_color_dark').\
                get_text(' ', strip=False)
            filteredClinics.append([str(id), name, infoClinic, address, mail, phone, str(passClinic)])

        page += 1
    else:
        break

hospitals = pd.DataFrame(filteredClinics, columns=['id[pk]', 'Название клиники', 'Специализация', 'Адрес', 'Email', 'Телефон', 'Пароль'])
hospitals.to_csv('hospitals.csv', index=False, sep=';')
