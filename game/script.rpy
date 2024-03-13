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

label label_maze:
    scene bg maze1
    knight "我们开始吧，朋友，已经拖了太久了"
    jump maze

label maze:

    python:
        import random
        user_step = 0
        c1_status = 0
        c1_step = random.randint(5,10)
        maze_step = random.randint(25,60)
        while user_step < maze_step:
            narrator("往哪个方向走？")
            result = renpy.display_menu([("向前走", 1), ("向左走", 2), ("向右走", 3)])
            if result == 1:
                narrator("你向前面的门走去")
                user_step += 1
            if result == 2:
                narrator("你向左边的门走去")
                user_step += 1
            if result == 3:
                narrator("你向右边的门走去")
                user_step += 1
            narrator("你走了" + str(user_step) + "道门")
            if user_step == c1_step:
                narrator("你发现了一个神秘生物")
                choice = renpy.display_menu([("救", 1), ("不救", 2), ("加餐", 3)])
                if choice == 1:
                    narrator("你成功救下了它，或许未来它会帮助你")
                    c1_status = 1
                if choice == 2:
                    narrator("你无视了它，它会记住的")
                    c1_status = 2
                if choice == 3:
                    narrator("你决定晚上加一道炖肉")
                    c1_status = 3
        else:
            narrator("你成功走出了迷宫")
            renpy.jump("end")

label end:
    menu:
        "重新开始":
            jump label_maze
        "返回主界面":
            return