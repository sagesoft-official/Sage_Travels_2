﻿define sage = Character("桑吉", color="#E7374E", image="sage")
define knight = Character("骑士", color="#fda0a5", image="knight")
define door = Character("神秘文字", color="#ff0022", image="sage")

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
    play music "<from 13>audio/1.mp3"

    "请选择游玩的章节"
    menu:
        "第一章":
            jump label_p1
        "第二章":
            jump label_p2
        "第三章-序章":
            jump label_overture
        "返回主界面":
            return

label label_overture:
    scene bg dream
    "... ..."
    "注：本章节为Early Access版本，不代表最终品质。"
    "... ..."
    "小生物的旅行仍在继续，本次的故事是旅行途中的一次意外事故"
    "小生物穿越到一处莫名的空间，在那里，她见到了一个身着骑士盔甲的女性"
    "而小生物在这次，将作为引导者，指引骑士度过难关。"
    jump label_dream

label label_dream:
    "战争，战争永不改变，从她记事起，本国对外的战争就没有停歇过，与侵略战争不同的是，他们打的都是自卫反击战"
    "作为整片大陆最边缘的国度，国家的西面南面都面临着那些荒野蛮子的威胁，而临近国度也一直对他们虎视眈眈"
    "而就在他们与邻国签订百年不侵犯条约的第十三年，邻国撕毁了条约，恬不知耻的与蛮子联手，妄图将他们消灭后平分领地，战争，再次打响。"
    "远眺着大军出征的方向，她默默的擦拭起了手中的剑。"
    knight "我也要跟你们去。"
    "她对着自己的祖父说着"
    knight "我修习武艺已经十四年了。而且已经过了成年礼，我也可以像你们一样上阵杀敌"
    "只是，被拒绝了。"
    "祖父" "让你们这些半大孩子上战场？我们这些老东西还没死绝呢！"
    "轻轻摸了摸她的头，年事已高的祖父亲自率军出征，只是，那军中紧随着祖父的马匹后的，便是一口由六个人抬着的棺材。"
    "这也是她对祖父的最后的印象，敌国大败。从未扔下过书笔的父亲，第一次拿起了武器，坐上那王位。"
    "常年的战争，民风淳朴的他们一直秉持着，战时亲征，父辈死光，子辈接上，听说登基最短的一任，十四岁接任，三天后便死在了战场上。"
    "在他的治理下，国家蒸蒸日上，愈发富强，就连率军出征也频频胜利，敌国在他的攻势下丢城弃地，直至灭亡。"
    "慢慢的，就连周围最强大的国家也对他们礼让三分。"
    "而她的父亲也被称为贤王，在如此闪耀的父辈的光环照耀下，官员百姓们，乃至父母都对她以后的成就更加期待，愈发严厉的父母，开始逼迫她学习各种礼仪，治国之道，战争之道。"
    "而她，也许是幼年时期的骑士小说看多了，又或是叛逆期，单纯的只是想做个骑士。"
    "正因如此，她总觉得她的父亲对她感到不满，尝试着学习父亲教导她的那些东西，却总是觉得父亲不满意。"
    "随着再一次的进军，域外的蛮子彻底溃败，他们本以为能就此安歇一段时间。"
    "但，某天，莫名的裂缝在全国各地出现，大大小小不计其数，紧接着，某种类人生物从那裂缝中爬出，大肆屠杀着"
    "直到某天，那耀眼的白光从太阳升起处绽放，一切的一切，都化作了泡影"
    "祖父" "你本该随我一同去死"
    #"化为白骨的祖父这样吼着"
    "国民" "你本该拯救我们！你是我们最后的希望！为什么要逃！"
    #"国民的骷髅这样吼着。"
    "国民" "你这废物！"
    jump dream_end

