default choice_p2_a1 = False
default choice_p2_a2 = False
default choice_p2_b1 = False
default choice_p2_b2 = False
default choice_p2_c1 = False
default choice_p2_c2 = False
default label_supermarket_show = False
default label_c102_show = False
default label_tomato_show = False

label p2_start:
    scene bridge_day
    play music "<from 13>audio/p1.mp3"

    "... ..."
    "... ..."
    "旅行能使人进步，对小生物来说也一样。"
    "上一次的旅行让小生物增进了对人类的了解，但距离真正成为人类似乎还差一点关键的东西。"
    "为了找到最后的一片拼图，小生物再一次踏上旅途。"

menu:
    sage "首先要去哪里调查呢？"

    "圣诞超市":
        jump label_supermarket

    "C102同人展":
        jump label_c102

    "平顶山土豆田":
        jump label_tomato

label label_supermarket:
    scene supermarket
    $ label_supermarket_show = True
    show sage_i at left
    sage "超市和我之前去过的菜市场有些相似。"
    sage "少了些喧闹人气，多了衣食住行里食以外的别项，或许这样熟悉又陌生的地方能够给我一些灵感。"
    sage "才走进超市，就有一段紧迫的音乐伴随着激情十足的念白传入我的耳朵。"
    hide sage_i
    "全新沉浸式抽卡手游——《楠桐语录》！"
    "无论你是对楠桐文化浅尝则止的小白萌新！还是对楠桐世界了如指掌的old ass！"
    "楠桐语录都能给你带来耳目一新的震撼体验！"
    "体验楠桐！了解楠桐！沉·醉·楠·桐！"
    "明日发售！"
    anoitos "我心动了！这一听就是非常符合桑礼的好游戏啊！"
    gz "快快快下一个！然后开服就把好友加上！"
    gambler "哇这首期UP的SSR卡“〔g120〕晨宝只能被窝走后门”我好喜欢！抽爆！"
    bread "你们要是胆敢比我欧就等着半夜被我薄纱吧！"
    wolf "呃噫啊嘶哈玩不到楠桐语录我要死了！"
    "几人说说笑笑地走远了，但在不远处的饮料柜台前，有两人却露出了哀戚的表情。"
    "两人满脸疲惫，黑眼圈深重，头顶稀疏，一看就是常年加班的码农模样。"
    haruki "怎么办，明天就发售了，还有这么多bug。"
    shdocter "sudo rm -rf gay_quotations/ && rm -rf hitokoto/"
    haruki "删nm熬夜修。"
    "狐日泽拿出手机，向对方展示了下时间。"
    shdocter "现在下午2点，明天0点开服。哪怕你从这一秒就开始修，也只有12小时了，还努力个屁。"
    haruki "一起码了一年半的库说删就删，你还是人吗。"
    haruki "你也听到了刚才那群楠桐的话了，我觉得这游戏能大卖。"
    haruki "那我俩的绩效奖金就大大的有了啊，再坚持坚持。"
    shdocter "要说舍不得那我也肯定是舍不得的。"
    shdocter "但修不完bug的话开局就得和2077一样暴死，那我俩也得一起暴死了。"
    shdocter "不如现在跑，把屎山毁掉就没人知道它曾经存在过。"
    haruki "唉...我还是觉得能救一下的。"
    haruki "再说了，里面不还有你和我的语录吗。"
    haruki "对我来说，楠桐语录就像是我的孩子一样。"
    haruki "我们...的孩子一样。"
    shdocter "高师傅..."
    shdocter "但我们，还可以一起创造新的孩子。"
    shdocter "...只要我们还在一起，去一起寻找新的未来。"
    shdocter "你愿意和我走吗？"
    haruki "我..."
    haruki "我想和你走。"
    haruki "但是你想删库，并不是因为想跑路吧。"
    "他不自觉地握紧拳头。"
    haruki "是因为...你不愿意面对灵狐。"
    "两人之间的空气一瞬间凝固了。"
    "高桥露出一个苦笑，语气颤抖。"
    scene cg_p2_1
    haruki "为什么会这样呢..."
    haruki "第一次有了喜欢的人。有了能做一辈子朋友的人。"
    haruki "两件快乐事情重合在一起。而这两份快乐，又给我带来更多的快乐。"
    haruki "得到的，本该是像梦境一般幸福的时间..."
    haruki "但是，为什么，会变成这样呢..."
    "他笑了，但是又在哭泣。"
    "眼泪落在高桥脚下，溅开一朵悲伤的花。"
    "痛苦，愧疚，在二人的心里奔腾。"
    shdocter "我...我们该怎么做..."

    jump label_p2_choice1

