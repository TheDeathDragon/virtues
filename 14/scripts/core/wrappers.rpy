define nz_display_list = []
define progress_display_list = []

init -2 python:
    def pass_time():
        time_proceed(1)
        if t.period == Evening:
            renpy.show("map_latenight", at_list=[show_t(0.7)])
        auto_event()

    def has_event(name):
        return EVENTS.get(name)

    def run_event(name):
        store.cEvent = name
        renpy.jump('run_event')

    def run_label(name):
        store.cLabel = name
        renpy.jump('run_label')

    def show_find_fix(nz=None):
        store.cInteraction = None
        show_find(nz)

    def show_find(nz=None):
        set_scene("Find")
        if nz:
            store.findee = nz
        idx = int(random.random() * len(findee.tweets[findee.relation]))
        store._bubble_what = findee.tweets[findee.relation][idx]
        store._bubble_color = findee.color
        renpy.show_screen('find')

    def show_home():
        set_scene("Home")
        renpy.show_screen('home')

    def set_time(time):
        store.t = time
        _on_time_change()

    def time_proceed(period=1):
        store.t.proceed(period)
        _on_time_change()

    def new_day():
        renpy.hide_screen('mansion')
        renpy.hide_screen('college')
        renpy.hide_screen('bnb')
        store.t.new_day()
        _on_time_change()
        auto_event()

    def time_proceed_to(time):
        store.t.proceed_to(time)
        _on_time_change()

    def next_stage(owner, obj, handle=True):
        obj.next_stage()
        if not obj.out_of_content:
            Push(_("{}的{}解锁,新的情节解锁").format(owner, obj))
        else:
            try:
                storyline_owner = obj.nz
            except AttributeError:
                storyline_owner = owner
            Push(_("现在你已经到达了{}的故事线的结尾.").format(storyline_owner))
            Push(_("请等待我们的下一次更新."))
            return

    def lock(obj, handle=True):
        obj.lock()

    def unlock(obj, handle=True):
        obj.unlock()


    def add(owner, obj, value, chance=0, handle=True):
        try:
            storyline_owner = obj.nz
        except AttributeError:
            storyline_owner = owner
        
        if type(obj) is Harem:
            if obj.value + value > obj.max_value:
                Push(_("在当前版本中,{}的后宫接受水平无法进一步提高.").format(storyline_owner))
                return
        
        if obj.is_plot_locked:
            if obj is B.love:
                if seen("B_love_1"): 
                    Push("我现在学习已经够了,也许我应该花些时间在薇拉身上")
            if obj is A.love:
                if seen("A_love_1"):
                    Push("我在薇拉身上花的时间太多了,也许我应该去上上课.")
            return
        
        if obj.is_stage_locked:
            _stage_lock_notification(owner, obj)
            return
        
        if obj.out_of_content:
            Push(_("现在你已经到达了{}的故事线的结尾.").format(storyline_owner))
            Push(_("请等待我们的下一次更新."))
            return
        
        r = obj.add(value, chance)
        if r != 0.0:
            Push(_("{}的{}增加了{}").format(owner, obj, r))
        else:
            Push(_("{}的{}没有变化").format(owner, obj))
        
        if obj.is_stage_locked:
            _stage_lock_notification(owner, obj)

    def _stage_lock_notification(owner, obj):
        if obj.owner == 'A':
            if obj >= 30:
                Push(_("{}的{}已经满了,在她的房间找到她提升她的属性.").format(owner, obj))
            else:
                Push(_("{}的{}已经满了,尝试通过相关事件解锁它.").format(owner, obj))
        
        elif obj.owner == 'B':
            if obj >= 60 and not seen("B_daily_21"):
                Push(_("你应该先和明娜和艾琳搞好关系."))
            elif obj >= 35:
                Push(_("{}的{}已经满了,在她的房间找到她提升她的属性.").format(owner, obj))
            else:
                Push(_("{}的{}已经满了,尝试通过相关事件解锁它").format(owner, obj))
        
        elif obj.owner == 'C':
            if obj >= 40:
                Push(_("{}的{}已经满了,在她的房间找到她提升她的属性.").format(owner, obj))
            else:
                Push(_("{}的{}已经满了,尝试通过相关事件解锁它").format(owner, obj))
        
        elif obj.owner == 'D':
            if obj >= 35:
                Push(_("{}的{}已经满了,在她的房间找到她提升她的属性.").format(owner, obj))
            else:
                Push(_("{}的{}已经满了,尝试通过相关事件解锁它").format(owner, obj))
        
        elif obj.owner == 'E':
            if obj >= 45:
                Push(_("{}的{}已经满了,在她的房间找到她提升她的属性.").format(owner, obj))
            else:
                Push(_("{}的{}已经满了,尝试通过相关事件解锁它").format(owner, obj))
        
        elif obj.owner == 'F':
            if obj >= 25 and not seen("A_love_5"):
                Push(_("在你改善与薇拉的关系后，更多关于雷切尔的故事将被解锁."))
            elif obj is F.love and obj >= 30 and not seen("B_train_inti_1"):
                Push(_("更多关于瑞秋的故事将在你与森宁改善关系后解锁."))
            elif obj is F.love and obj >= 35 and not seen("G_train_sha_2"):
                Push(_("在你改善与乌诺的关系后，更多关于瑞秋的故事将被解锁."))
            elif obj is F.love and obj >= 40 and not seen ('ACG_duo_4'):
                Push(_("你应该先提高维拉、西奥和乌诺的后宫度."))
            else:
                Push(_("{}的{}已经满了,尝试通过相关事件解锁它").format(owner, obj))
        
        elif obj.owner == 'G':
            if obj >= 35:
                Push(_("{}的{}已经满了,在她的房间找到她提升她的属性.").format(owner, obj))
            else:
                Push(_("{}的{}已经满了,尝试通过相关事件解锁它").format(owner, obj))
        
        return

    def sub(owner, obj, value):
        r = obj.sub(value)
        Push(_("{}的{}减少了{}").format(owner, obj.name, value))


    def not_implemented_message():
        Push("对不起，这个故事将在未来的版本中实现.")








    def time_warp(type):
        def ease(t):
            return .5 - math.cos(math.pi * t) / 2.0
        
        if type == "ease":
            return ease

    def show_map(at=False, time=0.7):
        set_scene("Map")
        
        renpy.music.play("music/Imagination - Rayn.opus", loop=True, if_changed=True)
        
        if is_day():
            
            if at:
                renpy.show("map_day", at_list=[show_t(time)])
            else:
                renpy.scene()
                renpy.show("map_day")
                renpy.with_statement(trans=Dissolve(time, time_warp=time_warp("ease")), always=False)
        else:
            
            if at:
                renpy.show("map_latenight", at_list=[show_t(time)])
            else:
                renpy.scene()
                renpy.show("map_latenight")
                renpy.with_statement(trans=Dissolve(time, time_warp=time_warp("ease")), always=False)

    def insensitive(image):
        return im.MatrixColor(image, im.matrix.saturation(0.0) * im.matrix.colorize("#303030", "#f0eee9"))

    def colorize(image, white_color):
        return im.MatrixColor(image, im.matrix.colorize("#000000", white_color))

    def dark_colorize(image, color):
        return im.MatrixColor(image, im.matrix.colorize(color, color) * im.matrix.brightness(-0.5))

    def dark(image):
        return im.MatrixColor(image, im.matrix.brightness(-0.3))

    def dark_insensitive(image):
        return im.MatrixColor(image,  im.matrix.brightness(-0.3) * im.matrix.saturation(0.0) * im.matrix.colorize("#303030", "#f0eee9"))

    class Handle(object):
        
        @classmethod
        def stage_locked(cls, obj):
            Push(_("{}的{}已经满了,尝试通过相关事件解锁它").format(obj.owner.name, obj.name))
        
        @classmethod
        def plot_locked(cls, obj):
            try:
                if not obj.is_visible:
                    return
            except AttributeError:
                pass
            Push(_("{}的{}未解锁,尝试通过相关事件解锁它").format(obj.owner.name, obj.name))
        
        @classmethod
        def unlocked(cls, obj):
            pass
            if isinstance(obj, Meter):
                Push(_("{}的{}未解锁").format(obj.owner.name, obj.name))
        
        @classmethod
        def increase(cls, obj, value):
            if value == 0.0:
                cls.unchanged()
            else:
                Push(_("{}的{}增加了{}").format(obj.owner.name, obj.name, value))
        
        @classmethod
        def decrease(cls, obj, value):
            if value == 0.0:
                cls.unchanged()
            else:
                Push(_("{}的{}减少了{}").format(obj.owner.name, obj.name, value))
        
        @classmethod
        def unchanged(cls, obj):
            Push(_("{}的{}没有发生变化").format(obj.owner.name, obj.name))
        
        @classmethod
        def cash_zero(cls, obj, value):
            Push(_("{}失去了所有的积蓄,总计{}".format(obj.name, value)))
        
        @classmethod           
        def cash_earn(cls, person, value, thing):
            Push(_("你赚了${}从{}").format(value, thing))
        
        @classmethod
        def purchase_succeeded(cls, obj, thing, value):
            Push(_("{0}的储蓄减少了${1}因为支付{2}").format(obj.name, value, thing))
        
        @classmethod
        def purchase_failed(cls, thing):
            Push(_("没有足够的钱买{}").format(thing))
        
        @classmethod
        def payment_succeeded(cls, obj, thing, value):
            Push(_("{0}的储蓄减少了${1}因为支付{2}").format(obj.name, value, thing))
        
        @classmethod
        def payment_failed(cls, thing):
            Push(_("没有足够的钱支付{}").format(thing))
            run_event('suicide_ending')
        
        @classmethod
        def notify_new_location(cls, *args):
            Push(_("{}未解锁").format(*args))
        
        @classmethod
        def time_pass(cls, value):
            if value == 1:
                Push(_("{}段时间过去了").format(value))
            else:
                Push(_("{}段时间过去了").format(value))
        
        @classmethod
        def lock_in_version(cls, obj):
            Push(_("现在你已经到达了{}的故事线的结尾.").format(obj.owner))
            Push(_("请等待我们的下一次更新."))

        @classmethod
        def out_of_content(cls, obj):
            Push(_("现在你已经到达了{}的故事线的结尾.").format(obj.owner))
            Push(_("请等待我们的下一次更新."))


