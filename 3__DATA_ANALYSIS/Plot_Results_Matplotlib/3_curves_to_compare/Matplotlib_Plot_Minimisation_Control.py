
from matplotlib import pyplot as plt
import pickle
import numpy as np

# Import results with pelvis rotZ
with open(
        "/2__FINAL_MODELES_OSCAR/5:FINAL_Squeletum_hand_finger_1_key_4_phases/pressed/2_10_000_100/*50_AVEC_MAX_BOUND.pckl", 'rb') as file:new_dict = pickle.load(file)
with open(
        "", 'rb') as file: new_dict2 = pickle.load(file)
with open(
        "/2__FINAL_MODELES_OSCAR/5:FINAL_Squeletum_hand_finger_1_key_4_phases/pressed/1_every_dof_100/test_contact_xyz_&_minim_divided.pckl", 'rb') as file: new_dict3 = pickle.load(file)

# Print the dic ###########################################
# print(new_dict)
# print(new_dict == "Piano_results.pckl")
# print(type(new_dict))
###########################################################

# COMMUN ##################################################
T = np.hstack((np.linspace(0, 0.3, num=99), np.linspace(0.3, 0.3+0.044, num=99), np.linspace(0.3+0.044, 0.3+0.044+0.051, num=99), np.linspace(0.3+0.044+0.051, 0.3+0.044+0.051+0.35, num=99)))

# Q ######################################################
figQ, axs = plt.subplots(3, 4)

q = np.hstack(new_dict["states"][i]["q"][:, :-1] if i < 3 else new_dict["states"][i]["q"] for i in range(4))
q2 = np.hstack(new_dict2["states"][i]["q"][:, :-1] if i < 3 else new_dict2["states"][i]["q"] for i in range(4))
q3 = np.hstack(new_dict2["states"][i]["q"][:, :-1] if i < 3 else new_dict3["states"][i]["q"] for i in range(4))


axs[0, 0].plot(T, q[0, :], 'tab:red', label="Index, hand, radius and ulna at 100 000. Others at 100")
axs[0, 0].set_title("pelvis_rotZ_anteversion(-)/retroversion(+) \n")
axs[0, 0].plot(T, q2[0, :], 'tab:blue', label="Index, and hand at 100 000. Others at 100.")
axs[0, 0].plot(T, q3[0, :], 'tab:orange', label="Every dof at 100.", linestyle='--')


axs[0, 1].plot(T, q[1, :], 'tab:red')
axs[0, 1].set_title("thorax_rotY_rotation_right(-)/left(+) \n")
axs[0, 1].plot(T, q2[1, :], 'tab:blue')
axs[0, 1].plot(T, q3[1, :], 'tab:orange', linestyle='--')

axs[0, 2].plot(T, q[2, :], 'tab:red')
axs[0, 2].set_title("thorax_rotZ_extension(-)/flexion(+) \n")
axs[0, 2].plot(T, q2[2, :], 'tab:blue')
axs[0, 2].plot(T, q3[2, :], 'tab:orange', linestyle='--')

axs[0, 3].plot(T, q[3, :], 'tab:red')
axs[0, 3].set_title("humerus_rotX_abduction(-)/adduction(+) \n")
axs[0, 3].plot(T, q2[3, :], 'tab:blue')
axs[0, 3].plot(T, q3[3, :], 'tab:orange', linestyle='--')

axs[1, 0].plot(T, q[4, :], 'tab:red')
axs[1, 0].set_title("humerus_rotY_rotation_extern(-)/intern(+) \n")
axs[1, 0].plot(T, q2[4, :], 'tab:blue')
axs[1, 0].plot(T, q3[4, :], 'tab:orange', linestyle='--')

axs[1, 1].plot(T, q[5, :], 'tab:red')
axs[1, 1].set_title("humerus_rotZ_extension(-)/flexion(+) \n")
axs[1, 1].plot(T, q2[5, :], 'tab:blue')
axs[1, 1].plot(T, q3[5, :], 'tab:orange', linestyle='--')

axs[1, 2].plot(T, q[6, :], 'tab:red')
axs[1, 2].set_title("ulna_effector_rotZ_extension(-)/flexion(+) \n")
axs[1, 2].plot(T, q2[6, :], 'tab:blue')
axs[1, 2].plot(T, q3[6, :], 'tab:orange', linestyle='--')

