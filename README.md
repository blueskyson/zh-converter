## zh Converter 繁簡中文轉換

受 [OpenCC](https://github.com/BYVoid/OpenCC) 啟發，可以連慣用語一起翻譯，或選擇完全照翻。

```
usage: zhc.py [-h] [-ts] [-st] [-ni] input

A translator for traditional and simplified Chinese

positional arguments:
  input

optional arguments:
  -h, --help        show this help message and exit
  -ts, --trad2simp  Convert string from traditional to simplified
  -st, --simp2trad  Convert string from simplified to traditional
  -ni, --noidiom    Do not convert into local idioms when translating
```

繁轉簡：

```
$ python zhc.py -ts "陣列 (Array) 是置於連續的記憶體"
数组 (Array) 是置于连续的内存
```

```
$ python zhc.py -ts -ni "陣列 (Array) 是置於連續的記憶體"
阵列 (Array) 是置于连续的记忆体
```

簡轉繁：

```
$ python zhc.py -st "数组 (Array) 是置于连续的内存"
陣列 (Array) 是置於連續的記憶體
```

```
$ python zhc.py -st -ni "数组 (Array) 是置于连续的内存"
數組 (Array) 是置於連續的內存
```

繁簡字源：[fanjian](https://github.com/kfcd/fanjian)  
片語、繁簡用語詞源：[OpenCC](https://github.com/BYVoid/OpenCC)
