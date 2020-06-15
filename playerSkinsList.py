# Skin Example
# skin = {"stand_l": "", "stand_r": "",
# "sword_high_l": "skeletonHighL.png",
# "sword_high_r": "skeletonHighR.png",
# "sword_med_l": "skeletonMedL.png",
# "sword_med_r": "skeletonMedR.png",
# "sword_low_l": "skeletonLowR.png",
# "sword_low_r": "skeletonLowR.png",
# "duck_l": "", "duck_r": "",
# "jump_l": "", "jump_r": "",
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
            "Resources/Images/stand_l": "Resources/Images/MontoyaRunL.png",
            "Resources/Images/stand_r": "Resources/Images/MontoyaRunR.png",
            "Resources/Images/sword_high_l": "Resources/Images/MontoyaHighL.png",
            "Resources/Images/sword_high_r": "Resources/Images/MontoyaHighR.png",
            "Resources/Images/sword_med_l": "Resources/Images/MontoyaMedL.png",
            "Resources/Images/sword_med_r": "Resources/Images/MontoyaMedR.png",
            "Resources/Images/sword_low_l": "Resources/Images/MontoyaLowL.png",
            "Resources/Images/sword_low_r": "Resources/Images/MontoyaLowR.png",
            "Resources/Images/duck_l": "Resources/Images/FillerSpriteL.png",
            "Resources/Images/duck_r": "Resources/Images/FillerSpriteR.png",
            "Resources/Images/jump_l": "Resources/Images/FillerSpriteL.png",
            "Resources/Images/jump_r": "Resources/Images/FillerSpriteR.png",
            "Resources/Images/thrust_high_l": "Resources/Images/FillerSpriteL.png",
            "Resources/Images/thrust_high_r": "Resources/Images/FillerSpriteR.png",
            "Resources/Images/thrust_med_l": "Resources/Images/FillerSpriteL.png",
            "Resources/Images/thrust_med_r": "Resources/Images/FillerSpriteR.png",
            "Resources/Images/thrust_low_l": "Resources/Images/FillerSpriteL.png",
            "Resources/Images/thrust_low_r": "Resources/Images/FillerSpriteR.png"
        }
    else:
        # set a default skin
        images_dictionary = {
            "Resources/Images/stand_l": "Resources/Images/MontoyaRunL.png",
            "Resources/Images/stand_r": "Resources/Images/MontoyaRunR.png",
            "Resources/Images/sword_high_l": "Resources/Images/MontoyaHighL.png",
            "Resources/Images/sword_high_r": "Resources/Images/MontoyaHighR.png",
            "Resources/Images/sword_med_l": "Resources/Images/MontoyaMedL.png",
            "Resources/Images/sword_med_r": "Resources/Images/MontoyaMedR.png",
            "Resources/Images/sword_low_l": "Resources/Images/MontoyaLowL.png",
            "Resources/Images/sword_low_r": "Resources/Images/MontoyaLowR.png",
            "Resources/Images/duck_l": "Resources/Images/FillerSpriteL.png",
            "Resources/Images/duck_r": "Resources/Images/FillerSpriteR.png",
            "Resources/Images/jump_l": "Resources/Images/FillerSpriteL.png",
            "Resources/Images/jump_r": "Resources/Images/FillerSpriteR.png",
            "Resources/Images/thrust_high_l": "Resources/Images/FillerSpriteL.png",
            "Resources/Images/thrust_high_r": "Resources/Images/FillerSpriteR.png",
            "Resources/Images/thrust_med_l": "Resources/Images/FillerSpriteL.png",
            "Resources/Images/thrust_med_r": "Resources/Images/FillerSpriteR.png",
            "Resources/Images/thrust_low_l": "Resources/Images/FillerSpriteL.png",
            "Resources/Images/thrust_low_r": "Resources/Images/FillerSpriteR.png"
        }
    return images_dictionary
