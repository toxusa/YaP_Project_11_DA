# YaP_Project_11_DA
## Дашборд для Яндeкc.Дзeн
### Описание проекта
Мы работаем аналитиком в Яндекс.Дзене. Почти всё наше время занимает анализ пользовательского взаимодействия с карточками статей.
Каждую карточку определяют её тема и источник (у него тоже есть тема). Примеры тем: «Красота и здоровье», «Россия», «Путешествия».
Пользователей системы характеризует возрастная категория. Скажем, «26-30» или «45+».

Есть три способа взаимодействия пользователей с системой:
- Карточка отображена для пользователя (show);
- Пользователь кликнул на карточку (click);
- Пользователь просмотрел статью карточки (view).

Каждую неделю начинающие менеджеры Денис и Валерия задают вам одни и те же вопросы:
1. Сколько взаимодействий пользователей с карточками происходит в системе с разбивкой по темам карточек?
2. Как много карточек генерируют источники с разными темами?
3. Как соотносятся темы карточек и темы источников?

На шестую неделю работы мы решаем, что процесс пора автоматизировать и нужно сделать дашборд.
Дашборд будет основываться на пайплайне, который будет брать данные из таблицы, в которых хранятся сырые данные, трансформировать данные и укладывать их в агрегирующую таблицу. Пайплайн будет разработан для нас дата-инженерами.