label label_c102:
    scene c102
    $ label_c102_show = True

    show sage_i at left
    sage "创作是人类的本能。"
    sage "将仅有自己能见的光景讲述、陈述、叙述、描述，让自己的谜因（MEME）传递下去。 "
    sage "同人展会，源同而不同。用一个谜因将不同人链接起来。不同的人在吸收了同样的谜因后又产出自己的谜因。"
    sage "在这张将人链接起来的创作之网之中，或许可以受到一些启发。"

    hide sage_i
    "展会主舞台区早已被围得水泄不通，主持人激情洋溢地问候兴奋的观众们。"
    taotao "各位亲爱的女桐们！男桐们！大家好吗——！"
    taotao "欢迎大家来到第102届“晨宝杯”（简称c102）同人创作大赛的决赛！我是你们的主持涛涛！"
    taotao "究竟哪一位选手能够获得我们最终的大奖限定粉红泳装晨宝？C102的冠军又将花落谁家？"
    taotao "话不多说！让我们先有请决胜局第一位选手登场！"
    taotao "第一位选手的作品竟然是一部续作！两年前备受好评的《〔c100〕晨宝放课后的私房小秘密》在粉丝千呼万唤后竟然迎来了全新的续集！"
    taotao "掌声欢迎毕方选手和他的《〔c102〕禁忌！晨宝的体育器材室小秘密♡》！"
    bf "感谢大家一直以来的支持♡本次我为大家带来了全新的晨宝作品♡"
    bf "加入了我对晨宝的满满的幻想和爱喵♡"
    bf "想必大家都很想对晨宝这样那样吧♡"
    scene cg_p2_3
    bf "虽然晨宝的追求者众多，但晨宝唯独中意于青梅竹马的木头少年日落。"
    bf "直到有一天，黄毛毕方拿着一叠照片把晨宝堵在了无人的体育器材室内..."
    bf "...♡♡♡"
    "【欢呼声】"
    scene c102
    taotao "太...太色禽了！斯哈...晨宝...斯哈斯哈..."
    taotao "不愧是毕方选手！一如既往令人心动的ntr剧情！恶堕要素更是给本就魅惑十足的晨宝更添风味！绝赞！"
    taotao "那么另一位选手又将要给我们带来怎样的体验呢？"
    taotao "第二位选手是本次大赛的黑马！用他的原创作品击穿了无数读者的心！"
    taotao "有请六翼选手和他的《〔c102〕白色季节里♡温暖晨宝呓语》！"
    ly "我的作品里只有爱。"
    ly "只要晨宝幸福就好了。"
    scene cg_p2_4
    ly "仅仅是守望着他，看着那个孩子的笑脸，这样我就满足了。"
    ly "即使我知道，那样的笑颜永远不会对我绽放。"
    ly "我眼睁睁看着他在机场和别人接吻；"
    ly "我眼睁睁看着他在车内和别人拥抱；"
    ly "我眼睁睁看着他...和别人..."
    ly "...♡♡♡"
    "【欢呼声】"
    scene c102
    taotao "呜呜呜...眼泪，止不住...细腻的情感描绘催人泪下！切身体会了败者的酸楚呜呜呜呜呜呜..."
    taotao "同为ntr作品但仅仅是角度不同竟能产生如此之大的情感区分！支配晨宝的恶堕迷情和放手晨宝的守望纯情！实在是让人难以抉择！"
    taotao "但——亲爱的观众朋友们，你们必须做出选择！"
    taotao "请为自己喜欢的作品投上宝贵的一票，决定C102的胜利者吧！"

    jump label_p2_choice2

