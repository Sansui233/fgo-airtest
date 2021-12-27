# -*- encoding=utf8 -*-
from functools import wraps
from actions import op, unlimited

__author__ = "sansui233"

from airtest.core.api import *
from cv2 import LSD_REFINE_STD, threshold
from math import floor
import logging

auto_setup(__file__)
connect_device("iOS:///127.0.0.1:8100")
logging.basicConfig(level='INFO')

def main():
    # 执行编队
    wrapTimes(teamlls)(calcRound(consume=5, now=121))
    # 抽无限池，需要手动进入无限池的页面。或者写三行 touch 自动进去
    # unlimited(10)
    logging.info("肝完了")

# 3T 编队脚本
def teamlls(left_round=0):
    if left_round < 0:
        return

    # 1. 助战选择
    swipe_count = 7
    while True:
        coor = exists(
            Template(
                r"20212020圣诞/friend1.png",
                threshold=0.8,
                rgb=True,
                resolution=(2208, 1242),
            )
        )
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
            r"20212020圣诞/lls-ready.png",
            record_pos=(-0.081, 0.086),
            resolution=(2208, 1242),
        ),
        timeout=20,
        interval=1,
    )
    op.skillChoose(3, 1, 0.5)
    op.skillServantPos(2)
    op.skillChoose(3, 2)
    op.skillChoose(3, 3)
    op.skillChoose(2, 1)
    op.masterSkillChoose(3, 0.5)
    op.masterChangeOrderPos(3, 4)
    op.skillChoose(3, 3, 0.5)
    op.skillServantPos(2)
    op.skillChoose(3, 2, 0.5)
    op.skillServantPos(2)

    op.attackBtn()
    op.attackPos(1, 2)
    op.attackPos(2, 1)
    op.attackPos(2, 2)
    sleep(20)

    # 二面
    wait(
        Template(
            r"20212020圣诞/lls-ready.png",
            record_pos=(-0.081, 0.086),
            resolution=(2208, 1242),
        ),
        timeout=20,
        interval=1,
    )
    op.skillChoose(1, 2, 0.5)
    op.skillServantPos(1)
    op.skillChoose(1, 3)
    op.skillChoose(3, 1)

    op.attackBtn()
    op.attackPos(1, 1)
    op.attackPos(2, 2)
    op.attackPos(2, 3)
    sleep(20)

    # 三面
    wait(
        Template(
            r"20212020圣诞/lls-ready.png",
            record_pos=(-0.081, 0.086),
            resolution=(2208, 1242),
        ),
        timeout=20,
        interval=1,
    )
    op.skillChoose(2, 3)
    op.masterSkillChoose(1)
    op.attackBtn()
    op.attackPos(1, 2)
    op.attackPos(2, 2)
    op.attackPos(2, 4)
    sleep(32)

    # 按卡面补刀
    while exists(
        Template(
            r"20212020圣诞/shanshan.png",
            record_pos=(-0.144, -0.063),
            resolution=(2208, 1242),
        )
    ):
        op.attackBtn()
        card = 3
        while card != 0:
            lls = exists(
                Template(
                    r"20212020圣诞/lls.png",
                    threshold=0.9,
                    record_pos=(-0.397, 0.076),
                    resolution=(2208, 1242),
                )
            )
            if lls:
                touch(lls)
            else:
                yj = exists(
                    Template(
                        r"20212020圣诞/yj.png",
                        threshold=0.9,
                        record_pos=(0.205, 0.089),
                        resolution=(2208, 1242),
                    )
                )
                if yj:
                    touch(yj)
                else:
                    cdai = exists(
                        Template(
                            r"20212020圣诞/cdai.png",
                            threshold=0.9,
                            record_pos=(-0.196, 0.091),
                            resolution=(2208, 1242),
                        )
                    )
                    if cdai:
                        touch(cdai)
            card = card - 1
        sleep(15)

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
    sleep(3)

def calcRound(consume=12, now=139, perApple=139):
    """
    在预计消耗苹果的基础上浮动 2 个苹果,使得体力剩余更少

    consume: 消耗苹果数
    now: 目前的体力
    perApple: 一个金苹果的体力
    返回值: 3T编队执行次数
    """
    l = []
    for i in range(-2, 3):
        l.append(((consume + i) * perApple + now) % 40)
    left = min(l)
    i = l.index(left)
    if consume + i - 2 > 0:
        result = floor(((consume + i - 2) * perApple + now) / 40)
        logging.info("消耗 %d 个苹果，剩体力 %d ",consume + i - 2,left)
        return result
    else:
        result = floor((consume * perApple + now) / 40)
        logging.info("消耗 %d 个苹果，剩体力 %d ", consume, l[2])
        return result
        
def wrapTimes(team_func):
    """
    指定某个函数执行多次

    用法: wrapTimes(afunc: function)(times: int)
    afunc: 目标函数名
    times: 次数
    """
    round = 1
    def wrapped(times:int):
        nonlocal round
        while(round <= times):
            logging.info("执行第 %d 轮",round)
            logging.info("剩余执行轮数: %d", times - round)
            team_func(times - round)
            round += 1
    return wrapped


# 主程序
if __name__ == "__main__":
    main()