axs[1, 3].plot(T, q[7, :], 'tab:red')
axs[1, 3].set_title("radius_effector_rotY_rotation_extern(-)/intern(+) \n")
axs[1, 3].plot(T, q2[7, :], 'tab:blue')
axs[1, 3].plot(T, q3[7, :], 'tab:orange', linestyle='--')

axs[2, 0].plot(T, q[8, :], 'tab:red')
axs[2, 0].set_title("hand_rotX_extension(-)/flexion(+) \n")
axs[2, 0].plot(T, q2[8, :], 'tab:blue')
axs[2, 0].plot(T, q3[8, :], 'tab:orange', linestyle='--')

axs[2, 1].plot(T, q[9, :], 'tab:red')
axs[2, 1].set_title("index_rotX_extension(-)/flexion(+) \n")
axs[2, 1].plot(T, q2[9, :], 'tab:blue')
axs[2, 1].plot(T, q3[9, :], 'tab:orange', linestyle='--')

axs[2, 2].set_title("NOBODY")
axs[2, 3].set_title("NOBODY")

# phase lines and axe titles
for i in range(0, 3):
    for j in range(0, 4):
        axs[i, j].axvline(x=0.3, color='gray', linestyle='--')
        axs[i, j].axvline(x=0.3+0.044, color='gray', linestyle='--')
        axs[i, j].axvline(x=0.3+0.044+0.051, color='gray', linestyle='--')
        axs[i, j].axvline(x=0.3+0.044+0.051+0.35, color='gray', linestyle='--')

for ax in axs.flat:
    ax.set(xlabel='Time (s)', ylabel='q (rad)')


figQ.suptitle('States (q) of limbs by minimizing finger, hand, radius & ulna\nor just finger & hand', fontname="Times New Roman", fontweight="bold")

figQ.legend(loc="upper right",        # Position of legend
           borderaxespad=0,        # Small spacing around legend box
           title="Weight of minimisation controls for :", prop={"size": 10})     # Title for the legend

plt.subplots_adjust(wspace=0.8, hspace=0.8)

# Qdot ######################################################
figQdot, axs = plt.subplots(3, 4)

qdot = np.hstack(new_dict["states"][i]["qdot"][:, :-1] if i < 3 else new_dict["states"][i]["qdot"] for i in range(4))
qdot2 = np.hstack(new_dict2["states"][i]["qdot"][:, :-1] if i < 3 else new_dict2["states"][i]["qdot"] for i in range(4))
qdot3 = np.hstack(new_dict2["states"][i]["qdot"][:, :-1] if i < 3 else new_dict3["states"][i]["qdot"] for i in range(4))


axs[0, 0].plot(T, qdot[0, :], 'tab:red', label="Index, hand, radius and ulna at 100 000. Others at 100")
axs[0, 0].set_title("pelvis_rotZ_anteversion(-)/retroversion(+) \n")
axs[0, 0].plot(T, qdot2[0, :], 'tab:blue', label="Index, and hand at 100 000. Others at 100")
axs[0, 0].plot(T, qdot3[0, :], 'tab:orange', label="Every dof at 100.", linestyle='--')


axs[0, 1].plot(T, qdot[1, :], 'tab:red')
axs[0, 1].set_title("thorax_rotY_rotation_right(-)/left(+) \n")
axs[0, 1].plot(T, qdot2[1, :], 'tab:blue')
axs[0, 1].plot(T, qdot3[1, :], 'tab:orange', linestyle='--')

axs[0, 2].plot(T, qdot[2, :], 'tab:red')
axs[0, 2].set_title("thorax_rotZ_extension(-)/flexion(+) \n")
axs[0, 2].plot(T, qdot2[2, :], 'tab:blue')
axs[0, 2].plot(T, qdot3[2, :], 'tab:orange')

axs[0, 3].plot(T, qdot[3, :], 'tab:red')
axs[0, 3].set_title("humerus_rotX_abduction(-)/adduction(+) \n")
axs[0, 3].plot(T, qdot2[3, :], 'tab:blue')
axs[0, 3].plot(T, qdot3[3, :], 'tab:orange', linestyle='--')

axs[1, 0].plot(T, qdot[4, :], 'tab:red')
axs[1, 0].set_title("humerus_rotY_rotation_extern(-)/intern(+) \n")
axs[1, 0].plot(T, qdot2[4, :], 'tab:blue')
axs[1, 0].plot(T, qdot3[4, :], 'tab:orange', linestyle='--')

