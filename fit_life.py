LENGTH_FRAME = 60

ML_WATER_PER_KG = 30
RATIO_ML_TO_L = 1000

MIN_AGE = 0
MAX_AGE = 120

MIN_WEIGHT = 0
MAX_WEIGHT = 600

MIN_HEIGHT = 0
MAX_HEIGHT = 3

# Список кортежей: 1 элемент - верхняя граница ИМТ,
# 2 элемент - название категории
BMI_CATEGORIES = [
    (16, 'Выраженный дефицит массы тела'),
    (18.5, 'Дефицит массы тела'),
    (25, 'Нормальная масса тела'),
    (30, 'Избыточная масса тела (предожирение)'),
    (35, 'Ожирение I степени'),
    (40, 'Ожирение II степени'),
    # float('inf') - положительная бесконечность
    (float('inf'), 'Ожирение III степени')
]


def validate_data(value, min_value, max_value):
    """Проверка, входит ли значение в допустимый диапазон."""
    if value <= min_value:
        print('Значение не может быть отрицательным.')
        return False
    elif value > max_value:
        print('Вы ввели слишком большое значение.')
        return False
    return True


def get_name():
    # Docstring - документация функции, класса или модуля
    """Проверка на ввод имени"""
    while True:
        user_name = input('Введите Ваше имя: ').strip()
        # Убираем дефисы и пробелы для проверки ввода
        clean_user_name = user_name.replace('-', '').replace(' ', '')

        if not user_name:
            print('Ваше имя не может быть пустым.')
        # .isalpha() для проверки ввода на буквы
        elif not clean_user_name.isalpha():
            print('Имя может содержать только буквы, дефис или пробел.')
        else:
            return user_name.title()


def get_age():
    """Ввод возраста"""
    while True:
        try:
            age = int(input('Введите ваш возраст: '))
        except ValueError:
            print('Пожалуйста, введите целое число.')
            continue
        if validate_data(age, MIN_AGE, MAX_AGE):
            return age


def get_weight():
    """Ввод веса"""
    while True:
        try:
            weight = float(input('Введите ваш вес'
                                 '(в кг - 65.5): ').replace(',', '.'))
        except ValueError:
            print('Пожалуйста, введите число.')
            # continue используется для пропуска оставшейся части итерации
            # и перехода к следующей. В моём случае - повторный ввод input()
            continue
        if validate_data(weight, MIN_WEIGHT, MAX_WEIGHT):
            return weight


def get_height():
    """Ввод роста"""
    while True:
        try:
            height = float(input('Введите ваш рост'
                                 '(в метрах - 1.72): ').replace(',', '.'))
        except ValueError:
            print('Пожалуйста, введите число.')
            continue
        if validate_data(height, MIN_HEIGHT, MAX_HEIGHT):
            return height


def get_age_suffix(age):
    """Склонения возраста"""
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'


def get_bmi_category(bmi):
    """Проверка категории ИМТ"""
    for limit, category in BMI_CATEGORIES:
        if bmi < limit:
            return category


# Переменные добавлены в связи с ошибкой
# FCS100 - множество вычислений в f-string
separator = '=' * LENGTH_FRAME

# str.center(width) для выравнивания по центру блока
title = 'FITLIFE'.center(LENGTH_FRAME)
greeting = 'Здравствуйте! Вас приветствует автономный фитнес-трекер.'
description = 'Мне нужно собрать базовую информацию о Вас.'

# str.ljust(width) для выравнивания по левому краю шириной width
greeting_line = greeting.ljust(LENGTH_FRAME)
description_line = description.ljust(LENGTH_FRAME)

print(f"""
{separator}
{title}
{separator}
{greeting_line}
{description_line}
{'-' * LENGTH_FRAME}
Краткая сводка:
- максимальный возраст человека 120 лет;
- максимальный рост человека 3 метра;
- максимальный вес человека 600 кг.
{'-' * LENGTH_FRAME}
""")

# Ввод данных

user_name = get_name()

user_age = get_age()

user_weight = get_weight()

user_height = get_height()

bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

water_ml = user_weight * ML_WATER_PER_KG
water_l = water_ml / RATIO_ML_TO_L
water_l = round(water_l, 2)

age_suffix = get_age_suffix(user_age)
bmi_category = get_bmi_category(bmi)

age_report = f'{user_age} {age_suffix}'
bmi_report = f'{bmi} - {bmi_category}'

report_title = 'ОТЧЁТ О ЗДОРОВЬЕ'.center(LENGTH_FRAME)
footer_title = 'БУДЬТЕ ЗДОРОВЫ!'.center(LENGTH_FRAME)

print(f"""
{separator}
{report_title}
{separator}

Пользователь: {user_name}
Возраст: {age_report}

Индекс массы тела: {bmi_report}

Рекомендуемая норма воды: {water_l} л. в день

{separator}
{footer_title}
{separator}
""")
