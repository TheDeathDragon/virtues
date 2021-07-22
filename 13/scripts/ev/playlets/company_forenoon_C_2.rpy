label company_forenoon_C_2:

    scene company_afternoon_c_1_1 with tstmgr

    c "[P],把这些档案填好,拿到我的办公室来."



    player "Eh,okay,经理,我马上就去做."



    c "... ... ... ..."



    player "Eh......还有什么吗?"



    c "No,没什么.继续工作吧."



    scene void with tstmgr

    player "... ... ... ..."



    $ add(C, C.love, 1)



    $ P.cash.add(500)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
