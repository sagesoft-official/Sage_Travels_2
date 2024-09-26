label art_of:
    scene sky
    play music "audio/art_of.mp3"
    jump art_of_menu

label art_of_menu:
    scene sky
    menu:
        "SageSoft":
            jump art_of_ss
        "桑吉Sage":
            jump art_of_sage
        "小晨":
            jump art_of_asahi
        "返回主菜单":
            return
    show text """
{size=+10}{color=#E7374E}
SageSoft
{/color}{/size}
""" with dissolve
    window hide
    pause
    jump art_of_menu

label art_of_ss:
    show text """
{size=+10}{color=#E7374E}
SageSoft成立于2023年11月20日，是一家成立于中国

服务器却在韩国和日本的专注于开发楠桐游戏的公司

旗下作品

《楠桐语录（ss-ana）》 | 《Sage_Travels系列》

《桑味书屋》 | 《桑尾草原》 | 《桥洞教堂忏悔室》 | 《合成大羊驼》

《驼地求升》 | 《三角之下》 | 《暗恋的目光》 | 《从桑尾草原合到桑味书屋》

《Sage Vs Asahi》

冷知识：

驼地求升和暗恋的目光的源代码已经丢失

Sage Vs Asahi立项于2023年8月，截止到2024年9月，开发进度为1%

{/color}{/size}
""" with dissolve
    window hide
    pause
    jump art_of_menu

label art_of_sage:
    show text """
{size=+10}{color=#E7374E}
来自于某个神秘次元的幼崽，最大的愿望是成为“人类”，俗称小生物

为了达成这一愿望并躲避神秘次元的追杀选择化身修女潜伏在一个名叫pilipili的地方

在官方设定中，小生物的部分设定为

修女、南极同人女、喜好楠桐、某任前男友是snake、虚拟主播

关于其身份背景的部分设定曾出现在SageSoft发行的某个DLC中
{/color}{/size}
""" with dissolve
    window hide
    pause
    jump art_of_menu

label art_of_asahi:
    show text """
{size=+10}{color=#E7374E}
楠桐、荷花人、土豆雷

因为他瘦小，群ID又带有晨字，头像又是荷花头

别人便从那些半懂不懂的话里，替他取下几个绰号，叫做小晨，又叫花开富贵
{/color}{/size}
""" with dissolve
    window hide
    pause
    jump art_of_menu