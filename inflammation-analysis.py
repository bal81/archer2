#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""
# small change to file
import argparse
from inflammation import models, views, compute_data
import os
import sys
sys.path.append("C:\\Users\\3048844\\OneDrive - Queen's University Belfast\\Documents\\cursos\\archer4\\archer2\\")


def main(args_var):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    data_dir=r"C:\\Users\\3048844\\OneDrive - Queen's University Belfast\\Documents\\cursos\\archer4\\archer2\\data\\"
    infiles=data_dir+"inflammation-01.csv"
    #if args_var.full_data_analysis:
    _, extension = os.path.splitext(infiles)
    if extension == '.json':

        data_source = compute_data.JSONDataSource(os.path.dirname(infiles))
    elif extension == '.csv':
        data_source = compute_data.CSVDataSource(os.path.dirname(infiles))
    else:
        raise ValueError(f'Unsupported file format: {extension}')
    data_result = compute_data.analyse_data(data_source)
    graph_data = {
            'standard deviation by day': data_result,
        }
    views.visualize(graph_data)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    args = parser.parse_args()

    main(args)
