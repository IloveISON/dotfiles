## Just my new config,...,.,.,..,.,###
from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile import hook
from libqtile.utils import guess_terminal
import datetime
import subprocess
from subprocess import check_output, call
import os
import sys
# from qtile_extras import widget as extras_widget

# Log the Python version to a file
home = os.path.expanduser('~')
log_file = os.path.join(home, '.config/qtile/python_version.log')
with open(log_file, 'w') as f:
    f.write(f"Python version: {sys.version}\n")
    f.write(f"Python executable: {sys.executable}\n")

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
    # subprocess.Popen(['~/.config/polybar/launch.sh'])

# ScratchPad and DropDown
from libqtile.config import ScratchPad

mod = "mod4"
alt = "AltL"
#count date = 'notify-send "Today: $(date -d now +'%B %d')" "+14 days: $(date -d 'now + 14 days' +'%B %d')'
count_days = """notify-send "Today: $(date -d now +'%B %d')" "+14 days: $(date -d 'now + 14 days' +'%B %d')"""
count_days2 = "notify-send 'hello'"
# qtile.cmd_terminal="/home/soilworker/.cargo/bin/alacritty"
terminal="alacritty"
# terminal = guess_terminal()
mod3 = 'ISO_Level3_Shift'

# modifier_keys = {
#     "AltGr": "mod5"
# }
#
# Scripts/Apps Variables
# home = os.path.expanduser('~')
# volume = home + "/.config/qtile/scripts/qtile_volume"

#Function to toggle keyboard layouts

# @lazy.function
# def kbd_switch(qtile):
#     ru_key = ['/usr/bin/setxkbmap', '-layout', 'ru', '-variant', 'typo-birman-ru']
#     en_key = ['/usr/bin/setxkbmap', '-layout', 'us', '-variant', 'typo-birman-en']
#     output = check_output(["/usr/bin/setxkbmap", "-query"], text=True)
#     call(ru_key) if "en" in output else call(en_key)


# Define your layouts and variants in lists
# layouts = ["us", "ru"]
# variants = ["typo-birman-en", "typo-birman-ru"]

# Create a KeyboardLayout widget instance
# keyboard_layout = widget.KeyboardLayout(
    # configured_keyboards=layouts,
    # configured_keyboards_options=variants
# )

# def toggle_keyboard_layout(qtile):
    # Get the current layout variant using setxkbmap
    # current_layout = qtile.core.input.xkb_options['layout']
    
    # if current_layout == 'ru':
        # If the current layout is "ru", toggle to "us"
        # lazy.spawn("setxkbmap -layout us -variant typo-birman-en")
    # else:
        # If the current layout is not "ru", toggle to "ru"
        # lazy.spawn("setxkbmap -layout ru -variant typo-birman-ru")

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    # Key(
        # [],              # Modifiers (empty for no modifiers)
        # "Shift_L",       # Key to trigger the layout toggle
        # lazy.function(toggle_keyboard_layout),
        # desc="Toggle keyboard layout",
    # ),
    # Key([mod3], "e", lazy.spawn("setxkbmap -layout us -variant typo-birman-en")),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    # Key([alt], "Shift_L", lazy.widget["keyboardlayout"].next_keyboard()),
    # Key([mod], "Shift_L", lazy.widget["keyboardlayout"].next_keyboard()),
    # Key([mod], "Shift_L", lazy.function(kbd_switch)),
    Key([mod], "Shift_L", lazy.spawn("setxkbmap -layout us -variant typo-birman-en")),
    Key([mod], "Shift_R", lazy.spawn("setxkbmap -layout ru -variant typo-birman-ru")),
    Key([mod], "p", lazy.spawn("rofi -show run")),
    Key([mod], "z", lazy.spawn(count_days2)),
    # Key([mod], "Shift_L", lazy.spawn("setxkbmap -layout ru -variant typo-birman-ru")),
    # Key([mod], "Shift_R", lazy.spawn("setxkbmap -layout us -variant typo-birman-en")),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Key(['mod5'], lazy.layout.)
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, "control"], "h", lazy.layout.grow_left(),
        # desc="Grow window to the left"),
    # Key([mod, "control"], "l", lazy.layout.grow_right(),
        # desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Key([mod], "Return", qtile.cmd_terminal(), desc="Launch Alacritty")
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([], 'Print', lazy.spawn("flameshot gui")),
    Key([mod], 'Print', lazy.spawn("flameshot screen")),
    Key([mod, 'control'], 'Print', lazy.spawn("flameshot full")),
    # Key([mod]), "p", os.system("betterlockscreen - l dim"),
    Key([mod], "l", lazy.next_screen(), desc="Move focus to next monitor"),
    # Switch focus to the previous screen
    Key([mod], "h", lazy.prev_screen(), desc="Move focus to previous monitor"),
]

