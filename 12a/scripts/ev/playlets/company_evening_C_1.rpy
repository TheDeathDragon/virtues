label company_evening_C_1:

    scene company_evening_c_1_1 with tstmgr

    c "... ... ... ..."



    "其他人都回家了,狄奥多拉还在工作."



    scene company_evening_c_1_2 with tstmgr

    c "Hmm?你怎么还在这?"



    player "我............"



    c "算了,既然你来了,为什么不跟我一起做些额外的工作呢?"



    player "我能得到额外的报酬吗?"



    scene company_evening_c_1_3 with tstmgr

    c "No."



    player "... ... ... ..."



    player "好吧......"



    $ add(C, C.love, 1)



    $ P.cash.add(500)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
