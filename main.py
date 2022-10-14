# vgmpicoTurbo: Pico Vgmplayer Turbo 0.5
# Copyright 2022, Layer8 https://twitter.com/layer812
# Licensed under the Apache License, Version 2.0
import vgmpicoTurbo
import os,time

#VGMファイルを一度に読む量
BUFFER_SIZE=2048
#ループ数、0にすると無限ループ(曲によってループしない指定のファイルもあります)
LOOP_NUM=0

#音源チップ毎の定数
CHIP_TYPE_NONE = 0
CHIP_TYPE_DCSG   = 1  #TO BE SUPPORTED (sn76489)a
CHIP_TYPE_SSC    = 2  #SUPPORTED (SoundCortexChip / Konami SSC & AY-3-8910)
CHIP_TYPE_YM2203 = 3  #TO BE SUPPORTED
CHIP_TYPE_YM3438 = 4  #SUPPORTED (FM PART)
CHIP_TYPE_YM2151 = 5  #SUPPORTED
CHIP_TYPE_YMF276 = 6  #TO BE SUPPORTED
CHIP_TYPE_SID    = 7  #TO BE SUPPORTED (Commodore Sound Chip)
CHIP_TYPE_YM2608 = 8  #TO BE SUPPORTED
CHIP_TYPE_YMZ294 = 9  #SUPPORTED
CHIP_TYPE_YM2610 = 10 #TO BE SUPPORTED
CHIP_TYPE_APU    = 11 #TO BE SUPPORTED (NES Sound Chip)
CHIP_TYPE_YM3812 = 12 #TO BE SUPPORTED
CHIP_TYPE_YM2413 = 13 #SUPPORTED
CHIP_TYPE_SPU    = 14 #TO BE SUPPORTED (SNES Sound Chip)
CHIP_TYPE_NSX1   = 15 #TO BE SUPPORTED (YAMAHA Vocaloid Soud Chip)

#音源チップ向け初期化定数(GPIOピン指定、PWMはPWMPSG用、SDA/SCLはSSC用、D0以降は生チップ用です。)
#            CHIPTYPE,          PWM, SDA, SCL, D0,D1,D2,D3,D4,D5,D6,D7,A0,A1,IC,WR,CS,RD,CLOCK
#Chips =    [[ CHIP_TYPE_YM3438,  -1,  -1,  -1,  0, 1, 2, 3, 4, 5, 6, 7,27,28,14,29,-1,-1, 26],
#Chips =     [[ CHIP_TYPE_YM2413, -1,  -1,  -1, 28,29, 0, 1, 2, 3, 4, 5, 8,-1,15,14,-1,-1, 6],
#            [ CHIP_TYPE_SSC,     -1,  12,  13, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
#Chips =    [[ CHIP_TYPE_YM2151,   -1,  -1,  -1, 14,15,26,27, 8, 7, 6, 5, 2,-1, 1, 3,-1, 4,-1],
#Chips =    [[ CHIP_TYPE_DCSG,    -1,  -1,  -1, 26,15,14, 8, 6, 5, 4, 3,-1,-1,-1,27,-1,-1, 7],
#Chips =    [[ CHIP_TYPE_YMZ294,   -1,  -1,  -1,  7, 6, 5, 4, 3, 2, 1, 0,15,-1,27,14,-1,-1,26],
Chips =    [[ CHIP_TYPE_YM2203,   -1,  -1,  -1,  29, 0, 1, 2, 3, 4, 5, 6,27,-1,14,15,-1,26,28],
            [ CHIP_TYPE_NONE,     -1,  -1,  -1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]] #番兵君

#GD3表示文戻し用領域
Gd3buff = bytearray(256)
MvGd3buff = memoryview(Gd3buff)

#ファイル入れ替えなどで止めたい人用
time.sleep(1)

#初期化
for i, chip in enumerate(Chips):
    rc = vgmpicoTurbo.modinit(chip, i, chip[0])
    print(chip[0], rc)
#main.pyと同じディレクトリにあるvgmファイルを全部再生
for file in os.listdir('/'):
    if ".vgm" not in file:
        continue
    with open(file, 'rb') as fr:
        Gd3buff[0] = LOOP_NUM
        vgm_data = fr.read(BUFFER_SIZE)
        rc = vgmpicoTurbo.vgminit(vgm_data, BUFFER_SIZE, MvGd3buff)
        print(file, rc)
        while rc > 0:
            fr.seek(rc, 0)
            vgm_data = fr.read(BUFFER_SIZE)
            rc = vgmpicoTurbo.play(vgm_data, BUFFER_SIZE)
            if rc <= 0:
                break
