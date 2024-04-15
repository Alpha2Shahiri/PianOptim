import biorbd
import numpy as np
import pickle
import matplotlib.pyplot as plt

def get_user_input():
    while True:
        pressed = input("Show 'Pressed' or 'Struck' condition? (p/s): ").lower()
        if pressed in ['p', 's']:
            pressed = pressed == 'p'
            break
        else:
            print("Invalid input. Please enter 'p' or 's'.")

    return pressed

pressed = get_user_input()

dirName = "/home/alpha/pianoptim/PianOptim/Nov.Codes/Updated_BioModFile_YeadonModel/Updated_Biomod_Distance/X_4/"

saveName_DT = dirName + ("Pressed" if pressed else "Struck") + "_with_Thorax.pckl"
saveName_ST = dirName + ("Pressed" if pressed else "Struck") + "_without_Thorax.pckl"

biorbd_model_path_DT = "./With.bioMod"
biorbd_model_path_ST = "./Without.bioMod"

# Load the musculoskeletal models
model_DT = biorbd.Model("./With.bioMod")
model_ST = biorbd.Model("./Without.bioMod")

with open(saveName_DT, "rb") as file:
    dict_DT = pickle.load(file)

with open(saveName_ST, "rb") as file:
    dict_ST = pickle.load(file)

# Number of Degrees of Freedom (DOFs)
num_DOFs_DT = model_DT.nbDof()
num_DOFs_ST = model_ST.nbDof()

# Number of Shooting Nodes
if pressed:
    num_nodes = 8
else:
    num_nodes = 7

# Extract joint positions (q) and velocities (qdot) from the loaded data
array_q_s_DT = [dict_DT["states_no_intermediate"][i]["q"] for i in range(len(dict_DT["states_no_intermediate"]))]
array_qdot_s_DT = [dict_DT["states_no_intermediate"][i]["qdot"] for i in range(len(dict_DT["states_no_intermediate"]))]

array_q_s_ST = [dict_ST["states_no_intermediate"][i]["q"] for i in range(len(dict_ST["states_no_intermediate"]))]
array_qdot_s_ST = [dict_ST["states_no_intermediate"][i]["qdot"] for i in range(len(dict_ST["states_no_intermediate"]))]

# List to store the detailed contributions for each DOF and node before summation
detailed_contributions_DT = []
detailed_contributions_ST = []

# Iterate over the nodes for the first file (DT)
for i in range(num_nodes):
    q_obj_DT = np.array([array_q_s_DT[1][j][i] for j in range(num_DOFs_DT)])
    qdot_obj_DT = np.array([array_qdot_s_DT[1][j][i] for j in range(num_DOFs_DT)])

    # Computing the Jacobian for the "finger_marker" in the first file (DT)
    fingertip_marker_name = "finger_marker"
    parent_name = "RightFingers"
    p = biorbd.NodeSegment(0, 0, -0.046782999938)
    update_kin = True
    markers_jacobian_DT = model_DT.markersJacobian(q_obj_DT, parent_name, p, update_kin)

    # Extract the Jacobian matrix as a NumPy array for the first file (DT)
    jacobian_array_DT = markers_jacobian_DT.to_array()

    # Initialize a matrix to store the contributions for this node in the first file (DT)
    contributions_matrix_DT = np.zeros((jacobian_array_DT.shape[0], jacobian_array_DT.shape[1]))

    # Calculate the contributions for each DOF in the first file (DT)
    for dof in range(jacobian_array_DT.shape[1]):
        for dim in range(jacobian_array_DT.shape[0]):
            contributions_matrix_DT[dim][dof] = jacobian_array_DT[dim][dof] * qdot_obj_DT[dof]

    # Store the contributions matrix for this node in the first file (DT)
    detailed_contributions_DT.append(contributions_matrix_DT)

