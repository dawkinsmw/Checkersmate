import numpy as np

import torch
from torch.utils.data import Dataset


class CheckersDataset(Dataset):

    def __init__(self,data_dir,first_file=0,last_file=1,records_per_file=60000):
        self.data_dir = data_dir
        self.first_file = first_file
        self.last_file = last_file
        self.current_file = first_file
        self.records_per_file = records_per_file
        
        data = np.loadtxt(f"{self.data_dir}{self.current_file}.csv",delimiter = ",",dtype=np.float32)
        self.x = torch.from_numpy(data[0:self.records_per_file,0:32])
        self.y = torch.from_numpy(data[0:self.records_per_file,[32]])

    def __getitem__(self, index):
        index = index + self.first_file * self.records_per_file
        ## Index out of range
        if( (index < self.first_file * self.records_per_file) | (index >= self.last_file * self.records_per_file)  ):
            raise IndexError(f"index out of range")
        ## Index in current file
        if( (index >= self.current_file*self.records_per_file) & (index<(self.current_file+1)*self.records_per_file)):
            adj_index = index - self.current_file*self.records_per_file
            return self.x[adj_index], self.y[adj_index]
        ## Index in unloaded file 
        else:
            # load new file
            self.current_file = index//self.records_per_file
            data = np.loadtxt(f"{self.data_dir}{self.current_file}.csv",delimiter = ",",dtype=np.float32)
            self.x = torch.from_numpy(data[0:self.records_per_file,0:32])
            self.y = torch.from_numpy(data[0:self.records_per_file,[32]])
            # return data
            adj_index = index - self.current_file*self.records_per_file
            return self.x[adj_index], self.y[adj_index]

    def __len__(self):
        return (self.last_file - self.first_file) * self.records_per_file