define asahi = Character("晨宝", color="#fda0a5", image="asahi")
define bf = Character("毕方", color="#fcce9a", image="bf")
define ly = Character("六翼", color="#a4faa1", image="ly")
define bl = Character("冰蓝", color="#95f3ff", image="bl")
define jj = Character("江江", color="#728A6A", image="jj")
define o27 = Character("027", color="#236a00", image="027")
define hb = Character("红白", color="#B93737", image="hb")
define xq = Character("袭秋", color="#70e2b1", image="xq")
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
image side sage_p3 = "side_sage3.png"
image side sage_p1 = "side_sage1.png"
image side knight = "side_knight.png"

image bg main = "main_menu.jpg"
image bg dream = "dream_1080.png"
image bg maze = "maze.png"
image bg maze1 = "maze1_1080.png"
image bg door = "door_1080.png"
image bg room = "room_1080.png"
image bg room1 = "room_1_1080.png"


# label before_main_menu:
#     $ renpy.movie_cutscene("images/trailer.webm")
#     scene bridge_day
#     "... ..."
#     "今天你检查更新了吗？"
#     menu:
#         "是":
#             return
#         "否":
#             $ updater.update("http://game.sage.osttsstudio.ltd/st2/updates.json", base=None, force=False, public_key=None, simulate=None, add=[], restart=True, confirm=True, patch=True)

label start:
    scene bg main

    "请选择游玩的章节"
    menu:
        "第一章":
            jump p1_start
        "第二章":
            jump p2_start
        "迷宫":
            jump label_maze
        "返回主界面":
            return