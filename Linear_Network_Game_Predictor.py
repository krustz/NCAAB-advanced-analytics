#Cullen Wise
#Linear_Network_Game_Predictor.py
#using a linear nueral network to try and predict ncaab games final scores
#Created 2/7/23 Last Modified 2/8/23
#hours sunk [3]

import torch
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from torch import nn
from torch import optim
import numpy as np

#first section of this is data management
#bringing data in from csv's two classes most likely, games and stats

stats_df = pd.read_csv('stats\\stats1-31-23.csv')

#variables in stats_df

#'Rank', 'Team', 'Confrence', 'Win_Loss', 'Adjusted_Efficiency_Margin', 'Adjusted_Offensive_Efficency'
#,'Adjusted_Defensive_Efficency', 'Adjusted_tempo', 'Luck', 'Strength_of_Schedule_Rating'
#,'Adverage_Adjusted_Offensive_Efficency_of_Opponents','Adverage_Adjusted_Defensive_Efficency_of_Opponents',
#'Non_Confrence_Strength_of_Schedule_Rating'

#variable shorthand 'WL' 'AEM' 'AOE' 'ADE' 'AT' 'Luck' 'SOSR' 'AAOEOO' 'AADEOO' 'NCSOSR'

games_df = pd.read_csv('games\\scores1-31-23.csv')

#variables in stats_df

#'Team_1', 'Team_2', 'Team_1_Score', 'Team_2_Score'

#variable shorthand 'T1' 'T2' 'T1S' 'T2S'

#ALL dataframe variables are brought in as strings
indexTest = stats_df[stats_df['Team']=='Alabama'].index.values
print(indexTest)
print(stats_df.loc[indexTest])
print(stats_df['Team'])

class StatsData(Dataset):
    def __init__(self, WL, AEM, AOE, ADE, AT, Luck, SOSR, AAOEOO, AADEOO, NCSOSR):
        self.WL = torch.from_numpy(WL.astype(np.float32))
        self.AEM = torch.from_numpy(AEM.astype(np.float32))
        self.AOE = torch.from_numpy(AOE.astype(np.float32))
        self.ADE = torch.from_numpy(ADE.astype(np.float32))
        self.AT = torch.from_numpy(AT.astype(np.float32))
        self.Luck = torch.from_numpy(Luck.astype(np.float32))
        self.SOSR = torch.from_numpy(SOSR.astype(np.float32))
        self.AAOEOO = torch.from_numpy(AAOEOO.astype(np.float32))
        self.AADEOO = torch.from_numpy(AADEOO.astype(np.float32))
        self.NCSOSR = torch.from_numpy(NCSOSR.astype(np.float32))
    def __getitem(self, index):
        return self.WL[index], self.AEM[index], self.AOE[index], self.ADE[index], self.AT[index], self.Luck[index], self.SOSR[index], self.AAOEOO[index], self.AADEOO[index], self.NCSOSR[index]
    #length is constant at 363 so no need for method        



#determining nodes in input hidden and output layers
input_dim = 20
hidden_dim_1 = 100
hidden_dim_2 = 100
output_dim = 2

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
