﻿## 此文件包含有可自定义您游戏的设置。
##
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。


## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

define config.name = _("Sage's Travels 2")


## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = True


## 游戏版本号。

define config.version = "Early_Access_α_v0.4.0"


## 放置在游戏内“关于”屏幕上的文本。将文本放在三个引号之间，并在段落之间留出空
## 行。

define gui.about = _p("""
制作： Nya-WSL

发行： SageSoft

编剧： 桑吉Sage（第一、二章） | 冰蓝IceBlue（第三章）

美术：桑吉Sage | 冰蓝IceBlue | 一个不愿意透露姓名的高中生


你知道吗：

第一章和第二章bgm为《黄昏之时》

现实中真的有楠桐语录

大部分主要角色的颜色都是从各自头像抽的色

主界面标题颜色和部分强调色是从桑吉头发抽色并加深以后的结果

第二章圣诞超市场景的SSR卡是羊驼在楠桐语录中随手抽的

这个游戏的原始版本是纯DOS窗口的文字游戏

第一章是22年的小生物1，第二章是23年的小生物2

小生物在不换引擎的情况下不会出3

其实我们一直相信桑吉能独立完成这个游戏！(除了几个小游戏)

骑士的画师是冰蓝IceBlue

第三章使用了大量的新功能和新机制

第三章所有场景的草图均来自冰蓝IceBlue，成图来自一个不愿意透露姓名的高中生（就算快40了也是高中生...吧）

每一章的代码行数都会比前一章更多

第一章和第二章都只写了一个脚本文件，但因为第三章过于复杂，我们不得不拆分为多个文件

我们计划将在每年的3月发布一个新的DLC，内容包括但不限于正传序章或与正传毫无关系的剧情


Together we make games and memes better.

We are all stories in the end.

But we hope our stories can lasts longer.

Thank you for playing.

希望各位玩家的每一天都是Happy Ending.
""")


## 在构建的发布版中，可执行文件和目录所使用的短名称。此处仅限使用 ASCII 字符，并
## 且不能包含空格、冒号或分号。

define build.name = "Sage_Travels_2"


## 音效和音乐 #######################################################################

## 这三个变量控制哪些内置的混音器会默认显示给用户。将其中一个设置为 False 将隐藏
## 对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 为了让用户在音效或语音轨道上播放测试音频，请取消对下面一行的注释并设置播放的
## 样本声音。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。

define config.main_menu_music = "main.mp3"


## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve


## 载入游戏后使用的转场。

define config.after_load_transition = None


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = dissolve


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 语句。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。若为 show，对话框将总是显示。若为 hide，对话框
## 仅在对话出现时显示。若为 auto，对话框会在 scene 语句前隐藏，并在有新对话时重
## 新显示。
##
## 在游戏开始后，可以用 window show、window hide 和 window auto 语句来改变其状
## 态。

define config.window = "auto"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 为瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 10


## 默认的自动前进延迟。数字越大，等待时间越长，有效范围为 0 - 30。

default preferences.afm_time = 15


## 存档目录 ########################################################################
##
## 控制 Ren'Py 放置游戏存档的特定操作系统目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该语句通常不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "Sage_Travels_2_Early_Access"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon (2).png"


## 构建配置 ########################################################################
##
## 此部分控制 Ren'Py 如何将您的项目转变为发行版文件。

init python:

    ## 以下函数接受文件模式。文件模式不区分大小写，并与基础目录的相对路径相匹
    ## 配，包括或不包括 /。如果多个模式匹配，则使用第一个模式。
    ##
    ## 在一个模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中的 txt 文件，“game/**.ogg”匹配游戏目录或任何子
    ## 目录中的 ogg 文件，“**.psd”匹配项目中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.psd', None)
    build.classify('game/pygame**', None)
    build.classify('game/cache**', None)
    build.classify('game/*.rpy', None)

    ## 若要封装文件，需将其列为“archive”。

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/fonts**', 'archive')

    ## 匹配为文档模式的文件会在 Mac 应用程序构建中被复制，因此它们同时出现在 APP
    ## 和 ZIP 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')
    build.include_update = True

## 执行应用内购需要一个 Google Play 许可密钥。许可密钥可以在 Google Play 开发者
## 控制台的“Monetize” > “Monetization Setup” > “Licensing”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 项目相关的用户名和项目名，以 / 分隔。

define build.itch_project = "Nya-WSL/sage-travels-2"