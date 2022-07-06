""""
This program first converts the api data of the workers to an excel file in the subdirectory 'result',
then displays a graph of every department's average salary
"""

import pandas as pd
import matplotlib.pyplot as plt
import analysis_tools as at

EXCEL_PATH = 'results/workers.xlsx'

def generate_excel():
    """
    Converting the api data of the workers to an excel file,
    replacing the links to the departments api with the departments' actual name in the process
    :return: none
    """
    workers_data = at.extract_api()
    df = pd.DataFrame(workers_data)
    df['department'].replace(at.deps_translate(), inplace=True)
    df.to_excel(EXCEL_PATH)


def main():
    generate_excel()
    workers_df = pd.read_excel(EXCEL_PATH)
    departments_df = workers_df.groupby(['department'])
    departments_df['salary'].mean().plot.bar()
    plt.show()


if __name__ == "__main__":
    main()
