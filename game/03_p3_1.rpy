label label_maze:
    scene bg maze1
    "注：本章节目前为玩法测试，所有内容均不代表正传，有关内容请以正式版为准"
    knight "我们开始吧，朋友，已经拖了太久了"
    jump maze

label maze:

    python:
        import random

        def maze_event_func():
            global maze_event_steps
            if maze_good_event == 1:
                mge_steps_1 = random.randint(1, 5)
                narrator("你在墙上发现了一个刻痕，似乎是张地图")
                narrator(f"迷宫步数-{mge_steps_1}")
                maze_event_steps = 1 + int(mge_steps_1)
            if maze_bad_event == 1:
                mbe_steps_1 = random.randint(1, 5)
                narrator("你迷失了方向，走错了路")
                narrator(f"迷宫步数+{mbe_steps_1}")
                maze_event_steps = 1 - int(mbe_steps_1)

        def check():
            global maze_good_event, maze_bad_event
            maze_good_event = 0
            maze_bad_event = 0
            status = random.randint(0, 2)
            if status == 1:
                maze_good_event = 1
                maze_event_func()
            if status == 2:
                maze_bad_event = 1
                maze_event_func()

        user_step = 0
        c1_status = 0
        c1_step = random.randint(10,15)
        maze_step = random.randint(30,40)
        while user_step < maze_step:
            narrator("往哪个方向走？")
            result = renpy.display_menu([("向前走", 1), ("向左走", 2), ("向右走", 3)])

            if result == 1:
                narrator("你向前面的门走去")
            if result == 2:
                narrator("你向左边的门走去")
            if result == 3:
                narrator("你向右边的门走去")

            if user_step > 3:
                check()
                user_step += maze_event_steps
            else:
                user_step += 1

            if user_step <= 0:
                user_step = 0

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
            if c1_status != 0:
                if user_step >= (maze_step - 4):
                    narrator("你发现前面的三道门都被石门堵住了")
                    if c1_status == 1:
                        narrator("正当你一筹莫展的时候，那个被你救下的神秘生物突然出现，并帮你撞开了石门")
                        c1_status = 0
                    if c1_status == 2:
                        narrator("你感觉到背后出现了什么东西，正当你准备转头的时候，你头一疼失去了意识")
                        narrator("当你醒来时你发现回到了遇见神秘生物的地方")
                        user_step = c1_step
                    if c1_status == 3:
                        narrator("""你突然开始感到胃疼，并且尝试了各种办法都无法打开石门

你的胃疼开始加剧

你开始头疼了

你感到昏昏欲睡

你昏迷了

当你醒来时你发现回到了遇见神秘生物的地方

而这次，你成为了那个神秘生物...""")
                        user_step = maze_step

        else:
            if c1_status != 3:
                narrator("你成功走出了迷宫")
            else:
                narrator("骑士因为吃了国民变成的“生物”，代替了国民承受永无止境的折磨，直到出现下一个来到这里的人")
                narrator("Bad Ending：spider man")
            renpy.jump("p0_end")

label p0_end:
    menu:
        "重新开始":
            jump label_maze
        "返回主界面":
            return