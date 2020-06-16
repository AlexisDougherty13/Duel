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
            "duck_l": "Resources/Images/FillerSpriteL.png",
            "duck_r": "Resources/Images/FillerSpriteR.png",
            "jump_l": "Resources/Images/FillerSpriteL.png",
            "jump_r": "Resources/Images/FillerSpriteR.png",
            "thrust_high_l": "Resources/Images/FillerSpriteL.png",
            "thrust_high_r": "Resources/Images/FillerSpriteR.png",
            "thrust_med_l": "Resources/Images/FillerSpriteL.png",
            "thrust_med_r": "Resources/Images/FillerSpriteR.png",
            "thrust_low_l": "Resources/Images/FillerSpriteL.png",
            "thrust_low_r": "Resources/Images/FillerSpriteR.png"
        }
    else:
        # set a default skin
        images_dictionary = {
            "stand_l": "Resources/Images/MontoyaRunL.png",
            "stand_r": "Resources/Images/MontoyaRunR.png",
            "sword_high_l": "Resources/Images/MontoyaHighL.png",
            "sword_high_r": "Resources/Images/MontoyaHighR.png",
            "sword_med_l": "Resources/Images/MontoyaMedL.png",
            "sword_med_r": "Resources/Images/MontoyaMedR.png",
            "sword_low_l": "Resources/Images/MontoyaLowL.png",
            "sword_low_r": "Resources/Images/MontoyaLowR.png",
            "duck_l": "Resources/Images/FillerSpriteL.png",
            "duck_r": "Resources/Images/FillerSpriteR.png",
            "jump_l": "Resources/Images/FillerSpriteL.png",
            "jump_r": "Resources/Images/FillerSpriteR.png",
            "thrust_high_l": "Resources/Images/FillerSpriteL.png",
            "thrust_high_r": "Resources/Images/FillerSpriteR.png",
            "thrust_med_l": "Resources/Images/FillerSpriteL.png",
            "thrust_med_r": "Resources/Images/FillerSpriteR.png",
            "thrust_low_l": "Resources/Images/FillerSpriteL.png",
            "thrust_low_r": "Resources/Images/FillerSpriteR.png"
        }
    return images_dictionary
