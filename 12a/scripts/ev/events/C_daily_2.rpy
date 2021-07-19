label C_daily_2:

    scene rcsj_c1 with tstmgr
    play music happy

    player "经理,有个文件需要你签字."

    c "把它放在桌子上.我待会签."

    player "好的."

    scene rcsj_c2 with tstmgr

    c "等一下,先别走."

    player "怎么了?"

    scene rcsj_c3 with tstmgr

    c "给我来杯咖啡,半糖,三倍奶油."

    player "... ... ... ..."

    c "你还在等什么?"

    player "... ... ... ..."

    scene rcsj_c5 with tstmgr

    c "[P.name]?"

    player "(突然惊醒)Oh,我马上给你拿来."

    player "... ... ... ..."

    c "... ... ... ..."

    player "老实说,我还是不习惯听你的命令."

    scene rcsj_c4 with tstmgr

    c "我知道这对你来说是一个艰难的改变.赶紧的."

    c "我还在等咖啡呢."

    player "Oh,当然,我...我马上回来..."

    c "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
