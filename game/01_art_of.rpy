label art_of:
    scene bg main
    menu:
        "测试1":
            jump art_of_1
        "测试2":
            jump art_of_2

label art_of_1:
    scene 设定集-测试1
    show text """
{size=+10}{color=#FFFFFF}
Art of 1
{/color}{/size}
""" with dissolve
    window hide
    pause
    jump art_of

label art_of_2:
    scene 设定集-测试2
    show text """
{size=+10}{color=#FFFFFF}
Art of 2
{/color}{/size}
""" with dissolve
    window hide
    pause
    jump art_of