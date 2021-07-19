label gysj_night:

    scene park_night_background with tstmgr

    narrator "为什么我晚上还在这里?我在期待什么?"

    narrator "我上次来这里的时候,听到了一些令人毛骨悚然的声音.嗯,我不得不说,这是非常难忘的."

    narrator "我还会听到那些声音吗?"

    "女人""(呻吟)Arf,arf,arf...Ah,主人..."

    "男人""大声点,婊子,大声点!"

    player "... ... ... ..."

    player "这一定是在开玩笑."

    label gysj_night_choices:

    menu:
        "回家":

            player "我不想看到这个."

            player "太恐怖了.我该回家了."
        "偷看":


            narrator "(美德需要小于30)"

            narrator "你可以期待它在未来的更新."
    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
