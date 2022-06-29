"""
This program generates a text file which lists all
workers whose salary is more than twice of the average salary,
while using numpy arrays
"""

import analysis_tools as at
import numpy as np


def main():
    workers = at.extract_api()
    salaries = np.array(
        [worker['salary'] for worker in workers]
    )
    average_salary = np.average(salaries)
    is_overpaid = salaries > (average_salary * 2)
    with open('results/overpaid.txt', 'w') as result_file:
        result_file.write('Average salary: %.2f\n' % average_salary)
        result_file.write('Workers whose salary is twice or more than average :\n\n')
        for index in range(len(workers)):
            if is_overpaid[index]:
                result_file.write(at.worker_str(workers[index]))


if __name__ == '__main__':
    main()
