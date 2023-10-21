# 参考資料論文

https://arxiv.org/abs/2210.04932

## issueに読んだ論文をまとめていく。

Issuesにサーベイした論文をゆっくりまとめる。
テンプレは模索中️。

最新のテンプレは👇
```
### 論文リンク

### 著者/所属機関

### 投稿年

## 概要：
## 研究背景

## 提案手法
 
## 実験

## 感想

## 参考

## どんなもの？

## 先行研究と比べてどこがすごい?

## 技術や手法のキモはどこ?

## どうやって有効だと検証した?

## 論文の主張やビジョンそのものに問題はないか？
```


# コードを変更したとき
プルリクを出してください。

https://qiita.com/samurai_runner/items/7442521bce2d6ac9330b

# 使用している点群データ
```
point_cloud_data/_point_cloud.ply
```
# windows GUI使い方
コマンドプロンプトを管理者権限で実行
```
ipcofig
```
Wireless LAN adapter Wi-Fi:IPv4 アドレスをの文字を引用して

```
export DISPLAY=< Wi-Fi:IPv4 アドレス>:0.0
echo $DISPLAY
```

```
xeyes
```

確認する

それかvscodeのエクステンションでpython PLY previewを入れる。

# octree実行
### octreeとは
https://tech-deliberate-jiro.com/open3-octree/

```
src/octree.py
```
# 床の穴を埋める。

```
src/histogram_point_generator.py
```
# docker実行
```
make run
```

# 次やること
- [x] 穴を埋めるためにhistogram_point_generator.pyを改造
- [x] docker構築
- [ ] Nerfの座標系と合わせる
- [ ] [unreal engine内で gltfのcollisionを設定する](https://forums.unrealengine.com/t/add-collision-and-socket-support-to-gltf-importer/133559)
- [ ] [unreal engine内で .plyは取り込めないのでgltfに変換](https://forums.unrealengine.com/t/add-collision-and-socket-support-to-gltf-importer/133559)あまりうまく行かない

# 参考文献のcollision設定
- [ ] 占有率のボクセル化: 予測された占有率をボクセル化し、それを利用してマーチングキューブアルゴリズムを使用してメッシュを計算します。(Nerfの作り方)
- [ ] シミュレーション内での衝突のためのメッシュ利用: このメッシュをシミュレーション内の衝突処理に利用します。
- [ ] COLMAPからのカメラポーズ取得: COLMAPからカメラポーズを取得し、それによって衝突メッシュの頂点も任意の参照フレームで表現されます。
- [ ] リジッド変換とスケールの推定: この参照フレームとシミュレータのワールドフレームとの間のリジッド変換とスケールを推定します。このために、最小二乗最適化を解決し、メッシュ内の支配的な床面の法線ベクトルがシミュレータのz軸と整列するように制約を設定します。
- [ ] Blenderの利用: Blenderを使って、この目的のためにメッシュの床上の点を手動で選択します。
- [ ] メッシュの手動回転: シミュレータのワールドフレームとの所望の整列を得るために、メッシュをz軸周りに手動で回転させます。
- [ ] NeRFとワールド間の相対スケールの計算: メッシュ内のオブジェクトのサイズと実世界でのサイズを比較して、NeRFとワールド間の相対スケールを計算します。
- [ ] 床頂点の置き換え: テクスチャの欠如によるアーティファクトを持つ可能性のあるメッシュの床頂点を、フラットプレーンで置き換えます。
- [ ] メッシュのクロップ: シミュレーションに必要な範囲にメッシュをクロップし、衝突計算を高速化します。

# RGB-DとNerfの一致評価

Voxel Grid:
https://ieeexplore.ieee.org/abstract/document/9653223

https://ieeexplore.ieee.org/document/8890921

https://tech-deliberate-jiro.com/downsampling-grid/

同じ空間をVoxelで区切ることで、各Voxel内の点群の位置と色を比較できます。Voxelの解像度は評価の精度に影響を与えるため、適切な解像度を選択することが重要です。
位置の評価:

各Voxel内で、RGB-D SLAMとNeRFによって生成された点群がどれだけ一致しているかを評価します。これには、各Voxel内の点の中心位置の平均や中央値を計算し、それらの位置の差を計算することが一般的です。
色の評価:

色の比較には、色空間での距離を計算することが一般的です。例えば、CIE76、CIE94、CIEDE2000などの色差公式を使用して、2つの色の差を計算できます。各Voxel内の点群の色の平均値を計算し、それらの色の差を評価することができます。
統計的評価:

位置と色の評価を組み合わせて、統計的に有意な差があるかどうかを評価することも可能です。これには、t検定やANOVA（分散分析）などの統計的手法を利用することができます。
可視化:

結果を可視化することで、RGB-D SLAMとNeRFの間でどのような違いがあるのかをより明確に理解できます。これには、点群のオーバーレイ、色の差のヒートマップ、または誤差のヒストグラムなどが利用できます。
