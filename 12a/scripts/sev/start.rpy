label start:
    scene void with Dissolve(0.4)

    window show
    "你叫什么名字?"
    window hide

    $ P_state.name = "御坂" if renpy.variant("pc") else "Leo"
    call screen name_input(prompt=_(""), prefix="我叫", suffix=".")

    $ hotel_room_rent = Attr(500.0, name=_("租金"))
    $ P.ie_suffix = _("/Day")
    $ P.ie_short_suffix = _("/D")
    $ P.expanses.append(hotel_room_rent)



    menu:
        "从头开始" if True:
            $ run_event('d1_1')
        "跳过序章" if True:

            $ fake_run('d4_1_bLine', 'd4_4_bLine', 'd5_2_bLine', 'd5_4_bLine')
            $ fake_run('d4_3', 'A_dgsjhx', 'd8_1', 'A_daily_1',
                    'A_swdgsj', 'd5_3', 'B_love_1', 'd7_1', 'd1_1', 'D_dqsj', 'd3_1', 'A_wsdgsj',
                    'A_wsdgsjhx', 'd6_1', 'A_love_1', 'A_xwdgsj', 'd2_1', 'd2_5',
                    'pcsj', 'pcsjhx', 'bjsj', 'sbsj', 'jjsj'
                )
            $ bLine = True
            $ B_gift, D_gift = True, True

            $ A.love.meter.value = 5.0
            $ B.love.meter.value = 5.0

            $ P.cash.value = 0
            $ P.virtue.value = 49

            $ set_time(Time(week=8, day=Monday, period=Morning))

            $ _on_event_complete()

    $ set_scene("Map")
    $ show_map()
    jump pauser
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
