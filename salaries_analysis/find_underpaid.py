"""
This program generates a text file which lists all the
workers who worked at the company more the one year and whose salary is less than average
"""

from statistics import mean
from datetime import datetime
import analysis_tools as at


def seniority_calc(date_str):
    """
    Calculating how many years a worker has worked in the company
    :param date_str: date of the worker's first day in the company
    :type date_str: str
    :return: how many years the worker has worked in the company
    :rtype: int
    """
    date_to_check = datetime.strptime(date_str, "%Y-%m-%d")
    today = datetime.now()
    seniority = today.year - date_to_check.year
    seniority -= ((today.month, today.day) < (date_to_check.month, date_to_check.day))
    return seniority


def main():
    workers = at.extract_api()
    average_salary = mean(
        [worker['salary'] for worker in workers]
    )
    with open('results/underpaid.txt', 'w') as result_file:
        result_file.write('Average salary: %.2f\n' % average_salary)
        result_file.write('Workers with more than one year of seniority and salary below average:\n\n')
        for worker in workers:
            if worker['salary'] < average_salary and seniority_calc(worker['hire_date']) >= 1:
                result_file.write(at.worker_str(worker))


if __name__ == "__main__":
    main()
