# callbacksは細かい処理を指定したいときに使う
学習時の様々なタイミングで特定の処理をしたいときに，用いる．
`DefaultCallbacks class`や`examples/custom_metrics_and_callbacks.py`を参照．
- `def on_algorithm_init`
- `def on_create_policy`
- `def on_episode_created`

などが定義できる．

## custom environment
`string`のnameか，直接PythonのClassを直接指定できる．
```python
from ray.tune.registry imoprt register_env
import gymnasium as gym

register_env()
# def env_creator(env_config):
#     env = gym.make()
```

# Preprocessor
observationが`Proprocessor`と`Filter`によって，前処理されて`Model`に渡される．

## Built-in `Preprocessors`
- `Discrete`は単純にone-hot encodingされる
- `Tuple`と`Dict`は`flatten`されている
- 他のケースでは`preprocessor`は用いられず，生の`observation`が`model`に直接送られる
# モデル（Model）
## defaultの`Model`設定


