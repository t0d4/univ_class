# 座標の集合からグラフ/アニメーションを作成する
このフォルダに含まれる`v_30_degree_20.csv`のような`(時刻, x座標, y座標)`の記述されたファイルを読み取り, 以下のようなグラフやアニメーションを生成します.

注) v_30_degree_20.csvは, 初速度v=30[m/s], 射出角度theta=30[degree]の意味.

<img src=graph.png width="40%">
<img src=animation.gif width="40%">

## Usage:
 python illustrate_graph.py [CSV filenames separated by space] {options}

 Options:
 - --export-png: export graph as a png file
 - --export-gif: export animation as a gif file
 - --remove-trace: remove trace in animation. Must be used with --export-gif

## Requirements:
  - numpy
  - matplotlib
  - pillow
