print(f"""
{'=' * 10} FITLIFE {'=' * 10}
Здравствуйте! Вас приветсвует автономный фитнес трекер.
Мне нужно собрать базовую информацию о Вас.
{'-' * 30}
""")

ML_WATER_PER_KG = 30
RATIO_ML_TO_L = 1000

user_name = input('Введите Ваше имя: ')

user_age = input('Введите Ваш возраст: ')
user_age = int(user_age)

user_weight = input('Введите ваш вес (в кг - 65.5): ')
# Замена запятой на точку дабы избежать ошибки при переопределении типа
user_weight = user_weight.replace(',', '.')
user_weight = float(user_weight)

user_height = input('Введите ваш рост (в метрах - 1.72): ')
user_height = user_height.replace(',', '.')
user_height = float(user_height)

bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

water_ml = user_weight * ML_WATER_PER_KG
water_l = water_ml / RATIO_ML_TO_L
water_l = round(water_l, 2)

print(f"""
{'=' * 30}
        ОТЧЁТ О ЗДОРОВЬЕ
{'=' * 30}

Пользователь: {user_name}
Возраст: {user_age} лет

Индекс массы тела: {bmi}

Рекомендуемая норма воды: {water_l} л. в день

{'=' * 30}
        БУДЬТЕ ЗДОРОВЫ!
{'=' * 30}
""")
