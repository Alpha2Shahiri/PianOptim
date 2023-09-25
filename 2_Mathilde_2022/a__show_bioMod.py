import bioviz

model_path = "/home/alpha/pianoptim/PianOptim/2_Mathilde_2022/2__final_models_piano/old_models/3___final___model_finger_hand_1_key/Pressed/FINAL_Pressed_Finger_hand_1_keys/FINAL_Pressed_Finger_hand_1_keys_7_phases.bioMod"

b = bioviz.Viz(
    model_path,
    markers_size=0.00150,
    contacts_size=0.00150,
    show_floor=False,
    show_segments_center_of_mass=False,
    show_global_ref_frame=True,
    show_local_ref_frame=False,
)
b.exec()