label label_tomato:
    scene tomato
    $ label_tomato_show = True

    "总是在城市内寻找灵感，偶尔来郊区看看不一样的风景，见见不一样的人，说不定能够让小生物灵光迸发。"
    "田地。"
    "一望无际的田地。"
    "像桌子一样的平顶山向来以出产高质量马铃薯闻名，平顶山土豆远销海外，广受好评，甚至某知名游戏厂商每年都会大批量在这里订购土豆。"
    "现在正是农闲时节，一眼望去田野空空落落，只有一个罐头人蹲在田坎侧边活动肩膀。"
    "一只大黄狗蹲在他的脚边一边懒散地甩甩尾巴，一边懒散地用鼻头拨弄田坎新草。"
    iron "老伙计，现在只有你和我了。"
    rock "汪！"
    "罐头人叹口气，摸了把黄狗的头。"
    iron "走啦，都走啦..."
    iron "小白把菜狗牵走了，铜宝也被妹妹带走了...就连嘴硬的绿皮兽人也有了自己的前辈..."
    iron "我们这儿啊，只有我和你这种老东西咯..."
    rock "汪呜——汪！"
    iron "以前好歹有冰蓝酱垫垫底，但她去年又被挂了路灯。"
    "回顾往昔，铁皮的眼眶不禁湿润起来。"
    iron "这下就咱俩就成了这儿被剩下的了。"
    rock "呜——"
    "黄狗低下头夹起尾巴。"
    iron "这平顶山土豆田也是，业绩一年比一年差。"
    iron "人全走光了...只剩跳也跳不动的老东西和天不怕地不怕的小崽子了。"
    iron "人少了，活没少，钱一点没多。"
    iron "过去好歹有点喘气的空档，现在...一年到头起早贪黑，身子骨都干垮了，兜里的子儿反倒是更少了。"
    rock "呜汪！"
    iron "年轻人也是一代不如一代。"
    iron "前两天有个穿盔甲的，说搞什么挑战极限，直接骑车从山上滚下去了。"
    iron "连最基础的防护都弄不懂，以后怎么适应西伯利亚的环境！"
    iron "真是没救了的下一代！"
    rock "汪汪——"
    zj "老哥，话可不兴这么说啊。"
    scene cg_p2_5
    "洛克一抬头，一满身肌肉的灰发男子正向自己露出闪耀的笑容。"
    zj "人生就是不断的相遇和分离，因为友人的离去感到寂寞是理所应当的事情。"
    zj "心灵被悲伤和失落填满，仿佛自己被抛弃了..."
    zj "这样的心情我也有过。"
    zj "心情可以理解，但话不能乱说，你不能从自己身上找找原因吗？"
    zj "依我看呐，老哥你是心态不行了。"
    zj "或许离开这里，开始一场新冒险调整下心态会是正确的选择。"
    "说到这里，男子的笑容更多了几分真诚。"
    zj "我倒是有个好去处。老哥有没有兴趣考虑下？"
    zj "我这有个公司在找人，朝九晚五双休有年假。转正月薪2w，需要去欧洲学习，实习期工资照发。坐飞机去，中转泰国。"
    zj "只要在这里签字摁手印，这份完美工作就是你的了。"
    zj "这么好的福利，这么好的前景，过了这个村就没这个店了！"
    zj "要不咱现在就签了？"

    jump label_p2_choice3