# Iterate over the nodes for the second file (ST)
for i in range(num_nodes):
    q_obj_ST = np.array([array_q_s_ST[1][j][i] for j in range(num_DOFs_ST)])
    qdot_obj_ST = np.array([array_qdot_s_ST[1][j][i] for j in range(num_DOFs_ST)])

    # Computing the Jacobian for the "finger_marker" in the second file (ST)
    fingertip_marker_name = "finger_marker"
    parent_name = "RightFingers"
    p = biorbd.NodeSegment(0, 0, -0.046782999938)
    update_kin = True
    markers_jacobian_ST = model_ST.markersJacobian(q_obj_ST, parent_name, p, update_kin)

    # Extract the Jacobian matrix as a NumPy array for the second file (ST)
    jacobian_array_ST = markers_jacobian_ST.to_array()

    # Initialize a matrix to store the contributions for this node in the second file (ST)
    contributions_matrix_ST = np.zeros((jacobian_array_ST.shape[0], jacobian_array_ST.shape[1]))

    # Calculate the contributions for each DOF in the second file (ST)
    for dof in range(jacobian_array_ST.shape[1]):
        for dim in range(jacobian_array_ST.shape[0]):
            contributions_matrix_ST[dim][dof] = jacobian_array_ST[dim][dof] * qdot_obj_ST[dof]

    # Store the contributions matrix for this node in the second file (ST)
    detailed_contributions_ST.append(contributions_matrix_ST)

z_contributions_by_nodes_DT = np.zeros((num_nodes, num_DOFs_DT))
z_contributions_by_nodes_ST = np.zeros((num_nodes, num_DOFs_ST))

for i in range(num_nodes):
    z_contributions_by_nodes_DT[i] = detailed_contributions_DT[i][2]
    z_contributions_by_nodes_ST[i] = detailed_contributions_ST[i][2]

# Calculate the final Z velocity for each node by summing the contributions across all DOFs
final_z_velocity_per_node_DT = np.sum(z_contributions_by_nodes_DT, axis=1)
final_z_velocity_per_node_ST = np.sum(z_contributions_by_nodes_ST, axis=1)

# Assign the DOF names for the first file (DT)
joint_dof_map_DT = {
    "Pelvic": [0],
    "Thoracic": [1, 2],
    "Upper Thoracic": [3, 4],
    "Shoulder": [5, 6, 7],
    "Elbow": [8, 9],
    "Wrist": [10],
    "MCP": [11]
}

# Assign the DOF names for the second file (ST)
joint_dof_map_ST = {
    "Shoulder": [0, 1, 2],
    "Elbow": [3, 4],
    "Wrist": [5],
    "MCP": [6]
}

joint_contributions_by_nodes_DT = {}
joint_contributions_by_nodes_ST = {}

# Sum the contributions of the DOFs belonging to the same joint for each node in the first file (DT)
for node_idx in range(num_nodes):
    joint_contributions_DT = {}
    for joint_name, dof_indices in joint_dof_map_DT.items():
        joint_contribution_DT = sum(z_contributions_by_nodes_DT[node_idx][dof_idx] for dof_idx in dof_indices)
        joint_contributions_DT[joint_name] = joint_contribution_DT
    joint_contributions_by_nodes_DT[node_idx] = joint_contributions_DT

# Sum the contributions of the DOFs belonging to the same joint for each node in the second file (ST)
for node_idx in range(num_nodes):
    joint_contributions_ST = {}
    for joint_name, dof_indices in joint_dof_map_ST.items():
        joint_contribution_ST = sum(z_contributions_by_nodes_ST[node_idx][dof_idx] for dof_idx in dof_indices)
        joint_contributions_ST[joint_name] = joint_contribution_ST
    joint_contributions_by_nodes_ST[node_idx] = joint_contributions_ST

# Calculate the total contribution of all joints for each node in the first file (DT)
total_contributions_by_nodes_DT = [sum(joint_contributions.values()) for joint_contributions in joint_contributions_by_nodes_DT.values()]

