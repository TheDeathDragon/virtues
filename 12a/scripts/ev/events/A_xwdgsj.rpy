label A_xwdgsj:

    scene void with tstmgr

    narrator "据杰克说,薇拉每天下午在一家服装店工作.也许我能在那儿碰到她.那将是改善我们关系的好办法."

    narrator "... ... ... ..."

    scene dressstore_background with tstmgr

    narrator "我下午去了那家服装店."

    narrator "Hmm...这个地方看起来很不错.如果薇拉真的在这里工作,她可能会得到一份公平的工资."

    narrator "我很快就找到了薇拉.她的脸蛋和身材使她在店里很显眼."

    scene a_dressstore_unhappy with tstmgr

    narrator "Wow,漂亮的制服."

    player "薇拉?好巧啊.你在这儿工作吗??"

    a "... ... ... ..."

    a "Yes,我每天下午都在这个地方工作."

    a "... ... ... ..."

    a "你怎么来了?我们只卖女装."

    player "Oh...关于这个..."

    a "你在跟踪我吗?"

    player "什么?不,天哪,你怎么会这么想?"

    player "我只是想...给我阿姨买个礼物."

    scene a_dressstore_frown with tstmgr

    a "阿姨?"

    player "Yes,我可以让你看看她的照片."

    a "没有必要这样做..."

    a "所以...你想买什么?"

    player "我还不知道.我只是随便看看."

    a "Oh... Okay..."

    a "... ... ... ..."

    player "... ... ... ..."

    narrator "作为一名销售人员,她应该一直与客人交谈.但是她现在肯定没有心情和我说话."

    narrator "太尴尬了."

    player "Eh... Well..."

    player "时间不早了,你一定要下班了吧?我想请你吃晚饭."

    scene a_dressstore_weird with tstmgr

    a "晚饭?"

    scene a_dressstore_frown with tstmgr

    a "谢谢你,但是不用了."

    a "这些天下班后我宁愿直接回家."

    player "我理解."

    a "抱歉."

    player "那我开车送你回家吧."

    scene a_dressstore_weird with tstmgr

    a "... ... ... ..."

    a "你为什么......"

    scene a_dressstore_smile3 with tstmgr

    a "好吧.谢谢你的好意."

    player "棒!"

    narrator "... ... ... ..."

    narrator "之后,我开车送她回家.我们在路上聊了会.我有一种感觉,我们之间的关系正在好转."


    $ add(A, A.love, 1)

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