label p2_end:
    scene bridge_day
    "......"
    show sage_i at left
    sage "太阳渐渐落下，是时候返回桥洞教堂了。"
    hide sage_i
    "在漫长一天的冒险后，小生物打开背包，开始清点今天的收获。"
    if choice_p2_a1 and choice_p2_b1 and choice_p2_c1:
        "... ..."
        "... ..."
        "码农的友谊 x 1"
        "晨宝ntr恶堕本 x 1"
        "狗（？） x 1"
        show sage_i at left
        sage "今天见过的每个人，都面临着人生重要的抉择。"
        sage "而在他们的抉择中，他们都选择了听从自己的内心的声音。"
        sage "相信自己，并坚持下去。"
        hide sage_i
        "或许某天，听到自己内心中真正的声音的时候，小生物会蜕变为人类。"
        "... ..."
        scene bridge_day
        "第二天，附近的人们听说，桥洞教堂产生了一些改变。"
        "听说在那里，人们可以寻求内心的安稳。"
        "摈除杂音，听从自己的声音，安稳坚定地在人生道路上继续前行。"
        "虽然据说修女有一条过于护主的黄狗，预约系统时不时会因为能让程序正常运行的bug被修理了而宕机，以及对恶堕有些超乎寻常的喜好。"
        "但人们都会这样称赞她："
        "“是个拨开人内心迷雾，让人勇敢前进的好修女。”"
        "Thank you for playing."
        scene ed_p2_1
        "Normal Ending: 守护内心的修女"
        "点击返回主界面"
        return

    elif choice_p2_a2 and choice_p2_b2 and choice_p2_c2:
        "... ..."
        "... ..."
        "楠桐语录礼包码 x 1"
        "晨宝ntr纯爱（？）本 x 1"
        "招聘广告 x 1"
        show sage_i at left
        "今天见过的每个人，都面临着人生重要的抉择。"
        "而在他们的抉择中，比起自己的欲望，他们都发现了除此之外更重要的东西。"
        "这些更伟大的东西，把他们从孤独的自己中引出，与更多的人相连，与这个世界相连。"
        hide sage_i
        "或许某天，再找到了只属于自己的，绝对不可以放弃的东西的时候，小生物会和世界相连，变成一个真正的人类。"
        "... ..."
        scene bridge_day
        "第二天，附近的人们听说，桥洞教堂产生了一些改变。"
        "听说在那里，人们可以不仅是一座孤岛。"
        "不管是怎样的人，不管是怎样的思考，不管是怎样的痛苦，人类并不是孤独的。"
        "和更多的人，更广大的世界，更多的思想连接起来时，或许就能找到全新的道路。"
        "虽然据说修女有时会过于沉迷一款名为《楠桐语录》的手游，时常会因为打工不见人影，以及对纯爱本有些超乎寻常的喜好。"
        "但人们都会这样称赞她："
        "“是个开拓视野，让人与人连接起来的好修女。”"
        "Thank you for playing."
        scene ed_p2_2
        "Good Ending: 连接内心的修女"
        "点击返回主界面"
        return

    else:
        "... ..."
        "... ..."
        show sage_i at left
        sage "似乎自己还没有足够的觉悟。"
        sage "又或许是还没有搜集到足够多的东西。"
        hide sage_i
        "... ..."
        "小生物闭上眼，进入了梦乡。"
        show sage_i at left
        sage "（呢喃）或许，或许——"
        sage "（呢喃）在下一次的冒险中，会有不同的结局...？"
        hide sage_i
        "Thank you for playing."
        scene ed_p2_3
        "Bad Ending: 不知前路为何的修女"
        "... ..."
        "或许下定决心，选择一种立场会比较好。"
        "... ..."
        "点击返回主界面"
        return

label label_p2_choice1:
    scene supermarket

    menu:
        sage "小生物应该对程序员二人组说？"

        "支持二人删库私奔":
            $ choice_p2_a1 = True
            jump label_p2_a1
        "劝说二人加班修改":
            $ choice_p2_a2 = True
            jump label_p2_a2

label label_p2_choice2:
    scene c102

    menu:
        sage "小生物的心仪作品是？"

        "投票给《〔c102〕禁忌！晨宝的体育器材室小秘密♡》":
            $ choice_p2_b1 = True
            jump label_p2_b1
        "投票给《〔c102〕白色季节里♡温暖晨宝呓语》":
            $ choice_p2_b2 = True
            jump label_p2_b2

label label_p2_choice3:
    scene tomato

    menu:
        sage "是否要劝说铁皮换工作？"

        "劝说铁皮奔赴新未来":
            $ choice_p2_c1 = True
            jump label_p2_c1
        "劝说铁皮留守土豆田":
            $ choice_p2_c2 = True
            jump label_p2_c2

label label_p2_a1:
    scene supermarket
    show sage_i at left
    sage "有些东西是熄灭不了的。"
    sage "即便在寒冷的冬夜，爱意也依旧在熊熊燃烧。"
    sage "偶尔自私一下，也没问题吧？"
    sage "哪怕是这样的我们，也有获得幸福的权力吧？"
    hide sage_i
    shdocter "不，是我...我背叛了他。"
    shdocter "残酷的人是我...卑鄙的人是我。"
    haruki "明白这一点，还愿意做你的共犯的我，才是最卑鄙的。"
    scene cg_p2_2
    "即便如此，即便如此。"
    "两人都是一脸想哭的样子，混杂着开心和痛苦，却充满幸福。"
    haruki "请带我走吧。"
    haruki "哪里我都和你一起。"
    haruki "再也不要...和你分开了。"
    shdocter "...嗯。"
    shdocter "谢谢你让我们下定决心。"
    shdocter "如果需要帮助的话，请联系我。"
    haruki "也记得来参加我们的婚礼。"
    scene supermarket
    "两人对视一下，手牢牢地十指相扣。"
    "... ..."
    "【获得物品：码农的友谊 x 1】"
    "小生物捂着胃离开了超市。"
    show sage_i at left
    "看清自己的内心，被感情所裹挟或许不是自私，而是一种勇敢。"
    "或许这样的真诚和勇气是人类的必须品。"
    hide sage_i
    if label_supermarket_show and label_c102_show and label_tomato_show:
        jump p2_end
    else:
        jump label_p2_choice_label

