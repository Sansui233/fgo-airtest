# FGO-Airtest

FGO 全自动刷本 3T 脚本模板，速度接近手刷。对手机的控制依赖于 [Airtest](https://airtest.doc.io.netease.com/)，Airtest 能连接到的手机即可使用，理论上不限平台。但安卓已经有更方便的脚本了，所以这里主要针对 iOS。

不同平台可使用的自动刷本方法汇总：
- Windows + Android: [FGO-py](https://github.com/hgjazhgj/FGO-py) 或 模拟器 + 按键精灵
- Windows + iOS: [虫洞](https://wormhole.app/) + 按键精灵
- Mac + iOS: Airtest
- Mac + Android: Airtest 或 模拟器 + 按键精灵


使用前先部署好环境（这一步可能需要花一些时间）。airtest IDE 可以不用装，但得确保安装 airtest 的 python 模块。
- [Mac + iOS 环境部署教程](https://zhuanlan.zhihu.com/p/414629796)
- [Airtest 文档](https://airtest.doc.io.netease.com/tutorial/6_IOS_automated_testing/)

## 运行方式

下载此仓库。仓库中提供一个刷 90+ 本 3T 通用模板，见 `fgotest.py`，包含自动补刀和自动喂金苹果，带自动循环抽无限池。此脚本的入口为助战选择界面，需要进入助战选择界面后开始运行。

以下运行仅为示例，按自己的编队写的流程，**请先[修改脚本](#修改脚本)，不要直接运行在你的编队上**。

```shell
python3 fgotest.py
```

## 修改脚本

由于每个人 3T 的差异很大，需要根据自己的编队完全重写操作。

对图像的操作，主要分为两种
- 图像匹配
- 坐标点击

### 1. 坐标点击

个人推荐能使用坐标点击的部分就直接点坐标，因为刷起来快。并且以后编写脚本也更快速

缺点是开始的工作量多一些。你需要获取所有用到的按钮的位置。

#### 1.1 修改 `actions.py`

战斗中会用到的所有操作（令咒除外）已经封装到 `actions.py`。根据此文件的 API 可以足够灵活而简洁地编写 3T 脚本。

操作主要根据画面坐标进行点击，由于不同手机的分辨率不同，使用时需要先更改为自己的坐标。此仓库的坐标基于 iPhone 7 Plus。

如果您愿意贡献其他 iPhone 型号的坐标，欢迎 PR。

#### 1.2 如何获取按钮坐标
个人推荐的方法是，手机截图后，用 Photoshop、Mac 自带的 preview 一类的工具查看。Preview 框选图片是会显示框选大小，从左上角开始框选则可取得按钮坐标。其他方法可以网上查阅。

用到的坐标 / 需要截图的界面有：
- 助战选择
- 助战选择确认
- 编队界面
- 开始战斗界面，同时展开御主技能
- 技能确认界面
- 技能选人界面（技能给别人的时候）
- 换人选择界面
- 结束战斗时的“下一步”
- 结束战斗时的“连续出击”
- 无限池重置确认、道具补充完成页（活动用）

上述截图准备好后，修改 `actions.py` 中的所有 `touch`方法中的坐标和`positions`。部分`touch`用的是图片，可不修改。

### 2. 图像匹配

如果选择用图像匹配点击为主，最好准备 AirTest IDE 编写代码（运行仍然不推荐开着 IDE，速度慢）。

此类教程 B 站很多。不再赘述。

参考：[Airtest API](https://airtest.readthedocs.io/zh_CN/latest/all_module/airtest.core.api.html)

### 修改 `fgotest.py`

此文件中包含了一个 3T 编队的基本写法。复制一份，需要修改的部分为

- 助战图
- 每一回合的操作（使用 `actions.py` 中的 op 类）
- 补刀识别图（不用补刀可无视）

请先测试好编队确保能 3T。对于一些额外情况，比如手机断开连接、网络长时间加载、fgo 闪退等等……此类错误会可能让脚本停止运行，并且无法手动恢复。

另外，助战需要的从者如果比较少，选择助战可能会花费较长时间，这时请勿手动加速，可能会导致错误的点击影响 3T（除非你明白如何不会让程序误点）。

### 监控刷本进度

因为 airtest 本身会输出大量 debug 信息，并且未见 API 中未提供日志级别相关的封装。所以不建议直接挂在终端看输出。

可以将运行输出重定向到一个 log 文件（见 `run.sh` 中的写法)， `tail` 查看。

```shell
python3 fgotest.py >> run.log 2>&1 &
tail -f -n 10000 run.log | grep "INFO:root\|error\|Error"
```