default available_interactions = defaultdict(set)
default available_clothes = defaultdict(set)
default auto_event_queue = set()

init python:

    def queue_auto_event():
        for ev_name in AUTO_EVENTS:
            ev = get_event(ev_name)
            if ev.is_auto_event and ev.triggerable and ev.runnable:
                auto_event_queue.add(ev_name)
                print("queue AutoEvent %s" % ev_name)

    def auto_event():
        if auto_event_queue:
            get_event(auto_event_queue.pop()).run()

    def _on_time_change():
        
        
        store.cPlaylets = get_cPlaylets()
        queue_auto_event()

    def _on_event_complete():
        print('_on_event_complete()')
        set_nz_locks()
        store.nz_display_list = get_displaying_nzs()
        store.fixed_rooms = get_bnb_rooms()
        update_nz_interactions()
        update_sleepers()
        
        store.cPlaylets = get_cPlaylets()


    def get_displaying_nzs():
        r = []
        if seen("d4_4") or seen('d4_4_bLine'):
            r.append(A)
        if seen("d1_1"):
            r.append(B)
        if seen("d2_1"):
            r.append(C)
        if seen("d7_1"):
            r.append(D)
        if seen("D_dqsj"):
            r.append(E)
        if seen("B_daily_5"):
            r.append(F)
        if seen("D_daily_3"):
            r.append(G)
        return r


    def set_nz_locks():
        plot_lock = False
        if seen("A_love_1"):
            plot_lock = True
        if seen("pcsj"):
            plot_lock = False
        
        A.love.meter.is_plot_locked = plot_lock
        
        
        plot_lock = True 
        if seen("d6_1"):
            plot_lock = False
        if seen("B_love_1"):
            plot_lock = True
        if seen("pcsj"):
            plot_lock = False
        
        B.love.meter.is_plot_locked = plot_lock

    def get_interaction(label):
        return INTERACTIONS.get(label)

    def get_nz_interactions(nz_code):
        return [it for it in NZ_INTERACTIONS[nz_code] if it.displaying]

    def get_nz_interaction_labels(nz_code):
        return [it.label for it in NZ_INTERACTIONS[nz_code] if it.displaying]




    def get_available_interactions(nz_code, type):
        its = []
        for it in available_interactions[nz_code]:
            it = get_interaction(it)
            if it.type == type:
                its.append(it)
        return its





    def update_nz_interactions():
        for nz in nz_display_list:
            old = available_interactions.get(nz.code, set())
            new = set(get_nz_interaction_labels(nz.code))
            for label in (new - old):
                Push('新的互动与 {} "{}" 已解锁.'.format(nz, get_interaction(label).name))
            available_interactions[nz.code] = new

    def get_nz_clothes(nz_code):
        return getattr(store, '%s_clothes' % nz_code)()

    def update_nz_clothes():
        for nz in nz_display_list:
            old = available_clothes.get(nz.code, set())
            new = set(get_nz_clothes(nz.code))
            for clothes in (new - old):
                if not clothes.startswith("Default"):
                    Push('{} 的新装扮 "{}" 已解锁.'.format(nz, clothes))
            available_clothes[nz.code] = new

    def to_next_day():
        t.proceed_to(Morning)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