# Calculate the total contribution of all joints for each node in the second file (ST)
total_contributions_by_nodes_ST = [sum(joint_contributions.values()) for joint_contributions in joint_contributions_by_nodes_ST.values()]

# Create a figure with two subplots for the time series plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plot the time series curves of the joint contributions for the first file (DT)
for joint_name in joint_dof_map_DT.keys():
    joint_contributions_DT = [joint_contributions_by_nodes_DT[node_idx][joint_name] for node_idx in range(num_nodes)]
    ax1.plot(range(num_nodes), joint_contributions_DT, label=joint_name)

ax1.plot(range(num_nodes), total_contributions_by_nodes_DT, label='Total', linestyle='--', linewidth=2)
ax1.set_xlabel('Node')
ax1.set_ylabel('Z Velocity Contribution')
ax1.set_title("Pressed_" if pressed else "Struck_" 'Joint Contributions (DT)')
ax1.legend()
ax1.grid(True)

# Plot the time series curves of the joint contributions for the second file (ST)
for joint_name in joint_dof_map_ST.keys():
    joint_contributions_ST = [joint_contributions_by_nodes_ST[node_idx][joint_name] for node_idx in range(num_nodes)]
    ax2.plot(range(num_nodes), joint_contributions_ST, label=joint_name)

ax2.plot(range(num_nodes), total_contributions_by_nodes_ST, label='Total', linestyle='--', linewidth=2)
ax2.set_xlabel('Node')
ax2.set_ylabel('Z Velocity Contribution')
ax2.set_title("Pressed_" if pressed else "Struck_" 'Joint Contributions (ST)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()


# Create a new figure with subplots for the table and final velocity plot
fig_table, (ax_table, ax_velocity) = plt.subplots(1, 2, figsize=(16, 6))

# Create a table to display the joint contributions for each node
table_data_DT = []
table_data_ST = []

# Prepare the table data for the first file (DT)
for node_idx in range(num_nodes):
    row_data_DT = [node_idx]
    for joint_name in joint_dof_map_DT.keys():
        row_data_DT.append(joint_contributions_by_nodes_DT[node_idx][joint_name])
    row_data_DT.append(total_contributions_by_nodes_DT[node_idx])
    table_data_DT.append(row_data_DT)

# Prepare the table data for the second file (ST)
for node_idx in range(num_nodes):
    row_data_ST = [node_idx]
    for joint_name in joint_dof_map_ST.keys():
        row_data_ST.append(joint_contributions_by_nodes_ST[node_idx][joint_name])
    row_data_ST.append(total_contributions_by_nodes_ST[node_idx])
    table_data_ST.append(row_data_ST)

# Create the table for the first file (DT)
columns_DT = ['Node'] + list(joint_dof_map_DT.keys()) + ['Total']
ax_table.axis('tight')
ax_table.axis('off')
table_DT = ax_table.table(cellText=table_data_DT, colLabels=columns_DT, loc='center', cellLoc='center')
table_DT.auto_set_font_size(False)
table_DT.set_fontsize(10)
table_DT.scale(1.2, 1.2)

# Create the table for the second file (ST)
columns_ST = ['Node'] + list(joint_dof_map_ST.keys()) + ['Total']
ax_table.axis('tight')
ax_table.axis('off')
table_ST = ax_table.table(cellText=table_data_ST, colLabels=columns_ST, loc='center', cellLoc='center')
table_ST.auto_set_font_size(False)
table_ST.set_fontsize(10)
table_ST.scale(1.2, 1.2)

# Plot the final velocity for each node
ax_velocity.plot(range(num_nodes), final_z_velocity_per_node_DT, label='Final Velocity (DT)')
ax_velocity.plot(range(num_nodes), final_z_velocity_per_node_ST, label='Final Velocity (ST)')
ax_velocity.set_xlabel('Node')
ax_velocity.set_ylabel('Final Z Velocity')
ax_velocity.set_title('Final Z Velocity per Node')
ax_velocity.legend()
ax_velocity.grid(True)

plt.tight_layout()
plt.show()