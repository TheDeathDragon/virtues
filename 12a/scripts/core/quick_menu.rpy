





define skipping = False
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:
        if is_scene("Map"):
            frame:

                background None
                xalign 1.0
                yalign 1.0

                has hbox
                button action Skip() alternate Skip(fast=True, confirm=True):
                    add "gui/phone/skip_button.png"
                button action Rollback():
                    add "gui/phone/back_button.png"
                button action ShowMenu():
                    add "gui/phone/menu_button.png"




        else:
            hbox:
                style_prefix "quick"

                xalign 0.5
                yalign 1.0

                textbutton _("返回") action Rollback()
                textbutton _("跳过") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("自动") action Preference("auto-forward", "toggle")
                textbutton _("隐藏") action HideInterface()
                if _in_replay:
                    textbutton _("结束播放") action EndReplay(confirm=False)
                else:
                    textbutton _("菜单") action ShowMenu()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
