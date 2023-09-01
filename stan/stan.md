# stan codeの概要
stan codeは次のブロックに分けられる
- `data`
- `parameters`
- `model`

`data`，`parameters`は各変数の属性を明示的に宣言するために必須．  
`model`にて事後分布を定義して，MCMCサンプルに用いる．




# targetとはなにか
MCMCは↓の式を用いてサンプリングする．
$$
\begin{align}
P(\bm{\theta|\mathcal{D}}) &= \frac{P(\mathcal{D}|\bm{\theta})P(\bm{\theta})}{P(\mathcal{D})} \propto P(\mathcal{D}|\bm{\theta})P(\bm{\theta})\\
&=\Big(\Pi^n_{i=1}model(\bm{x}_i|\bm{\theta})\Big)P(\bm{\theta}) 
\end{align}
$$
最後の行からわかるように，事後分布は複数の確率密度関数の積になっている．

Stan内部では事後分布を対数を取って利用しているので，
- 事後分布に積を追加することが
- 確率密度関数の対数に対して和をとること

に対応する．

この事後確率（の定数倍）の対数を取ったものを`target`と呼ぶので，`model`ブロックの中で上式を定義する際に，
- `<random variable> ~ <distoribution>`の形でなく，
- `target += <log distribution>`の形

でも書ける．








# 参考文献
[Stan - 高速MCMCでパラメータ推定](https://heavywatal.github.io/rstats/stan.html)
