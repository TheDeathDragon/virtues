label B_daily_3:

    scene class_background with tstmgr
    play music happy

    narrator "... ... ... ..."

    narrator "后来,在一节课上..."

    scene b_class_normal with tstmgr

    b "你最近怎么样?你告诉我你已经找了两份工作了.一切都好吗?"

    player "Eh,yeah,一切似乎都好."

    player "事实上,除了这两份工作,我现在也开始了自己的事业."

    scene b_class_surprise with tstmgr

    b "自己的事业吗?这是什么意思?"

    narrator "我现在应该告诉她关于民宿的事情吗?"

    narrator "... ... ... ..."

    narrator "没关系,等我确定生意做对了再告诉她."

    player "我想暂时保密,因为这个业务还处于初期阶段.我不确定它能走多远.你不需要知道,因为我可能随时关闭它."

    scene b_class_normal with tstmgr

    b "... ... ... ..."

    scene b_class_smile with tstmgr

    b "好吧.如果你现在不想告诉我也没关系."

    b "如果有什么我能帮忙的,请告诉我.我真的想为你做点什么."

    player "我很感激,森,有你这样的朋友是我的幸运.事实上,我确实需要你帮个忙."

    b "说吧,是什么."

    player "谢谢你."

    player "嗯,你看,我可能没有以前那么多时间花在学习上了."

    scene b_class_normal with tstmgr

    b "我理解.你将来肯定会有很多事业上的事情要担心."

    player "所以如果我碰巧错过了一两节课,你能帮我复习功课吗?"

    scene b_class_smile with tstmgr

    b "当然,没问题.你不用说我也会的."

    player "谢谢你,森柠."

    b "顺便说一下,[P.name],你有地方住吗?我知道在这一切发生之前你住过酒店,但现在你再也负担不起了?"

    player "是的,我已经搬出去了.别担心,我爸爸在遇到麻烦之前给我在这个城市留了一所房子.现在我住在那个地方."

    b "很高兴听到这个."

    scene class_background with tstmgr

    narrator "教授这时走进了教室."

    "基斯教授""同学们,最近怎么样?我们开始前做个突击测验吧."

    narrator "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
