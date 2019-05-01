"""
基地臺位址選擇
- n 個城鎮: 編號 1 ~ n
- n 個城鎮中挑選 p 個城鎮設置基地臺
8個城鎮: 人口數 Pi 由城鎮 1 至城鎮 8 分別是 10、15、10、20、20、25、15 和 10
P1=10, P2=15.....P8=10

假設覆蓋半徑 d=3，要如何用你的演算法找出 p=3 個城鎮來設置基地臺呢？

第一列存放三個整數 n、p 跟 d
第二列至第 n+1 列
第 i 列存放三個整數 xi−1、yi−1 與 Pi−1
​分別表示第 i−1 個城鎮的 xx 座標、yy 座標和人口數。
在任意一列中，兩個數字之間都以一個空白隔開。
已知 2≤n≤1000、n2≤p≤n、−100≤xi≤100、−100≤yi≤100、1≤Pi≤100。不會有兩個城鎮落在同一個地點。
**兩點之間的距離算法:
  int(sqrt(((x1-x2)**2) + ((y1-y2)**2)))
"""

from math import sqrt

# 初始測試資料
# indata = "16 4 10"  # n, p, d:半徑距離
# 
# p1=[-49,-62,36]
# p2=[-78,-68,35]
# p3=[64,78,38]
# p4=[54,17,21]
# p5=[27,-22,34]
# p6=[-76,44,12]
# p7=[27,-29,18]
# p8=[-29,40,16]
# p9=[-26,10,12]
# p10=[46,69,24]
# p11=[-76,-67,16]
# p12=[80,35,32]
# p13=[-54,-11,14]
# p14=[-68,-70,18]
# p15=[73,44,38]
# p16=[-80,14,24]
# pn = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]

# 初始測試資料
# p1 = [3, -2, 10]    # x, y, population
# p2 = [-1, 1, 15]
# p3 = [-1, 4, 10]
# p4 = [3, 2, 20]
# p5 = [4, 3, 20]
# p6 = [-3, -4, 25]
# p7 = [2, -3, 15]
# p8 = [0, 2, 10]
# pn = [p1, p2, p3, p4, p5, p6, p7, p8]

# indata = "8 3 3"  # n, p, d:半徑距離


indata = input("請輸入n p d(以空白隔開): ")
# 從第一列取得資料 n: n_city, p: g_base_no, d: radius
indata = indata.split(" ")
for i in range(len(indata)):    # Convert String to int
    indata[i] = int(indata[i])

n_city = indata[0]      # amount number of cities
g_base_no = indata[1]   # amount number of g_base
radius = indata[2]      # radius
print("城鎮總數:", n_city, "基地台:", g_base_no, "半徑範圍:", radius)

# 取得 n_city 後 loop 輸入每個城鎮 x,y座標及人口數
pn = []
for i in range(n_city):
    p = input("請輸入x y 人口(以空白隔開): ")
    p = p.split(" ")
    for j in range(len(p)):     # Convert String to int
        p[j] = int(p[j])
    pn.append(p)
# print(pn)

# 將城鎮的座標資料轉為距離清單, 並將人口數各自取出
dst_list = []
pop_list = []
for i in range(len(pn)):
    dst_tmp = []        # 臨時產生的距離清單
    last_x = pn[i][0]
    last_y = pn[i][1]
    pop_list.append(pn[i][2])
    #print("loop i:", i, "last_x=", last_x, "last_y=", last_y)
    for j in range(len(pn)):
        x = pn[j][0]
        y = pn[j][1]
        # 計算距離並重新寫入到距離清單
        dst = round(float(sqrt((((last_x) - (x)) ** 2) + (((last_y) - (y)) ** 2))), 2)
        #print("  loop j:", j, "x=", x, "y=", y, "dst:", dst)
        dst_tmp.append(dst)
    #print(dst_tmp)
    dst_list.append(dst_tmp)
print("各城鎮間的距離清單:\n", dst_list)
print("各城鎮的人口清單\n", pop_list)

"""
1. 在所有城鎮中，你找出「如果蓋在這裡，將可以覆蓋最多人」的城鎮
2. 如法泡製，在所有還沒有基地臺的城鎮中，找出「如果蓋在這裡，將可以覆蓋最多還沒被覆蓋的人」的城鎮
**條件: 
如果在任一時刻遇到有兩個以上的城鎮可以被選，就選編號較小的那個。

"""
# 設定未知的距離的初始值: dst (城鎮A 至 城鎮B 用來計算是否兩地距離 小於等於 半徑距離(d))
# 設定初始基地台選定的地點: gbase_list
# 設定初始總和人口數: max_pop
origin = 0     # 初始開始的城鎮

tour = [origin]     # 下一個要檢查的城鎮會放到 tour
unvisited = []      # 紀錄目前還沒去過的城鎮
base = []
cand = 0
for i in range(n_city):
    unvisited.append(i)
unvisited.remove(origin)
print("尚未進行的城鎮", unvisited)

amount_pop = 0
for g in range(g_base_no):
    print("loop start")
    cand_list = []
    cur = origin
    max_pop = -1
    for i in range(n_city):
        next = -1
        count_pop = 0
        print("蓋在城鎮", i+1,  dst_list[i])
        for j in range(len(dst_list[i])):
            if dst_list[i][j] <= radius:
                count_pop = count_pop + pop_list[j]
                print("城鎮:", j+1, "人口數:", pop_list[j])
        print("------總和人數:", count_pop)
        if max_pop < count_pop:
            max_pop = count_pop
            cand = i
            count = 1
        elif max_pop == count_pop:
            count += 1

    print("最多人數:", max_pop, "在城鎮:", cand + 1, "相同人口數筆數:", count)

    amount_pop = amount_pop + max_pop
    base.append(cand+1)

    # 選擇基地台位置後, 將pop_list[] 被覆蓋的城鎮人口數 歸0
    print("基地台:", dst_list[cand])
    for i in range(len(dst_list[cand])):
        if dst_list[cand][i] <= radius:
            pop_list[i] = 0
            print("城鎮:", i+1, "人口", pop_list[i])
            if count > 1:
                cand_list.append(i+1)
    print("更新後 pop_list:", pop_list)
    print("有相同的筆數的城鎮", cand_list)
    print("--------------------------------------------------------")

print(base, amount_pop)

"""
以最短距離的方式找尋下一個城鎮
origin = 0     # 初始開始的城鎮

tour = [origin]     # 下一個要檢查的城鎮會放到 tour
tourLen = 0         # 一個loop 後的距離加總數
unvisited = []      # 紀錄目前還沒去過的城鎮
for i in range(n_city):
    unvisited.append(i)
unvisited.remove(origin)
print("尚未進行的城鎮", unvisited)

cur = origin
for i in range(n_city - 1):
    # find the next location(距離最近的) to visit
    next = -1
    minDst = 999
    for j in unvisited:
        if dst_list[cur][j] < minDst:
            next = j
            minDst = dst_list[cur][j]
        print("  [cur][j]=", cur, j, dst_list[cur][j], "minDst=", minDst)

    # move "next" from unvisited to tour
    unvisited.remove(next)
    tour.append(next)
    tourLen = tourLen + minDst

    # run the next iteration from next location
    cur = next
    print("i圈:", i, "unvisited:", unvisited, "tour:", tour, "下個城鎮:", cur)
    print("距離 tourLen=", tourLen)

# complete the tour
tour.append(origin)
tourLen = tourLen + dst_list[cur][origin]

print("檢查過的城鎮:", tour, "距離:", tourLen)
"""


