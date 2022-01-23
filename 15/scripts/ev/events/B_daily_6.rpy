label B_daily_6:

    scene school_day_background with tstmgr
    play music happy

    narrator "我在校园里遇到了森柠."

    player "Hi,森柠."

    scene b_school_day_normal with tstmgr

    b "Oh, hi, [P]. "

    player "Eh,你手里拿的是什么?"

    narrator "我注意到她拿着一张传单."

    scene b_school_day_frown with tstmgr

    b "这是一个...广告传单."

    scene b_school_day_smile with tstmgr

    b "我在考虑找一份兼职工作.我看到这家书店正在招聘店员..."

    b "我想我会试一试."

    player "你为什么要这么做?你父母也进了监狱吗?"

    scene b_school_day_unhappy with tstmgr

    b "... ... ... ..."

    b "这不好笑."

    player "抱歉,森,我的错."

    player "但说实话,你为什么想要一份兼职工作?"

    scene b_school_day_smile with tstmgr

    b "我认为这是一种拥抱你的文化的好方法,不是吗?"

    b "同时我可以得到一些宝贵的工作经验."

    player "我明白了..."

    b "而且,我看到你工作做得很好.它激励着我."

    player "Wow,谢谢你这样说."

    player "所以...你什么时候去那家书店面试?"

    scene b_school_day_frown with tstmgr

    b "我不知道.准备好了他们会打电话给我."

    player "Okay,你去面试前一定要通知我.我和你一起去."

    scene b_school_day_normal with tstmgr

    b "你为什么想和我一起去?"

    player "...确保你的安全?"

    b "... ... ... ..."

    scene b_school_day_smile with tstmgr

    b "舒服..."

    b "好吧,有消息我会告诉你的.谢谢你为我担心."

    player "不用客气,森,我们是好朋友吧?我们就应该这样."

    scene b_school_day_frown with tstmgr

    b "... ... ... ... "

    b "是的,我们是."

    scene void with tstmgr

    narrator "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
