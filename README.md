# Ближайшие бары

Для поиска ближайшего бара используются:
1. Текущие координаты пользователя
2. Координаты баров из json файла

На сайте data.mos.ru есть список московских баров.
Чтобы скачать файл в json-формате нужно:
1. Зарегистрироваться на сайте и получить ключ API;
2. Скачать файл по ссылке вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}
    
Выходные данные:
json-текст в консоль или json-файл с информацией о ближайшем баре


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
    
Запуск на Linux:

$ python bars.py {source_file} [destination_file]

 где source_file - json-файл источник данных,
 destination_file - json-файл выходных данных

```bash

$ python bars.py bars.json 
Choose option:
1 - Find the biggest bar.
2 - Find the smallest one.
3 - Find the closest one.
Type option number: 3
longitude: 37.57
latitude: 55.77
# Выведет результат работы в консоль
# Пример ответа скрипта:
 {"geometry": {"coordinates": [37.58699411741135, 55.77085237743563], "type": "Point"}, "properties": {"DatasetId": 1796, "VersionNumber": 2, "ReleaseNumber": 2, "RowId": "4b5eb176-f50c-4610-b3b0-de68378e53ce", "Attributes": {"global_id": 20731657, "Name": "Бар «ДЖЕМ»", "IsNetObject": "нет", "OperatingCompany": null, "AdmArea": "Центральный административный округ", "District": "Пресненский район", "Address": "Васильевская улица, дом 4", "PublicPhone": [{"PublicPhone": "(499) 254-28-22"}], "SeatsCount": 56, "SocialPrivileges": "нет"}}, "type": "Feature"}

$ python bars.py bars.json bars_out.json # Выведет результат работы в файл bars_out.json 
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