label label_p2_a2:
    scene supermarket
    show sage_i at left
    sage "或许比起自己的恋情，还有更重要的东西。"
    sage "多年的友谊，以及大家心血楠桐语录的未来。"
    sage "怎样的纠结与苦涩，在时间的磨砺下，终有一日也会开出幸福的花。"
    hide sage_i
    haruki "是的，他是我最好的朋友。"
    haruki "他对我亲口说过，他没有你活不下去。"
    haruki "你要我背叛他吗？"
    haruki "你要逃避，要以他的不幸作为代价吗？"
    haruki "哪怕你逃跑了，你也能心安理得地度过自己的余生吗。"
    shdocter "...你是对的。"
    "两人的眼神坚定起来，各自抓起几大瓶力保健放进购物车。"
    shdocter "修点算点吧。"
    shdocter "没有bug的程序是不存在的；如果有，那一定死了不止一个程序员。 "
    haruki "如果有，那我也不输出错误日志，不输出就没有问题。"
    haruki "谢谢你让我们下定决心。"
    haruki "明天我们的游戏就发售了，记得来玩。"
    "【获得物品：楠桐语录礼包码 x 1】"
    "小生物捂着胃离开了超市。"
    show sage_i at left
    sage "在自己的情感外，责任或许更加重要。"
    sage "事业、友谊，以及其他的东西会支持你的人生。"
    hide sage_i

    if label_supermarket_show and label_c102_show and label_tomato_show:
        jump p2_end
    else:
        jump label_p2_choice_label

label label_p2_b1:
    scene c102
    show sage_i at left
    sage "创作应当忠于自己。"
    sage "既然是自己的创作，那么当然要展示自己的欲望。"
    sage "如果连作者的欲望都无法满足，作者自身的热情都无法体现，作品怎么可能感动他人呢？"
    hide sage_i
    "投票结束，主持人重返舞台。"
    taotao "两位的作品都非常优秀，实在是让人难以割舍..."
    taotao "但比赛就是比赛，是时候宣布本次的胜利者了！"
    taotao "本届C102的冠军是——"
    taotao "瑟中之瑟，恶堕中的恶堕，将作者xp体现地淋漓尽致，大胆表达对晨宝的幻想妄想创想——"
    scene cg_p2_3
    taotao "来自毕方的《〔c102〕禁忌！晨宝的体育器材室小秘密♡》！"
    "【欢呼声】"
    bf "哇♡非常感谢大家♡"
    bf "一个不懂恶堕晨宝妙处的人是品味低下的，只能度过一个相对失败的人生♡"
    bf "我会坚持不懈地继续在作品里狠狠疼爱晨宝的♡"
    bf "今后也请大家继续支持梦色晨宝系列♡"
    bf "人家已经在筹备新作了♡"
    bf "新作还将加入新角色同级生鸽子王♡更有前辈登场♡"
    bf "更加蜿蜒曲折，暧昧背德的全新故事♡敬请期待♡"
    scene c102
    "... ..."
    "【获得物品：晨宝ntr恶堕本 x 1】"
    "小生物满意地抱着毕方老师的签名本离开了会场。"
    show sage_i at left
    sage "自己的欲望非常重要。"
    sage "爱自己，诚实地面对自己，这或许是小生物在成为人的道路上的必须学会的第一课。"
    hide sage_i

    if label_supermarket_show and label_c102_show and label_tomato_show:
        jump p2_end
    else:
        jump label_p2_choice_label

