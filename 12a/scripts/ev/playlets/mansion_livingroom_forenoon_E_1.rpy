label mansion_livingroom_forenoon_E_1:

    scene void with tstmgr

    "早上我来到了伊莉莎阿姨的家."



    scene e_mansion_inside_smile with tstmgr

    e "Hi,[P].你怎么在这里?"



    player "Eh,hi,伊莉莎阿姨.你有我爸爸的消息吗?"



    player "你知道,我有点担心."



    scene e_mansion_inside_frown with tstmgr

    e "Oh,[P].我理解你的感受."



    e "很抱歉,我现在没有什么好消息要告诉你."



    scene e_mansion_inside_smile with tstmgr

    e "但是相信我,你爸爸很好.他很快就会获准保释."



    e "现在,既然你来了,也许你愿意和我一起吃早餐?"



    player "我很乐意,伊莉莎阿姨."



    scene void with tstmgr

    "... ... ... ..."



    $ add(E, E.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
