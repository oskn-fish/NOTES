# rllibとのapi
## やり方1．Algorithm.Configのパラメータ空間に直接指定する
`param_space`は`Algorithm.Config`をわたしてもよい．
```python
import ray
from ray import air, tune

ray.init()

config = PPOConfig().training(lr=tune.grid_search([0.01, 0.001, 0.0001]))
tuner = tune.Tuner(
    param_space = config
)
```
##やりかた2．


# Key Concepts
1. Search Spaces（探索対象のパラメータの定義）
2. Trainables（ハイパラ渡す対象．rllibのconfigなど）
3. Search Algorithms
4. Scheduler（見込みのない実験の早期終了）
5. Tuner（Trialsを生成）
6. Analyses（Trialsの結果の分析）

![tune key concepts](/図/tune_key_concepts.png)

## Trainables
trainableは`score`の中途報告を`session`へ報告する．
最終的に`return`してもよい．
```python
from ray.air import session

def objective(x, a, b):
    return a*(x**0.5)+b

# やり方1
def trainable(config):
    for x in range(20):
        score = objective(x, config["a"], config["b"])
        # 中途報告
        session.report({"score":score})

# やり方2
def trainable(config):
    for x in range(20):
        score = objective(x, config["a"], config["b"])
    # 最終報告のみ
    return {"score":score}
```

## Search Space
探索空間と，パラメータのサンプリング方法を指定した辞書．
```python
config = {
    "uniform": tune.uniform(-5, -1),
    "randn": tune.randn(10, 2)
}
```

## `Tuner.fit`によるTrialsの生成
```python
tuner = tune.Tuner(
    trainable, 
    param_space=search_space, 
    tune_config=tune.TuneConfig(num_samples=10)
)
turer.fit()
```

## Search Algorithms
探索アルゴリズムの指定は，`tune.TuneConfig`内で行う．
```python
from ray.tune.search.bayesopt import BayesOptSearch
from ray import air

# Define the search space
search_space = {"a": tune.uniform(0, 1), "b": tune.uniform(0, 20)}

algo = BayesOptSearch(random_search_steps=4)

tuner = tune.Tuner(
    trainable,
    tune_config=tune.TuneConfig(
        metric="score",
        mode="min",
        search_alg=algo,
    ),
    run_config=air.RunConfig(stop={"training_iteration": 20}),
    param_space=search_space,
)
tuner.fit()
```

# rllib Getting started
```python 
import ray 
from ray import air, tune

ray.init()

config = 

```

