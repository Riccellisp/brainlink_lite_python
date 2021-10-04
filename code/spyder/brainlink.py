import numpy as np
import pandas as pd
import json
import time
from telnetlib import Telnet
import matplotlib.pyplot as plt
# Performing telnet connection
tn=Telnet('localhost',13854);

# Initializing time counter
start=time.time();

# Capture time in seconds
# capture_time = 10

# Declaring variables for data acquisition
attention_values = np.array([])
meditation_values = np.array([])
delta_values = np.array([])
theta_values = np.array([])
lowAlpha_values = np.array([])
highAlpha_values = np.array([])
lowBeta_values = np.array([])
highBeta_values = np.array([])
lowGamma_values = np.array([])
highGamma_values = np.array([])
blinkStrength_values = np.array([])
records = []
rawEegs = []
dataset = []
tn.write(b'{"enableRawOutput": true, "format": "Json"}');

# Reading data from brainlink for a chosen time
while True:
    try:
        # Read data until enter character
        line=tn.read_until(b'\r');
        
        # Convert json to string
        str_line=json.loads(line);
        
        # Saving records
        records.append(str_line)
        
        # Separing each record from brainlink and storing
        if "rawEeg" in str_line:
            rawEeg = str_line['rawEeg']
            rawEegs.append(rawEeg)
        if "poorSignalLevel" in str_line:
            signalLevel=str_line['poorSignalLevel'];
        if "blinkStrength" in str_line:
            blinkStrength=str_line['blinkStrength'];
        if "eegPower" in str_line:            
            waveDict=str_line['eegPower'];
            eSenseDict=str_line['eSense'];
            
            # Storing values from eegPower and eSense
            lowGamma_values = np.append(lowGamma_values, [waveDict['lowGamma']]);
            highGamma_values = np.append(highGamma_values, [waveDict['highGamma']]);
            highAlpha_values = np.append(highAlpha_values, [waveDict['highAlpha']]);
            delta_values = np.append(delta_values, [waveDict['delta']]);
            lowBeta_values = np.append(lowBeta_values, [waveDict['lowBeta']]);
            highBeta_values = np.append(highBeta_values, [waveDict['highBeta']]);
            theta_values = np.append(theta_values, [waveDict['theta']]);
            lowAlpha_values = np.append(lowAlpha_values, [waveDict['lowAlpha']]);
            attention_values = np.append(attention_values, [eSenseDict['attention']]);
            meditation_values = np.append(meditation_values, [eSenseDict['meditation']]);
        time_elapsed = time.time() - start 
    except KeyboardInterrupt:
        break
capture_time = time.time() - start
# Joining all eegPower records into a matrix        
eegPower_records = np.vstack([lowGamma_values,highGamma_values,highAlpha_values,delta_values,
                      lowBeta_values,highBeta_values,theta_values,lowAlpha_values,
                      attention_values,meditation_values])

# transpose matrix - num of records x num of signals
eegPower_records = np.transpose(eegPower_records)

# Declaring columns to Dataframe
columns = ['lowAlpha_values','highAlpha_values', 'lowBeta_values', 'highBeta_values',
           'lowGamma_values','highGamma_values','delta_values','theta_values',
           'attention_values','meditation_values']

# Making dataset 
dataset = pd.DataFrame(eegPower_records,columns=columns)

#storing dataset
dataset.to_csv(f'brainlink_lite {capture_time} seconds.csv',index=False)