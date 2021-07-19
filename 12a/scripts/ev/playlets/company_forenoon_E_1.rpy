label company_forenoon_E_1:

    scene company_forenoon_e_1_1 with tstmgr

    c "妈妈?你怎么在这?"



    e "只是想看看你和[P]."



    "Wow,他们看起来像姐妹而不是母女."



    scene company_forenoon_e_1_2 with tstmgr

    e "工作怎么样,[P]?"



    player "Eh,我感觉很好.谢谢你的关心,伊莉莎阿姨."



    e "很高兴知道这个."



    scene void with tstmgr

    "... ... ... ..."



    $ add(E, E.love, 1)



    $ P.cash.add(500)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
