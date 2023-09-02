# 使い方
```python
import stan
import matplotlib.pyplot as plt
import arviz as az
# jupyterで使うときは必要
import nest_asyncio
nest_asyncio.apply()

posterior = stan.build(stan_code, data=data, random_seed=1)
fit = posterior.sample(num_chains=4, num_samples=1000)
df = fit.to_frame()

az.plot_trace(fit)
plt.show()
```


# stan code のブロック
stan codeは次のブロックに分けられる
- `data`
- `parameters`
- `model`
- `generated quantities`
## data・parameters
`data`，`parameters`は各変数の属性を明示的に宣言するために必須．  

## model
`model`にて事後分布を定義して，MCMCサンプルに用いる．

## generated quantities
`generated quantities`はパラメータのサンプリングには使わない．サンプルした値を使って何らかの値を取得すると気に使う．例えば，事後予測分布を取得できる．  
事後予測分布は，
1. モデルパラメータをサンプリングすることによりモデルをサンプリングし，
2. そこからさらにデータをサンプリングする．

このように，モデルパラメータのサンプルから直接計算できる量を`generated quantities`を用いてサンプリング剃ることができる．

# 型（配列・ベクトル・行列）
`vector`，`matrix`は数学的にvector，matrixなので行列演算などが定義されているところがarrayと違う．
## array
`real x[5]`のように定義．

## vector
`vector[10] v`のように定義．


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
[data, parameters, modelなどのブロックの意味と使い方](https://stats.biopapyrus.jp/bayesian-statistics/stan/stan-block.html)  
[Stanのデータ型についてまとめてみた](https://qiita.com/hoxo_m/items/e4dab11fed062689eff2)