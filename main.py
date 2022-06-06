import requests
from bs4 import BeautifulSoup as BS

page = 1
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
            isName = clinic.find('div', class_='b-card__name').\
                find('a', class_='b-card__name-link b-link ui-text ui-text_h5 ui-text_color_primary-blue')
            name = next(isName.stripped_strings)
            address = clinic.find('div', class_='b-card__address-container').find('div', class_='b-card__address').text
            isPhone = clinic.find('div', class_='d-flex').find('div', class_='b-card__lpu-phone-container')
            if (isPhone is not None):
                phone = isPhone.find('div', class_='b-card__lpu-phone').find('span', class_='b-card__lpu-phone-num').text
            else:
                phone = str("-")

            link = clinic.find('div', class_='b-card__name').find('a', class_='b-card__name-link b-link ui-text ui-text_h5 ui-text_color_primary-blue').get('href')
            clinicUrl = "https://prodoctorov.ru" + str(link)
            clinicR = requests.get(clinicUrl)
            title = BS(clinicR.text, "html.parser")
            infoClinic = title.find('div', class_='b-clinic-profile__content b-text-unit b-text-unit_color_dark').get_text('\n', strip=False)
            filteredClinics.append('Название клиники: ' + name + "\n" 'Адрес: ' + address + "\n" + 'Телефон: ' + phone + "\n" + infoClinic + "\n\n")

        page += 1
    else:
        break

for data in filteredClinics:
    print(data)
