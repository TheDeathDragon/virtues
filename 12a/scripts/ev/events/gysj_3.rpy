label gysj_3:

    scene park_night_background with tstmgr

    narrator "晚饭后我去公园散步."

    narrator "这是如此安静和黑暗.老实说,我开始后悔了.这个地方晚上很恐怖."

    player "Hmm?... ... ... ..."

    narrator "我听到有些说话声."

    narrator "... ... ... ..."

    "女人""哦,主人,我再也爬不动了.我太累了."

    "男人""操,你这条懒狗,把你的屁股翘起来!你需要受到惩罚."

    "女人""Ah...主人,惩罚我,请把你的大鸡儿放到我肮脏的小穴里."

    "男人""(拍打女人的屁股)你只是条狗.狗应该怎么叫呢?"

    "女人""(呻吟)Arf,arf,woof...Ah...用力,用力,拜托...Woof,woof..."

    narrator "... ... ... ..."

    player "Eh... ... ... ..."

    player "那是什么鬼东西..."

    player "听起来像是某种奇怪的角色扮演游戏."

    label gysj_3_choices:

    menu:
        "悄然离去":


            player "我不想看到这个,这侵犯了别人的隐私..."

            player "这太令人毛骨悚然了.我该回家了."
        "偷看":

            if P.virtue < 30:
                $ not_implemented_message()
                jump gysj_3_choices
            else:
                "(美德需要小于30)"

                narrator "你可以期待它在未来的更新."

                jump gysj_3_choices

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
