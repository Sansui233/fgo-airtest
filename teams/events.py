# -*- encoding=utf8 -*-
import logging
from airtest.core.api import *
__author__ = "sansui233"
from lib.actions import op


def teammogen(left_round=0):
    if left_round < 0:
        return
    op.chooseFriend([1294, 1087])
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
    op.ending(left_round > 0)


def teamdmogen(left_round=0):
    if left_round < 0:
        return

    op.chooseFriend([1294, 800])
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(3, 1)
    op.skillChoose(2, 3)
    op.attack(1, 2, 2, 3, 2, 5, 10)
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(1, 1)
    op.skillChoose(2, 3, 1)
    op.attack(1, 1, 2, 3, 2, 5)
    wait(Template(r"common/攻击.jpeg", rgb=True), timeout=20, interval=1)
    op.skillChoose(2, 1, 1)
    op.skillChoose(2, 2, 1)
    op.skillChoose(3, 2, 1)
    op.skillChoose(3, 3, 1)
    op.masterSkillChoose(1, 1)
    op.attack(1, 1, 2, 3, 2, 5)
    op.ending(left_round > 0)
