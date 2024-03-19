define sage = Character("桑吉", color="#E7374E", image="sage")
define knight = Character("骑士", color="#fda0a5", image="knight")
define door = Character("神秘文字", color="#E7374E")

image bg main = "main_menu.jpg"
image bg dream = "dream_1080.png"
image bg maze = "maze.png"
image bg maze1 = "maze1_1080.png"
image bg door = "door_1080.png"
image bg room = "room_1080.png"
image bg room1 = "room_1_1080.png"
image side sage = "side_sage.png"
image side knight = "side_knight.png"

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
        "迷宫":
            jump label_maze
        "返回主界面":
            return