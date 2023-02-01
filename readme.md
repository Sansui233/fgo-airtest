# FGO-Airtest

FGO 全自动刷本 3T 脚本模板，速度接近手刷。对手机的控制依赖于 [Airtest](https://airtest.doc.io.netease.com/)，Airtest 能连接到的手机即可使用，理论上不限平台。但安卓已经有更方便的脚本了，所以这里主要针对 iOS。

主要优点
- 高度自定义 3T，适合宝具队
- 速度还不错，稍微逊色于手势录制，优于全图像匹配
- 不开虚拟机与模拟器，较小的 CPU 和内存负担

缺点
- 环境部署麻烦
- 首次录入屏幕坐标麻烦

<details>
 <summary>不同平台可使用的自动刷本方法汇总</summary>
 <ul>
  <li>Windows + Android: [FGO-py](https://github.com/hgjazhgj/FGO-py) 或 模拟器 + 按键精灵（如[BBchannel](https://www.bilibili.com/read/readlist/rl474502))</li>
  <li>Windows + iOS: [虫洞](https://er.run/) + 按键精灵（如[BBchannel](https://www.bilibili.com/read/readlist/rl474502))</li>
  <li>Mac + iOS: Airtest</li>
  <li>Mac + Android: Airtest 或 模拟器 + 按键精灵</li>
 </ul>
</details>

使用前先部署好环境（这一步需要花亿些时间）。airtest IDE 可以不用装，但得确保安装 airtest 的 python 模块。
- [Mac + iOS 环境部署教程](https://zhuanlan.zhihu.com/p/414629796)
- [Airtest 文档](https://airtest.doc.io.netease.com/tutorial/6_IOS_automated_testing/)

## 运行方式

下载此仓库。打开`daily.py`，参考已有例子编写自己编队的 3T 操作。编队的入口为助战选择界面，需要进入游戏的助战选择界面后开始运行。

然后运行 main.py 即可。运行前一定先**先[修改脚本](#修改脚本)，不要直接运行在你的编队上**（~~也没事最多浪费 40AP~~）

```shell
python3 main.py 编队函数名 运行次数
```

运行截图：
![](https://raw.githubusercontent.com/NamiLing/upic/master/uPic/W2zcvo.png)

## 修改编队

由于每个人 3T 的差异很大，需要根据自己的编队完全重写操作。

点击操作主要分为两种：
- 图像匹配后点击
- 根据坐标点击

### 1. 坐标点击

个人推荐能使用坐标点击的部分就直接点坐标，因为刷起来快。并且以后编写脚本也更快速。缺点是开始的工作量多一些。你需要获取所有用到的按钮的位置。

#### 1.1 修改 `actions.py`

战斗中会用到的所有操作（令咒除外）已经封装到 `lib/actions.py` 中的 `op` 类。根据此文件的 API 可以足够简洁地编写 3T 脚本。

由于不同手机的分辨率不同，使用时需要先更改为自己手机的坐标。此仓库包含 iPhone7 Plus 与 iPhone13 Pro 的坐标。如果您愿意贡献其他 iPhone 型号的坐标，欢迎 PR。

#### 1.2 如何获取按钮坐标

个人推荐的方法是，手机截图后，用 Photoshop、Mac 自带的 preview 一类的工具查看。Preview 在框选图片时会显示框选大小，从左上角开始框选则可取得按钮坐标。其他方法可以网上查阅。

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

上述截图准备好后，在 lib/iphone_example.py 中填入自己手机型号的坐标，并在 action.py 中 import 自己的手机坐标为 iphone 变量。

### 2. 图像匹配

如果选择用图像匹配点击为主，最好准备 AirTest IDE 编写代码（运行仍然不推荐开着 IDE，速度慢）。

此类教程 B 站很多。不再赘述。

需要的注意的是图像置信度，实测默认的 0.7 置信度（不带 RGB）下会把师匠的脸识别为 C呆。确保图像可以在任何情况下准确识别是稳定运行的关键。常见的方法是打开 RGB 校验以及提高置信度到 0.8 以上。

```python
Template(r"20212020圣诞/lls.png",threshold=0.9,rgb=True)
```

参考：[Airtest API](https://airtest.readthedocs.io/zh_CN/latest/all_module/airtest.core.api.html)

### 修改 `daily.py`
根据已有的编队写法，增加自己的编队。需要修改的部分为
- 助战选择
- 战斗打法

并一定要以 `op.ending()` 结尾，此函数会处理最后的动画并自动吃苹果。
### 意外情况

对于一些额外情况，比如手机断开连接、网络长时间加载、fgo 闪退等等……此类错误会可能让脚本停止运行，并且无法手动恢复。

对于网络长时间加载，解决方法是在需要网络连接的地方使用 airtest 的 wait，并且增加等待时长。以B服的情况，等上一分钟都是可能的。

对于断开连接重试，可另起线程检测截屏是否出现重试按钮。抽无限池的函数中已经带有此功能，实测检测时会卡约 1s 的操作时间。

另外，助战需要的从者如果比较少，选择助战可能会花费较长时间，这时请勿手动加速，可能会导致错误的点击影响 3T（除非你明白如何不会让程序误点）。
