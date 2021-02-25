f1::SetTimer, main, on
f2::SetTimer, main, off

main(){
	PixelGetColor, col1, 860, 580
	PixelGetColor, col2, 960, 580
	PixelGetColor, col3, 1060, 580
	PixelGetColor, col4, 1160, 580
	PixelGetColor, col11, 860, 560
	PixelGetColor, col21, 960, 560
	PixelGetColor, col31, 1060, 560
	PixelGetColor, col41, 1160, 560
	if (col1 == 0x111111 and col11 == 0x111111){
	MouseClick, Left, 860, 640
	}
	if (col2 == 0x111111 and col21 == 0x111111){
	MouseClick, Left, 960, 640
	}
	if (col3 == 0x111111 and col31 == 0x111111){
	MouseClick, Left, 1060, 640
	}
	if (col4 == 0x111111 and col41 == 0x111111){
	MouseClick, Left, 1160, 640
	}
}
