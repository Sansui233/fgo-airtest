from airtest.core.api import *
from cv2 import threshold
from threading import Thread

"""
# 命名规则
Img 结尾以图像匹配
Btn 为坐标匹配
Pos 为坐标合集
其他为组合操作
"""


class op:
    def attackBtn(delay=1.5):
        """
        战斗界面-攻击键钮
        """
        touch([1955, 1033])
        sleep(delay)

    def attackPos(x_num: int, y_num: int):
        """
        点击攻击的卡面，第一行宝具卡，第二行普通指令卡
        取值: (1,1)-(1,3)，(2,1)-(2,5)
        """
        positions = [
            [(600, 300), (1000, 300), (1570, 300)],
            [(230, 1000), (630, 1000), (1130, 1000), (1570, 1000), (1980, 1000)],
        ]
        touch(positions[x_num - 1][y_num - 1])

    def continueBattleBtn():
        """
        战斗结束-连续出击
        """
        touch([1485, 977])
        sleep(1)

    def eatApple():
        """
        检测是否出现苹果补充界面，出现了就补苹果
        """
        coor = exists(Template(r"common/黄金果实.PNG"))
        if coor:
            touch(coor)
            sleep(1)
            touch([1476, 988])
            sleep(1)

    def masterSkillChoose(num: int, delay=3):
        """
        选择 master 的技能,
        num: 御主技能位置，取值 1-3
        """
        touch((2066, 535))
        positions = [1558, 1717, 1856]
        touch((positions[num - 1], 535))
        op.skillConfirmBtn(delay)

    def masterChangeOrderPos(svt1: int, svt2: int, delay=5):
        """
        svt1, svt2 为从者位置，取值 1-6，且不可为相同数字
        """
        positions = [228, 629, 917, 1300, 1600, 2000]
        touch((positions[svt1 - 1], 587))
        sleep(0.3)
        touch((positions[svt2 - 1], 587))
        sleep(0.3)
        touch([1187, 1089])  # 进行更替
        sleep(delay)

    def nextBtn(delay=1):
        """
        战斗结束-下一步
        """
        touch([1898, 1092])
        sleep(delay)

    def refreshList(delay=4):
        """
        刷新好友列表
        """
        touch([1479, 225])  # 列表刷新
        sleep(1)
        touch([1472, 977])  # 是
        sleep(delay)

    @staticmethod
    def skillConfirmBtn(delay=3):
        touch([1483, 738])
        sleep(delay)

    def skillChoose(servant: int, skill: int, delay=3):
        """
        选择从者技能
        servant: 从者占位，取值1-3
        skill: 技能占位, 取值1-3
        """
        positions = [
            [(123, 1000), (279, 1000), (434, 1000)],
            [(669, 1000), (831, 1000), (982, 1000)],
            [(1219, 1000), (1379, 1000), (1535, 1000)],
        ]
        touch(positions[servant - 1][skill - 1])
        sleep(0.3)
        op.skillConfirmBtn(delay)

    def skillServantPos(svt: int, delay=3):
        """
        技能给其他从者时的选择从者界面
        svt: 从者位置，取值 1-3
        """
        positions = [567, 1082, 1657]
        touch([positions[svt - 1], 755])
        sleep(delay)

    def startTaskImg():
        """
        检测编队确认界面，如果出现了则按开始任务
        """
        coor = exists(Template(r"common/开始任务.png", threshold=0.8))
        if coor:
            touch(coor)
    
    @staticmethod
    def retryBtn():
        coor = exists(Template(r"common/重试.jpeg"))
        if coor: 
            touch(coor)


def unlimited(round=5):
    """
    抽无限池
    """
    def resetPresent():
        coor = wait(Template(r"common/重置礼物.jpeg", threshold=0.9), timeout=10)
        touch(coor)
        touch([1452, 983])  # 执行
        sleep(2)
        touch([1073, 983])  # 关闭
    
    stop_threads = False
    def detectInterrpt(interval=5):
        nonlocal stop_threads 
        while not stop_threads:
            sleep(5)
            op.retryBtn()
    
    th_intrpt = Thread(target=detectInterrpt)
    th_intrpt.start()

    for _ in range(1, round + 1):
        touch([650, 800], 135)
        try:
            resetPresent()
        except:
            touch([650, 800], 30)
            resetPresent()
    
    stop_threads = True
    th_intrpt.join()