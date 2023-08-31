# matplotlibには2つのインターフェースがある
## pyplotインターフェース
plt.~で記述するもの．
後述のobjectインターフェースの糖衣構文．

## objectインターフェース
Figureは画面全体，axはグラフのオブジェクト．**axesはaxの複数形で，axisは軸であることに注意!**
```
fig, ax = plt.subpots()
ax.plot(x, y)
```
で生成できる．

![matplotlib overview](/図/matplotlib_overview.avif)



# 参考
https://qiita.com/skotaro/items/08dc0b8c5704c94eafb9
https://qiita.com/DeepTama/items/dfb714f155b529711109
