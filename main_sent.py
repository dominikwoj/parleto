import datetime


def get_median_of_first_week_expenses(expenses):
    result = None
    median_day_name = 'Sun'
    median_days = {'Mon': 0, 'Thu': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    expenses_list = []

    for year_month_key in expenses.keys():
        year, month = year_month_key.split('-')
        # date.weekday(): Mon = 0, ... , Sun = 6
        median_day_value = median_days[median_day_name] - datetime.date(int(year), int(month), 1).weekday() + 1
        for day_key, expense_day in expenses[year_month_key].items():
            if int(day_key) <= median_day_value:
                gen = (expense_kind for expense_kind in expense_day.values())
                expenses_list.extend(gen)

    expenses_list = [item for sub_list in expenses_list for item in sub_list]

    def midian(values: list) -> float:
        values.sort()
        middle = len(values) // 2
        return (values[middle] + values[~middle]) / 2

    result = None if len(expenses_list) == 0 else midian(expenses_list)
    return result
    # return result None if len(expenses_list) == 0 else midian(expenses_list)


get_median_of_first_week_expenses(expenses)
