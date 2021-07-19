label company_afternoon_C_1:

    scene company_afternoon_c_1_1 with tstmgr

    c "[P]."



    c "... ... ... ..."



    scene company_afternoon_c_1_2 with tstmgr

    c "[P]!"



    player "(突然惊醒)怎么了?发生了什么?"



    player "Oh... ... ... ..."



    player "对不起,我知道我不应该在工作时打盹.我太累了."



    scene company_afternoon_c_1_1 with tstmgr

    c "... ... ... ..."



    c "这次我饶了你.继续工作."



    scene void with tstmgr

    "... ... ... ..."



    $ add(C, C.love, 1)



    $ P.cash.add(500)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
