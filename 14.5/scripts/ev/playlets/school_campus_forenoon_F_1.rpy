label school_campus_forenoon_F_1:

    scene void with tstmgr

    "我和瑞秋在校园里闲逛."



    scene school_day_background with tstmgr

    player "你最喜欢的电影是什么?"



    scene f_school_day_frown with tstmgr

    f "Hmm?我从来没想过这个.为什么这么问?"



    player "只是想更多地了解你."



    scene f_school_day_wink with tstmgr

    f "Oh,yeah,我们是朋友."



    scene f_school_day_frown with tstmgr

    f "但是...我想我没有最喜欢的电影.对不起."



    scene f_school_day_wink with tstmgr

    f "如果你愿意,我可以告诉你我最喜欢的油管健身博主."



    player "Oh, eh... ..."



    player "Okay,我想......"



    $ add(F, F.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