# colers = {
#     "Hit": "1",
#     "Shit": "2",
#     "Fit": "3"
# }
#
layout_theme = {
    "border_width": 3,
    "margin": 15,
    "border_focus": "FFFFFF",
    "border_normal": "CCCCCC"
}

groups = [Group(i) for i in "12345"]
# groups = [Group(i) for i in colers.items()]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # layout.MonadTall(font="Ubuntu"),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(single_border_width=0,
                     single_margin=None, border_width=1, border_focus='#22e3c9'),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]],

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/Pictures/wallpapers/0308.jpg",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                # GroupBox(
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    #foreground=colors[1],
                    #background=colors[2],
                ),
                #     borderwidth=0,
                #     disable_drag=True,
                # ),
                widget.Image(
                filename="~/.config/qtile/icons/terminal-iconx14.png",
                mouse_callbacks={
                        'Button1': lambda lazy : lazy.spawn("/home/soilworker/.cargo/bin/alacritty")}
                ),

                widget.CurrentLayout(),
                # widget.CurrentLayoutIcon(custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                #                          foreground=colors[2],
                #                          background=colors[0],
                #                          padding=0,
                #                          scale=0.7
                #                          ),
                widget.GroupBox(highlight_method='block',
                                hide_unused=True, inactive="ffffff"),
                widget.GenPollText(
                    # name="testfeature",
                    fmt="hihi {} ", update_interval=60,
                    # foreground=colors[1], background=colors[7],
                    func=lambda: subprocess.check_output(
                        "~/Documents/polltext.sh").decode("utf-8"),
                    # padding=0
                ),
                widget.Prompt(cursor=True, cursor_color="008080",
                              font="Ubuntu bold"),
                widget.Clipboard(maxchars=14, selection='CLIPBOARD'),
                widget.WindowName(font="Ubuntu", fontsize="12", max_chars=12),
                # widget.Net(interface="enp2s0"),
                # widget.TextBox(f"hi"),
                # widget.Net(interface="enp2s0"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.lower(),
                ),
                widget.KeyboardLayout(configured_keyboards=["us", "ru typo-birman-ru"]),
                widget.Notify(position='top_right', width=100, action=True,
                              maxchars=10, scroll=True, scroll_repeat=False),
                # widget.NetGraph(frequency=1),
                widget.BatteryIcon(battery=1, update_interval=60),
                # widget.Wallpaper(directory='~/Pictures/wallpapers/',
                #  option='stretch', random_selection=True),
                #   display_map={"us typo-birman-en": "US", "ru typo-birman-ru": "RU"}, font="Ubuntu"),
                # widget.KeyboardLayout(configured_keyboards=[
                #                       'us ttypo-birman-en', 'ru ttypo-birman-ru']),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn",
                #                foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%H:%M"),
                widget.QuickExit(default_text='[X]', countdown_format='[{}]'),
            ],
            24,
            border_width=[1, 0, 1, 0],  # Draw top and bottom borders
            border_color=["264B56", "367588", "264B56",
                          "008080"]  # Borders are magenta
            ),
        ),

    Screen(
        # top=bar.Gap(30)
        #         [
        #             # widget.Systray(),
        #             widget.Clock(format="%H:%M"),
        #             # extras_widget.PulseVolume(),
        #         ],
        #         24,
        #     ),
        ),
            ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
