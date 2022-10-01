# vgmpicoTurbo
vgmpicoTurbo[Raspberry PICO]は、(https://www.switch-science.com/catalog/6900/)向けの[VGMファイル](https://www.jpedia.wiki/blog/en/VGM_(file_format))簡易プレイヤーTurboです。<br>
MicroPython版の[vgmpico](https://github.com/Layer812/vgmpico/)に比べて遅延を低減し、物理FM音源チップに対応しました。<br>

## vgmpicoTurboの特徴
 - [Raspberry PICO](https://www.switch-science.com/catalog/6900/)と物理FM音源チップとブレッドボードが有れば、手軽にFM音源が楽しめます。
 - 対応する物理的なFM音源チップを、対応するチップ毎に各2個づつ接続できます。
 - FM音源チップ毎のピンアサインを自由に変更できます。
 - FM音源チップ毎に必要となるクロックをソフトウェアで出力できます。（水晶発振子不要）
 - [Thonny](https://thonny.org/)を使う事で、簡単にVGMファイルの入れ替えが出来ます。

## 使い方
### 使う物
 - Raspbery pico(以降Pico) 1個
 - ブレッドボード
 - 小型スピーカまたはイヤホン
 - ジャンパ線適宜
 - FM音源チップ(対応状況は以下です。)
   - SCC([SoundCortexLPC](https://github.com/toyoshim/SoundCortexLPC) / Konami SSC & AY-3-8910) : 対応
   - YM2413(OPLL) : 対応
   - YM3438(OPN2 = YM2612) : 対応 (FM音源部)
   - YM2149 : 近日対応
   - DSCG(sn76489) : 近日対応
   - YM2203 ： 近日対応
   - YM2151 ： 未対応
   - YMF276 ： 未対応
   - SID    ： 未対応
   - YM2608 ： 未対応
   - YM2610 ： 未対応
   - APU    ： 未対応
   - YM3812 ： 未対応
   - SPU    ： 未対応
   - NSX1   ： 未対応

## 設定のしかた
### ソフトウェア設定
1.firmware.uf2をPicoにアップロードします<br>
2.[Thonny](https://thonny.org/)を使い、main.pyをアップロードします。<br>
3.接続するFM音源チップ、ピンアサインに応じてmain.pyを変更します。<br>
　変更箇所は30行目～40行目までの、PythonのList形式で表現されるChips定義です。<br>
　#[CHIPTYPE,          PWM, SDA, SCL, D0,D1,D2,D3,D4,D5,D6,D7,A0,A1,IC,WR,CS,CLOCK],<br>
　- CHIPTYPEは接続する物理FM音源チップ(12行目～28行目までに定義)の定数を入れます、同じ種類のチップの定義は２行まで有効です。
  - PWMは使用しないので -1とします。
  - SDAとSCLはSCC([SoundCortexLPC](https://github.com/toyoshim/SoundCortexLPC)向けの定義です。I2C通信に使用するGPIOを指定します。
  - D0～CSまでは、物理チップのピンに接続するGPIOを指定します。定義不要なピンは-1とします。
  - CLOCKにはクロックを出力するGPIOを指定します。物理チップ毎に決められた周波数のクロックを出力します。
  - 最終行のCHIPS_TYPE_NONEは削除しないでください。

### 接続のしかた
1.YM2413 + SCCの接続例
![接続図](https://user-images.githubusercontent.com/111331376/193421841-b2023a7a-d450-4506-9125-61ee690a7262.png)
``` Chips定義
#[CHIPTYPE,          PWM, SDA, SCL, D0,D1,D2,D3,D4,D5,D6,D7,A0,A1,IC,WR,CS,CLOCK],
Chips =     [[ CHIP_TYPE_YM2413,  -1,  -1,  -1, 28,29, 0, 1, 2, 3, 4, 5, 8,-1,15,14,-1, 6],
            [ CHIP_TYPE_SSC,   -1,  12,  13, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [ CHIP_TYPE_NONE,  -1,  -1,  -1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]] #番兵君
```

2.YM3438(YM2612)の接続例
![接続図](https://user-images.githubusercontent.com/111331376/193421951-c0c07c5c-f851-422f-a71b-bd2a036278a2.png)
``` Chips定義
　#[CHIPTYPE,          PWM, SDA, SCL, D0,D1,D2,D3,D4,D5,D6,D7,A0,A1,IC,WR,CS,CLOCK],
Chips =    [[ CHIP_TYPE_YM3438,  -1,  -1,  -1,  0, 1, 2, 3, 4, 5, 6, 7,27,28,14,29,-1, 26],
            [ CHIP_TYPE_NONE,  -1,  -1,  -1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]] #番兵君
```

### VGMファイルの再生方法
 - VGMファイルがvgz形式の場合、7zipやgzipなどで展開しvgm形式にします。
 - [Thonny](https://thonny.org/)などを使い、main.pyと上記vgmファイルを同じディレクトリに転送します。
 - Thonnyの実行を押すか、再起動するとmain.pyと同じディレクトリのvgmファイルが読み込まれ、再生が始まります

### 止め方(ファイルの入れ替え方)
 - Raspberry Picoのリセット後、1秒以内にThonnyの停止ボタンを押すとThonnyによるファイル入れ替えが可能です。
 - VGMファイルはmain.pyと同じディレクトリにThonnyでアップロードしてください。

## TODO
 - 対応音源の増加
 - VGMコマンド全対応
 - GD3表示対応
 - DAC(YM3012/YM3014)をState Machineで実装
 - USB HID経由でmidiコマンド受付

## 制限
 - OPN2のDACによるPCM再生は対応していません。
 - VGMコマンド全てには対応していません。
 - ループ回数はソース内の定数部分に有ります。
 - ~~読み込めるVGMファイルサイズは160Kbyte位までです。~~
 - 音が小さいのでアンプを繋ぐと良いです。耳が若い人向けにはローパスフィルタもおすすめです。
 - ~~firmware.uf2に含むPwmPSGの実装は[とよしまさん](https://twitter.com/toyoshim)及び[boochowpさん](https://twitter.com/boochowp)のコードをパ..参考にしています。~~
 - 本記事内容及びプログラムを使用したことにより発生する、いかなる損害も補償しません。

## Thanks to
 - [SoundCortexLPC](https://github.com/toyoshim/SoundCortexLPC) 最近は低遅延の基盤インタフェース作成中らしい、欲しい...
 - [楽しくやろう。](https://blog.boochow.com/) いつも楽しく参考にさせていただいています！

## ライセンス
 [Apache License v2.0](http://www.apache.org/licenses/LICENSE-2.0)に基づいてご利用ください。ご連絡は[layer8](https://twitter.com/layer812)までお願いします。