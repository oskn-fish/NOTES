# 基本的な使い方
```python
class TestClass:
    def square(self, a, b):
        """
        >>> testclass = TestClass()
        >>> testclass.square(1, 2)
        3
        >>> testclass.square(-1,0)
        -1
        """
        return a+b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

## なぜ`if __name__ == "__main__"`ではだめか
自作モジュールを`import`しているとき，`path`的にエラーが出る．

## なぜdoctestではだめか
`class`のメソッドをテストするときに

## プロジェクト構成
### `test folder`を分ける
わけると，`test file`から`module`への相対的な`path`がずれるため，`python`の環境変数的なところをいじらないといけない．
`tests/context.py`に
```python
import os
import sys
# module検索リストの0番目に自作モジュールを追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sample
```
### 参考
[Structuring Your Project](https://docs.python-guide.org/writing/structure/)

