#!/usr/bin/python
# -*- coding: utf-8 -*-

# импортируем библиотеки

import pandas as pd
from sqlalchemy import create_engine

db_config = {'user': 'praktikum_student', # имя пользователя
            'pwd': 'Sdf4$2;d-d30pp', # пароль
            'host': 'rc1b-wcoijxj3yxfsf3fs.mdb.yandexcloud.net',
            'port': 6432, # порт подключения
            'db': 'data-analyst-zen-project-db'} # название базы данных

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
                                                db_config['pwd'],
                                                db_config['host'],
                                                db_config['port'],
                                                db_config['db'])
# создаем движок
engine = create_engine(connection_string)

# выбираем все данные из соответствующей таблицы
query = 'SELECT * FROM dash_visits'

# читаем все данные в объект pandas 
dash_visits = pd.io.sql.read_sql(query, con = engine)

# импортируем в csv-файл (разделители автоматически - запятая)
dash_visits.to_csv('dash_visits.csv', index=False)