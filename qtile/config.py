# Copyright (c) 2010 Aldo Cortesi 
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
from libqtile.widget import CPUGraph, Memory, Image, PulseVolume, Wttr

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
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
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # My own keybindings
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn("rofi -modi drun -show drun -show-icons"), desc="Launch rofi"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+"), desc="Raise volume 5%"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%-"), desc="Lower volume 5%"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5.00"), desc="Raise brightness 5%"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5.00"), desc="Lower brightness 5%"),
    Key([mod], "f", lazy.spawn("pcmanfm"), desc="Launch pcmanfm file manager"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox www browser"),
    Key([mod], "n", lazy.spawn("nitrogen --restore"), desc="Nitrogen restore wallpaper"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc='Toggle floating'),
    Key([mod], "c", lazy.spawn("picom"), desc="Launch Picom"),
    Key([mod], "p", lazy.spawn("picom"), desc="Launch Picom"),
]

groups = [Group(i) for i in "123456789"]

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
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
		border_focus="#ff5555", 
		border_normal="#44475a", 
		border_focus_stack="#ff5555", 
		border_width=2, 
		margin=3
	),
    layout.MonadTall(
		border_focus='#ff5555', 
		border_normal='#44475a', 
		border_width=4
	),
    layout.Floating(
		border_focus="#ff5555", 
		border_normal="#44475a", 
		border_width=2, 
		margin=3
	),
    # layout.Max(margin=5),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2, border_focus="#ff5555", border_normal="#44475a",border_width=2, margin=3),
    # layout.Bsp(border_focus="#ff5555", border_normal="#44475a",border_width=2, margin=3),
    # layout.Matrix(border_focus="#ff5555", border_normal="#44475a",border_width=2, margin=3),
    layout.MonadWide(
		border_focus="#ff5555", 
		border_normal="#44475a",
		border_width=2, 
		margin=3
	),
    # layout.RatioTile(border_focus="#ff5555", border_normal="#44475a",border_width=2, margin=3),
    # layout.Tile(border_focus="#ff5555", border_normal="#44475a",border_width=2, margin=3),
    # layout.TreeTab(),
    # layout.VerticalTile(border_focus="#ff5555", border_normal="#44475a",border_width=2, margin=3),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=6,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
				widget.CurrentLayout(),
				widget.Image(
					filename="~/.config/qtile/menu_icon.png",
					background="#282a36",
					mouse_callbacks = {'Button1': lazy.spawn("rofi -modi drun -show drun -show-icons")}
				),
				widget.GroupBox(
					background="#282a36"
				),
				widget.Prompt(),
				widget.WindowName(
					background="#6272a4"
				),
				widget.Chord(
					chords_colors={
						"launch": ("#ff0000", "#ffffff"),
					},
					name_transform=lambda name: name.upper(),
				),
				widget.Systray(
                ),
                widget.Wttr(
                    location={'Preston': 'Preston'},
                    background="#ffb86c",
                    foreground="#282a36",
                    units="u"
                ),
				widget.Image(
					filename="~/.config/qtile/blue_arrow.png",
					background="#ffb86c"
				),
				widget.CPU(
					foreground="#282a36", 
					background="#8be9fd",
					mouse_callbacks = {'Button1': lazy.spawn("gnome-terminal -e 'htop'")}
				),
				widget.Image(
					filename="~/.config/qtile/purple_arrow.png",
					background="#8be9fd"
				),
				widget.Memory(
					foreground="#282a36", 
					background="#bd93f9",
					mouse_callbacks = {'Button1': lazy.spawn("gnome-terminal -e 'htop'")}
				),
				widget.Image(
					filename="~/.config/qtile/green_arrow.png",
					background="#bd93f9"
				),
                widget.TextBox(
                    text='🕑',
                    foreground="#282a36",
                    background="50fa7b"
                    ),
				widget.Clock(
					format="%d/%m/%y %H:%M", 
					foreground="#282a36", 
					background="#50FA7B"
				),
				widget.Image(
					filename="~/.config/qtile/yellow_arrow.png",
					background="#50FA7B"
				),
				widget.TextBox(
					text='🔊',
					foreground="#282a36",
					background="#F1FA8C",
					mouse_callbacks = {'Button1': lazy.spawn("pavucontrol")}
				),
				widget.PulseVolume(
					fmt="{}", 
					background="#F1FA8C", 
					foreground="#282a36",
                    device='default',
                    emoji_list=['🔇', '🔈', '🔉', '🔊'],
                    emoji=True
				),
				widget.Image(
					filename="~/.config/qtile/red_arrow.png",
					background="#F1FA8C"
				),
				widget.QuickExit(
					foreground="#282a36", 
					background="#ff5555", 
					default_text='✖',
					countdown_format="[{}]"
				),
            ],
            24,
            background="#44475a"
		),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
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
	Match(wm_class="pavucontrol"), # pavucontrol
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

@hook.subscribe.startup_once
def autostart():
	lazy.spawn("firefox")
	
wmname = "LG3D"

