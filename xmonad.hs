import XMonad
import XMonad.ManageHook
import XMonad.Hooks.DynamicLog

import XMonad.Layout.Accordion
import XMonad.Layout.GridVariants (Grid(Grid))
import XMonad.Layout.SimplestFloat
import XMonad.Layout.Spiral
import XMonad.Layout.ResizableTile
import XMonad.Layout.Tabbed
import XMonad.Layout.ThreeColumns

import XMonad.Util.EZConfig

myStartupHook = do
	spawn "compton --vsync opengl"
	spawn "nitrogen --restore"

myLayout = tiled ||| Mirror tiled ||| Full
  where
    tiled   = Tall nmaster delta ratio
    nmaster = 1      -- Default number of windows in the master pane
    ratio   = 1/2    -- Default proportion of screen occupied by master pane
    delta   = 3/100  -- Percent of screen to increment by when resizing panes

main = xmonad =<< xmobar myConfig

myConfig = def {terminal 	= "kitty"
	, modMask  	= mod4Mask
	, borderWidth 	= 2
	, startupHook 	= myStartupHook
	, logHook = dynamicLog
	, layoutHook = myLayout	
	}
	`additionalKeysP`
	[("M-r", spawn "rofi -modi 'drun' -show drun -show-icons")
	,("M-w", spawn "firefox")
	,("M-f", spawn "nemo")
	,("M-a", spawn "pavucontrol")
	] 
