define asahi = Character("小晨", color="#fda0a5", image="asahi")
define bf = Character("毕方", color="#ff5623", image="bf")
define ly = Character("六翼", color="#a4faa1", image="ly")
define bl = Character("冰蓝", color="#95f3ff", image="bl")
define jj = Character("江江", color="#728A6A", image="jj")
define o27 = Character("027", color="#236a00", image="027")
define hb = Character("红白", color="#B93737", image="hb")
define xq = Character("袭秋", color="#70e2b1", image="xq")
define anoitos = Character("【路人】Anoitos", color="#212121", image="anoitos")
define gz = Character("【路人】观众", color="#C11E32", image="gz")
define gambler = Character("【路人】gambler:", color="#533D25", image="gambler")
define bread = Character("【路人】面包", color="#8C95B4", image="bread")
define wolf = Character("【路人】狼崽桑", color="#FEBCCA", image="wolf")
define haruki = Character("高桥", color="#000c4e", image="haruki")
define shdocter = Character("狐日泽", color="#CDBAA3", image="shdocter")
define taotao = Character("涛涛", color="#413644", image="taotao")
define ly = Character("六翼", color="#F5BCCE", image="ly")
define iron = Character("铁皮", color="#FFE260", image="iron")
define zj = Character("崽架", color="#6093B7", image="zj")
define rock = Character("洛克", color="#8B5F11", image="rock")
define sage = Character("桑吉", color="#E7374E", image="sage")
define knight = Character("骑士", color="#fda0a5", image="knight")
define door = Character("神秘文字", color="#E7374E")

image sage_i = "sage.png"

image side asahi = "side_asahi.png"
image side bf = "side_bf.png"
image side ly = "side_ly.png"
image side bl = "side_bl.png"
image side jj = "side_jj.png"
image side 027 = "side_027.png"
image side hb = "side_hb.png"
image side xq = "side_xq.png"
image side anoitos = "side_anoitos.png"
image side gz = "side_gz.png"
image side gambler = "side_gambler.png"
image side bread = "side_bread.png"
image side wolf = "side_wolf.png"
image side haruki = "side_haruki.png"
image side shdocter = "side_shdocter.png"
image side taotao = "side_taotao.png"
image side iron = "side_iron.png"
image side zj = "side_zj.png"
image side rock = "side_rock.png"
image side sage = "side_sage3.png"
image l2d sage = "l2d_sage.png"
image side knight = "side_knight.png"

image bg main = "main_menu.png"
image bg gym = "gym.jpg"


label splashscreen:
    # $ updater.update("http://game.sage.osttsstudio.ltd/st2/updates.json", base=None, force=False, public_key=None, simulate=None, add=[], restart=True, confirm=True, patch=True)
    scene black
    with Pause(1)
    show splash2 with dissolve
    with Pause(3)
    scene black with dissolve
    with Pause(1)
    scene splash1 with dissolve
    with Pause(3)
    scene black with dissolve
    with Pause(2)
    $ renpy.movie_cutscene("images/op.webm")
    return

label start:
    scene bg main
    menu:
        "设定集":
            jump art_of
        "第一章 - 教堂修女":
            jump p1_start
        "第二章 - 人类的意义":
            jump p2_start
        "第三章 - 人类观察日记":
            jump p3_start
        "返回主界面":
            return