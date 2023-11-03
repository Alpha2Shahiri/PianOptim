import pickle
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator


# data_1:strucked  _s    data_2:pressed   _p
def degrees(radians):
    return np.degrees(radians)


with open("/home/alpha/Desktop/NEW oCT. 16/Felipe and Optimal Control Group - Pressed Touch 23 October./Results For Struck Touch_20/V1_All_Strcuck30_20.pckl", 'rb') as file:
    data_1 = pickle.load(file)

specific_points_s = [data_1['phase_time'][0], data_1['phase_time'][0] + data_1['phase_time'][1],
                     data_1['phase_time'][0] + data_1['phase_time'][1] + data_1['phase_time'][2],
                     data_1['phase_time'][0] + data_1['phase_time'][1] + data_1['phase_time'][2] + data_1['phase_time'][3],
                     data_1['phase_time'][0] + data_1['phase_time'][1] + data_1['phase_time'][2] + data_1['phase_time'][3] + data_1['phase_time'][4]]

#####################

with open("/home/alpha/Desktop/NEW oCT. 16/Felipe and Optimal Control Group - Pressed Touch 23 October./Results For Struck Touch_20/V1_All_Strcuck23_20.pckl", 'rb') as file:
    data_2 = pickle.load(file)

specific_points_p = [data_2['phase_time'][0], data_2['phase_time'][0] + data_2['phase_time'][1],
                     data_2['phase_time'][0] + data_2['phase_time'][1] + data_2['phase_time'][2],
                     data_2['phase_time'][0] + data_2['phase_time'][1] + data_2['phase_time'][2] + data_2['phase_time'][3],
                     data_2['phase_time'][0] + data_2['phase_time'][1] + data_2['phase_time'][2] + data_2['phase_time'][3] + data_2['phase_time'][4]]
#####################
#
with open('/home/alpha/Desktop/NEW oCT. 16/V1_ELBOW_2_NEW_FP.pckl', 'rb') as file:
    data_3 = pickle.load(file)

specific_points_t = [data_3['phase_time'][0], data_3['phase_time'][0] + data_3['phase_time'][1],
                     data_3['phase_time'][0] + data_3['phase_time'][1] + data_3['phase_time'][2],
                     data_3['phase_time'][0] + data_3['phase_time'][1] + data_3['phase_time'][2] + data_3['phase_time'][3],
                     data_3['phase_time'][0] + data_3['phase_time'][1] + data_3['phase_time'][2] + data_3['phase_time'][3] + data_3['phase_time'][4]]

#####################
#
with open("/home/alpha/Desktop/NEW oCT. 16/V1_Elbow_NEW23_25.pckl", 'rb') as file:
    data_4 = pickle.load(file)

specific_points_d = [data_4['phase_time'][0], data_4['phase_time'][0] + data_4['phase_time'][1],
                     data_4['phase_time'][0] + data_4['phase_time'][1] + data_4['phase_time'][2],
                     data_4['phase_time'][0] + data_4['phase_time'][1] + data_4['phase_time'][2] + data_4['phase_time'][3],
                     data_4['phase_time'][0] + data_4['phase_time'][1] + data_4['phase_time'][2] + data_4['phase_time'][3] + data_4['phase_time'][4]]
#####################

with open("/home/alpha/Desktop/July/Sept./2ndmeeting/0.5.pckl", 'rb') as file:
    data_5 = pickle.load(file)

specific_points_e = [data_5['phase_time'][0], data_5['phase_time'][0] + data_5['phase_time'][1],
                     data_5['phase_time'][0] + data_5['phase_time'][1] + data_5['phase_time'][2],
                     data_5['phase_time'][0] + data_5['phase_time'][1] + data_5['phase_time'][2] + data_5['phase_time'][3],
                     data_5['phase_time'][0] + data_5['phase_time'][1] + data_5['phase_time'][2] + data_5['phase_time'][3] + data_5['phase_time'][4]]

#####################

with open('/home/alpha/Desktop/July/Sept./2ndmeeting/0.4.pckl', 'rb') as file:
    data_6 = pickle.load(file)

specific_points_f = [data_6['phase_time'][0], data_6['phase_time'][0] + data_6['phase_time'][1],
                     data_6['phase_time'][0] + data_6['phase_time'][1] + data_6['phase_time'][2],
                     data_6['phase_time'][0] + data_6['phase_time'][1] + data_6['phase_time'][2] + data_6['phase_time'][3],
                     data_6['phase_time'][0] + data_6['phase_time'][1] + data_6['phase_time'][2] + data_6['phase_time'][3] + data_6['phase_time'][4]]
#####################
#
with open('/home/alpha/Desktop/July/Sept./2ndmeeting/0.3.pckl', 'rb') as file:
    data_7 = pickle.load(file)

specific_points_g = [data_7['phase_time'][0], data_7['phase_time'][0] + data_7['phase_time'][1],
                     data_7['phase_time'][0] + data_7['phase_time'][1] + data_7['phase_time'][2],
                     data_7['phase_time'][0] + data_7['phase_time'][1] + data_7['phase_time'][2] + data_7['phase_time'][3],
                     data_7['phase_time'][0] + data_7['phase_time'][1] + data_7['phase_time'][2] + data_7['phase_time'][3] + data_7['phase_time'][4]]

#####################
#
with open('/home/alpha/Desktop/July/Sept./2ndmeeting/0.2.pckl', 'rb') as file:
    data_8 = pickle.load(file)

specific_points_h = [data_8['phase_time'][0], data_8['phase_time'][0] + data_8['phase_time'][1],
                     data_8['phase_time'][0] + data_8['phase_time'][1] + data_8['phase_time'][2],
                     data_8['phase_time'][0] + data_8['phase_time'][1] + data_8['phase_time'][2] + data_8['phase_time'][3],
                     data_8['phase_time'][0] + data_8['phase_time'][1] + data_8['phase_time'][2] + data_8['phase_time'][3] + data_8['phase_time'][4]]
