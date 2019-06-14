'''
1. создаем словарь fert_dic_1960 и fert_dic_2018
2. открыть archives/fertility.csv
3. выбираем из archives/fertility.csv в выбранный год (1960 и 2018) -
    страну[0] и процент[4] и [62].
        Проверяем на ошибки. Если Value Error то берем [62 - i] где i += 1
    Страну вначале прогоняем через get_code
        чтобы получить ее код.
4. Записываем в fert_dic код: процент
5. Заносим данные в pygal
'''

import pygal
import csv
from get_code import get_code
from pygal.style import RotateStyle as RS

fert_1_1960 = {}
fert_2_1960 = {}
fert_3_1960 = {}
fert_1_2018 = {}
fert_2_2018 = {}
fert_3_2018 = {}

with open('archives/fertility.csv') as f:
    fert_data = csv.reader(f)
    for i in fert_data:
        country = i[0]
        code = get_code(country)
        if code:
            if i[4]:
                f_60 = float(i[4])
                if f_60 < 3:
                    fert_1_1960[code] = f_60
                elif f_60 < 6:
                    fert_2_1960[code] = f_60
                else:
                    fert_3_1960[code] = f_60
            if i[61]:
                f_18 = float(i[61])
                if f_18 < 2:
                    fert_1_2018[code] = f_18
                elif f_18 < 3:
                    fert_2_2018[code] = f_18
                else:
                    fert_3_2018[code] = f_18

# print(len(fert_dic_1960))
# print(len(fert_dic_2018))
# print(fert_dic_2018)

wm_style = RS('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Fertility womans in the world 1960'
wm.add('< 3 children', fert_1_1960)
wm.add('3 - 6 children', fert_2_1960)
wm.add('> 6 children', fert_3_1960)
wm.render_to_file('fertility.svg')


wm_style = RS('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Fertility womans in the world 2017'
wm.add('< 2 children', fert_1_2018)
wm.add('2 - 3 children', fert_2_2018)
wm.add('> 3 children', fert_3_2018)
wm.render_to_file('fertility2018.svg')











