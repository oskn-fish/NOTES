# torch.utils.data.DataLoaderはデータセットをいてレート可能な形にラップして使いやすくするもの
# torch.utils.data.Datasetはデータセット管理

# torch.nnにはモデル構築に必要なものが全て入っている

# gpu使用不可判定
```python
import torch.cuda
device = 'cuda' if torch.cuda.is_available() else 'cpu'
```

# ニューラルネットワークの定義
- `torch.nn.Module`を継承
- 順伝搬関数`forward`の実装
1. nnのスタックインスタンス`nn.Sequential`を生成
2. forward（順伝搬計算）時は`nn.Sequential`に入力`x`を入れる
```python
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28,512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
            nn.ReLU()
        )
    
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logitsお
```