#####################

with open("/home/alpha/Desktop/July/Sept./2ndmeeting/0.1.pckl", 'rb') as file:
    data_9 = pickle.load(file)

specific_points_i = [data_9['phase_time'][0], data_9['phase_time'][0] + data_9['phase_time'][1],
                     data_9['phase_time'][0] + data_9['phase_time'][1] + data_9['phase_time'][2],
                     data_9['phase_time'][0] + data_9['phase_time'][1] + data_9['phase_time'][2] + data_9['phase_time'][3],
                     data_9['phase_time'][0] + data_9['phase_time'][1] + data_9['phase_time'][2] + data_9['phase_time'][3] + data_9['phase_time'][4]]

#####################

with open('/home/alpha/Desktop/July/Sept./1st Meeting with Begon/V3.pckl', 'rb') as file:
    data_10 = pickle.load(file)

specific_points_j = [data_10['phase_time'][0], data_10['phase_time'][0] + data_10['phase_time'][1],
                     data_10['phase_time'][0] + data_10['phase_time'][1] + data_10['phase_time'][2],
                     data_10['phase_time'][0] + data_10['phase_time'][1] + data_10['phase_time'][2] +
                     data_10['phase_time'][3],
                     data_10['phase_time'][0] + data_10['phase_time'][1] + data_10['phase_time'][2] +
                     data_10['phase_time'][3] + data_10['phase_time'][4]]
#####################


label_1 = input("Please enter the label data_1: ")
label_2 = input("Please enter the label data_2: ")
label_3 = input("Please enter the label data_3: ")
label_4 = input("Please enter the label data_4: ")
label_5 = input("Please enter the label data_5: ")
label_6 = input("Please enter the label data_6: ")
label_7 = input("Please enter the label data_7: ")
label_8 = input("Please enter the label data_8: ")
label_9 = input("Please enter the label data_9: ")
label_10 = input("Please enter the label data_10: ")

#####################

array_0_q_s = data_1["states_no_intermediate"][0]['q']  # First array
array_1_q_s = data_1["states_no_intermediate"][1]['q']  # Second array
array_2_q_s = data_1["states_no_intermediate"][2]['q']  # Third array
array_3_q_s = data_1["states_no_intermediate"][3]['q']  # Fourth array

x1_s, y1_s = (array_0_q_s.shape)
x2_s, y2_s = (array_1_q_s.shape)
x3_s, y3_s = (array_2_q_s.shape)
x4_s, y4_s = (array_3_q_s.shape)

y_q_s = y1_s + y2_s + y3_s + y4_s
print(y_q_s)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_s = degrees(
    np.concatenate((array_0_q_s, array_1_q_s, array_2_q_s, array_3_q_s), axis=1))  # All Phases

#####################
array_0_q_p = data_2["states_no_intermediate"][0]['q']  # First array
array_1_q_p = data_2["states_no_intermediate"][1]['q']  # Second array
array_2_q_p = data_2["states_no_intermediate"][2]['q']  # Third array
array_3_q_p = data_2["states_no_intermediate"][3]['q']  # Fourth array

x1_p, y1_p = (array_0_q_p.shape)
x2_p, y2_p = (array_1_q_p.shape)
x3_p, y3_p = (array_2_q_p.shape)
x4_p, y4_p = (array_3_q_p.shape)

y_q_p = y1_p + y2_p + y3_p + y4_p
print(y_q_p)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_p = degrees(
    np.concatenate((array_0_q_p, array_1_q_p, array_2_q_p, array_3_q_p), axis=1))  # All Phases

#####################
array_0_q_t = data_3["states_no_intermediate"][0]['q']  # First array
array_1_q_t = data_3["states_no_intermediate"][1]['q']  # Second array
array_2_q_t = data_3["states_no_intermediate"][2]['q']  # Third array
array_3_q_t = data_3["states_no_intermediate"][3]['q']  # Fourth array

x1_t, y1_t = (array_0_q_t.shape)
x2_t, y2_t = (array_1_q_t.shape)
x3_t, y3_t = (array_2_q_t.shape)
x4_t, y4_t = (array_3_q_t.shape)

y_q_t = y1_t + y2_t + y3_t + y4_t
print(y_q_t)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_t = degrees(
    np.concatenate((array_0_q_t, array_1_q_t, array_2_q_t, array_3_q_t), axis=1))  # All Phases

#####################

array_0_q_d = data_4["states_no_intermediate"][0]['q']  # First array
array_1_q_d = data_4["states_no_intermediate"][1]['q']  # Second array
array_2_q_d = data_4["states_no_intermediate"][2]['q']  # Third array
array_3_q_d = data_4["states_no_intermediate"][3]['q']  # Fourth array

x1_d, y1_d = (array_0_q_d.shape)
x2_d, y2_d = (array_1_q_d.shape)
x3_d, y3_d = (array_2_q_d.shape)
x4_d, y4_d = (array_3_q_d.shape)

y_q_d = y1_d + y2_d + y3_d + y4_d
print(y_q_d)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_d = degrees(
    np.concatenate((array_0_q_d, array_1_q_d, array_2_q_d, array_3_q_d), axis=1))  # All Phases

#####################

array_0_q_e = data_5["states_no_intermediate"][0]['q']  # First array
array_1_q_e = data_5["states_no_intermediate"][1]['q']  # Second array
array_2_q_e = data_5["states_no_intermediate"][2]['q']  # Third array
array_3_q_e = data_5["states_no_intermediate"][3]['q']  # Fourth array

