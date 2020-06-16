# Engine游戏引擎说明

## 结构说明
1. Engine 本身为引擎核心模块

## 初始化

Engine 使用一个 `str` 或者 `dict` 来设定游戏的一些基本信息，你首先需要将它转化成 `GlobalSettings` 对象，然后直接构造一个 `Engine` 就可以了

以下属性是必须的

* `windows_size` 

* `windows_name`

* `windows_var`

* `frame_rate`

```
game_setting = '''{
    "windows_size" : [960, 540],
    "windows_name" : "game",
    "windows_var" : "screen",
    "frame_rate" : 30,
    "resizable" : true,
    "resource" : {
        "ball" : ["image", "intro_ball.gif"]
    }
}'''

game_setting = Engine.GlobalSettings(game_setting)
engine = Engine.Engine(game_setting)

```

之后你可以得到两个有用的对象

`engine.screen`

`engine.asset`


