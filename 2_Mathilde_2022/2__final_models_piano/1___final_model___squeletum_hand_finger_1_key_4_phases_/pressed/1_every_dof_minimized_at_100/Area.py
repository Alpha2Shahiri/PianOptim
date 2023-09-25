
import numpy as np
import matplotlib.pyplot as plt
import pickle
from scipy.signal import find_peaks
from scipy.spatial.distance import cdist

#data_1:strucked  _s
def degrees(radians):
    return np.degrees(radians)

with open('/home/alpha/Desktop/July/Sept./2ndmeeting/Freezing/Freezing/B3-Shoulder-Acceptable/B3.pckl', 'rb') as file:
    data_1 = pickle.load(file)

specific_points_s = [data_1['phase_time'][0], data_1['phase_time'][0] + data_1['phase_time'][1], data_1['phase_time'][0] + data_1['phase_time'][1] + data_1['phase_time'][2], data_1['phase_time'][0] + data_1['phase_time'][1] + data_1['phase_time'][2] + data_1['phase_time'][3],data_1['phase_time'][0] + data_1['phase_time'][1] + data_1['phase_time'][2] + data_1['phase_time'][3]+ data_1['phase_time'][4]]
#####################

array_0_q_s = data_1["states_no_intermediate"][0]['q']  # First array
array_1_q_s = data_1["states_no_intermediate"][1]['q']  # Second array
array_2_q_s = data_1["states_no_intermediate"][2]['q']  # Third array
array_3_q_s = data_1["states_no_intermediate"][3]['q']  # Fourth array

x1_s,y1_s=(array_0_q_s.shape)
x2_s,y2_s=(array_1_q_s .shape)
x3_s,y3_s=(array_2_q_s.shape)
x4_s,y4_s=(array_3_q_s.shape)

y_q_s=y1_s+y2_s+y3_s+y4_s
print(y_q_s)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_s=degrees(np.concatenate((array_0_q_s, array_1_q_s, array_2_q_s, array_3_q_s), axis=1))  #All Phases

#####################

array_0_qdot_s = data_1["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_s = data_1["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_s = data_1["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_s = data_1["states_no_intermediate"][3]['qdot']  # Fourth array

x1_s,y1_s=(array_0_qdot_s.shape)
x2_s,y2_s=(array_1_qdot_s .shape)
x3_s,y3_s=(array_2_qdot_s.shape)
x4_s,y4_s=(array_3_qdot_s.shape)

y_qdot_s=y1_s+y2_s+y3_s+y4_s
print(y_qdot_s)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_s=degrees(np.concatenate((array_0_qdot_s, array_1_qdot_s, array_2_qdot_s, array_3_qdot_s), axis=1))  #All Phases

#####################

array_0_tau_s = data_1['controls'][0]['tau']  # First array

array_1_tau_s= data_1['controls'][1]['tau']  # Second array
first_column = array_1_tau_s[:, 0]
array_0_tau_s[:,-1]=first_column

array_2_tau_s= data_1['controls'][2]['tau']  # Third array
first_column = array_2_tau_s[:, 0]
array_1_tau_s[:,-1]=first_column

array_3_tau_s= data_1['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_s[:, 0]
array_2_tau_s[:,-1]=first_column

array_3_tau_s = np.delete(array_3_tau_s, -1, axis=1)
last_column = array_3_tau_s[:, -1]
array_3_tau_s = np.hstack((array_3_tau_s, last_column.reshape(-1, 1)))


x1_s,y1_s=(array_0_tau_s.shape)
x2_s,y2_s=(array_1_tau_s.shape)
x3_s,y3_s=(array_2_tau_s.shape)
x4_s,y4_s=(array_3_tau_s.shape)

concatenated_array_tau_s= np.concatenate((array_0_tau_s, array_1_tau_s, array_2_tau_s, array_3_tau_s), axis=1)

#####################
array_0_time_s = specific_points_s[0]  # zero array
array_1_time_s = specific_points_s[1] # first array
array_2_time_s = specific_points_s[2] # second array
array_3_time_s = specific_points_s[3] # Third array
array_4_time_s = specific_points_s[4] # Fourth array


t_1=np.linspace(array_0_time_s,array_1_time_s,len(data_1['states_no_intermediate'][0]['q'][0]))
t_2=np.linspace(array_1_time_s,array_2_time_s,(len(data_1['states_no_intermediate'][1]['q'][0])))
t_3=np.linspace(array_2_time_s,array_3_time_s,(len(data_1['states_no_intermediate'][2]['q'][0])))
t_4=np.linspace(array_3_time_s,array_4_time_s,(len(data_1['states_no_intermediate'][3]['q'][0])))

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_time_s= np.concatenate((t_1,t_2,t_3,t_4), axis=0)  #All Phases


def trapezoidal_rule(x, y):
    """Calculate area under the curve using trapezoidal rule."""
    n = len(x)
    area = 0
    for i in range(n - 1):
        area += 0.5 * (x[i + 1] - x[i]) * (y[i + 1] + y[i])
    return area

def calculate_centroid(x, y, area):
    """Calculate the centroid of the curve using trapezoidal rule."""
    n = len(x)
    x_centroid_integral = 0
    y_centroid_integral = 0
    for i in range(n - 1):
        dx = x[i + 1] - x[i]
        x_centroid_integral += dx * (x[i] * y[i] + x[i + 1] * y[i + 1]) / 2
        y_centroid_integral += dx * (y[i]**2 / 2 + y[i + 1]**2 / 2) / 2
    x_centroid = x_centroid_integral / area
    y_centroid = y_centroid_integral / area
    return x_centroid, y_centroid

def plot_area_under_curve(x, y, color, alpha=0.2):
    plt.fill_between(x, y, color=color, alpha=alpha)

# Generate example data
time1=concatenated_array_time_s
tau1=concatenated_array_tau_s[5,:]
tau2=concatenated_array_tau_s[6,:]

# Calculate area and centroid for Graph 1
area1 = trapezoidal_rule(time1, tau1)
centroid1 = calculate_centroid(time1, tau1, area1)

# Calculate area and centroid for Graph 2
area2 = trapezoidal_rule(time1, tau2)
centroid2 = calculate_centroid(time1, tau2, area2)

# Plotting
plt.figure(figsize=(12, 6))

# Plot and fill area for Graph 1
plt.scatter(time1, tau1, label=f'Wrist (Area: {area1:.2f}, Centroid: {centroid1})', c='b')
plot_area_under_curve(time1, tau1, 'b')

# Plot and fill area for Graph 2
plt.scatter(time1, tau2, label=f'Finger (Area: {area2:.2f}, Centroid: {centroid2})', c='r')
plot_area_under_curve(time1, tau2, 'r')

# Plot centroids
plt.scatter(*centroid1, c='b', marker='x', s=100)
plt.scatter(*centroid2, c='r', marker='x', s=100)

plt.xlabel('Time')
plt.ylabel('Tau')
plt.legend()
plt.title('B (Tau-Time)')
plt.grid(True)
plt.show()

