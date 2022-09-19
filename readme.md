# vgmpicoTurbo
[Raspberry PICO](https://www.switch-science.com/catalog/6900/)向けの[VGMファイル](https://www.jpedia.wiki/blog/en/VGM_(file_format))簡易プレイヤーTurboです。<br>
MicroPython版の[vgmpico](https://github.com/Layer812/vgmpico/)に比べて遅延を低減しています。(効果には個人差...)<br>
他に以下を改善、及び改善予定です。<br>
 - 仕様書に沿ったSample Wait/処理高速化     (できました)
 - 最大VGMサイズの撤廃(FM/PCM音源に向けて)　(よくできました)
 - 対応音源の増加　　　　　　　　　　　　   (がんばりましょう)
 - VGMコマンド全対応                        (がんばりましょう)
 - GD3表示対応(戻す器まではできた)　　　　　(もうすこしです)

##使い方
### 使う物
 - Raspbery pico(以降Pico) 1個
 - ブレッドボード
 - 小型スピーカまたはイヤホン
 - ジャンパ線適宜

### 設定
firmware.uf2をPicoにアップロードします<br>
main.pyの以下の行を変更します<br>
Pwm_enabled (Trueにすると有効)<br>
Pwm_pin = 26 (スピーカー(+)を接続するピン)<br>
Pwm_pin = 27 (スピーカー(+)を接続するピン)<br>
### つなぎ方
1.以下の様に物理結線を行います。<br> 
 - イヤホンやスピーカのGND端子にPicoのGND (物理38ピンなど)を接続
 - イヤホンやスピーカのAudio端子に26ピンと27ピンを接続(短絡防止のため抵抗を挟むと良い説有)
![接続図](https://user-images.githubusercontent.com/111331376/189489764-80342a3c-8d08-4ac3-8800-2fcdb988d3fd.png)

### 再生方法
 - VGMファイルがvgz形式の場合、7zipやgzipなどで展開しvgm形式にする
 - [Thonny](https://thonny.org/)などを使い、main.pyと上記vgmファイルを同じディレクトリに転送する
 - Thonnyの実行を押すか、再起動するとmain.pyと同じディレクトリのvgmファイルが読み込まれ、再生が始まります

### 止め方(ファイルの入れ替え方)
 - Raspberry Picoのリセットボタンを押します。
 - 1秒以内にThronyの停止ボタンを押すと、止まります（*´∀｀*）
 - VGMファイルはThonnyでアップロードしてください。

## 制限
 - VGMコマンド全てには対応していません。
 - ループ回数はソース内の定数部分に有ります。
 - ~~読み込めるVGMファイルサイズは160Kbyte位までです。~~
 - 音が小さいのでアンプを繋ぐと良いです。耳が若い人向けにはローパスフィルタもおすすめです。
 - firmware.uf2に含むPwmPSGの実装は[とよしまさん](https://twitter.com/toyoshim)及び[boochowpさん](https://twitter.com/boochowp)のコードをパ..参考にしています。
 - 本記事内容及びプログラムを使用したことにより発生する、いかなる損害も補償しません。

## Thanks to
 - [SoundCortexLPC](https://github.com/toyoshim/SoundCortexLPC) 最近は低遅延の基盤インタフェース作成中らしい、欲しい...
 - [楽しくやろう。](https://blog.boochow.com/) いつも楽しく参考にさせていただいています！

## ライセンス
 [Apache License v2.0](http://www.apache.org/licenses/LICENSE-2.0)に基づいてご利用ください。ご連絡は[layer8](https://twitter.com/layer812)までお願いします。