label dream_end:
    scene black
    knight "啊！"
    "大叫着，骑士从梦中惊醒，冷汗已浸透她甲胄内的衣衫。"
    sage "怎么了？"
    "深呼吸了几次，她努力平复着自己那跳动过快的心脏。"
    knight "没什么，只是做了一场噩梦。"
    "听到那个声音，她的心情镇定了一些。"
    "就在白光闪过后，世界如雪花般崩坏，就在她以为自己在劫难逃的时候，精神一阵恍惚，等她反应过来，已经来到了这里。"
    scene maze1
    "一处洞穴，在她面前的是一座迷宫，洞穴并没有出口，所以除了向迷宫内前进之外，她没有别的出路。"
    "检查了一下随身装备，除了本身就携带的剑盾和穿戴的甲胄之外，多了一些水和干粮。"
    "在她进入迷宫后不知多长时间，耳边传来了一个声音。"
    sage "你好"
    "骤然响起的声音，惊得她直接拔出了剑。"
    knight "谁？！"
    "她举剑架盾环顾着四周。"
    "从她进入这里的开始，四周便安静得可怕，只有她自己的脚步声在幽深的走廊中回荡，四周黑得可怕，仅有的光源则是每隔几十米出现在墙壁上的火把"
    "她试过将火把取下，但火把仿佛和空间融为一体似的纹丝不动。"
    "唯一幸运的是，食物和水会隔一段时间自动补充，使得她不至于饿死在这迷宫中。"
    knight "出来！"
    "她的精神高度警惕。"
    sage "不要害怕，我并没有恶意"
    sage "我是一个旅行者，你可以叫我____，我可以帮助你离开这里"
    knight "怎么证明你说的是真的？"
    sage "听着，我也不知道是怎么来到这里的，接下来的话可能你不会相信"
    sage "我就站在你面前"
    "听到这话，她环顾四周，但是并没有看到半个人影，但是声音确实是从她前方不远处传来的。"
    knight "在我面前？开什么玩笑，我什么都没看见"
    sage "距离你不到半米，我能看到你，你却看不到我，我也无法触碰到你，你能接触到的只有我的声音"
    sage "而经过我刚才的尝试，我能离开你的最大距离也只有五米，超过这个距离后就像接触到坚硬的墙壁一样无法前进"
    sage "所以我跟你一样，也被困在了这里"
    sage "我会协助你离开这里，作为回报，我也可以离开这里，帮你就等于帮我自己，就当我们做个交易，成交么"
    "思索片刻，她收起了剑。"
    knight "成交"
    "这就是小生物与骑士旅程的开始。"
    jump label_maze

label label_maze:
    # maze
    knight "我们已经在这里多久了，朋友"
    "胡乱往自己嘴里塞了点干粮后，她站起了身，拍打了几下身上的尘土，向前走去。"
    sage "不清楚，不过我们已经在这里绕了不知道多少圈了"
    "她已经看到了之前在墙壁上用剑划出的印记。"
    knight "慢慢来吧，总能走出去的"
    "她给自己打着气。"
    knight "我们开始吧，朋友，已经拖了太久了"
    jump maze

label maze:

    python:
        import os
        os.system("maze.exe")

    "... ..."

    python:
        if not os.path.exists("maze.txt"):
            maze_status = False
        else:
            maze_status = True

    if not maze_status:
        knight "我好像走错了路，朋友..."
        menu:
            "重新开始":
                jump label_maze
            "返回主菜单":
                return

    "从迷宫走出的瞬间，刺眼的光芒晃得她不禁眯起了双眼，好一会才看清眼前的情况。"
    scene bg room
    "那是一个灯火通明的大厅，遍布各处的魔法灯将这里映照得恍若白昼。"
    "大厅的中间是一张长条形的桌子，桌子上摆满了各式山珍海味，见过的没见过的应有尽有，桌子的旁边放着一把椅子。"
    scene bg door
    "在大厅的尽头处，立着一扇古典的石质大门，上面用着金色的金属组成神秘的纹路，仿佛是个法阵，又仿佛是某种神秘的图腾。"
    "而大门的两侧，矗立着两尊雕像。"
    "一尊骑士与一尊羊角恶魔，它们面向而立，骑士手中的剑与恶魔的爪子相交组成了大门的穹顶，雕刻精细得仿若生者。"
    knight "这里是......"
    sage "我也不清楚"
    "就在这时，门上的金属部分流光闪动，如同液体一样从大门上流淌而下，在她们的面前组成文字。"
    door "世界被毁灭的滋味如何？"
    "看到内容的她，不禁瞪大了双眼。但还没等她有动作，文字又有了变化。"
    door "别急，看下去。"
    door "你所在的世界泡已经变成了虚空中的尘埃，只剩下一些残渣。"
    door "只不过，我这人心善，在即将毁灭的时候将你救了下来，那么，我问你，你想拯救你的世界么？"
    door "当然，不管你同意与否，至少这桌大餐都是属于你的，就当作我犒劳你和你的伙伴穿越迷宫的奖励。"
    jump choose

