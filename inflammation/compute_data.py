"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np
import sys
sys.path.append("C:\\Users\\3048844\\OneDrive - Queen's University Belfast\\Documents\\cursos\\archer4\\archer2\\")

from inflammation import models, views

class CSVDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir
    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        data = map(models.load_csv, data_file_paths)
        return data

class JSONDataSource:
  """
  Loads patient data with inflammation values from JSON files within a specified folder.
  """
  def __init__(self, dir_path):
    self.dir_path = dir_path

  def load_inflammation_data(self):
    data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json'))
    if len(data_file_paths) == 0:
      raise ValueError(f"No inflammation JSON files found in path {self.dir_path}")
    data = map(models.load_json, data_file_paths)
    return list(data)
  

def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    data= data_source.load_inflammation_data()
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation

if __name__ == '__main__':
    data_dir=r"C:\\Users\\3048844\\OneDrive - Queen's University Belfast\\Documents\\cursos\\archer4\\archer2\\data\\"
    infiles=data_dir+"inflammation-01.csv"
    _, extension = os.path.splitext(infiles)
    print('=======================')
    print('reading files with extension= ', extension)
    print('data_dir= ', data_dir)
    print('=======================')
    if extension == '.json':
        data_source = JSONDataSource(os.path.dirname(infiles))
    elif extension == '.csv':
        data_source = CSVDataSource(os.path.dirname(infiles))
    else:
        raise ValueError(f'Unsupported data file format: {extension}')
    analyse_data(data_source)
    #data_source=CSVDataSource(data_dir) 
    #analyse_data(data_source)