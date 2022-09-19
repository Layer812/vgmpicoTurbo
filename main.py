# vgmpicoTurbo: Pico Vgmplayer Turbo 0.2
# Copyright 2022, Layer8 https://twitter.com/layer812
# Licensed under the Apache License, Version 2.0
import vgmpicoTurbo
import os,time

#VGMファイルを一度に読む量
BUFFER_SIZE=2048
#ループ数、0にすると無限ループ
LOOP_NUM=1

#チップタイプの定数
CHIP_TYPE_NONE = 0
CHIP_TYPE_PWMPSG = 1  #SUPPORTED (PwmでPSGを鳴らすやつ)
PWM_PIN=[27, 26]

CHIP_TYPE_SSC    = 2  #TO BE SUPPORTED
#           SCL SDA  SCL SDA
SSC_PIN = [[0,  0], [0,  0]]

CHIP_TYPE_YM3824 = 3  #TO BE SUPPORTED
CHIP_TYPE_YM2149 = 4  #TO BE SUPPORTED
CHIP_TYPE_YM2151 = 5  #TO BE SUPPORTED
CHIP_TYPE_YM2203 = 6  #TO BE SUPPORTED
CHIP_TYPE_YM2208 = 7  #TO BE SUPPORTED
CHIP_TYPE_YM2210 = 8  #TO BE SUPPORTED
CHIP_TYPE_SID    = 9  #TO BE SUPPORTED
CHIP_TYPE_SPU    = 10 #TO BE SUPPORTED
CHIP_TYPE_APU    = 11 #TO BE SUPPORTED

#            ENABLE, D0,D1,D2,D3,D4,D5,D6,D7,A0,A1,WR,IC,CS,CLOCK
CHIP_PINS =[[ 0,     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0,     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]]

#チップ初期化(チップが刺さっている種類と順番)
Chips = [CHIP_TYPE_PWMPSG, CHIP_TYPE_NONE]

Gd3buff = bytearray(256)
MvGd3buff = memoryview(Gd3buff)
Gd3buff[0] = LOOP_NUM

time.sleep(1)

#初期化
for i, chip in enumerate(Chips):
    if chip == CHIP_TYPE_PWMPSG:
        rc = vgmpicoTurbo.modinit(i, chip, ",".join(map(str, PWM_PIN)))
        print("rc", rc)
    elif chip == CHIP_TYPE_SSC:
        vgmpicoTurbo.modinit(i, chip, ",".join(map(str, SSC_PIN)))
    else:
        vgmpicoTurbo.modinit(i, chip, ",".join(map(str, CHIP_PINS)))

#main.pyと同じディレクトリにあるvgmファイルを全部再生
for file in os.listdir('/'):
    if ".vgm" not in file:
        continue
    with open(file, 'rb') as fr:
        vgm_data = fr.read(BUFFER_SIZE)
        rc = vgmpicoTurbo.vgminit(vgm_data, BUFFER_SIZE, MvGd3buff)
        while True:
            fr.seek(rc, 0)
            vgm_data = fr.read(BUFFER_SIZE)
            rc = vgmpicoTurbo.play(vgm_data, BUFFER_SIZE)
            if rc <= 0:
                break

