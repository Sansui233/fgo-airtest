from airtest.core.api import *
from cv2 import threshold
from threading import Thread
from lib.iphone7_plus import iphone7p as iphone


class op:
    """
    各种点击操作
    """
    def attack(x: int, y: int, x2: int, y2: int, x3: int, y3: int, delay=20):
        """
        开始攻击，传入三张卡的位置和宝具时间，默认20s
        (x,y)取值: (1,1)-(1,3)，(2,1)-(2,5)
        第一行宝具卡，第二行普通指令卡
        """
        touch(iphone.attackBtn)
        sleep(1.5)
        touch(iphone.attackPos[x - 1][y - 1])
        touch(iphone.attackPos[x - 1][y - 1])
        sleep(delay)
        touch((10, 300))
        sleep(5)

    def chooseFriend(friend):
        """
        助战选择，传入图片文件路径，或一个屏幕坐标，比如(1121,332)
        """
        if not isinstance(friend, str):  # if not string,treate it as coordiante
            touch(friend)
            sleep(1)
            return
        swipe_count = 7
        while True:
            coor = exists(Template(friend, threshold=0.8, rgb=True))
            if not coor:
                swipe([500, 900], [500, 500])
                swipe_count -= 1
            else:  # Choose friend and break
                touch(coor)
                sleep(1.5)
                break
            if swipe_count == 0:
                touch(iphone.refreshList)  # 列表刷新
                sleep(1)
                touch(iphone.refreshBtn)  # 是
                sleep(1)
                swipe_count = 5
        if swipe_count == -1:
            return  # TODO 错误处理
        coor = exists(Template(r"common/开始任务.png", threshold=0.8))
        if coor:
            touch(coor)
        sleep(5)

    def skillChoose(servant: int, skill: int, svt=-1, delay=3):
        """
        选择从者技能
        servant: 从者位置，取值1-3
        skill: 技能位置, 取值1-3
        svt: （可选）单体技能给别人的位置，取值 1-3
        """
        touch(iphone.skillChoose[servant - 1][skill - 1])
        touch(iphone.skillConfirmBtn)
        sleep(.3)
        touch(1162, 361)
        if svt != -1:
            touch(iphone.skillSvtPos[svt - 1])
            touch((10, 300))
        sleep(delay)

    def masterSkillChoose(num: int, svt=-1, delay=3):
        """
        选择 master 的技能,
        num: 御主技能位置，取值 1-3
        svt: （可选）单体技能给别人的位置，取值 1-3
        """
        touch(iphone.masterSkill)
        touch(iphone.masterSkillPos[num - 1])
        touch(iphone.skillConfirmBtn)
        touch(100, 10)
        if svt != -1:
            touch(iphone.skillSvtPos[svt - 1])
            touch((10, 300))
        sleep(delay)

    def masterChangeOrderPos(svt1: int, svt2: int, delay=5):
        """
        换人服的从者位置，svt1, svt2 为从者位置，取值 1-6，且不可为相同数字
        """
        touch((iphone.orderPos[svt1 - 1], 587))
        sleep(0.3)
        touch((iphone.orderPos[svt2 - 1], 587))
        sleep(0.3)
        touch(iphone.orderPosConfirm)  # 进行更替
        sleep(delay)

    def ending(eatApple=False):
        '''
        处理结尾
        '''
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
        touch(iphone.nextBtn)
        sleep(1)
        touch(iphone.closeFrd)
        sleep(.5)
        touch(iphone.continueBattleBtn)
        sleep(1)
        if eatApple:
            op._eatApple()
        sleep(3)

    def _eatApple():
        """
        检测是否出现苹果补充界面，出现了就补苹果
        """
        coor = exists(Template(r"common/黄金果实.PNG"))
        if coor:
            touch(coor)
            sleep(.3)
            touch(iphone.confirmApple)

    def clickRetry():
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
        touch(iphone.unlimitedExec)  # 执行
        sleep(2)
        touch(iphone.unlimitedClose)  # 关闭

    stop_threads = False

    def detectInterrpt(interval=5):
        nonlocal stop_threads
        while not stop_threads:
            sleep(5)
            op.clickRetry()

    th_intrpt = Thread(target=detectInterrpt)
    th_intrpt.start()

    for _ in range(1, round + 1):
        touch(iphone.unlimitedReset, 135)
        try:
            resetPresent()
        except:
            touch(iphone.unlimitedReset, 30)
            resetPresent()

    stop_threads = True
    th_intrpt.join()