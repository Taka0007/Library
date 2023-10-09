N = int(input())
A = list(map(int, input().split()))

# 重複削除&ソート
sorted_unique_A = sorted(set(A))

# 座標圧縮マップ
coordinate_map = {value: index + 1 for index, value in enumerate(sorted_unique_A)}

# 座標圧縮を行い、Bに格納
B = [coordinate_map[a] for a in A]

print(*B)
