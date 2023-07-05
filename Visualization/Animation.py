import bioviz
import numpy as np
from matplotlib import pyplot as plt
import pickle

with open(
        "/home/alpha/pianoptim/PianOptim/2_Mathilde_2022/2__final_models_piano/1___final_model___squeletum_hand_finger_1_key_4_phases_/pressed/Results/Presssed_AllDOFs.pckl", "rb"
) as file:
    new_dict = pickle.load(file)


biorbd_model_path: str = "/home/alpha/pianoptim/PianOptim/2_Mathilde_2022/2__final_models_piano/1___final_model___squeletum_hand_finger_1_key_4_phases_/bioMod/Squeletum_hand_finger_3D_2_keys_octave_LA.bioMod"

# # --- Animate --- # #

b = bioviz.Viz(
    biorbd_model_path,
    markers_size=0.010,
    contacts_size=0.010,
    show_floor=False,
    show_segments_center_of_mass=False,
    show_global_ref_frame=True,
    show_global_center_of_mass=False,
    show_markers=False,
    n_frames=500,
    show_local_ref_frame=False,
)

all_q = np.hstack(
    (new_dict["states"][0]["q"], new_dict["states"][1]["q"], new_dict["states"][2]["q"], new_dict["states"][3]["q"])
)

b.load_movement(all_q)
b.exec()
plt.show()