x1_e, y1_e = (array_0_q_e.shape)
x2_e, y2_e = (array_1_q_e.shape)
x3_e, y3_e = (array_2_q_e.shape)
x4_e, y4_e = (array_3_q_e.shape)

y_q_e = y1_e + y2_e + y3_e + y4_e
print(y_q_e)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_e = degrees(
    np.concatenate((array_0_q_e, array_1_q_e, array_2_q_e, array_3_q_e), axis=1))  # All Phases

#####################
array_0_q_f = data_6["states_no_intermediate"][0]['q']  # First array
array_1_q_f = data_6["states_no_intermediate"][1]['q']  # Second array
array_2_q_f = data_6["states_no_intermediate"][2]['q']  # Third array
array_3_q_f = data_6["states_no_intermediate"][3]['q']  # Fourth array

x1_f, y1_f = (array_0_q_f.shape)
x2_f, y2_f = (array_1_q_f.shape)
x3_f, y3_f = (array_2_q_f.shape)
x4_f, y4_f = (array_3_q_f.shape)

y_q_f = y1_f + y2_f + y3_f + y4_f
print(y_q_f)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_f = degrees(
    np.concatenate((array_0_q_f, array_1_q_f, array_2_q_f, array_3_q_f), axis=1))  # All Phases

#####################
array_0_q_g = data_7["states_no_intermediate"][0]['q']  # First array
array_1_q_g = data_7["states_no_intermediate"][1]['q']  # Second array
array_2_q_g = data_7["states_no_intermediate"][2]['q']  # Third array
array_3_q_g = data_7["states_no_intermediate"][3]['q']  # Fourth array

x1_g, y1_g = (array_0_q_g.shape)
x2_g, y2_g = (array_1_q_g.shape)
x3_g, y3_g = (array_2_q_g.shape)
x4_g, y4_g = (array_3_q_g.shape)

y_q_g = y1_g + y2_g + y3_g + y4_g
print(y_q_g)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_g = degrees(
    np.concatenate((array_0_q_g, array_1_q_g, array_2_q_g, array_3_q_g), axis=1))  # All Phases

#####################

array_0_q_h = data_8["states_no_intermediate"][0]['q']  # First array
array_1_q_h = data_8["states_no_intermediate"][1]['q']  # Second array
array_2_q_h = data_8["states_no_intermediate"][2]['q']  # Third array
array_3_q_h = data_8["states_no_intermediate"][3]['q']  # Fourth array

x1_h, y1_h = (array_0_q_h.shape)
x2_h, y2_h = (array_1_q_h.shape)
x3_h, y3_h = (array_2_q_h.shape)
x4_h, y4_h = (array_3_q_h.shape)

y_q_h = y1_h + y2_h + y3_h + y4_h
print(y_q_h)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_h = degrees(
    np.concatenate((array_0_q_h, array_1_q_h, array_2_q_h, array_3_q_h), axis=1))  # All Phases

#####################
array_0_q_i = data_9["states_no_intermediate"][0]['q']  # First array
array_1_q_i = data_9["states_no_intermediate"][1]['q']  # Second array
array_2_q_i = data_9["states_no_intermediate"][2]['q']  # Third array
array_3_q_i = data_9["states_no_intermediate"][3]['q']  # Fourth array

x1_i, y1_i = (array_0_q_i.shape)
x2_i, y2_i = (array_1_q_i.shape)
x3_i, y3_i = (array_2_q_i.shape)
x4_i, y4_i = (array_3_q_i.shape)

y_q_i = y1_i + y2_i + y3_i + y4_i
print(y_q_g)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_i = degrees(
    np.concatenate((array_0_q_i, array_1_q_i, array_2_q_i, array_3_q_i), axis=1))  # All Phases

#####################

array_0_q_j = data_10["states_no_intermediate"][0]['q']  # First array
array_1_q_j = data_10["states_no_intermediate"][1]['q']  # Second array
array_2_q_j = data_10["states_no_intermediate"][2]['q']  # Third array
array_3_q_j = data_10["states_no_intermediate"][3]['q']  # Fourth array

x1_j, y1_j = (array_0_q_j.shape)
x2_j, y2_j = (array_1_q_j.shape)
x3_j, y3_j = (array_2_q_j.shape)
x4_j, y4_j = (array_3_q_j.shape)

y_q_j = y1_j + y2_j + y3_j + y4_j
print(y_q_j)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_q_j = degrees(
    np.concatenate((array_0_q_j, array_1_q_j, array_2_q_j, array_3_q_j), axis=1))  # All Phases

#####################
#####################

