# Ближайшие бары

Для поиска ближайшего бара используются:

Входные данные:
1. Текущие координаты пользователя
2. Координаты баров из json файла

Выходные данные:
json-текст или json-файл с информацией о ближайшем баре


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

$ python bars.py {source_file} [destination_file]
где source_file - json-файл источник данных,
    destination_file - json-файл выходных данных

```bash

$ python bars.py bars.json # Выведет результат работы в консоль
# Пример ответа скрипта:
 {"geometry": {"coordinates": [37.5506184192192, 55.75909089705614], "type": "Point"}, "properties": {"DatasetId": 1796, "VersionNumber": 2, "ReleaseNumber": 2, "RowId": "0f82e78b-58a2-40a4-802a-77373093f624", "Attributes": {"global_id": 20660867, "Name": "Бар «Разлив»", "IsNetObject": "нет", "OperatingCompany": null, "AdmArea": "Центральный административный округ", "District": "Пресненский район", "Address": "улица Сергея Макеева, дом 4", "PublicPhone": [{"PublicPhone": "(499) 256-41-20"}], "SeatsCount": 15, "SocialPrivileges": "нет"}}, "type": "Feature"} 

$ python bars.py bars.json bars_out.json # Выведет результат работы в файл bars_out.json 
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
