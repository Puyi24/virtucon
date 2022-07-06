"""
This program generates two text files in the subdirectory 'result'.

first one lists the workers who have worked at the company more the one year
and whose salary is less than average

The second one lists the workers whose salary is more than twice of the average salary,
while using numpy arrays as much as possible

The two processes will be executed simultaneously via the multiprocessing module.
"""

import numpy as np
import multiprocessing as mp
import analysis_tools as at


def find_underpaid(workers):
    """
    Generating the text file listing the workers who have worked at the company more than one year
    and whose salary is less than average
    :param workers: list of dictionaries containing each worker's details
    :type workers: list
    :return: none
    """
    average_salary = at.get_average(workers)
    with open('results/underpaid.txt', 'w') as result_file:
        result_file.writelines(['Average salary: %.2f\n' % average_salary,
                                'Workers with more than one year of seniority and salary below average:\n\n'])
        for worker in workers:
            if worker['salary'] < average_salary and at.seniority_calc(worker['hire_date']) >= 1:
                result_file.writelines([at.worker_str(worker),
                                        '\n******************\n\n'])


def find_overpaid(workers):
    """
    Generating the text file listing the workers whose salary is more than twice of the average salary,
    while using numpy arrays as much as possible
    :param workers: list of dictionaries containing each worker's details
    :type workers: list
    :return: none
    """
    # A list of the salaries is needed for further use later in this function. Therefore, in order to prevent
    # code repetition the get_average() function of the analysis_tools module won't be called in this function
    salaries = np.array(
        [worker['salary'] for worker in workers]
    )
    average_salary = np.average(salaries)
    is_overpaid = salaries >= (average_salary * 2)
    with open('results/overpaid.txt', 'w') as result_file:
        result_file.writelines(['Average salary: %.2f\n' % average_salary,
                                'Workers whose salary is twice or more than average:\n\n'])
        for index in range(len(workers)):
            if is_overpaid[index]:
                result_file.writelines([at.worker_str(workers[index]),
                                        '\n******************\n\n'])


def main():
    workers = at.extract_api()
    overpaid = mp.Process(target=find_overpaid, args=[workers])
    underpaid = mp.Process(target=find_underpaid, args=[workers])
    overpaid.start()
    underpaid.start()
    overpaid.join()
    underpaid.join()


if __name__ == "__main__":
    main()
