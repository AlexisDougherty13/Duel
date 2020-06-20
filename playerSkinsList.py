# Skin Example
# skin = {"stand_l": "",
# "stand_r": "",
# "sword_high_l": "",
# "sword_high_r": "",
# "sword_med_l": "",
# "sword_med_r": "",
# "sword_low_l": "",
# "sword_low_r": "",
# "duck_l": "",
# "duck_r": "",
# "jump_l": "",
# "jump_r": "",
# "thrust_high_l": "",
# "thrust_high_r": "",
# "thrust_med_l": "",
# "thrust_med_r": "",
# "thrust_low_l": "",
# "thrust_low_r": ""}


def getSkin(character_type):
    images_dictionary = dict()
    if character_type == "Montoya":
        images_dictionary = {
            "run_l": "Resources/Images/MontoyaRunL.png",
            "run_r": "Resources/Images/MontoyaRunR.png",
            "sword_high_l": "Resources/Images/MontoyaHighL.png",
            "sword_high_r": "Resources/Images/MontoyaHighR.png",
            "sword_med_l": "Resources/Images/MontoyaMedL.png",
            "sword_med_r": "Resources/Images/MontoyaMedR.png",
            "sword_low_l": "Resources/Images/MontoyaLowL.png",
            "sword_low_r": "Resources/Images/MontoyaLowR.png",
            "duck_l": "Resources/Images/MontoyaDuckL.png",
            "duck_r": "Resources/Images/MontoyaDuckR.png",
            "thrust_high_l": "Resources/Images/MontoyaHighThrustL.png",
            "thrust_high_r": "Resources/Images/MontoyaHighThrustR.png",
            "thrust_med_l": "Resources/Images/MontoyaMedThrustL.png",
            "thrust_med_r": "Resources/Images/MontoyaMedThrustR.png",
            "thrust_low_l": "Resources/Images/MontoyaLowThrustL.png",
            "thrust_low_r": "Resources/Images/MontoyaLowThrustR.png",
            "dead_l_1": "Resources/Images/MontoyaDeath1L.png",
            "dead_r_1": "Resources/Images/MontoyaDeath1R.png",
            "dead_l_2": "Resources/Images/MontoyaDeath2L.png",
            "dead_r_2": "Resources/Images/MontoyaDeath2R.png",
            "dead_l_3": "Resources/Images/MontoyaDeath3L.png",
            "dead_r_3": "Resources/Images/MontoyaDeath3R.png"
            "ghost_run_l": "Resources/Images/MontoyaGhostRunL.png",
            "ghost_run_r": "Resources/Images/MontoyaGhostRunR.png",
            "ghost_sword_high_l": "Resources/Images/MontoyaGhostHighL.png",
            "ghost_sword_high_r": "Resources/Images/MontoyaGhostHighR.png",
            "ghost_sword_med_l": "Resources/Images/MontoyaGhostMedL.png",
            "ghost_sword_med_r": "Resources/Images/MontoyaGhostMedR.png",
            "ghost_sword_low_l": "Resources/Images/MontoyaGhostLowL.png",
            "ghost_sword_low_r": "Resources/Images/MontoyaGhostLowR.png",
            "ghost_duck_l": "Resources/Images/MontoyaGhostDuckL.png",
            "ghost_duck_r": "Resources/Images/MontoyaGhostDuckR.png",
            "ghost_thrust_high_l": "Resources/Images/MontoyaGhostHighThrustL.png",
            "ghost_thrust_high_r": "Resources/Images/MontoyaGhostHighThrustR.png",
            "ghost_thrust_med_l": "Resources/Images/MontoyaGhostMedThrustL.png",
            "ghost_thrust_med_r": "Resources/Images/MontoyaGhostMedThrustR.png",
            "ghost_thrust_low_l": "Resources/Images/MontoyaGhostLowThrustL.png",
            "ghost_thrust_low_r": "Resources/Images/MontoyaGhostLowThrustR.png",
            "ghost_dead_l_1": "Resources/Images/MontoyaGhostDeath1L.png",
            "ghost_dead_r_1": "Resources/Images/MontoyaGhostDeath1R.png",
            "ghost_dead_l_2": "Resources/Images/MontoyaGhostDeath2L.png",
            "ghost_dead_r_2": "Resources/Images/MontoyaGhostDeath2R.png",
            "ghost_dead_l_3": "Resources/Images/MontoyaGhostDeath3L.png",
            "ghost_dead_r_3": "Resources/Images/MontoyaGhostDeath3R.png"
        }
    else:
        # set a default skin
        images_dictionary = {
            "run_l": "Resources/Images/MontoyaRunL.png",
            "run_r": "Resources/Images/MontoyaRunR.png",
            "sword_high_l": "Resources/Images/MontoyaHighL.png",
            "sword_high_r": "Resources/Images/MontoyaHighR.png",
            "sword_med_l": "Resources/Images/MontoyaMedL.png",
            "sword_med_r": "Resources/Images/MontoyaMedR.png",
            "sword_low_l": "Resources/Images/MontoyaLowL.png",
            "sword_low_r": "Resources/Images/MontoyaLowR.png",
            "duck_l": "Resources/Images/MontoyaDuckL.png",
            "duck_r": "Resources/Images/MontoyaDuckR.png",
            "thrust_high_l": "Resources/Images/MontoyaHighThrustL.png",
            "thrust_high_r": "Resources/Images/MontoyaHighThrustR.png",
            "thrust_med_l": "Resources/Images/MontoyaMedThrustL.png",
            "thrust_med_r": "Resources/Images/MontoyaMedThrustR.png",
            "thrust_low_l": "Resources/Images/MontoyaLowThrustL.png",
            "thrust_low_r": "Resources/Images/MontoyaLowThrustR.png",
            "dead_l_1": "Resources/Images/MontoyaDeath1L.png",
            "dead_r_1": "Resources/Images/MontoyaDeath1R.png",
            "dead_l_2": "Resources/Images/MontoyaDeath2L.png",
            "dead_r_2": "Resources/Images/MontoyaDeath2R.png",
            "dead_l_3": "Resources/Images/MontoyaDeath3L.png",
            "dead_r_3": "Resources/Images/MontoyaDeath3R.png"
            "ghost_run_l": "Resources/Images/MontoyaGhostRunL.png",
            "ghost_run_r": "Resources/Images/MontoyaGhostRunR.png",
            "ghost_sword_high_l": "Resources/Images/MontoyaGhostHighL.png",
            "ghost_sword_high_r": "Resources/Images/MontoyaGhostHighR.png",
            "ghost_sword_med_l": "Resources/Images/MontoyaGhostMedL.png",
            "ghost_sword_med_r": "Resources/Images/MontoyaGhostMedR.png",
            "ghost_sword_low_l": "Resources/Images/MontoyaGhostLowL.png",
            "ghost_sword_low_r": "Resources/Images/MontoyaGhostLowR.png",
            "ghost_duck_l": "Resources/Images/MontoyaGhostDuckL.png",
            "ghost_duck_r": "Resources/Images/MontoyaGhostDuckR.png",
            "ghost_thrust_high_l": "Resources/Images/MontoyaGhostHighThrustL.png",
            "ghost_thrust_high_r": "Resources/Images/MontoyaGhostHighThrustR.png",
            "ghost_thrust_med_l": "Resources/Images/MontoyaGhostMedThrustL.png",
            "ghost_thrust_med_r": "Resources/Images/MontoyaGhostMedThrustR.png",
            "ghost_thrust_low_l": "Resources/Images/MontoyaGhostLowThrustL.png",
            "ghost_thrust_low_r": "Resources/Images/MontoyaGhostLowThrustR.png",
            "ghost_dead_l_1": "Resources/Images/MontoyaGhostDeath1L.png",
            "ghost_dead_r_1": "Resources/Images/MontoyaGhostDeath1R.png",
            "ghost_dead_l_2": "Resources/Images/MontoyaGhostDeath2L.png",
            "ghost_dead_r_2": "Resources/Images/MontoyaGhostDeath2R.png",
            "ghost_dead_l_3": "Resources/Images/MontoyaGhostDeath3L.png",
            "ghost_dead_r_3": "Resources/Images/MontoyaGhostDeath3R.png"
        }
    return images_dictionary
