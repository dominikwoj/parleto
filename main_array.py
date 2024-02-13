def get_median_of_first_week_expenses(expenses):
    '''
    # for empty dict on start
    >>> get_median_of_first_week_expenses({}) is None
    True

    # typical situation: many values is list
    >>> get_median_of_first_week_expenses({ \
    "2023-01": { \
        "01": { \
            "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ], \
            "fuel": [ 210.22 ] \
        }, \
        "09": { \
            "food": [ 11.9 ], \
            "fuel": [ 190.22 ] \
        } \
    }, \
    "2023-03": { \
        "07": { \
            "food": [ 20, 11.9, 30.20, 11.9 ] \
        }, \
        "04": { \
            "food": [ 10.20, 11.50, 2.5 ], \
            "fuel": [] \
        } \
    }, \
    "2023-04": {} \
})
    11.72

    # 2 values in list
    >>> get_median_of_first_week_expenses({ \
    "2023-01": { \
        "01": { \
            "fuel": [ 210.22 ] \
        }, \
        "09": { \
            "food": [ 11.9 ], \
            "fuel": [ 190.22 ] \
        } \
    }, \
    "2023-03": { \
        "07": { \
            "food": [ 20, 11.9, 30.20, 11.9 ] \
        }, \
        "04": { \
            "food": [ 10.20 ], \
            "fuel": [] \
        } \
    }, \
    "2023-04": {} \
})
    110.21

    # for one element list
    >>> get_median_of_first_week_expenses({ \
    "2023-01": { \
        "01": { \
            "fuel": [ 210.22 ] \
        }, \
        "09": { \
            "food": [ 11.9 ], \
            "fuel": [ 190.22 ] \
        } \
    }, \
    "2023-03": { \
        "07": { \
            "food": [ 20, 11.9, 30.20, 11.9 ] \
        }, \
        "04": { \
            "food": [], \
            "fuel": [] \
        } \
    }, \
    "2023-04": {} \
})
    210.22

    # empty list
    >>> get_median_of_first_week_expenses({ \
    "2023-01": { \
        "01": { \
            "fuel": [] \
        }, \
        "09": { \
            "food": [ 11.9 ], \
            "fuel": [ 190.22 ] \
        } \
    }, \
    "2023-03": { \
        "07": { \
            "food": [ 20, 11.9, 30.20, 11.9 ] \
        }, \
        "04": { \
            "food": [], \
            "fuel": [] \
        } \
    }, \
    "2023-04": {} \
}) is None
    True

    '''
    import datetime
    import array as arr

    result = None
    median_day_name = 'Sun'
    median_days = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    # homogenic data for expense: list -> array
    expenses_list = arr.array('f') #<- array, but is problem

    for year_month_key in expenses.keys():
        year, month = year_month_key.split('-')
        # date.weekday(): Mon = 0, ... , Sun = 6
        median_day_value = median_days[median_day_name] - datetime.date(int(year), int(month), 1).weekday() + 1
        for day_key, expense_day in expenses[year_month_key].items():
            if int(day_key) <= median_day_value:
                # 1.
                # for expense_kind in expense_day.values():
                #    expenses_list += expense_kind

                # 2.
                # [expenses_list.extend(expense_kind) for expense_kind in expense_day.values()]

                # 3.
                gen = (expense_kind for expense_kind in expense_day.values())
                expenses_list.extend(gen)

    expenses_list = [item for sub_list in expenses_list for item in sub_list]

    def midian(values: list) -> float:
        values.sort()
        # print(values)
        middle = len(values) // 2
        return (values[middle] + values[~middle]) / 2

    return None if len(expenses_list) == 0 else midian(expenses_list)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# get_median_of_first_week_expenses(expenses)
