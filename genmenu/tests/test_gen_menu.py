# -*- coding: utf-8 -*-

from genmenu.genmenu import GenMenu
import pytest
import os

my_lunch_menu = ['Köttbullar', 'hamburgare']
my_dinner_menu = [
    'Pizza',
    'Pasta carbonara',
    'Burgers',
    'Hot dogs',
    'Salad',
    'Soup',
    'Phad Thai',
    'Omelette',
]


@pytest.fixture
def genmenu_instance():
    genmenu_obj = GenMenu()
    genmenu_obj.insert_lunch_menu(my_lunch_menu)
    genmenu_obj.insert_dinner_menu(my_dinner_menu)
    return genmenu_obj


def test_lunch_dict(genmenu_instance):
    assert isinstance(genmenu_instance.lunch_menu, dict)
    for day in genmenu_instance.week_days:
        assert day in genmenu_instance.lunch_menu


def test_dinner_dict(genmenu_instance):
    assert isinstance(genmenu_instance.dinner_menu, dict)
    for day in genmenu_instance.week_days:
        assert day in genmenu_instance.dinner_menu


def test_insert_lunch_menu(genmenu_instance):
    assert my_lunch_menu[0] == genmenu_instance.lunch_menu['Monday']
    assert my_lunch_menu[1] == genmenu_instance.lunch_menu['Tuesday']


def test_insert_dinner_menu(genmenu_instance):
    assert my_dinner_menu[0] == genmenu_instance.dinner_menu['Monday']
    assert my_dinner_menu[1] == genmenu_instance.dinner_menu['Tuesday']


def test_generate_menu(genmenu_instance):
    assert isinstance(genmenu_instance.my_menu, dict)
    genmenu_instance.generate_menu()
    assert my_lunch_menu[0] == genmenu_instance.my_menu['Monday']['lunch']
    assert my_dinner_menu[0] == genmenu_instance.my_menu['Monday']['dinner']


def test_insert_dinners_with_json_file():
    base_dir = os.path.dirname(__file__)
    test_file = os.path.join(base_dir, 'test_dinners.json')
    genmenu_instance = GenMenu()
    genmenu_instance.insert_dinner_menu(test_file, file_format='json')
    assert genmenu_instance.dinner_menu['Monday'] == 'Pizza'
    assert genmenu_instance.dinner_menu['Tuesday'] == 'Pasta carbonara'


def test_insert_random_dinners():
    genmenu_instance = GenMenu()
    genmenu_instance.insert_dinner_menu(my_dinner_menu, randomize=True)
    for day in genmenu_instance.week_days:
        assert genmenu_instance.dinner_menu[day] in my_dinner_menu


def test_randomize():
    genmenu_instance = GenMenu()
    test_list1 = [x for x in range(100)]
    test_list2 = list(test_list1)
    genmenu_instance._randomize(test_list1)
    assert test_list1 != test_list2


# Make sure the week days are in correct order
def test_menu_ordered_days():
    genmenu_instance = GenMenu()
    for day1, day2 in zip(genmenu_instance.week_days, genmenu_instance.my_menu.keys()):
        assert day1 == day2


def test_wrong_type():
    genmenu_instance = GenMenu()
    with pytest.raises(TypeError):
        genmenu_instance.insert_lunch_menu('string')