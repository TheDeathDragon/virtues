label E_daily_10:

    scene void with tstmgr
    play music happy

    "今天早上我去了医院..."



    scene e_daily10_1 with tstmgr

    player "康妮医生,你必须救我的命!我想我得了脑癌!"



    "这位可爱的大个子女士是康妮医生,一位很棒的医生,在她的领域非常专业."



    scene e_daily10_2 with tstmgr

    "康妮医生""Wow...不要惊慌,[P].详细地向我描述你的问题."



    player "最近我总是在晚饭后昏过去,一直睡到第二天早上."



    player "而且,我醒来后会很累..."



    "康妮医生""这很奇怪.Okay,让我们做一些测试,给你的大脑拍个片子."



    scene void with tstmgr

    "... ... ... ..."



    "一段时间后..."



    scene e_daily10_1 with dissolve

    "康妮医生""有个好消息告诉你,[P].你非常健康.你的大脑没有问题."



    player "你百分百确定吗?"



    "康妮医生""Yeah.我做了几次检查,没有发现任何异常."



    player "这就奇怪了.那你怎么解释我的问题呢?"



    scene e_daily10_2 with tstmgr

    "康妮医生""我...不要真的认为那是你大脑的故障造成的."



    "康妮医生""也许是因为某种药物?你知道,嗜睡和头晕可能是许多药物的副作用."



    "康妮医生""你说过你只会在一天的特定时段昏倒."



    player "但是...我没有服用任何药物......"



    player "... ... ... ..."



    player "不管怎样,知道我还健康是件好事.谢谢你,康妮医生.如果事情变得更糟,我会再来找你."



    scene e_daily10_1 with tstmgr

    "康妮医生""祝你好运,[P]."



    scene void with tstmgr

    "Okay,如果不是我的大脑的问题,那么一定是其他什么东西导致了我的问题.我要查出是什么."



    "Hmmm... ... ... ..."



    "我之后会想出一个计划的.现在,我需要去伊莉莎阿姨家辅导艾琳."



    "等待...等等...伊莉莎阿姨的房子?"



    "看来我只有在伊莉莎家的时候才会出现这个问题."



    "是因为我在那儿吃的东西吗?或者是某种过敏反应?"



    player "... ... ... ..."



    "这太奇怪了..."



    $ add(E, E.love, 1)

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