label label_p2_b2:
    scene c102
    show sage_i at left
    sage "欲望非常重要，自我满足相当美好。"
    sage "但爱不止于此。"
    sage "从利己走向利他，爱不仅是对晨宝这样那样，爱也是尊重、放手，与守望。"
    hide sage_i
    "投票结束，主持人重返舞台。"
    taotao "两位的作品都非常优秀，实在是让人难以割舍..."
    taotao "但比赛就是比赛，是时候宣布本次的胜利者了！"
    taotao "本届C102的冠军是——"
    scene cg_p2_4
    taotao "温和的笔触下埋藏着火热的内心，NTR但不失纯情，情色却不掩悲伤，创作出如初冬一般冷峻，但却直击人心的故事的——"
    taotao "六翼！"
    "【欢呼声】"
    ly "谢谢，谢谢大家。"
    ly "对晨宝的爱能够被大家所认可...我很开心。"
    ly "尽管是在本子里中，是在妄想中"
    ly "我都期盼着他能够获得幸福。"
    ly "单相思让我心酸、苦楚和落寞，但我从来没有后悔过。"
    ly "守望晨宝的笑容...守望晨宝被撅撅，我的内心生出的满足感远大于这份痛苦。"
    ly "——这就是我对晨宝的爱。"
    scene c102
    "... ..."
    "【获得物品：晨宝ntr纯爱（？）本 x 1】"
    "小生物满意地抱着六翼老师的签名本离开了会场。"
    show sage_i at left
    sage "爱的对象不仅仅局限于自己。"
    sage "人可以选择成为一座孤岛，但在去爱别人，去看世界，去与人的连接的过程中，或许人可以获得更多的东西。"
    hide sage_i

    if label_supermarket_show and label_c102_show and label_tomato_show:
        jump p2_end
    else:
        jump label_p2_choice_label

label label_p2_c1:
    scene tomato
    show sage_i at left
    sage "世界上唯一不变的真理是“一切都会改变”。"
    sage "树挪死，人挪活，该挪挪脚了。"
    hide sage_i
    iron "你说的对，这样的机会的确不该错过。"
    iron "老头子我种了大半辈子的土豆，也该看看服务器之外的东西了。"
    iron "现在，是时候为了自己而活下去了吧。"
    iron "谢谢兄弟，那我们签了吧。"
    zj "好！我一看兄弟你就是个干脆人！"
    iron "只是...我还有一件事情放心不下。"
    iron "我走了之后我的老伙计洛克可该怎么办呀。"
    rock "汪？"
    iron "这样吧，好心的旅行者，我就把洛克托付给你了。"
    iron "他是个忠心的家伙，一定能好好保护你的。"
    "... ..."
    "【获得物品：狗（？） x 1】"
    "小生物若有所思地牵着洛克离开了土豆田。"
    show sage_i at left
    "听从自己内心的声音，告别常态，迈出崭新一步。"
    "或许成为人类，就意味着先了解自己。"
    hide sage_i

    if label_supermarket_show and label_c102_show and label_tomato_show:
        jump p2_end
    else:
        jump label_p2_choice_label

label label_p2_c2:
    scene tomato
    show sage_i at left
    sage "人不吃，就会死。"
    sage "所以铁皮啊，你在生产粮食，你的工作非常伟大，你在做一件很有意义的事情。"
    sage "每天十四小时工作制怎么了？又累又饿怎么了？"
    sage "没有你的平顶山土豆，国家和社会就将不复存在！"
    sage "你为大家吃点苦怎么了怎么了怎么了？	"
    "铁皮低头挠挠黄狗的头，露出了一个释然的笑容。"
    hide sage_i
    iron "谢谢兄弟，但是不了，我想我还是喜欢这里。"
    zj "啧，固执的老东西。"
    zj "哎这位朋友，你要不要来公司？"
    zj "来来来，这份资料你拿着，什么细节都在上面，多看看多考虑考虑。"

    "【获得物品：招聘广告 x 1】"
    "小生物若有所思地拿着传单离开了土豆田。"
    show sage_i at left
    sage "让人忍受数年如一日服务器的，是比那更高的理想，比痛苦日常更需要关注的东西。"
    sage "或许人类就是这样活下去的。"
    hide sage_i

    if label_supermarket_show and label_c102_show and label_tomato_show:
        jump p2_end
    else:
        jump label_p2_choice_label

label label_p2_choice_label:
    scene bridge_day
    "......"
    "......"

    menu:
        sage "要去哪里调查呢？"

        "圣诞超市" if not label_supermarket_show:
            jump label_supermarket

        "C102同人展" if not label_c102_show:
            jump label_c102

        "平顶山土豆田" if not label_tomato_show:
            jump label_tomato