axs[1, 1].plot(T, qdot[5, :], 'tab:red')
axs[1, 1].set_title("humerus_rotZ_extension(-)/flexion(+) \n")
axs[1, 1].plot(T, qdot2[5, :], 'tab:blue')
axs[1, 1].plot(T, qdot3[5, :], 'tab:orange', linestyle='--')

axs[1, 2].plot(T, qdot[6, :], 'tab:red')
axs[1, 2].set_title("ulna_effector_rotZ_extension(-)/flexion(+) \n")
axs[1, 2].plot(T, qdot2[6, :], 'tab:blue')
axs[1, 2].plot(T, qdot3[6, :], 'tab:orange', linestyle='--')

axs[1, 3].plot(T, qdot[7, :], 'tab:red')
axs[1, 3].set_title("radius_effector_rotY_rotation_extern(-)/intern(+) \n")
axs[1, 3].plot(T, qdot2[7, :], 'tab:blue')
axs[1, 3].plot(T, qdot3[7, :], 'tab:orange', linestyle='--')

axs[2, 0].plot(T, qdot[8, :], 'tab:red')
axs[2, 0].set_title("hand_rotX_extension(-)/flexion(+) \n")
axs[2, 0].plot(T, qdot2[8, :], 'tab:blue')
axs[2, 0].plot(T, qdot3[8, :], 'tab:orange', linestyle='--')

axs[2, 1].plot(T, qdot[9, :], 'tab:red')
axs[2, 1].set_title("index_rotX_extension(-)/flexion(+) \n")
axs[2, 1].plot(T, qdot2[9, :], 'tab:blue')
axs[2, 1].plot(T, qdot3[9, :], 'tab:orange', linestyle='--')

axs[2, 2].set_title("NOBODY")
axs[2, 3].set_title("NOBODY")

# phase lines and axe titles
for i in range(0, 3):
    for j in range(0, 4):
        axs[i, j].axvline(x=0.3, color='gray', linestyle='--')
        axs[i, j].axvline(x=0.3 + 0.044, color='gray', linestyle='--')
        axs[i, j].axvline(x=0.3 + 0.044 + 0.051, color='gray', linestyle='--')
        axs[i, j].axvline(x=0.3 + 0.044 + 0.051 + 0.35, color='gray', linestyle='--')
for ax in axs.flat:
    ax.set(xlabel='Time (s)', ylabel='Qdot (rad.s⁻1)')
figQdot.suptitle('States (qdot) of limbs by minimizing finger, hand, radius & ulna\nor just finger & hand', fontname="Times New Roman", fontweight="bold")

# legends
figQdot.legend(loc="upper right", borderaxespad=0, title="Weight of minimisation controls for :", prop={"size": 10})

plt.subplots_adjust(wspace=0.8, hspace=0.8)

# TAU ######################################################
figU, axs = plt.subplots(3, 4)

T2 = np.hstack((np.linspace(0, 0.3, num=20), np.linspace(0.3, 0.3+0.044, num=20), np.linspace(0.3+0.044, 0.3+0.044+0.051, num=20), np.linspace(0.3+0.044+0.051, 0.3+0.044+0.051+0.35, num=20)))

U = np.hstack((new_dict["controls"][i]["tau"][:, :-1] if i < 3 else new_dict["controls"][i]["tau"] for i in range(4)))
U2 = np.hstack((new_dict2["controls"][i]["tau"][:, :-1] if i < 3 else new_dict2["controls"][i]["tau"] for i in range(4)))
U3 = np.hstack((new_dict2["controls"][i]["tau"][:, :-1] if i < 3 else new_dict3["controls"][i]["tau"] for i in range(4)))


axs[0, 0].plot(T2, U[0, :], 'tab:red', label="Index, hand, radius and ulna at 100 000. Others at 100")
axs[0, 0].set_title("Tau_pelvis_rotZ_anteversion(-)/retroversion(+) \n")
axs[0, 0].plot(T2, U2[0, :], 'tab:blue', label="Index, and hand at 100 000. Others at 100")
axs[0, 0].plot(T2, U3[0, :], 'tab:orange', label="Every dof at 100.", linestyle='--')


