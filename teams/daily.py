# -*- encoding=utf8 -*-
from airtest.core.api import *
__author__ = "sansui233"
from lib.actions import op


def team1(left_round=0):
    '''
    通用1: 五加成短宝具队
    站位: 1大英雄，2班扬，3C呆，4任意光炮（50初始np）
    衣服: 20np充能服
    '''
    if left_round < 0:
        return

    op.chooseFriend([1000, 600])  # 助战选择，不限助战，坐标乱点

    # 战斗
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(1, 3)
    op.attack(1, 1, 2, 1, 2, 2, delay=8)
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(3, 1)
    op.skillChoose(3, 2, 2)
    op.attack(1, 2, 2, 1, 2, 2, delay=10)
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.attack(1, 1, 2, 1, 2, 2, delay=17)

    # 处理结尾
    op.ending(left_round > 0)


def teammogen(left_round=0):
    if left_round < 0:
        return
    op.chooseFriend([1000, 500])
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(1, 2, 1)
    op.masterSkillChoose(3, 1)
    op.attack(1, 1, 2, 4, 2, 5)
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(1, 1)
    op.skillChoose(3, 1)
    op.skillChoose(3, 2, 1)
    op.masterSkillChoose(1, 1)
    op.attack(1, 1, 2, 4, 2, 5)
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(2, 1, 2)
    op.skillChoose(2, 2, 2)
    op.skillChoose(2, 3, 2)
    op.skillChoose(3, 3, 2)
    op.attack(1, 2, 2, 3, 2, 5)
    op.finalAttack()  # 运气极其差时要补刀
    op.ending()


def teamqige(left_round=0):
    '''
    齐格 C呆 10np衣服
    站位: 齐呆呆
    '''
    if left_round < 0:
        return

    op.chooseFriend(r"teams/assets/C呆.jpeg")
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(1, 1)
    op.skillChoose(2, 1)
    op.skillChoose(3, 1)
    op.skillChoose(2, 2, 1)
    op.skillChoose(3, 2, 1)
    op.skillChoose(2, 3, 1)
    op.skillChoose(3, 3, 1)
    op.attack(1, 1, 2, 4, 2, 5)
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.attack(1, 1, 2, 4, 2, 5)
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(1, 2)
    op.masterSkillChoose(1, 1)
    op.attack(1, 1, 2, 4, 2, 5)
    # 这个队伍刷90本要补刀
    op.finalAttack()

    op.ending(left_round > 0)


def teamchin(left_round=0):
    '''
    通用: 五加成陈宫队
    站位: 1陈宫（50初始np），2C呆（助战），3C呆，4孔明，5兰陵王
    '''
    if left_round < 0:
        return

    op.chooseFriend(r"teams/assets/C呆.jpeg")
    # 一面
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(2, 1)
    op.skillChoose(2, 2, 1)
    op.skillChoose(2, 3, 0.4, 1)
    op.skillChoose(3, 3, 0.4, 1)
    op.attack(1, 1, 2, 1, 2, 2, 18)

    # 二面
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(2, 1, 1)
    op.skillChoose(2, 2)
    op.skillChoose(2, 3)
    op.skillChoose(1, 2)
    op.attack(1, 1, 2, 1, 2, 2, 18)

    # 三面
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(2, 2, 1)
    op.skillChoose(2, 3)
    op.skillChoose(3, 1)
    op.skillChoose(3, 2, 1)
    op.attack(1, 1, 2, 1, 2, 2, 18)

    op.ending(left_round > 0)
