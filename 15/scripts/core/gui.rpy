









init -2 python:
    gui.init(1920, 1080)












define -2 color.xpf = "#b79c9d"
define -2 color.nxpf = "#9e8687"
define -2 color.gnxpf = "#8f797a"
define -2 color.cream = "#f0eee9"
define -2 color.grey0 = "#aaaaaa"
define -2 color.grey1 = "#6f6f6f"
define -2 color.rpf0 = "#e066a3"
define -2 color.powerder = "#f2e6dd"
define -2 color.mh = "#cc0066"
define -2 color.blackish = "#2e2e2c"
define -2 color.some_pink = "#E08E8E"
define -2 color.important = "#ffcd5c"


define -2 gui.main_accent_color = "#ef869f"


define -2 gui.selected_color = "#f0a6b2"

define -2 confirm_overlay = Solid("#00000060")

define -2 gui.bi70_solid = Solid("#2e2e2cb3")
define -2 gui.bi70_frame = Frame("/gui/frame2020.png", 15, 15)
define -2 gui.frame_margin = -15
define -2 gui.frame_padding = 20

define -2 gui.not_implemented_color = color.grey1
define -2 gui.hovered_color = gui.main_accent_color


define -2 gui.frame_borders = Borders(5, 5, 5, 5, -5, -5, -5,- 5)
define -2 gui.frame_tile = True

define -2 gui.dialogue_color = "#E6E6E6"


define -2 gui.ultra = 48
define -2 gui.huge = 34
define -2 gui.big = 30
define -2 gui.semi = 28
define -2 gui.regular = 24
define -2 gui.small = 22

init -3 python in font:
    pass

define -2 font.light = "fonts/Monorale-Light.otf"
define -2 font.regular = "fonts/Monorale-Regular.otf"
define -2 font.medium = "fonts/Monorale-Medium.otf"
define -2 font.semibold = "fonts/Monorale-SemiBold.otf"
define -2 font.bold = "fonts/Monorale-Bold.otf"
define -2 font.black = None
define -2 font.thin = "fonts/Monorale-Thin.otf"

define -2 gui.dialogue_outlines = [(3, "#514546")]

define -2 gui.regular_outlines = [ (0, "#00000059", 1, 1), (1, "#51454659") ]
define -2 gui.large_outlines = [ (0, "#00000059", 1, 1), (2, "#51454659") ]

define -2 gui.regular_light_default_outlines = [(1, "#635556")]

define -2 gui.interface_text_size = 32


define -2 gui.accent_color = gui.main_accent_color
define -2 gui.accent_outlines = [(2, "#514546")]


define -2 gui.text_size = gui.semi
define -2 gui.text_color = gui.dialogue_color
define -2 gui.text_outlines = gui.regular_outlines


define -2 gui.name_text_size = 45
define -2 gui.protagonist_name_size = 45


define -2 gui.idle_color = "#E6E6E6"



define -2 gui.idle_small_color = gui.main_accent_color


define -2 gui.hover_color = gui.main_accent_color


define -2 gui.insensitive_color = '#aaaaaa7f'



define -2 gui.muted_color = gui.main_accent_color
define -2 gui.hover_muted_color = "#f0eee9"


define -2 gui.name_text_color = "#f0eee9"
define -2 gui.name_text_outlines = [ (1, "#00000059", 1, 1), (1, "#514546")]
define -2 gui.namebox_background = None



define -2 gui.interface_text_color = "#E6E6E6"
define -2 gui.interface_text_outlines = gui.large_outlines



define -2 gui.label_text_font = font.medium
define -2 gui.label_text_size = gui.huge
define -2 gui.label_text_color = "#f0a6b2"
define -2 gui.label_text_outlines = [ (0, "#00000059", 1, 1), (1, "#514546") ]

define -2 gui.frame_text_outlines = gui.large_outlines




define -2 gui.clock_font = font.light


define -2 gui.text_font = font.regular

define -2 gui.dialogue_text_font = "fonts/SourceHanSansJP-medium.ttf"


define -2 gui.name_text_font = "fonts/SourceHanSansJP-medium.ttf"


define -2 gui.interface_text_font = font.regular


define -2 gui.notify_text_size = 24


define -2 gui.title_text_size = 75
define -2 gui.title_text_outlines = [(6, "#514546")]





define -2 gui.game_menu_background = "gui/game_menu.png"








define -2 gui.textbox_height = 278



define -2 gui.textbox_yalign = 1.0




define -2 gui.name_xpos = 360
define -2 gui.name_ypos = 0



define -2 gui.name_xalign = 0.0



define -2 gui.namebox_width = None
define -2 gui.namebox_height = None



define -2 gui.namebox_borders = Borders(5, 5, 5, 5)



define -2 gui.namebox_tile = False





define -2 gui.dialogue_xpos = 402
define -2 gui.dialogue_ypos = 75


define -2 gui.dialogue_width = 1116



