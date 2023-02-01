class iphone:
    attackBtn = (0, 0)                                      # 攻击按钮
    attackPos = [                                           # 点击攻击的卡面，第一行宝具卡，第二行普通指令卡
        [(0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    ]
    skillChoose = [                                         # 技能选择，一行一个从者
        [(0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0)],
    ]
    skillConfirmBtn = (0, 0)                                # 技能确认
    skillSvtPos = [(0, 0), (0, 0), (0, 0)]                  # 技能给单体时选人
    masterSkill = (0, 0)                                    # Master的技能
    masterSkillPos = [(0, 0), (0, 0), (0, 0)]               # Master的技能位
    orderPos = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]  # 换人服的从者位置
    orderPosConfirm = (0, 0)                                # 确认换人
    # 战斗结束
    continueBattleBtn = (0, 0)  # 连续出击
    nextBtn = (0, 0)            # 下一步
    confirmApple = (0, 0)       # 补苹果
    refreshList = (0, 0)        # 好友列表刷新
    refreshBtn = (0, 0)         # 好友列表刷新确认
    closeFrd = (0, 0)           # 关闭是否发送好友申请
    # 无限池
    unlimitedExec = (0, 0)      # 执行
    unlimitedClose = (0, 0)     # 关闭
    unlimitedReset = (0, 0)     # 重置礼物
