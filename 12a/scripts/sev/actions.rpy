init python:
    Action.current_parent = None
    none_action = Action("none", "")

    Action.current_parent = None
    map_action = Action("map", _("Map"), has_children=True)

    Action.current_parent = "map"
    hotel = Action("hotel", _("酒店"), has_children=True, pos=(1480, 230), displaying="not seen('pcsj') or seen('B_daily_18')")
    my_room_in_hotel = Action("my_room_in_hotel", _("我的房间"), "not seen('pcsj')")
    hotel_shop = Action("hotel_shop", _("商店"), "seen('B_daily_18')")

    Action.current_parent = "map"
    park = Action("park", _("公园"), has_children=True, pos=(1614, 713-60))
    hang_park = Action("hang_park", _("散步"), "seen('d8_1')")
    exercise = Action("exercise", _("锻炼"), "seen('gysj_4') and is_day()")




    Action.current_parent = None
    college = Action("college", _("学校"), has_children=True)

    Action.current_parent = "college"
    college_facilities = Action("college_facilities", _("大学设施"), has_children=True, pos=(522, 432))
    campus = Action("campus", _("校园"), "is_day()")
    library = Action("library", _("图书馆"))

    Action.current_parent = "college"
    apartment = Action("apartment", _("学生公寓"), has_children=True, pos=(522, 432))
    B_room = Action("B_room", _("找森柠"), "t.period in (Forenoon, Afternoon)", displaying="seen('B_love_1')", to_map=False, training_nz="B")
    F_room = Action("F_room", _("找瑞秋"), "is_day()", displaying="seen('F_love_2')", to_map=False, training_nz="F")
    college_bathroom = Action("college_bathroom", _("女生公共浴室"))

    Action.current_parent = "college"
    college_action = Action("college_action", "", has_children=True)
    course = Action("course", _("去上课"), "t.period in (Forenoon, Afternoon) and t.day not in (Saturday, Sunday)")




    Action.current_parent = None
    mansion = Action("mansion", _("别墅"), has_children=True)

    Action.current_parent = "mansion"
    mansion_rooms = Action("mansion_rooms", _("伊莉莎的家"), displaying="seen('d7_1')", has_children=True, rename=[("伊莉莎的家", "seen('D_dqsj')")], pos=(950, 485))
    C_room = Action("C_room", _("狄奥多拉的房间"), "t.period in (Forenoon, Afternoon, Evening, LateNight)", displaying="seen('pcsj')")
    D_room = Action("D_room", _("找艾琳"), "t.period in (Afternoon, Evening)", to_map=False, training_nz="D")
    E_room = Action("E_room", _("找伊莉莎"), "t.period in (Forenoon, Afternoon, Evening)", displaying="seen('pcsj', 'D_dqsj')", to_map=False, training_nz="E")
    mansion_pool = Action("mansion_pool", _("游泳池"))
    mansion_bathroom = Action("mansion_bathroom", _("浴室"))
    mansion_toilet = Action("mansion_toilet", _("厕所"), xysize=(135, 124))
    mansion_livingroom = Action("mansion_livingroom", _("客厅"))
    mansion_guestroom = Action("mansion_guestroom", _("客房"))

    Action.current_parent = "mansion"
    mansion_action = Action("mansion_action", "", has_children=True)
    tutor = Action("tutor", _("辅导"), "t.period in (Afternoon, Evening) and tutor.count_of_day < 1", displaying="seen('pcsj')")




    Action.current_parent = "map"
    company = Action("company", _("新光大厦"), has_children=True, pos=(676, 378-60))
    work = Action("work", _("工作"), "seen('pcsj') and t.period in (Forenoon, Afternoon) and Monday <= t.day <= Friday"),
    find_C_company = Action("find_C_company", _("找狄奥多拉"), "seen('pcsj') and t.period in (Forenoon, Afternoon) and Monday <= t.day <= Friday", to_map=False, training_nz="C")

    Action.current_parent = "map"
    find_A_restaurant = Action("find_A_restaurant", _("餐厅"), "t.period is Evening and Monday<=t.day<=Saturday and seen('A_wsdgsj')", pos=(500, 713-60))

    Action.current_parent = "map"
    find_A_cafe = Action("find_A_cafe", _("咖啡馆"), "t.period is Forenoon and Monday <= t.day <= Saturday and seen('d6_1')", pos=(1436, 500-60))


    Action.current_parent = "map"
    bookstore = Action("bookstore", _("书店"), "seen('G_MoveIn') and t.period is Afternoon", pos=(698, 604-60))


    Action.current_parent = "map"
    downtown = Action("downtown", _("商业街"), pos=(1569, 387-60), has_children=True)
    Action("street", _("街道"), "seen('d8_1')")
    Action("shop", _("波西亚的商店"), displaying="seen('store_1_cj')")

    Action.current_parent = "map"
    find_A_clothing = Action("find_A_clothing", _("服装店"), "t.period is Afternoon and Monday <= t.day <= Saturday and seen('d8_1')", pos=(257, 811-60))

    alley = Action("alley", _("黑暗的小巷"), "t.period in (Evening, LateNight)", pos=(257, 600-60))

    Action('beach', _('海滩'), "t.period in (Forenoon, Afternoon)", pos=(590, 187))

    Action('bungalow', _('平房'), displaying="seen('E_daily_13')", pos=(196, 325-60))


    Action.current_parent = None
    bnb = Action("bnb", _("民宿"), has_children=True, pos=(522, 432))

    Action.current_parent = "bnb"
    bnb_action = Action("bnb_action", "", has_children=True)
    clean = Action("clean", _("清洁"), "(t.period is not LateNight) and clean.count_of_day < 1", displaying="seen('A_daily_5') and clean_count < 5")
    build_pool = Action("build_pool", _("建设游泳池"), "build_pool.count_of_day < 1", displaying="seen('C_daily_13') and build_pool_count < 7")

    Action.current_parent = "bnb"
    bnb_rooms = Action("bnb_rooms", _("民宿房间"), has_children=True)
    basic_room = Action("basic_room", _("卧室"))
    couple_room = Action("couple_room", _("双人间"))
    my_room = Action("my_room", _("我的房间"), to_map=False)
    frontyard = Action("frontyard", _("前院"))
    livingroom = Action("livingroom", _("客厅"))
    kitchen = Action("kitchen", _("厨房"))
    bathroom = Action("bathroom", _("浴室"))
    toilet = Action("toilet", _("厕所"))

    def G_room_hover():
        if t.period == Morning:
            return "乌诺在睡觉."
        if is_weekday() and t.period < Evening:
            return "乌诺不在家."

    def A_room_hover():
        if not is_A_home():
            return "她不在家."

    def is_G_home():
        if is_weekday() and t.period in (Evening, LateNight):
            return True
        elif is_weekend() and t.period in periods_except(Morning, Afternoon):
            return True
        return False

    def is_A_home():
        if is_weekday() and t.period in (Morning, LateNight):
            return True
        elif is_weekend() and t.period in (Morning, Evening, LateNight):
            return True
        return False

    G_room = Action("G_room", _("找乌诺"), "is_G_home()", hover_message=G_room_hover, to_map=False, training_nz="G")
    A_room = Action("A_room", _("找薇拉"), "is_A_home()", hover_message=A_room_hover, to_map=False, training_nz="A")
    C_room_2 = Action("C_room_2", ("狄奥多拉的房间"))

    Action.current_parent = None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
