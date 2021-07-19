label weekend_plan_tutorial:
    $ show_map()
    $ UI.show()
    $ weekend_button_displaying = True
    call screen tutorial(5, 5) with Dissolve(0.5)
    jump event_post

label reset_days_worked:
    $ days_worked = 0
    jump event_post

label pay_room:
    $ P.pay(P.expanses[0].value, P.expanses[0].name)
    jump event_post




default bLine = True

label post_d1_1:
    $ show_map()
    call screen hint("现在游戏正式开始.享受你的人生!")
    call screen tutorial(2, 4) with Dissolve(0.5)
    jump post_event_post

label post_jjsj:


    $ P.ie_suffix = _("/Week")
    $ P.ie_short_suffix = ("/Wk")



    $ P.cash._value = 0.0

    $ show_map()
    call screen bigclock

    jump post_event_post

default G_MoveIn_Room_Change = False
label post_G_MoveIn:
    if seen("G_MoveIn") and not G_MoveIn_Room_Change:
        $ G_MoveIn_Room_Change = True
        $ store.player_rooms["basic_room"] -= 1
    jump post_event_post

label post_F_daily_1:
    $ exercise.add_count_of_day()
    jump post_event_post
label post_F_daily_2:
    $ exercise.add_count_of_day()
    jump post_event_post
label post_F_love_2:
    $ exercise.add_count_of_day()
    jump post_event_post

label post_C_daily_13:
    call screen hint("现在你可以在房子里建游泳池了.你要几次才能把它建好.每次花费$200.")
    jump post_event_post

label post_A_daily_5:
    call screen hint("现在你可以打扫你的房子了,这样做你会得到一些小费,甚至也许你会发现...房子的秘密.")
    jump post_event_post




label auto_sleep_prologue:
    scene void with Dissolve(0.5)
    window show wipeup(.2)
    "天晚了,我该去睡觉了."
    window hide wipedown(.2)
    menu:
        "上床睡觉":

            pass
    jump event_post

label auto_sleep:
    scene void with Dissolve(0.3)
    window show wipeup(.2)
    "天晚了,我该去睡觉了."
    window hide wipedown(.2)

    $ show_home()
    jump event_post

label sleep_event:
    if t.period < LateNight:
        "现在睡觉太早了."
    else:

        $ new_day()
    jump label_post


label pay_bill:



    $ P.cash._value -= 1500

    if P.cash._value < 0:
        $ P.cash._value = 0

    $ Push("你支付了$1500土地税和维护费用")

    jump event_post

label wage:
    $ temp_wage = days_worked * 50 * (0.85 + 0.15*C.love.stage)
    if temp_wage > 0:
        "收入到账."
        $ P.earn( temp_wage, "工资", t )
    jump event_post

label earn:
    $ P.earn(get_bnb_revenue(), "民宿")
    jump event_post


label w2_d6_1_hint:
    call screen hint("现在周末没什么可做的,因为你还没有和任何女孩建立起亲密的关系.你可以点击右上角,然后跳过这个周末.")
    jump event_post





label first_company:
    "这家公司是狄奥多拉家族的.我不知道我为什么在这里."
    return

label E_inspect_work:
    scene void with tstmgr
    narrator "... ... ... ..."
    narrator "我上班的时候,伊莉莎阿姨进来了,远远地看着我."
    scene e_office_smile with tstmgr
    e "(他工作很努力...)"
    e "(我能看出他的女同事们是多么崇拜他.他真是个迷人的年轻人.)"
    $ add(E, E.love, 1)
    return

label E_inspect_tutor:
    scene void with tstmgr
    narrator "... ... ... ..."
    narrator "当我在辅导艾琳的时候,伊莉莎阿姨轻轻地打开了门,往里面看了看."
    scene e_droom_smile with tstmgr
    e "([P]教艾琳教得好像很好.)"
    e "(他很有耐心,也很温柔,就像他爸爸以前的样子.)"
    $ add(E, E.love, 1)
    return

label first_lose_credit_sj:

    "... ... ... ..."

    narrator "现在我遇到了一个严重的问题..."

    narrator "我没有足够的钱支付本周的账单."

    narrator "现在还不是什么大问题,因为我可以向我的有钱朋友借钱.我甚至不需要偿还.这对他们来说只是一笔小钱,没什么大不了的."

    narrator "但我不能一直这么做.如果我太依赖朋友的帮助,我的信誉和声誉都会下降.没有我父亲的财富,人们会认为我是个彻底的失败者."

    narrator "那不是我想要的."

    narrator "我必须更加努力才能独自解决这个财务问题.让我们看看下周的进展如何."

    jump event_post

label lose_credit_sj:

    "... ... ... ..."

    "我没有足够的钱支付本周的账单."

    "现在还不是什么大问题,因为我可以向我的有钱朋友借钱.我甚至不需要偿还.这对他们来说只是一笔小钱,没什么大不了的."

    "但我不能一直这么做.如果我太依赖朋友的帮助,我的信誉和声誉都会下降.没有我父亲的财富,人们会认为我是个彻底的失败者."

    "那不是我想要的."

    "我必须更加努力才能独自解决这个财务问题.让我们看看下周的进展如何."

    jump event_post



label reset_shop:
    $ fortunetelling_today = False
    $ cleansing_today = False
    $ blessing_today = False
    $ hotel_shop_chat_today = False
    $ satisfy_her_need_today = False
    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
