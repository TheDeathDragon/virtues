init python:
    def run_replay(event, source):
        store._replaying_event = event
        store._replay_source = source
        renpy.jump("run_event")

    def late_replay(label):
        Replay(label, scope={"_game_menu_screen":None, "P_state":P_state})()

define _replaying_event = None
define _replay_source = None

label run_event:
    if _replaying_event:
        $ renpy.music.stop(fadeout=1.0)
        $ _value_before_replay = [(nz.love.value, nz.harem.value) for nz in NZS]
        $ set_scene("Event")
        jump expression _replaying_event
    else:

        if not getCEvent().repeatable:
            $ renpy.music.stop(fadeout=1.0)
        $ set_scene("Event")
        $ getCEvent().start_time = t.copy()
        $ getCEvent().seeing = True

        if getCEvent().label:
            jump expression getCEvent().label
        if getCEvent().func:
            $ getCEvent().func()

    label event_post:

    if _in_replay:
        $ renpy.end_replay()
        return

    if _replaying_event:
        python:
            for i, nz in enumerate(NZS):
                nz.love.value = _value_before_replay[i][0]
                nz.harem.value = _value_before_replay[i][1]

        $ _replaying_event = None

        if _replay_source == "home":
            $ show_home()
        else:
            $ show_find(_replay_source)
        jump pauser
    else:


        if getCEvent().proceed_to:
            $ time_proceed_to(getCEvent().proceed_to)
        else:
            $ time_proceed(getCEvent().duration)

        $ getCEvent().end_time = t.copy()
        $ EventHistory.append(getCEvent().name)

        $ persistent.seens.append(getCEvent().label)

        $ getCEvent().seen = True
        $ getCEvent().seeing = False
        $ getCEvent().count += 1
        $ getCEvent().count_of_day += 1
        $ getCEvent().count_day = Date(t)

        $ getCEvent().run_results()

        $ _on_event_complete()

        if getCEvent().type and (getCEvent().type.endswith("Love") or getCEvent().type == "Training"):
            $ next_stage(getCEvent().nz, getCEvent().nz.love)
            $ renpy.block_rollback()

        $ post_label = "post_{}".format(getCEvent().label)
        if renpy.has_label(post_label):
            jump expression post_label

        label post_event_post:

        $ queue_auto_event()
        $ auto_event()

        if getCEvent().label == "auto_sleep":
            pass
        else:
            $ show_map()

        $ clearCEvent()

        $ print('Event Clear')

        $ renpy.music.play("music/Imagination - Rayn.opus", loop=True, if_changed=True)

        jump pauser
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