axs[0, 1].plot(T2, U[1, :], 'tab:red')
axs[0, 1].set_title("Tau_thorax_rotY_rotation_right(-)/left(+) \n")
axs[0, 1].plot(T2, U2[1, :], 'tab:blue')
axs[0, 1].plot(T2, U3[1, :], 'tab:orange', linestyle='--')

axs[0, 2].plot(T2, U[2, :], 'tab:red')
axs[0, 2].set_title("Tau_thorax_rotZ_extension(-)/flexion(+) \n")
axs[0, 2].plot(T2, U2[2, :], 'tab:blue')
axs[0, 2].plot(T2, U3[2, :], 'tab:orange', linestyle='--')

axs[0, 3].plot(T2, U[3, :], 'tab:red')
axs[0, 3].set_title("Tau_humerus_rotX_abduction(-)/adduction(+) \n")
axs[0, 3].plot(T2, U2[3, :], 'tab:blue')
axs[0, 3].plot(T2, U3[3, :], 'tab:orange', linestyle='--')

axs[1, 0].plot(T2, U[4, :], 'tab:red')
axs[1, 0].set_title("Tau_humerus_rotY_rotation_extern(-)/intern(+) \n")
axs[1, 0].plot(T2, U2[4, :], 'tab:blue')
axs[1, 0].plot(T2, U3[4, :], 'tab:orange', linestyle='--')


axs[1, 1].plot(T2, U[5, :], 'tab:red')
axs[1, 1].set_title("Tau_humerus_rotZ_extension(-)/flexion(+) \n")
axs[1, 1].plot(T2, U2[5, :], 'tab:blue')
axs[1, 1].plot(T2, U3[5, :], 'tab:orange', linestyle='--')

axs[1, 2].plot(T2, U[6, :], 'tab:red')
axs[1, 2].set_title("Tau_ulna_effector_rotZ_extension(-)/flexion(+) \n")
axs[1, 2].plot(T2, U2[6, :], 'tab:blue')
axs[1, 2].plot(T2, U3[6, :], 'tab:orange', linestyle='--')

axs[1, 3].plot(T2, U[7, :], 'tab:red')
axs[1, 3].set_title("Tau_radius_effector_rotY_rotation_extern(-)/intern(+) \n")
axs[1, 3].plot(T2, U2[7, :], 'tab:blue')
axs[1, 3].plot(T2, U3[7, :], 'tab:orange', linestyle='--')

axs[2, 0].set_title("Tau_hand_rotX_extension(-)/flexion(+) \n")
axs[2, 0].plot(T2, U[8, :], 'tab:red')
axs[2, 0].plot(T2, U2[8, :], 'tab:blue')
axs[2, 0].plot(T2, U3[8, :], 'tab:orange', linestyle='--')

axs[2, 1].set_title("index_rotX_extension(-)/flexion(+) \n")
axs[2, 1].plot(T2, U[9, :], 'tab:red')
axs[2, 1].plot(T2, U2[9, :], 'tab:blue')
axs[2, 1].plot(T2, U3[9, :], 'tab:orange', linestyle='--')

axs[2, 2].set_title("NOBODY")
axs[2, 3].set_title("NOBODY")

# phase lines, legends and axe titles
for i in range(0, 3):
    for j in range(0, 4):
        axs[i, j].axvline(x=0.3, color='gray', linestyle='--')
        axs[i, j].axvline(x=0.3+0.044, color='gray', linestyle='--')
        axs[i, j].axvline(x=0.3+0.044+0.051, color='gray', linestyle='--')
        axs[i, j].axvline(x=0.3+0.044+0.051+0.35, color='gray', linestyle='--')
for ax in axs.flat:
    ax.set(xlabel='Time (s)', ylabel='Tau (N.m)')
figU.suptitle('Torque (tau) of limbs by minimizing finger, hand, radius & ulna\nor just finger & hand', fontname="Times New Roman", fontweight="bold")
figU.legend(loc="upper right", borderaxespad=0, title="Weight of minimisation controls for :", prop={"size": 10})

plt.subplots_adjust(wspace=0.8, hspace=0.8)

# show the graph
plt.show()

# Save images
# figU.savefig('State q of each DoF depending of the time for multiple contexts.png')
# figQdot.savefig('Velocity Qdot of each DoF depending of the time for multiple contexts.png')
# figQ.savefig('Torque of each DoF depending of the time for multiple contexts.png')
