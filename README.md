# 参考資料論文

https://arxiv.org/abs/2210.04932

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
docker-compose build
docker-compose up
```

# 次やること
- [ ] 穴を埋めるためにhistogram_point_generator.pyを改造

# 参考文献のcollision設定
- [ ] 占有率のボクセル化: 予測された占有率をボクセル化し、それを利用してマーチングキューブアルゴリズムを使用してメッシュを計算します。
- [ ] シミュレーション内での衝突のためのメッシュ利用: このメッシュをシミュレーション内の衝突処理に利用します。
- [ ] COLMAPからのカメラポーズ取得: COLMAPからカメラポーズを取得し、それによって衝突メッシュの頂点も任意の参照フレームで表現されます。
- [ ] リジッド変換とスケールの推定: この参照フレームとシミュレータのワールドフレームとの間のリジッド変換とスケールを推定します。このために、最小二乗最適化を解決し、メッシュ内の支配的な床面の法線ベクトルがシミュレータのz軸と整列するように制約を設定します。
- [ ] Blenderの利用: Blenderを使って、この目的のためにメッシュの床上の点を手動で選択します。
- [ ] メッシュの手動回転: シミュレータのワールドフレームとの所望の整列を得るために、メッシュをz軸周りに手動で回転させます。
- [ ] NeRFとワールド間の相対スケールの計算: メッシュ内のオブジェクトのサイズと実世界でのサイズを比較して、NeRFとワールド間の相対スケールを計算します。
- [ ] 床頂点の置き換え: テクスチャの欠如によるアーティファクトを持つ可能性のあるメッシュの床頂点を、フラットプレーンで置き換えます。
- [ ] メッシュのクロップ: シミュレーションに必要な範囲にメッシュをクロップし、衝突計算を高速化します。