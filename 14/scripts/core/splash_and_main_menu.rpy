label splashscreen:

    scene expression gui.main_menu_background
    show expression gui.splash_art with dissolve
    with Pause(0.7)
    hide expression gui.splash_art with dissolve

image title:
    "gui/title.png"
    alpha 0.0
    pause 0.3
    linear 1.0 alpha 1.0

define pause_merge_trans = MultipleTransition([False, Dissolve(0.5),
    False, Pause(0.5),
    False, dissolve, True])

screen main_menu():
    on "show" action If(persistent.update_note_dontshowagain, true=Show("web_notifications", transition=pause_merge_trans), 
    false=[
        Show("web_notifications", transition=pause_merge_trans), 
        ShowTransient("update_note", transition=pause_merge_trans)
    ])
    tag menu



    add gui.main_menu_background

    if gui.show_name:
        add "title" pos (128, 220) at title


    fixed at pause_emerge(0.5):

        frame:
            style "navigation_frame_style"
            has hbox:
                style_prefix "navigation_0"




                spacing gui.navigation_spacing

            if main_menu:

                textbutton _("新的开始") action [Hide("main_menu"), Show("timed_start")]

            else:
                textbutton _("历史") action ShowMenu("history")

                textbutton _("保存") action ShowMenu("save")

            textbutton _("读档") action ShowMenu("load")

            textbutton _("设置") action ShowMenu("preferences")

            textbutton _("加群") action OpenURL("https://jq.qq.com/?_wv=1027&k=9MsL1MC7")

            textbutton _("画廊") action ShowMenu("gallery")

            if _in_replay:

                textbutton _("结束回放") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("主菜单") action MainMenu()

            textbutton _("关于") action ShowMenu("about")

            textbutton _("额外章节") action ToggleScreen("bonus_chapters")

            if renpy.variant("pc"):


                textbutton _("帮助") action ShowMenu("help")



            if renpy.variant("pc") or renpy.variant("android"):

                textbutton _("退出") action Quit(confirm=not main_menu)

        hbox:
            xalign .0 yalign 1.0
            text "( 版本号: [gui.display_version] [gui.version_suffix])":
                xoffset 18 size 20
                xalign .0 yalign 1.0
            button:
                background Solid("2e2e2cb3", xysize=(140, 28), xoffset=4, yoffset=4)
                xoffset 24 yoffset 6
                text "更新日志" size 20
                action ShowTransient("update_note", transition=Dissolve(0.2))

        text "在Patreon上{font=[gui.name_text_font]}↑{/font}支持我们":
            xalign 1.0 yalign 1.0 size 24 xoffset -4

        button:
            add "patreon_button"
            xpos 1720

            ypos 966
            action OpenURL("https://www.patreon.com/NoMeme")


image patreon_button:
    "gui/patreon_idle.png"
    on idle:
        "gui/patreon_idle.png" with Dissolve(0.2)
    on hover:
        "gui/patreon_hover.png" with Dissolve(0.2)



style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style earth_frame:
    background "#00000055"

style title_frame_style is earth_frame
style title_frame_style:
    xpos 370
    ypos 270
    xpadding 20
    ypadding 10






style main_menu_text:
    properties gui.text_properties("main_menu")
    color gui.interface_text_color
    outlines [ (2, "#00000059", 1, 1), (2, "#514546") ]
    font gui.clock_font

style main_menu_title:
    properties gui.text_properties("title")


    color gui.interface_text_color
    outlines [ (2, "#00000059", 1, 1), (2, "#514546") ]
    font gui.clock_font

style main_menu_version:
    properties gui.text_properties("version")
    font gui.clock_font


screen timed_start():
    timer 0.5 action Start()

style navigation_0_button is gui_button
style navigation_0_button_text is gui_button_text:
    font font.semibold

style navigation_0_button:


    properties gui.button_properties("navigation_button")

style navigation_0_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    outlines [ (2, "#00000059", 1, 1), (2, "#514546") ]


style navigation_frame_style:
    xpos 140
    ypos 970

define gui.special_thanks = _('''{size=-4}特别感谢我们的重要赞助者:
{color=#ffcd5c}{/color}''')

screen thanks():
    frame at normal_t(0.4):
        xpadding 60
        ypadding 40
        background Solid("#00000080")
        xsize 800 ysize 600
        xalign .5 yalign .5
        text gui.special_thanks
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