label choose:
    menu:
        "拯救":
            jump label_choose1
        "拒绝":
            jump label_choose2

label label_choose1:
    "理所当然的选项，不管是作为骑士的本能，亦或是作为那世界仅存的人，又或是身为皇家的骄傲与责任感。"
    "骑士毫不犹豫的选择了拯救世界的选项。"
    knight "如果我能成功的拯救这个世界的话，父亲，你是否会为我感到骄傲呢？"
    "她这样想着。"
    door "这样么，那么，在这座大门打开后，你和你的伙伴需要闯过七层关卡，在打开最底层的大门后，世界的残渣便会重新凝结，你就拯救了世界。"
    door "当然，这路上，困难和危险是无处不在的，如果你死在路上，我不会救你第二次，死了就是死了，而拯救世界自然成了一纸空谈，你，明白了么。"
    "点了点头，骑士表示自己已经知晓"
    "骑士坐在了椅子上，摘下了自己的头盔，一头柔顺的金发倾泻而下，虽然看上去有些毛躁，但是给人感觉手感肯定很好"
    "碧绿的双眼死死盯着眼前的食物，眼中仿佛闪烁着星星，伸手拿了个鸡腿塞到嘴里一口吞下，再将骨头吐出，让人不禁思考那张小嘴到底是怎么塞下那么大的东西的。"
    "而骑士也早就将礼仪什么的抛到了脑后，在迷宫里关了不知道多长时间，天天干粮淡水充饥，她早就馋坏了。"
    door "加油吧勇者，希望你能给我带来足够的乐趣。"
    "... ..."
    "... ..."
    "序章完"
    jump end

label label_choose2:
    "拯救世界，四个字听起来简单，但是，那责任的重担仿佛能将人压垮。"
    "骑士跪倒在地，大口地呼吸着，抉择的艰难压得她喘不过气。"
    "说白了，她只是个无能的骑士，甚至连一句父亲的夸奖都得不到，废物中的废物罢了。"
    "拯救世界？这么伟大的事情换她的父亲来，肯定会非常简单的做到的吧。"
    "至于她，不行的吧，做不到的吧。"
    "既然做不到，不如，就这么陪大家一起去死吧。"
    "这么想着，她拔出了剑，将它架到了自己的脖子上，划了过去。"
    "随着尸体倒地的声音，小生物的视角也随之一暗，一股强烈的吸力将她抽了进去。"
    "... ..."
    "... ..."
    "达成结局：'L'oser"
    jump end

label end:
    menu:
        "重新选择":
            jump choose
        "返回主界面":
            return

label label_p1:
    "该版本为Early Access版本，第一章将在正式版开放，敬请期待..."
    "注：第一章内容为SageSoft在2022年发布的小生物历险记重制版"
    "如需游玩请访问【https://sagesoft.ltd/sagesoft】 | 【https://nya-wsl.itch.io】"
    menu:
        "返回主界面":
            return
        "选择章节":
            jump start

label label_p2:
    "该版本为Early Access版本，第二章将在正式版开放，敬请期待..."
    "注：第二章内容为SageSoft在2023年发布的小生物历险记2"
    "如需游玩请访问【https://sagesoft.ltd/sagesoft】 | 【https://nya-wsl.itch.io】"
    menu:
        "返回主界面":
            return
        "选择章节":
            jump start