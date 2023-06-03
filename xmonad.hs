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

main = xmonad =<< xmobar myConfig

myConfig = def {terminal 	= "kitty"
	, modMask  	= mod4Mask
	, borderWidth 	= 2
	, startupHook 	= myStartupHook
	, logHook = dynamicLog	
	}
	`additionalKeysP`
	[("M-r", spawn "rofi -modi 'drun' -show drun -show-icons")
	,("M-w", spawn "firefox")
	,("M-f", spawn "nemo")
	,("M-a", spawn "pavucontrol")
	] 
