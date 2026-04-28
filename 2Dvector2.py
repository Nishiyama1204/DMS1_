import math

# ベクトル(2次元)
a = [3,13] #東京のベクトル
b = [4,14] #札幌のベクトル

# --- 簡単版(成分による定義) ---
dot_component = a[0]*b[0] + a[1]*b[1]

# --- 複雑版(幾何学的定義)を求める準備 ---
# --- 各ベクトルの方向角(内積は使わない) ---
phi_a = math.atan2(a[1], a[0]) # ベクトルaの方向角
phi_b = math.atan2(b[1], b[0]) # ベクトルb

# なす角　θ
# theta = abs(phi_a - phi_b) # ベクトルaとbのなす角
# 正規化 (小さい方の角度を取るのが標準的)
delta = abs(phi_a - phi_b) # ベクトルaとbのなす角の絶対値
theta = min(delta, 2*math.pi - delta)   # ベクトルaとbのなす角

# cosθ(普通の三角関数)
cos_theta = math.cos(theta)

# --- ノルム ---
norm_a = math.hypot(a[0], a[1]) # ベクトルaのノルム
norm_b = math.hypot(b[0], b[1]) # ベクトルbのノルム

# --- 複雑版(幾何学的定義) ---
dot_geometric = norm_a * norm_b * cos_theta

# --- 結果の表示 ---
print("θ（度) =", math.degrees(theta))
print("内積計算（簡単版）:", dot_component)
print("内積計算（複雑版）:", dot_geometric)