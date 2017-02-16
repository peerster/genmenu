[![Build Status](https://travis-ci.org/peerster/genmenu.svg?branch=master)](https://travis-ci.org/peerster/genmenu)
# genmenu
## INTRO
A meal menu/planner written in python.
## Why
To try to simplify and automate the process of planning what to eat.
## Install
`pip install genmenu`
## Example
```
>>> example_menu = genmenu.GenMenu()
>>> example_menu.insert_lunch_menu(['spam', 'eggs'])
>>> example_menu.insert_dinner_menu(['spam', 'eggs'])
>>> example_menu.generate_menu()
>>> example_menu.my_menu
OrderedDict([('Monday', {'dinner': 'spam', 'lunch': 'spam'}), ('Tuesday', {'dinner': 'eggs', 'lunch': 'eggs'}), ('Wednesday', {'dinner': '', 'lunch': ''}), ('Thursday', {'dinner': '', 'lunch': ''}), ('Friday', {'dinner': '', 'lunch': ''}), ('Saturday', {'dinner': '', 'lunch': ''}), ('Sunday', {'dinner': '', 'lunch': ''})])
>>>
```
## What I want to add
* A simple webpage (what web framework to use?)
* Simple DB backend (probably nosql. What DB to use?)
* Fetch recipies from external resources (what resources to use?)
* Make it multilingual (what tool and how to do that?)
* The option to specify how many days/weeks to plan for
* Add the dates to the days