array_0_qdot_s = data_1["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_s = data_1["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_s = data_1["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_s = data_1["states_no_intermediate"][3]['qdot']  # Fourth array

x1_s, y1_s = (array_0_qdot_s.shape)
x2_s, y2_s = (array_1_qdot_s.shape)
x3_s, y3_s = (array_2_qdot_s.shape)
x4_s, y4_s = (array_3_qdot_s.shape)

y_qdot_s = y1_s + y2_s + y3_s + y4_s
print(y_qdot_s)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_s = degrees(
    np.concatenate((array_0_qdot_s, array_1_qdot_s, array_2_qdot_s, array_3_qdot_s), axis=1))  # All Phases

#####################
array_0_qdot_p = data_2["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_p = data_2["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_p = data_2["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_p = data_2["states_no_intermediate"][3]['qdot']  # Fourth array

x1_p, y1_p = (array_0_qdot_p.shape)
x2_p, y2_p = (array_1_qdot_p.shape)
x3_p, y3_p = (array_2_qdot_p.shape)
x4_p, y4_p = (array_3_qdot_p.shape)

y_qdot_p = y1_p + y2_p + y3_p + y4_p
print(y_qdot_p)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_p = degrees(
    np.concatenate((array_0_qdot_p, array_1_qdot_p, array_2_qdot_p, array_3_qdot_p), axis=1))  # All Phases

#####################
array_0_qdot_t = data_3["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_t = data_3["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_t = data_3["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_t = data_3["states_no_intermediate"][3]['qdot']  # Fourth array

x1_t, y1_t = (array_0_qdot_t.shape)
x2_t, y2_t = (array_1_qdot_t.shape)
x3_t, y3_t = (array_2_qdot_t.shape)
x4_t, y4_t = (array_3_qdot_t.shape)

y_qdot_t = y1_t + y2_t + y3_t + y4_t
print(y_qdot_t)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_t = degrees(
    np.concatenate((array_0_qdot_t, array_1_qdot_t, array_2_qdot_t, array_3_qdot_t), axis=1))  # All Phases

#####################

array_0_qdot_d = data_4["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_d = data_4["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_d = data_4["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_d = data_4["states_no_intermediate"][3]['qdot']  # Fourth array

x1_d, y1_d = (array_0_qdot_d.shape)
x2_d, y2_d = (array_1_qdot_d.shape)
x3_d, y3_d = (array_2_qdot_d.shape)
x4_d, y4_d = (array_3_qdot_d.shape)

y_qdot_d = y1_d + y2_d + y3_d + y4_d
print(y_qdot_d)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_d = degrees(
    np.concatenate((array_0_qdot_d, array_1_qdot_d, array_2_qdot_d, array_3_qdot_d), axis=1))  # All Phases

#####################

array_0_qdot_e = data_5["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_e = data_5["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_e = data_5["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_e = data_5["states_no_intermediate"][3]['qdot']  # Fourth array

x1_e, y1_e = (array_0_qdot_e.shape)
x2_e, y2_e = (array_1_qdot_e.shape)
x3_e, y3_e = (array_2_qdot_e.shape)
x4_e, y4_e = (array_3_qdot_e.shape)

y_qdot_e = y1_e + y2_e + y3_e + y4_e
print(y_qdot_e)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_e = degrees(
    np.concatenate((array_0_qdot_e, array_1_qdot_e, array_2_qdot_e, array_3_qdot_e), axis=1))  # All Phases

#####################
array_0_qdot_f = data_6["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_f = data_6["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_f = data_6["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_f = data_6["states_no_intermediate"][3]['qdot']  # Fourth array

x1_f, y1_f = (array_0_qdot_f.shape)
x2_f, y2_f = (array_1_qdot_f.shape)
x3_f, y3_f = (array_2_qdot_f.shape)
x4_f, y4_f = (array_3_qdot_f.shape)

y_qdot_f = y1_f + y2_f + y3_f + y4_f
print(y_qdot_f)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_f = degrees(
    np.concatenate((array_0_qdot_f, array_1_qdot_f, array_2_qdot_f, array_3_qdot_f), axis=1))  # All Phases

#####################
array_0_qdot_g = data_7["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_g = data_7["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_g = data_7["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_g = data_7["states_no_intermediate"][3]['qdot']  # Fourth array

x1_g, y1_g = (array_0_qdot_g.shape)
x2_g, y2_g = (array_1_qdot_g.shape)
x3_g, y3_g = (array_2_qdot_g.shape)
x4_g, y4_g = (array_3_qdot_g.shape)

y_qdot_g = y1_g + y2_g + y3_g + y4_g
print(y_qdot_g)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_g = degrees(
    np.concatenate((array_0_qdot_g, array_1_qdot_g, array_2_qdot_g, array_3_qdot_g), axis=1))  # All Phases

#####################

array_0_qdot_h = data_8["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_h = data_8["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_h = data_8["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_h = data_8["states_no_intermediate"][3]['qdot']  # Fourth array

x1_h, y1_h = (array_0_qdot_h.shape)
x2_h, y2_h = (array_1_qdot_h.shape)
x3_h, y3_h = (array_2_qdot_h.shape)
x4_h, y4_h = (array_3_qdot_h.shape)

y_qdot_h = y1_h + y2_h + y3_h + y4_h
print(y_qdot_h)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_h = degrees(
    np.concatenate((array_0_qdot_h, array_1_qdot_h, array_2_qdot_h, array_3_qdot_h), axis=1))  # All Phases

#####################
array_0_qdot_i = data_9["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_i = data_9["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_i = data_9["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_i = data_9["states_no_intermediate"][3]['qdot']  # Fourth array

x1_i, y1_i = (array_0_qdot_i.shape)
x2_i, y2_i = (array_1_qdot_i.shape)
x3_i, y3_i = (array_2_qdot_i.shape)
x4_i, y4_i = (array_3_qdot_i.shape)

y_qdot_i = y1_i + y2_i + y3_i + y4_i
print(y_qdot_g)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_i = degrees(
    np.concatenate((array_0_qdot_i, array_1_qdot_i, array_2_qdot_i, array_3_qdot_i), axis=1))  # All Phases

#####################

array_0_qdot_j = data_10["states_no_intermediate"][0]['qdot']  # First array
array_1_qdot_j = data_10["states_no_intermediate"][1]['qdot']  # Second array
array_2_qdot_j = data_10["states_no_intermediate"][2]['qdot']  # Third array
array_3_qdot_j = data_10["states_no_intermediate"][3]['qdot']  # Fourth array

x1_j, y1_j = (array_0_qdot_j.shape)
x2_j, y2_j = (array_1_qdot_j.shape)
x3_j, y3_j = (array_2_qdot_j.shape)
x4_j, y4_j = (array_3_qdot_j.shape)

y_qdot_j = y1_j + y2_j + y3_j + y4_j
print(y_qdot_j)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_qdot_j = degrees(
    np.concatenate((array_0_qdot_j, array_1_qdot_j, array_2_qdot_j, array_3_qdot_j), axis=1))  # All Phases

#####################

array_0_tau_s = data_1['controls'][0]['tau']  # First array

array_1_tau_s = data_1['controls'][1]['tau']  # Second array
first_column = array_1_tau_s[:, 0]
array_0_tau_s[:, -1] = first_column

array_2_tau_s = data_1['controls'][2]['tau']  # Third array
first_column = array_2_tau_s[:, 0]
array_1_tau_s[:, -1] = first_column

array_3_tau_s = data_1['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_s[:, 0]
array_2_tau_s[:, -1] = first_column

array_3_tau_s = np.delete(array_3_tau_s, -1, axis=1)
last_column = array_3_tau_s[:, -1]
array_3_tau_s = np.hstack((array_3_tau_s, last_column.reshape(-1, 1)))

x1_s, y1_s = (array_0_tau_s.shape)
x2_s, y2_s = (array_1_tau_s.shape)
x3_s, y3_s = (array_2_tau_s.shape)
x4_s, y4_s = (array_3_tau_s.shape)

y_tau_s = y1_s + y2_s + y3_s + y4_s
print(y_tau_s)
# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_tau_s = np.concatenate((array_0_tau_s, array_1_tau_s, array_2_tau_s, array_3_tau_s), axis=1)

#####################

array_0_tau_p = data_2['controls'][0]['tau']  # First array

array_1_tau_p = data_2['controls'][1]['tau']  # Second array
first_column = array_1_tau_p[:, 0]
array_0_tau_p[:, -1] = first_column

array_2_tau_p = data_2['controls'][2]['tau']  # Third array
first_column = array_2_tau_p[:, 0]
array_1_tau_p[:, -1] = first_column

array_3_tau_p = data_2['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_p[:, 0]
array_2_tau_p[:, -1] = first_column

array_3_tau_p = np.delete(array_3_tau_p, -1, axis=1)
last_column = array_3_tau_p[:, -1]
array_3_tau_p = np.hstack((array_3_tau_p, last_column.reshape(-1, 1)))

x1_p, y1_p = (array_0_tau_p.shape)
x2_p, y2_p = (array_1_tau_p.shape)
x3_p, y3_p = (array_2_tau_p.shape)
x4_p, y4_p = (array_3_tau_p.shape)

y_tau_p = y1_p + y2_p + y3_p + y4_p
print(y_tau_p)
# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_tau_p = np.concatenate((array_0_tau_p, array_1_tau_p, array_2_tau_p, array_3_tau_p), axis=1)

#####################
#
array_0_tau_t = data_3['controls'][0]['tau']  # First array

array_1_tau_t = data_3['controls'][1]['tau']  # Second array
first_column = array_1_tau_t[:, 0]
array_0_tau_t[:, -1] = first_column

array_2_tau_t = data_3['controls'][2]['tau']  # Third array
first_column = array_2_tau_t[:, 0]
array_1_tau_t[:, -1] = first_column

array_3_tau_t = data_3['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_t[:, 0]
array_2_tau_t[:, -1] = first_column

array_3_tau_t = np.delete(array_3_tau_t, -1, axis=1)
last_column = array_3_tau_t[:, -1]
array_3_tau_t = np.hstack((array_3_tau_t, last_column.reshape(-1, 1)))

x1_t, y1_t = (array_0_tau_t.shape)
x2_t, y2_t = (array_1_tau_t.shape)
x3_t, y3_t = (array_2_tau_t.shape)
x4_t, y4_t = (array_3_tau_t.shape)

y_tau_t = y1_t + y2_t + y3_t + y4_t
print(y_tau_p)
# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_tau_t = np.concatenate((array_0_tau_t, array_1_tau_t, array_2_tau_t, array_3_tau_t), axis=1)

#####################
array_0_tau_d = data_4['controls'][0]['tau']  # First array

array_1_tau_d = data_4['controls'][1]['tau']  # Second array
first_column = array_1_tau_d[:, 0]
array_0_tau_d[:, -1] = first_column

array_2_tau_d = data_4['controls'][2]['tau']  # Third array
first_column = array_2_tau_d[:, 0]
array_1_tau_d[:, -1] = first_column

array_3_tau_d = data_4['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_d[:, 0]
array_2_tau_d[:, -1] = first_column

array_3_tau_d = np.delete(array_3_tau_d, -1, axis=1)
last_column = array_3_tau_d[:, -1]
array_3_tau_d = np.hstack((array_3_tau_d, last_column.reshape(-1, 1)))

x1_d, y1_d = (array_0_tau_d.shape)
x2_d, y2_d = (array_1_tau_d.shape)
x3_d, y3_d = (array_2_tau_d.shape)
x4_d, y4_d = (array_3_tau_d.shape)

y_tau_d = y1_d + y2_d + y3_d + y4_d
print(y_tau_d)
# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_tau_d = np.concatenate((array_0_tau_d, array_1_tau_d, array_2_tau_d, array_3_tau_d), axis=1)

#####################

array_0_tau_e = data_5['controls'][0]['tau']  # First array

array_1_tau_e = data_5['controls'][1]['tau']  # Second array
first_column = array_1_tau_e[:, 0]
array_0_tau_e[:, -1] = first_column

array_2_tau_e = data_5['controls'][2]['tau']  # Third array
first_column = array_2_tau_e[:, 0]
array_1_tau_e[:, -1] = first_column

array_3_tau_e = data_5['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_e[:, 0]
array_2_tau_e[:, -1] = first_column

array_3_tau_e = np.delete(array_3_tau_e, -1, axis=1)
last_column = array_3_tau_e[:, -1]
array_3_tau_e = np.hstack((array_3_tau_e, last_column.reshape(-1, 1)))

x1_e, y1_e = (array_0_tau_e.shape)
x2_e, y2_e = (array_1_tau_e.shape)
x3_e, y3_e = (array_2_tau_e.shape)
x4_e, y4_e = (array_3_tau_e.shape)

y_tau_e = y1_e + y2_e + y3_e + y4_e
print(y_tau_e)
# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_tau_e = np.concatenate((array_0_tau_e, array_1_tau_e, array_2_tau_e, array_3_tau_e), axis=1)

#####################

array_0_tau_f = data_6['controls'][0]['tau']  # First array

array_1_tau_f = data_6['controls'][1]['tau']  # Second array
first_column = array_1_tau_f[:, 0]
array_0_tau_f[:, -1] = first_column

array_2_tau_f = data_6['controls'][2]['tau']  # Third array
first_column = array_2_tau_f[:, 0]
array_1_tau_f[:, -1] = first_column

array_3_tau_f = data_6['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_f[:, 0]
array_2_tau_f[:, -1] = first_column

array_3_tau_f = np.delete(array_3_tau_f, -1, axis=1)
last_column = array_3_tau_f[:, -1]
array_3_tau_f = np.hstack((array_3_tau_f, last_column.reshape(-1, 1)))

x1_f, y1_f = (array_0_tau_f.shape)
x2_f, y2_f = (array_1_tau_f.shape)
x3_f, y3_f = (array_2_tau_f.shape)
x4_f, y4_f = (array_3_tau_f.shape)

y_tau_f = y1_f + y2_f + y3_f + y4_f
print(y_tau_f)
# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_tau_f = np.concatenate((array_0_tau_f, array_1_tau_f, array_2_tau_f, array_3_tau_f), axis=1)

#####################

array_0_tau_g = data_7['controls'][0]['tau']  # First array

array_1_tau_g = data_7['controls'][1]['tau']  # Second array
first_column = array_1_tau_g[:, 0]
array_0_tau_g[:, -1] = first_column

array_2_tau_g = data_7['controls'][2]['tau']  # Third array
first_column = array_2_tau_g[:, 0]
array_1_tau_g[:, -1] = first_column

array_3_tau_g = data_7['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_g[:, 0]
array_2_tau_g[:, -1] = first_column

array_3_tau_g = np.delete(array_3_tau_g, -1, axis=1)
last_column = array_3_tau_g[:, -1]
array_3_tau_g = np.hstack((array_3_tau_g, last_column.reshape(-1, 1)))

x1_g, y1_g = (array_0_tau_g.shape)
x2_g, y2_g = (array_1_tau_g.shape)
x3_g, y3_g = (array_2_tau_g.shape)
x4_g, y4_g = (array_3_tau_g.shape)

y_tau_g = y1_g + y2_g + y3_g + y4_g
print(y_tau_g)
# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_tau_g = np.concatenate((array_0_tau_g, array_1_tau_g, array_2_tau_g, array_3_tau_g), axis=1)

#####################

array_0_tau_h = data_8['controls'][0]['tau']  # First array

array_1_tau_h = data_8['controls'][1]['tau']  # Second array
first_column = array_1_tau_h[:, 0]
array_0_tau_h[:, -1] = first_column

array_2_tau_h = data_8['controls'][2]['tau']  # Third array
first_column = array_2_tau_h[:, 0]
array_1_tau_h[:, -1] = first_column

array_3_tau_h = data_8['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_h[:, 0]
array_2_tau_h[:, -1] = first_column

array_3_tau_h = np.delete(array_3_tau_h, -1, axis=1)
last_column = array_3_tau_h[:, -1]
array_3_tau_h = np.hstack((array_3_tau_h, last_column.reshape(-1, 1)))

x1_h, y1_h = (array_0_tau_h.shape)
x2_h, y2_h = (array_1_tau_h.shape)
x3_h, y3_h = (array_2_tau_h.shape)
x4_h, y4_h = (array_3_tau_h.shape)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_tau_h = np.concatenate((array_0_tau_h, array_1_tau_h, array_2_tau_h, array_3_tau_h), axis=1)

#####################

array_0_tau_i = data_9['controls'][0]['tau']  # First array

array_1_tau_i = data_9['controls'][1]['tau']  # Second array
first_column = array_1_tau_i[:, 0]
array_0_tau_i[:, -1] = first_column

array_2_tau_i = data_9['controls'][2]['tau']  # Third array
first_column = array_2_tau_i[:, 0]
array_1_tau_i[:, -1] = first_column

array_3_tau_i = data_9['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_i[:, 0]
array_2_tau_i[:, -1] = first_column

array_3_tau_i = np.delete(array_3_tau_i, -1, axis=1)
last_column = array_3_tau_i[:, -1]
array_3_tau_i = np.hstack((array_3_tau_i, last_column.reshape(-1, 1)))

x1_i, y1_i = (array_0_tau_i.shape)
x2_i, y2_i = (array_1_tau_i.shape)
x3_i, y3_i = (array_2_tau_i.shape)
x4_i, y4_i = (array_3_tau_g.shape)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_tau_i = np.concatenate((array_0_tau_i, array_1_tau_i, array_2_tau_i, array_3_tau_i), axis=1)

#####################


array_0_tau_j = data_10['controls'][0]['tau']  # First array

array_1_tau_j = data_10['controls'][1]['tau']  # Second array
first_column = array_1_tau_j[:, 0]
array_0_tau_j[:, -1] = first_column

array_2_tau_j = data_10['controls'][2]['tau']  # Third array
first_column = array_2_tau_j[:, 0]
array_1_tau_j[:, -1] = first_column

array_3_tau_j = data_10['controls'][3]['tau']  # Fourth array
first_column = array_3_tau_j[:, 0]
array_2_tau_j[:, -1] = first_column

array_3_tau_j = np.delete(array_3_tau_j, -1, axis=1)
last_column = array_3_tau_j[:, -1]
array_3_tau_j = np.hstack((array_3_tau_j, last_column.reshape(-1, 1)))

x1_j, y1_j = (array_0_tau_j.shape)
x2_j, y2_j = (array_1_tau_j.shape)
x3_j, y3_j = (array_2_tau_j.shape)
x4_j, y4_j = (array_3_tau_g.shape)

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_tau_j = np.concatenate((array_0_tau_j, array_1_tau_j, array_2_tau_j, array_3_tau_j), axis=1)

#####################

array_0_time_s = specific_points_s[0]  # zero array
array_1_time_s = specific_points_s[1]  # first array
array_2_time_s = specific_points_s[2]  # second array
array_3_time_s = specific_points_s[3]  # Third array
array_4_time_s = specific_points_s[4]  # Fourth array

t_1 = np.linspace(array_0_time_s, array_1_time_s, (len(data_1['states_no_intermediate'][0]['q'][0])))
t_2 = np.linspace(array_1_time_s, array_2_time_s, (len(data_1['states_no_intermediate'][1]['q'][0])))
t_3 = np.linspace(array_2_time_s, array_3_time_s, (len(data_1['states_no_intermediate'][2]['q'][0])))
t_4 = np.linspace(array_3_time_s, array_4_time_s, (len(data_1['states_no_intermediate'][3]['q'][0])))

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_time_s = np.concatenate((t_1, t_2, t_3, t_4), axis=0)  # All Phases
print(len(concatenated_array_time_s))
#####################

array_0_time_p = specific_points_p[0]  # zero array
array_1_time_p = specific_points_p[1]  # first array
array_2_time_p = specific_points_p[2]  # second array
array_3_time_p = specific_points_p[3]  # Third array
array_4_time_p = specific_points_p[4]  # Fourth array

t_1 = np.linspace(array_0_time_p, array_1_time_p, (len(data_2['states_no_intermediate'][0]['q'][0])))
t_2 = np.linspace(array_1_time_p, array_2_time_p, (len(data_2['states_no_intermediate'][1]['q'][0])))
t_3 = np.linspace(array_2_time_p, array_3_time_p, (len(data_2['states_no_intermediate'][2]['q'][0])))
t_4 = np.linspace(array_3_time_p, array_4_time_p, (len(data_2['states_no_intermediate'][3]['q'][0])))

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_time_p = np.concatenate((t_1, t_2, t_3, t_4), axis=0)  # All Phases
print(len(concatenated_array_time_p))

#####################

array_0_time_t = specific_points_t[0]  # zero array
array_1_time_t = specific_points_t[1]  # first array
array_2_time_t = specific_points_t[2]  # second array
array_3_time_t = specific_points_t[3]  # Third array
array_4_time_t = specific_points_t[4]  # Fourth array

t_1 = np.linspace(array_0_time_t, array_1_time_t, (len(data_3['states_no_intermediate'][0]['q'][0])))
t_2 = np.linspace(array_1_time_t, array_2_time_t, (len(data_3['states_no_intermediate'][1]['q'][0])))
t_3 = np.linspace(array_2_time_t, array_3_time_t, (len(data_3['states_no_intermediate'][2]['q'][0])))
t_4 = np.linspace(array_3_time_t, array_4_time_t, (len(data_3['states_no_intermediate'][3]['q'][0])))

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_time_t = np.concatenate((t_1, t_2, t_3, t_4), axis=0)  # All Phases
print(len(concatenated_array_time_t))

#####################

array_0_time_d = specific_points_d[0]  # zero array
array_1_time_d = specific_points_d[1]  # first array
array_2_time_d = specific_points_d[2]  # second array
array_3_time_d = specific_points_d[3]  # Third array
array_4_time_d = specific_points_d[4]  # Fourth array

t_1 = np.linspace(array_0_time_d, array_1_time_s, (len(data_1['states_no_intermediate'][0]['q'][0])))
t_2 = np.linspace(array_1_time_s, array_2_time_s, (len(data_1['states_no_intermediate'][1]['q'][0])))
t_3 = np.linspace(array_2_time_s, array_3_time_s, (len(data_1['states_no_intermediate'][2]['q'][0])))
t_4 = np.linspace(array_3_time_s, array_4_time_s, (len(data_1['states_no_intermediate'][3]['q'][0])))

# Concatenate the new arrays along axis 1 (horizontally)
concatenated_array_time_d = np.concatenate((t_1, t_2, t_3, t_4), axis=0)  # All Phases
print(len(concatenated_array_time_d))

Name = ["Pelvic Tilt, Anterior (-) and Posterior (+) Rotation", "Thorax, Left (+) and Right (-) Rotation",
        "Thorax, Flexion (-) and Extension (+)", "Right Shoulder, Abduction (-) and Adduction (+)",
        "Right Shoulder, Internal (+) and External (-) Rotation", "Right Shoulder, Flexion (+) and Extension (-)",
        "Elbow, Flexion (+) and Extension (-)", "Elbow, Pronation (+) and Supination (-)",
        "Wrist, Flexion (-) and Extension (+)", "MCP, Flexion (+) and Extension (-)"]
#
#
# for i in range(0, 10):
#     fig, axs = plt.subplots(nrows=3, ncols=1)
#
#     axs[0].plot(concatenated_array_time_s, concatenated_array_q_s[i, :], color='red', label=label_1)
#     axs[0].plot(concatenated_array_time_p, concatenated_array_q_p[i, :], color='blue', label=label_2)
#     #axs[0].plot(concatenated_array_time_t, concatenated_array_q_t[i-6, :], color='green', label=label_3)
#     # axs[0].plot(concatenated_array_time_p, concatenated_array_q_p[i, :], color='cyan', label=label_2)
#     # axs[0].plot(concatenated_array_time_t, concatenated_array_q_t[i, :], color='gray', label=label_3)
#     # axs[0].plot(concatenated_array_time_d, concatenated_array_q_g[i, :], color='yellow', label=label_7)
#     # axs[0].plot(concatenated_array_time_d, concatenated_array_q_h[i, :], color='black', label=label_8)
#     # axs[0].plot(concatenated_array_time_d, concatenated_array_q_i[i, :], color='hotpink', label=label_9)
#     # axs[0].plot(concatenated_array_time_d, concatenated_array_q_j[i, :], color='blue', label=label_10)
#
#     axs[0].set_title(Name[i])
#     axs[0].set_ylabel('θ (deg)', fontsize=12)
#     axs[0].legend()
#     axs[0].spines['top'].set_visible(False)
#     axs[0].spines['right'].set_visible(False)
#     axs[0].spines['bottom'].set_visible(True)
#     axs[0].spines['left'].set_visible(True)
#     axs[0].axis('auto')
#
#     axs[1].plot(concatenated_array_time_s, concatenated_array_qdot_s[i, :], color='red', label=label_1)
#     axs[1].plot(concatenated_array_time_p, concatenated_array_qdot_p[i, :], color='black', label=label_2)
#     # axs[1].plot(concatenated_array_time_t, concatenated_array_qdot_t[i, :], color='green', label=label_3)
#     # axs[1].plot(concatenated_array_time_d, concatenated_array_qdot_d[i, :], color='orange', label=label_4)
#     # axs[1].plot(concatenated_array_time_d, concatenated_array_qdot_e[i, :], color='cyan', label=label_5)
#     # axs[1].plot(concatenated_array_time_d, concatenated_array_qdot_f[i, :], color='gray', label=label_6)
#     # axs[1].plot(concatenated_array_time_d, concatenated_array_qdot_g[i, :], color='yellow', label=label_7)
#     # axs[1].plot(concatenated_array_time_d, concatenated_array_qdot_h[i, :], color='black', label=label_8)
#     # axs[1].plot(concatenated_array_time_d, concatenated_array_qdot_i[i, :], color='hotpink', label=label_9)
#     # axs[1].plot(concatenated_array_time_d, concatenated_array_qdot_j[i, :], color='darkviolet', label=label_10)
#     #
#     axs[1].set_ylabel(r'$\dot{\theta}$ (deg/sec)', fontsize=12)
#     axs[1].legend()
#     axs[1].spines['top'].set_visible(False)
#     axs[1].spines['right'].set_visible(False)
#     axs[1].spines['bottom'].set_visible(True)
#     axs[1].spines['left'].set_visible(True)
#     axs[1].axis('auto')
#
#     axs[2].plot(concatenated_array_time_s, concatenated_array_tau_s[i, :], color='red', label=label_1)
#     axs[2].plot(concatenated_array_time_p, concatenated_array_tau_p[i, :], color='blue', label=label_2)
#     #axs[2].plot(concatenated_array_time_t, concatenated_array_tau_t[i-6, :], color='green', label=label_3)
#     # axs[2].plot(concatenated_array_time_p, concatenated_array_tau_p[i, :], color='cyan', label=label_2)
#     # axs[2].plot(concatenated_array_time_t, concatenated_array_tau_t[i, :], color='gray', label=label_3)
#     # axs[2].plot(concatenated_array_time_t, concatenated_array_tau_g[i, :], color='yellow', label=label_7)
#     # axs[2].plot(concatenated_array_time_d, concatenated_array_tau_h[i, :], color='black', label=label_8)
#     # axs[2].plot(concatenated_array_time_t, concatenated_array_tau_i[i, :], color='hotpink', label=label_9)
#     # axs[2].plot(concatenated_array_time_d, concatenated_array_tau_j[i, :], color='blue', label=label_10)
#
#     axs[2].set_ylabel(r'$\tau$ (N/m)')
#     axs[2].set_xlabel('Time (sec)')
#     axs[2].legend()
#     axs[2].spines['top'].set_visible(False)
#     axs[2].spines['right'].set_visible(False)
#     axs[2].spines['bottom'].set_visible(True)
#     axs[2].spines['left'].set_visible(True)
#     axs[2].axis('auto')
#
#     for ax in axs:
#         ax.grid(True)
#         ax.xaxis.set_minor_locator(AutoMinorLocator())
#         ax.yaxis.set_minor_locator(AutoMinorLocator())
#         ax.grid(which='minor', linestyle=':', linewidth='0.2', color='gray')
#
#         for point in specific_points_s:
#             ax.axvline(x=point, color='r', linestyle='--')
#
#         for point in specific_points_p:
#             ax.axvline(x=point, color='b', linestyle=':')
#
#     plt.tight_layout()
# #
#
# plt.show()

# # #
Force_Values_V1 = np.array(data_1["Force_Values"][:,2])
Force_Values_V1[-1]=abs(Force_Values_V1[-1])
Force_Values_V2 = np.array(data_2["Force_Values"][:,2])
# Force_Values_V3 = np.array(data_3["Force_Values"][:,2])

x = np.arange(len(Force_Values_V1))
# Bar width
width = 0.2
# Plotting
plt.bar(x - 1.5*width, Force_Values_V1.flatten(), width=width, label='Flexion', color='red')
plt.bar(x - 0.5*width, Force_Values_V2.flatten(), width=width, label='Extension', color='blue')
# plt.bar(x + 0.5*width, Force_Values_V3.flatten(), width=width, label='Elbow')
# plt.bar(x + 1.5*width, Force_Values_V4.flatten(), width=width, label='V1_Shoulder_2')
# Labeling
plt.xlabel('Nodes')
plt.ylabel('Force Values (N)')
plt.title('Force Values for Different Versions')
plt.xticks(x)
plt.legend()
# Display
plt.tight_layout()
plt.show()