#２次元ベクトルの内積計算が簡単版と複雑版で一致することをPythonプログラミングで確認してみましょう。

# 簡単版の内積計算
def dot_product_simple(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] 

# 複雑版の内積計算
def dot_product_complex(v1, v2):
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total

# ベクトルの定義
sapporo = [4, 14]
tokyo = [3, 13]   

# 内積の計算
simple_result = dot_product_simple(sapporo, tokyo)
complex_result = dot_product_complex(sapporo, tokyo)

# 結果の表示
print("簡単版の内積計算結果:", simple_result)
print("複雑版の内積計算結果:", complex_result)

# 結果の確認
if simple_result == complex_result:
    print("両方の内積計算結果は一致しています。")
else:    print("両方の内積計算結果は一致していません。")  