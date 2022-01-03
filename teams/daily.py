# -*- encoding=utf8 -*-
from functools import wraps
from airtest.core.api import *
from cv2 import LSD_REFINE_STD, threshold
import logging

__author__ = "sansui233"
from actions import op

logging.basicConfig(level="INFO")

'''
通用1: 五加成短宝具队
站位: 1大英雄，2班扬，3C呆，4任意光炮（50初始np）
衣服: 20np充能服
'''
def team1(left_round=0):
    if left_round < 0:
      return
    # 1. 助战选择
    touch([1000, 600])
    sleep(.3)
    op.startTaskImg()
    # 2. 战斗
    sleep(5)
    wait(Template(r"common/攻击.jpeg",rgb=True),timeout=20,interval=1)
    op.skillChoose(1,3)
    op.attackBtn()
    op.attackPos(1,1)
    op.attackPos(2,1)
    op.attackPos(2,2)
    sleep(8)
    touch([1000,500])
    sleep(6)
    wait(Template(r"common/攻击.jpeg",rgb=True),timeout=20,interval=1)
    op.skillChoose(3,1)
    op.skillChoose(3,2,.3)
    op.skillServantPos(2)
    op.attackBtn()
    op.attackPos(1,2)
    op.attackPos(2,1)
    op.attackPos(2,2)
    sleep(10)
    wait(Template(r"common/攻击.jpeg",rgb=True),timeout=20,interval=1)
    op.masterSkillChoose(2,.3)
    op.skillServantPos(1)
    op.attackBtn()
    op.attackPos(1,1)
    op.attackPos(2,1)
    op.attackPos(2,2)
    sleep(17)

    ending()


'''
通用: 五加成陈宫队
站位: 1陈宫（50初始np），2C呆（助战），3C呆，4孔明，5兰陵王
'''
def teamchin(left_round=0):
    if left_round < 0:
        return

    # 1. 助战选择
    swipe_count = 7
    while True:
        coor = exists(Template(r"20212020圣诞/friend2.jpeg", threshold=0.9,rgb=True))
        if not coor:
            swipe([500, 900], [500, 500])
            swipe_count -= 1
        else:  # Choose friend and break
            touch(coor)
            sleep(1.5)
            break
        if swipe_count == 0:
            op.refreshList()
            swipe_count = 5

    op.startTaskImg()

    # 2. 战斗
    sleep(5)

    # 一面
    wait(
        Template(
            r"20212020圣诞/chin-ready.jpeg",
            rgb=True
        ),
        timeout=20,
        interval=1,
    )
    op.skillChoose(2, 1)
    op.skillChoose(2, 2, 0.4)
    op.skillServantPos(1)
    op.skillChoose(2, 3, 0.4)
    op.skillServantPos(1)
    op.skillChoose(3, 3, 0.4)
    op.skillServantPos(1)

    op.attackBtn()
    op.attackPos(1, 1)
    op.attackPos(2, 1)
    op.attackPos(2, 2)
    sleep(18)
    touch((1000,400))
    sleep(5)


    # 二面
    wait(
        Template(
            r"20212020圣诞/chin-ready.jpeg",
            rgb=True
        ),
        timeout=20,
        interval=1,
    )
    op.skillChoose(2, 1, 0.4)
    op.skillServantPos(1)
    op.skillChoose(2, 2)
    op.skillChoose(2, 3)
    op.skillChoose(1, 2)

    op.attackBtn()
    op.attackPos(1, 1)
    op.attackPos(2, 1)
    op.attackPos(2, 2)
    sleep(18)
    touch((1000,400))
    sleep(5)

    # 三面
    wait(
        Template(
            r"20212020圣诞/chin-ready.jpeg",
            rgb=True
        ),
        timeout=20,
        interval=1,
    )
    op.skillChoose(2,2,.4)
    op.skillServantPos(1)
    op.skillChoose(2,3)
    op.skillChoose(3,1)
    op.skillChoose(3,2,.3)
    op.skillServantPos(1)

    op.attackBtn()
    op.attackPos(1, 1)
    op.attackPos(2, 2)
    op.attackPos(2, 4)
    sleep(19)
    touch((1000,400),2)
    sleep(3)
    touch((1000,400),2)
    sleep(5)

    # 3. 结束
    wait(
        Template(
            r"common/与从者的羁绊.png", record_pos=(-0.351, -0.136), resolution=(2208, 1242)
        ),
        timeout=45,
        interval=1,
    )
    touch((100, 10))
    sleep(1)
    touch((100, 10))
    sleep(1)
    touch((100, 10))
    sleep(1)  # 防止意外情况，升级什么的
    op.nextBtn()
    op.closeFrdApplication()
    op.continueBattleBtn()
    if left_round != 0:
        op.eatApple()
    sleep(2)


'''
通用: 瞎几把打
'''
def teamxjbd(left_round=0):
    if left_round < 0:
        return
    # 1. 助战选择
    touch([1000, 600])
    op.startTaskImg()
    # 2. 战斗
    sleep(5)
    for _ in range(0,9):
      try:
        normalAttack()
      except:
        break

    ending()

'''
普通攻击
'''
def normalAttack():
    wait(Template(r"common/攻击.jpeg",rgb=True),timeout=20,interval=1)
    op.attackBtn()
    op.attackPos(2, 5)
    op.attackPos(2, 1)
    op.attackPos(2, 4)
    sleep(10)

'''
结尾动画
'''
def ending(left_round=0):
    wait(
        Template(
            r"common/与从者的羁绊.png", record_pos=(-0.351, -0.136), resolution=(2208, 1242)
        ),
        timeout=45,
        interval=1,
    )
    touch((100, 10))
    sleep(1)
    touch((100, 10))
    sleep(1)
    touch((100, 10))
    sleep(1)  # 防止意外情况，升级什么的
    op.nextBtn()
    op.closeFrdApplication()
    op.continueBattleBtn()
    if left_round != 0:
        op.eatApple()
    sleep(3)