label mansion_bathroom_evening_E_1:

    scene void with tstmgr

    "伊莉莎阿姨在浴室里叫我."



    scene mansion_bathroom_evening_e_1_1 with tstmgr

    e "[P],请把我的毛巾拿来好吗?它在门把手上."



    player "Eh,当然,伊莉莎阿姨."



    e "谢谢,[P].你真贴心."



    scene mansion_bathroom_evening_e_1_2 with tstmgr

    e "你想来浴缸加入我吗?"



    player "什么?我............"



    e "放松点,我只是开个玩笑."



    player "... ... ... ..."



    $ add(E, E.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
