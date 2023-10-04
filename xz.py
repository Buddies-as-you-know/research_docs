import open3d as o3d
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# ステップ1: .ply ファイルをロード
pwd = os.getcwd()
pcd = o3d.io.read_point_cloud(pwd+"/data/_point_cloud.ply")

# ステップ2: 法線推定
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# ステップ3: 法線が向きを揃える (オプショナル)
pcd.orient_normals_towards_camera_location(camera_location=np.array([0., 0., 0.], dtype="float64"))

# ステップ4: Poisson Surface Reconstructionを使用してメッシュを作成
poisson_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8)[0]

# ステップ3: メッシュの頂点を取得し、XY平面に射影 (Z座標を0に設定)
vertices = np.asarray(poisson_mesh.vertices)
vertices_projected = vertices.copy()
vertices_projected[:, 2] = 0  # Z座標を0に設定

# ステップ4: XY平面にビンを作成し、各ビンに対する頂点のカウントを計算
xy_bins = {}  # xy_binsに変更
for vertex in vertices_projected:
    xy_bin = tuple(vertex[:2])  # vertex[:2]に変更
    xy_bins[xy_bin] = xy_bins.get(xy_bin, 0) + 1  # xy_binsに変更

# ステップ5: 閾値以上のカウントを持つビンを地面として扱う
threshold = 5  # この閾値は変更可能
ground_bins = {k: v for k, v in xy_bins.items() if v >= threshold}  # xy_binsに変更

# 新しい点群を生成
new_points = []
new_colors = []  # 新しいカラーリストを追加
norm = Normalize(vmin=0, vmax=max(ground_bins.values()))  # カウントの正規化
cmap = plt.get_cmap("viridis")  # 使用するカラーマップを選択

for xy_bin, count in ground_bins.items():  # xy_binに変更
    for i in range(count):
        new_points.append([xy_bin[0], xy_bin[1], 0])  # Z座標は0に設定
        new_colors.append(cmap(norm(count))[:3])  # カウントに基づいて色を割り当て

# 新しい点群をOpen3DのPoint Cloudオブジェクトに変換
new_pcd = o3d.geometry.PointCloud()
new_pcd.points = o3d.utility.Vector3dVector(np.array(new_points))
new_pcd.colors = o3d.utility.Vector3dVector(np.array(new_colors))  # カラーを設定

# 結果を表示
#o3d.visualization.draw_geometries([new_pcd])

# 結果を保存
o3d.io.write_point_cloud("output_xz.ply", new_pcd)