define -2 gui.dialogue_text_xalign = 0.0








define -2 gui.button_width = None
define -2 gui.button_height = None

define -2 gui.button_padding = (0, 0)


define -2 gui.button_borders = Borders(6, 6, 6, 6)



define -2 gui.button_tile = False


define -2 gui.button_text_font = gui.interface_text_font


define -2 gui.button_text_size = gui.interface_text_size


define -2 gui.button_text_idle_color = gui.idle_color
define -2 gui.button_text_hover_color = gui.hover_color
define -2 gui.button_text_selected_color = gui.selected_color
define -2 gui.button_text_insensitive_color = gui.insensitive_color



define -2 gui.button_text_xalign = 0.0








define -2 gui.radio_button_borders = Borders(27, 6, 6, 6)

define -2 gui.check_button_borders = Borders(27, 6, 6, 6)

define -2 gui.confirm_button_text_xalign = 0.5

define -2 gui.page_button_borders = Borders(15, 6, 15, 6)

define -2 gui.quick_button_borders = Borders(15, 6, 15, 0)
define -2 gui.quick_button_text_size = 21
define -2 gui.quick_button_text_idle_color = gui.idle_small_color
define -2 gui.quick_button_text_selected_color = gui.accent_color















define -2 gui.navigation_xpos = 60


define -2 gui.skip_ypos = 15


define -2 gui.notify_ypos = 68


define -2 gui.navigation_spacing = 12


define -2 gui.pref_spacing = 15


define -2 gui.pref_button_spacing = 0


define -2 gui.main_menu_text_xalign = 1.0
define -2 gui.main_menu_text_outlines = gui.frame_text_outlines











define -2 gui.confirm_frame_borders = Borders(60, 60, 60, 60)


define -2 gui.skip_frame_borders = Borders(24, 8, 75, 8)


define -2 gui.notify_frame_borders = Borders(24, 8, 60, 8)














define -2 gui.bar_size = 38
define -2 gui.scrollbar_size = 10
define -2 gui.slider_size = 38


define -2 gui.bar_tile = False
define -2 gui.scrollbar_tile = False
define -2 gui.slider_tile = False


define -2 gui.bar_borders = Borders(6, 6, 6, 6)
define -2 gui.scrollbar_borders = Borders(6, 6, 6, 6)
define -2 gui.slider_borders = Borders(6, 6, 6, 6)


define -2 gui.vbar_borders = Borders(6, 6, 6, 6)
define -2 gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define -2 gui.vslider_borders = Borders(6, 6, 6, 6)



define -2 gui.unscrollable = "hide"







define -2 config.history_length = 250



define -2 gui.history_height = None



define -2 gui.history_name_xpos = 160
define -2 gui.history_name_ypos = 0
define -2 gui.history_name_width = 160
define -2 gui.history_name_xalign = 1.0


define -2 gui.history_text_xpos = 182
define -2 gui.history_text_ypos = 3
define -2 gui.history_text_width = 1040
define -2 gui.history_text_xalign = 0.0







define -2 gui.nvl_borders = Borders(0, 15, 0, 30)



define -2 gui.nvl_list_length = 6



define -2 gui.nvl_height = 173



define -2 gui.nvl_spacing = 15



define -2 gui.nvl_name_xpos = 645
define -2 gui.nvl_name_ypos = 0
define -2 gui.nvl_name_width = 225
define -2 gui.nvl_name_xalign = 1.0


define -2 gui.nvl_text_xpos = 675
define -2 gui.nvl_text_ypos = 12
define -2 gui.nvl_text_width = 885
define -2 gui.nvl_text_xalign = 0.0



define -2 gui.nvl_thought_xpos = 360
define -2 gui.nvl_thought_ypos = 0
define -2 gui.nvl_thought_width = 1170
define -2 gui.nvl_thought_xalign = 0.0


define -2 gui.nvl_button_xpos = 675
define -2 gui.nvl_button_xalign = 0.0







define -2 gui.language = "unicode"






init -2 python:



    if renpy.variant("touch"):
        
        gui.quick_button_borders = Borders(60, 21, 60, 0)



    if renpy.variant("small"):
        
        gui.scrollbar_size = 54
        
        
        gui.text_size = 38
        gui.name_text_size = 52
        gui.notify_text_size = 34
        gui.interface_text_size = 36
        gui.button_text_size = 36
        gui.label_text_size = 36
        
        
        gui.textbox_height = 390
        gui.name_xpos = 220
        gui.dialogue_xpos = 240
        gui.dialogue_ypos = 85
        gui.dialogue_width = 1440
        
        
        gui.slider_size = 50
        
        gui.navigation_spacing = 26 
        gui.pref_button_spacing = 15
        
        gui.history_height = 285
        gui.history_text_width = 1035
        
        gui.quick_button_text_size = 34
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        
        gui.nvl_height = 255
        
        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488
        
        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8
        
        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30
        
        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
