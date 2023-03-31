#Cullen Wise
#Linear_Network_Game_Predictor.py
#using a linear nueral network to try and predict ncaab games final scores
#Created 2/7/23 Last Modified 2/12/23
#hours sunk [11]

import torch
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from torch import nn
from torch import optim
import matplotlib.pyplot as plt
import numpy as np
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")
#first section of this is data management
#bringing data in concatnated csv

stats_df = pd.read_csv('compiled_stats\\cbbdata.csv')
df = stats_df.drop(['Date'], axis=1)
df = df.drop(['Team_1'], axis=1)
df = df.drop(['Team_2'], axis=1)
dataset = torch.tensor(df.values, dtype=torch.float32)
print(dataset)
#variables in cbbdata.csv

#Date,Team_1,Team_2,T1AEM,T1AOE,T1ADE,T1AT,T1Luck,T1SOSR,T1AAOEOO,T1AADEOO,T1NCSOSR,
#T2AEM,T2AOE,T2ADE,T2AT,T2Luck,T2SOSR,T2AAOEOO,T2AADEOO,T2NCSOSR,Team_1_Score,Team_2_Score

#variable shorthand 'WL' 'AEM' 'AOE' 'ADE' 'AT' 'Luck' 'SOSR' 'AAOEOO' 'AADEOO' 'NCSOSR'


class StatsData(Dataset):
    def __init__(self, data_file):
        self.data = torch.load(data_file)  # assuming the data is saved as a PyTorch tensor

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        inputs = self.data[index, 3:21]  # first 18 columns of data are input features
        outputs = self.data[index, 21:]  # last 2 columns of data are output labels
        return inputs, outputs



#determining nodes in input hidden and output layers
input_dim = 18 #statistical fields
hidden_dim_1 = 100
hidden_dim_2 = 100
output_dim = 2 #scores

class LinearNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim_1, hidden_dim_2, output_dim):
        super(LinearNetwork, self).__init__()#properties from super class
        self.layer_1 = nn.Linear(input_dim, hidden_dim_1)
        nn.init.kaiming_uniform_(self.layer_1.weight, nonlinearity= "relu")
        self.layer_2 = nn.Linear(hidden_dim_1, hidden_dim_2)
        nn.init.kaiming_uniform_(self.layer_2.weight, nonlinearity= "relu")
        self.layer_3 = nn.Linear(hidden_dim_2, output_dim)
    
    def forward(self, x):#forward propagating
        x = torch.nn.functional.relu(self.layer_1(x))
        x = torch.nn.functional.relu(self.layer_2(x))
        x = torch.nn.functional.relu(self.layer_3(x))
        #trying the linear activation (relu) to "get this off the ground" may change later
        return x
    
model = LinearNetwork(input_dim, hidden_dim_1, hidden_dim_2, output_dim)#making the model    
#print(model)
loss_fn = nn.MSELoss()
#loss fn is chosen as mean squared here since our results should be closer to an n layred regression
optimizer = torch.optim.Adam(model.parameters(), lr=.01, weight_decay=.0001)
#training here

#testing here

