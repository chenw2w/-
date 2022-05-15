import time
import random
import os
import json #导入Json库
print('欢迎来到本游戏（《除夕晚宴》）')
print('春节是中国民间最隆重盛大的传统节日，它不仅集中体现了中华民族的思想信仰、理想愿望、生活娱乐和文化心理，而且还是祈福攘灾、饮食和娱乐活动的狂欢式展示……')
Lifevalue1 = 100
# 血量上限
Lifevaluelimit = 100
money = 6666
n889 = 0
chengjiu = 0
dogblood = 0
# 一群无关紧要的初始数据区：
huanhundan = 0
u1 = '0'
u2 = '0'
u100 = 1
u3 = '0'
u4 = '0'
u5 = '0'
u6 = '0'
u7='0'
#木兰诗
huanghe=1
xue=0
#古城幻境
#青龙
qingbao1 = 0
qlj = 0
percent = 0
#天气
tianqi = 0
#青龙
qinglongjishu = 0
#连续两次
lianxu2 = -1
xishicishu = 0
#驯服一次
xunfu1 = 0
#望闻问切成就一次
wangyici = 0
#东坡肉buff
dongpo = 0
#马市
numa = 0
#花市
jia = 0
#沉香木
chenxiang = 0
#算命4讨
tao1 = 0
tao2 = 0
tao3 = 0
tao4 = 0
taoyici = 0
#捕鱼剧情
yujuqing = 0
# 望闻问切
wang = 0
wen = 0
wen2 = 0
qie = 0
# 到此
rpc = 0
shu = 0
# 年兽血量
Lifevalue2 = 1000
# 背包
L1 = []
# 战斗背包
L2 = []
#军队背包
L3 = []
# 坐骑栏
L4 = []
# 收藏栏
L5 = []
# 睡觉起始点次数
e1 = 0
#打字机
def dz(x):
    for i in (x):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
#白底黑字
def bdhz(x):
    print('\033[1;30;47m ',x ,' \033[0m')
#红字蓝底
def hzld(x):
    print('\033[1;31;44m',x ,'\033[0m')
#红字蓝底战斗
def hzld3(x):
    print('\033[1;31;44m',x ,'\033[0m',end='')
#红色
def hs2(x):
    print('\033[1;31m', x, '\033[0m')
#红色战斗
def hs23(x):
    print('\033[1;31m', x, '\033[0m',end='')
#灰色#亮点的白色
def hs1(x):
    print('\033[1;37m', x, '\033[0m')
#紫色
def zs(x):
    print('\033[1;35m', x, '\033[0m')
#青色
def qs(x):
    print('\033[1;32m', x, '\033[0m')
#黄色
def hs(x):
    print('\033[1;33m', x, '\033[0m')
#蓝色
def ls(x):
    print('\033[1;34m',x,'\033[0m')
#团队血量
def xue1():
                                            global xue
                                            global xiaxian
                                            xiaxian=0
                                            if '壮士' in L3:
                                               zhuangshi = L3.count('壮士')
                                               if '骏马' in L4:
                                                 junma = L4.count('骏马')
                                                 if junma >= zhuangshi:
                                                     xue = xue+zhuangshi*200
                                                     junma = junma-zhuangshi
                                                     xiaxian = xiaxian+zhuangshi*20
                                                     qs('注意！')
                                                     print('你的', zhuangshi, '名壮士骑上了骏马，团队生命+', zhuangshi*200)
                                                     zhuangshi = 0
                                                 else:
                                                     xue = xue+junma*200
                                                     zhuangshi = zhuangshi-junma
                                                     xiaxian = xiaxian+junma*20
                                                     qs('注意！')
                                                     print('你的', junma, '名壮士骑上了骏马，团队生命+', junma*200)
                                                     junma = 0
                                               elif '骐骥' in L4 and zhuangshi>0:
                                                 qiji = L4.count('骐骥')
                                                 if qiji >= zhuangshi:
                                                     xue = xue+zhuangshi*150
                                                     qiji = qiji-zhuangshi
                                                     xiaxian = xiaxian+zhuangshi*15
                                                     qs('注意！')
                                                     print('你的', zhuangshi, '名壮士骑上了骐骥，团队生命+',zhuangshi*150)
                                                     zhuangshi = 0
                                                 else:
                                                     xue = xue+qiji*150
                                                     zhuangshi = zhuangshi-qiji
                                                     xiaxian = xiaxian+qiji*15
                                                     qs('注意！')
                                                     print('你的', qiji, '名壮士骑上了骐骥，团队生命+',qiji*150)
                                                     qiji = 0
                                               elif '良马' in L4 and zhuangshi > 0:
                                                 liangma = L4.count('良马')
                                                 if liangma >= zhuangshi:
                                                     xue = xue+zhuangshi*100
                                                     liangma = liangma-zhuangshi
                                                     xiaxian = xiaxian+zhuangshi*10
                                                     qs('注意！')
                                                     print('你的', zhuangshi, '名壮士骑上了良马，团队生命+',zhuangshi*100)
                                                     zhuangshi = 0
                                                 else:
                                                     xue = xue+liangma*100
                                                     zhuangshi = zhuangshi-liangma
                                                     xiaxian = xiaxian+liangma*10
                                                     qs('注意！')
                                                     print('你的', liangma, '名壮士骑上了良马，团队生命+',liangma*100)
                                                     liangma = 0
                                               elif '驽马' in L4 and zhuangshi > 0:
                                                 numa1 = L4.count('驽马')
                                                 if numa1 >= zhuangshi:
                                                     xue = xue+zhuangshi*50
                                                     numa1 = numa1-zhuangshi
                                                     xiaxian = xiaxian+zhuangshi*5
                                                     qs('注意！')
                                                     print('你的', zhuangshi, '名壮士骑上了驽马，团队生命+',zhuangshi*50)
                                                     zhuangshi = 0
                                                 else:
                                                     xue = xue+numa1*50
                                                     zhuangshi = zhuangshi-numa1
                                                     xiaxian = xiaxian+numa*5
                                                     qs('注意！')
                                                     print('你的', zhuangshi, '名壮士骑上了驽马，团队生命+',zhuangshi*50)
                                                     numa1 = 0
                                            print('总攻击增加了','攻击+',xiaxian)
                                            xue = xue+Lifevalue1
                                            print('共计血量：', xue)
                                            return xue,xiaxian
savelist = ['L1', 'L2','L3','L4','L5','rpc','shu','huanhundan','huanghe','Lifevalue2','tao1','tao2','tao3','tao4','taoyici','yujuqing','numa','jia','chenxiang','dongpo','wangyici','xunfu1','lianxu2','xishicishu','tianqi','percent','qlj','qingbao1','u1','u2','u3','u4','u5','u6','u7','u100','e1','wang','wen','wen2','qie','Lifevalue1','Lifevaluelimit','money','chengjiu','dogblood','n889','qinglongjishu']  #需要存读的变量
def save_save():  #保存存档 
	try:  #尝试执行代码
		savefile = open(os.getcwd()+r'/save.txt', mode='w+')   #打开文件
		#print(savefile)
		globallist = globals()  #读取全局变量
		#print(globallist)
		savedict ={}  #预设需要保存的变量字典
		#print(savedict)
		for val in savelist:  #从需要要保存的变量的列表中读取出变量名到val变量直到读取完毕
			#print(val)
			savetempdict={val:globallist[val]} #设置缓存列表为(变量名:变量的内容)
			#print(savetempdict)
			savedict.update(savetempdict) #添加缓存列表数据到变量字典
			#print(savedict)
		savefile.write(json.dumps(savedict)) #将字典转换成json之后写入文件
		#print(json.dumps(savedict))
		savefile.close() #关闭文件
		print('存档完毕')
	except BaseException as error: #抓取try代码中所有错误的类型和原因给error并执行代码
		print('发生错误QAQ:'+str(error))
def save_read():  #读取存档
	try:  #尝试执行代码
		 savefile = open(os.getcwd()+r'/save.txt', mode='r+')  #读取文件
		 savereaddata  =  json.loads(savefile.read()) #读取文件中的json并转换成字典
		#print(savereaddata)
		 for val in savereaddata: #从字典中找出变量并赋值给val直至查找完毕
		 	#print(val)
		 	evalcommand = str('global '+val+';'+val+'='+str(savereaddata[val]))#设置给全局模式命令行需要调用的代码，代码的意思是设置变量为全局变量后给变量赋值存档的变量
		 	#print(evalcommand)
		 	exec(evalcommand) #以全局模式调用代码(而不是在函数里调用代码)
		 	#print(savereaddata)
		 	savefile.close()   #关闭文件
		 #print( locals())
		 print('读档完毕')
	except IOError: #捕获输入/出错误和原因给error并执行代码
		print('没有存档文件QWQ')
	except BaseException as error: #捕获所有错误和原因给error并执行代码
		print('发生错误QAQ:'+str(error))
	

print('今年轮到了你负责做春节的准备，现在离除夕晚宴还剩下36个小时，你接下来要做什么呢')
a1 = '1'
#save_read()
#print(globals())
while (True):
    print('1.出门')
    print('2.睡觉')
    print('3.存档')
    print('4.读档')
    print('当前血量:'+str(Lifevalue1))
    a1 = input('请输入数字选项：')
    if a1 == '2':
       e1=e1+1
       print('输入错误，请重新输入')
    elif a1 == '3':
        save_save()
    elif a1 == '4':
        save_read()
    else:
    	print('操作错误，请重新选择')
    if (e1 >= 2):
        print('大过年的你睡觉的执念竟如此之强，友情提示别试了，再坚持也不能让你睡觉')
    if (e1 == 4):
        print('系统消息：恭喜你达成了成就“锲而不舍”，成就点+20')
        chengjiu = (chengjiu + 20)
    if (e1 >= 5):
        print('你睡的深沉，生命-10')
        Lifevalue1 = (Lifevalue1 - 10)
        print('当前生命值：', Lifevalue1)
        if (Lifevalue1 == 0):
            print('你成功睡死了过去，恭喜你达成成就——睡死，成就点+50,并将血量回复至15点')
            chengjiu = (chengjiu + 50)
            Lifevalue1 = 15
    if e1 > 100:
        for i in range(1, 1000):
            i = random.randint(1, 2)
            if i == 1:
             print('生命-1')
            else:
                print('生命-1.0')
            time.sleep(0.0000001)
            Lifevalue1 = (Lifevalue1 - 10)
        print('当前生命值：', Lifevalue1)
# 2022.05.12 GreenYoshi edit
    if (a1 == '1'):
      w = '1'
      # 回到出发点循环
      while (w == '1'):
        w = 2
        if Lifevalue1<=0:
            if '还魂丹（三转）' in L1  :
                     Lifevalue1=Lifevaluelimit
                     del L1[L1.index('还魂丹（三转）')]
                     if Lifevaluelimit>1000:
                                                               Lifevalue1=1000
                                                               print('三转还魂丹的药效只能坚持将生命值回复至1000')
                     else:
                            print('还魂丹已使用，生命值已回复至100点')
            else:
                break
        if money<0:
            Lifevalue1=Lifevalue1-50
            print('由于欠钱，生命值-50，剩余生命值',Lifevalue1)
        print('你要去哪？')
        print('1.大街')
        print('2.天台')
        print('3.郊外')
        print('4.晚宴开始（暂未施工）')
        print('5.左拐')
        print('6.存档')
        a2 = input('请输入数字选项：')
        if a2=='6':
            save_save()
        elif (a2 == '2'):
            if '骏马'in L4 and '长鞭'in L4 and '辔头'in L4 and '鞍鞯'in L4 and huanghe==1:
              huanghe=huanghe+1
              time.sleep(0.5)
              hs('黄河之水天上来——') 
              time.sleep(1)
              hs('——奔流到海不复回')
              time.sleep(1)
              hs('郊外出现了黄河！')
              time.sleep(1)
            print('天台四万八千丈，对此欲倒东南倾……')
            print('1.沿原路返回')
            a3 = input('请输入：')
            a4 = '我欲因之梦吴越'
            as3 = '个人'
            if a3=='操作页面':
                www=1
                while www==1:
                      print('0.返回1.抢劫操作2.丢弃操作')
                      i = input('请输入：')
                      if i == '0':
                          www = 0
                      elif i == '2':
                          print('丢弃操作：输入你要丢弃的物品即可丢弃')
                          o = input('请输入要丢弃的物品名称')
                          if o in L1:
                              del L1[L1.index(o)]
                              print('已成功丢弃')
                          elif o in L2:
                              del L2[L2.index(o)]
                              print('已成功丢弃')
                          elif o in L3:
                              del L3[L3.index(o)]
                              print('已成功丢弃')
                          elif o in L4:
                              del L4[L4.index(o)]
                              print('已成功丢弃')
                          elif o in L5:
                              del L5[L5.index(o)]
                              print('已成功丢弃')
                          else:
                                 print('您的背包里没有此物品')
                      elif i=='1':
                          print('抢劫操作：输入“抢劫+空+Npc名”即可执行')
                          m, n = input('').split()
                          if m=='抢劫':
                              if n=='李四':
                                  print('你抢到了个李子，功德-1')
                              elif n=='张三':
                                  sui=random.randint(1, 5)
                                  if sui==1:
                                     print('你打劫失败，生命-10，功德-1')
                                  else:
                                      print('你打劫成功，获得金钱2000，功德-1')
                              elif n=='吴长青'or n=='吴书生':
                                  sui=random.randint(1, 5)
                                  if sui==1:
                                     print('你打劫失败，功德-2')
                                  elif sui==2:
                                      print('吾只是个书生，吾与汝本无仇无怨，汝何必劫吾。')
                                  else:
                                      print('你打劫成功，获得吴长青的秘密，功德-1')
                              elif n=='王老五':
                                  sui=random.randint(1, 5)
                                  if sui==1:
                                     print('你打劫失败，生命-10，功德-1')
                                  elif sui==2:
                                      print('你打劫成功，获得王老五秘制辟邪狗血，功德-1')
                                  else:
                                      print('你打劫成功，获得五块猪肉，功德-1')
                              elif n=='青龙':
                                  sui=random.randint(1, 5)
                                  if sui==1:
                                     print('你打劫失败，生命-100，功德-10')
                                  elif sui==2:
                                      print('你吃了熊心豹子胆了？')
                                  else:
                                      print('青龙：谁给你的胆子，敢来打劫我')
                              elif n == '李四方':
                                  sui = random.randint(1, 5)
                                  if sui == 1:
                                     print('你打劫失败，生命-10，功德-1')
                                  elif sui == 2:
                                      print('你打劫成功，获得金钱868，功德-1')
                                  elif sui==3:
                                      print('龙非龙，凤非凤，老鼠的儿子会打洞')
                                  else:
                                      print('你打劫成功，获得金钱686，功德-1')
                              elif n == '小混混甲':
                                  sui=random.randint(1, 5)
                                  if sui==1:
                                     print('你打劫失败，生命-15')
                                  elif sui==2:
                                      print('你打劫成功，获得金钱500')
                                  else:
                                      print('你打劫成功，获得金疮药*1')
                              elif n=='小混混乙':
                                  sui=random.randint(1, 5)
                                  if sui==1:
                                     print('你打劫失败，生命-11')
                                  elif sui==2:
                                      print('你打劫成功，获得金钱200')
                                  else:
                                      print('你打劫成功，获得金疮药*2')
                              elif n=='小混混丁':
                                  sui=random.randint(1, 5)
                                  if sui==1:
                                     print('你打劫失败，生命-1')
                                  elif sui==2:
                                      print('你打劫成功，获得金钱30')
                                  else:
                                      print('你打劫成功，对方一贫如洗，什么也没获得')
                              elif n=='小混混丙':
                                  sui=random.randint(1, 5)
                                  if sui==1:
                                     print('你打劫失败，生命-10')
                                  elif sui==2:
                                      print('你打劫成功，获得金钱300')
                                  else:
                                      print('你打劫成功，获得金疮药*1')
                              else:
                                  print('输入错误')
                          else:
                              print('输入错误')
                      else:
                          print('输入错误')
            elif a3=='小还丹':
                if '小还丹'in L1:
                   print('您已使用小还丹，生命上限+10')
                   Lifevalue1=100
                   Lifevaluelimit=Lifevaluelimit+10
                   del L1[L1.index('小还丹')]
                   if Lifevalue1>=Lifevaluelimit:
                      Lifevalue1=Lifevaluelimit
                      print("你现在的生命值为：",Lifevalue1)
                   else:
                      print("你没有此道具")
            elif a3=='金疮药':
               if '金疮药'in L1:
                   print('您已使用金疮药')
                   Lifevalue1=Lifevalue1+60
                   del L1[L1.index('金疮药')]
                   if Lifevalue1>=Lifevaluelimit:
                      Lifevalue1=Lifevaluelimit
                      print("你现在的生命值为：",Lifevalue1)
                   else:
                      print("你没有此道具")
            elif (a3 == a4):
                print('系统消息：恭喜你解锁隐藏关卡')
                print('只听“嗖——”的一声，你一夜之间飞度了月光照耀之下的镜湖……镜湖上的月光照着你的影子，一直伴随你到了剡溪……')
                print('系统消息：目前离晚宴还剩下12个小时')
                print('系统消息：恭喜你达成成就“不走寻常路”')
                print('你的下一步行动是？')
                print('1. 来都来了，不去探访一下谢公宿处怎么能行呢')
                print('2. 前往渌水')
                print('3.一键回城')
                a4 = input('请输入选项：')
                if (a4 == '1'):
                    print('你进入了尘封已久的谢公宿处，发现你来晚了，里面的东西早已被人洗劫一空……')
                    print('你：1.走人2.看看还有没有什么暗格之类的3.为可怜的谢公宿处默哀一分钟')
                    xiegong=input('请输入选项')
                    if xiegong=='3':
                        print('触发事件“谢公显灵”，功德+1，还望玩家多多行善，早日超脱苦海~') 
                    elif xiegong=='2':
                        print('这种地方怎么可能会有暗格之类的东西嘛~')
                    elif xiegong=='1':
                        print('你走之前发现脚踩在了什么东西上面，低头一看，原来是谢公屐。')
                        print('恭喜您获得谢公屐一只')
                        L1.append('谢公屐')
                    else:
                        print('输入错误，无任何奖励')
                    print('0.返回1.返回2.返回3.（广告位招租）4.有待玩家踊跃投稿，官方QQ群：439394084')
                    w='1'
                elif (a4 == '2'):
                    print('月亮爬上东山顶，照着树林，照着山峰，照着小河水匆匆')
                else:
                    w = '1'
            elif (a3 == as3):
                print('生命：', Lifevalue1, '/', Lifevaluelimit)
                print('金钱：', money)
                print('背包：', L1)
                print('坐骑：', L4)
                print('收藏品：', L5)
                print('成就点',chengjiu)
                w = '1'
            elif (a3 == 'cxr666'):
                print('您已成功进入后台程序')
                print('请操作……')
                Lifevalue1 = float(input('生命及上限：'))
                Lifevaluelimit = float(Lifevalue1)
                money = float(input('金钱：'))
                wuping = input('背包：')
                L1.append(wuping)
                wuping = input('军队：')
                L3.append(wuping)
                w = '1'
            else:
                w = '1'
        elif (a2 == '5'):
            w='1'
            print('1.一直走2.小巷（暂未开通）3.乌衣巷')
            az1 = input('请输入选项')
            if (az1 == '1'):
                print('你进入了隔壁老王家，正好隔壁老王有事不在……')
                time.sleep(1)
                w = '1'
            elif (az1 == '2'):
                print('    3.朱雀巷')
                print('1.青龙巷   2.白虎巷')
                print('    4.玄武巷')
                az2 = input('请输入选项')
                if az2=='1':
                  qinglong='1'
                  while qinglong=='1':
                    print('11.村口老人')
                    print('1.东海')
                    az21=input('请输入选项')
                    if az21=='11':
                        qinglongjishu=qinglongjishu+1
                        if qinglongjishu==1:
                           qs('村口老人：青龙巷与东市本为一体……')
                        elif qinglongjishu==3:
                            qs('村口老人：四市往来，青龙最上！')
                        elif qinglongjishu==2:
                            qs('村口老人：青龙本是四方神兽中最强大的一个……')
                        elif qinglongjishu==4:
                            qs('村口老人：多少年过去了，青龙巷虽然衰败，但底蕴犹存！')
                        elif qinglongjishu==5:
                            qs('村口老人：如今黄龙不显，惟留四巷，不知我之青龙何时再兴！')
                        elif qinglongjishu==6:
                            qs('村口老人：现今白虎乖张，青龙也是时候再见其之当日辉煌！')
                    else:
                        print('输入错误，请重新输入')
                else:
                    print('输入错误，请重新输入')
            elif (az1 == '3'):
                print('1.学堂')
                az3 = input('请输入选项')
                if (az3 == '1'):
                    print('保安：“站住，你滴干嘛滴！”')
                    print('1.打他2.我是来读书的')
                    az4 = input('请输入选项')
                    if (az4 == '1'):
                        print('第二天，头条上刊登了《关于爱国青年狂殴日籍保安这件事》')
                        time.sleep(1)
                    else:
                        print('保安：“那我问你，大日本帝国是几几年创建滴！')
                        print('1.揍他2.（不要输入2，直接输入年份）')
                        az4 = input('请输入选项')
                        if (az4 == '1'):
                            print('第二天，头条上刊登了《关于爱国青年狂殴日籍保安这件事》')
                            time.sleep(1)
                        else:
                            print('“错误，竟然敢羞辱我们大日本帝国，打”说着保安便拔出了刀（等等，不是警棍吗？），给了你一下，生命值-30')
                            Lifevalue1 = (Lifevalue1 - 30)
                            print('当前生命值：', Lifevalue1)
                            print('这个保安立马被警察带走了')
                            print('你终究无缘得入学堂……你被警察带去录口供了……在临走前，你依稀听到4句童谣：“天子重英豪，文章教尔曹，万般皆下品，唯有读书高。”')
                            time.sleep(1)
                            print('第二天，头条上刊登了《关于日籍保安寻衅滋事这件事》')
                            time.sleep(1)
            else:
                print('输入错误，请重新输入')
        elif (a2 == '3'):
            wjiaowai = '10'
            while (wjiaowai == '10'):
                wjiaowai = '1'
                if huanghe==2:
                    print('21.黄河0.跳过')
                    a5 = input('请输入选项：')
                    if huanghe==2 and a5=='21':
                      huitou1=0
                      while huitou1==0:
                       huitou1=2
                       hs('黄河流水鸣溅溅~')
                       print('\033[1;30;47m 0.返回1.黑山头 \033[0m')
                       aws=input('请输入选项：')
                       if aws=='0':
                           zs('自古从征不回头！')
                           huitou1=0
                       elif aws=='1':
                           print('\033[1;30;47m 燕山胡骑鸣啾啾！ \033[0m')
                           hzld('1.回头2.赴戎机3.燕山（未开）')
                           aws=input('请输入选项2：')
                           if aws=='1':
                               print('你回头一看，一队胡骑赶了上来，你头没了~')
                               Lifevalue1=0
                               break
                           elif aws=='3':
                               huqi=1000
                               xue1() 
                               while huqi>0 and xue>0:
                                     zs('你又来到了燕山，遇到了在这盘踞的一股胡骑势力~')
                                     bdhz('0.尝试和谈1.尝试说服收编2.战！')
                                     aws=input('请输入选项：')
                                     if aws=='0':
                                         hs1('和谈是不可能的，永远都不可能的！')
                                     elif aws=='1':
                                         hs1('胡骑：就你？想要收编我们？')
                                     elif aws=='2':
                                      while huqi>0 and xue>0:
                                        print('1.攻击2.道具')
                                        aws=input('请输入选项：')
                                        if aws=='1':
                                         hzld('胡骑对你发起了冲锋！') 
                                         gongji2=random.randint(10, 100)
                                         xue=xue-gongji2
                                         hzld3('胡骑对你的军团造成了')
                                         print(gongji2,end='')
                                         hzld3('点伤害，你的军团还剩')
                                         print(xue,end='')
                                         hzld('点血量')
                                         #主角团队攻击 
                                         gongji=random.randint(0+xiaxian, 100+xiaxian)
                                         huqi=huqi-gongji
                                         hs23('你的军团对胡骑造成了')
                                         print(gongji,end='')
                                         hs23('点伤害，胡骑还剩')
                                         print(huqi,end='')
                                         hs2('点血量')
                                        else:
                                            print('战斗当中还打岔？')
                                     else:
                                         print('好家伙，你这一路上都错了多少回了~')
                           elif aws=='2':
                             huitou2=0
                             while huitou2==0:
                                huitou2=2
                                if '骏马'in L4:
                                    print('你骑着骏马，风驰电掣，一路上扬起了一片黄沙~')
                                else:
                                    print('说，你把我家木兰的马弄到哪去了！')
                                    time.sleep(4)
                                if '鞍鞯'in L4:
                                    print('这一路稳稳当当，十分顺利')
                                else:
                                     print('说，你把我家木兰的鞍鞯弄到哪去了！')
                                     time.sleep(3)
                                if '辔头'in L4:
                                    print('你的方向感十分准确，一路顺利')
                                else:
                                    print('说，你把我家木兰的辔头弄到哪去了！')
                                    time.sleep(3)
                                hzld('1.关山0.回头')
                                aws=input('请输入选项：')
                                if aws=='0':
                                    hs1('莫回头，白了少年头，空悲切【手动滑稽】')
                                    huitou2=0
                                elif aws=='1':
                                    hzld('')#还未写
                                else:
                                    print('你说你是不是故意的！')
                           else:
                                print('故意的吧，你！')
                       else:
                           print('输入错误')
                print('出了城外，有3条岔路，你选哪一条？')
                print('0.返回')
                print('1.西宫南苑')
                print('2.古战场（暂未开放）')
                print('3.人迹罕至的那一条（暂未开放）')
                print('4.走没有路的通向未知的草地')
                print('5.小溪')
                print('6.古城幻境')
                a5 = input('请输入选项：')
                if a5=='6':
                    k='1'
                    while k=='1':
                        print('你穿越时空，来到了好多年前的龙城')
                        print('0.返回1.青龙街（仅此开放）2.白虎街3.朱雀街4.玄武街5.黄龙广场')
                        huan=input('请输入选项：')
                        if huan=='0':
                            k=0
                            wjiaowai='10'
                        elif huan=='2':
                            kbk=0
                            while kbk==0:
                                 hs1('白虎街上，白虎的雕像熠熠生辉，威武而又霸气')
                                 print('0.返回1.城卫管理者')
                                 huan=input('请输入')
                                 if huan=='0':
                                     kbk=1
                                 else:
                                     print('输错')
                        elif huan=='1':
                            qlj=qlj+1
                            if qlj==1:
                                qs('你来到了青龙街，正好碰到了青龙出行，人们纷纷退到道路的两旁，恭敬地看着站在车上的青龙，这时，青龙似有所察觉地向你这的方向看了一眼，眼睛明亮而又深邃。')
                            elif qlj==2:
                                qs('你再次来到了青龙街，这一次，你只看到了匆匆回来的青龙一眼，青龙似乎无奈而又焦急。')
                            kkk='0'
                            while kkk=='0':
                                print('0.返回1.马家店东市分店2.李四方情报店3.王大郎肉食店（未开发）')
                                huan=input('请输入')
                                if huan=='0':
                                    kkk=0
                                elif huan=='2':
                                  klisi='1'
                                  while klisi=='1':
                                    print('0.返回1.随便聊聊2.购买情报3.偷听对话')
                                    huan=input('请输入')
                                    if huan=='3':
                                        huan=random.randint(1, 3)
                                        if huan==3:
                                           print('对话没听到，反被察觉，生命-15')
                                           Lifevalue1=Lifevalue1-15
                                        elif huan==2:
                                            print('你什么也没听到')
                                        else:
                                            print('客人：你听说了吗，据说最近城里有大事要发生')
                                    elif huan=='0':
                                        klisi=0
                                    elif huan=='1':
                                        ls('李四方：青龙此次出行似乎是去找黄龙讨论一些事情的。')
                                    elif huan=='2':
                                        qingbao1=qingbao1+1
                                        if qingbao1==1:
                                           money=money-1
                                           print('你花费了1元，买了一个情报')
                                           ls('情报：这一年城里发生了大事！')
                                        elif qingbao1==2:
                                            money=money-10
                                            print('你花费了10元，买了一个假情报')
                                            ls('假情报：四大神兽和黄龙将不会离开')
                                        elif qingbao1==3:
                                            money=money-100
                                            print('你花费了100元，买了一个据说可靠的情报')
                                            ls('据说可靠的情报：四大神兽将会留下传承')
                                        elif qingbao1==4:
                                            money=money-1000
                                            print('你花费了1000元，买了一个真情报')
                                            ls('真情报：四大神兽都将留下东西')
                                        elif qingbao1==5:
                                           if money>100000:
                                            money=money-10000
                                            print('你花费了10000元，买了一个十分详细千真万确的情报')
                                            ls('十分详细千真万确的情报：青龙留下了“青龙玉佩”，白虎留下了“白虎令”，朱雀留下了“朱雀宝珠”，玄武留下了“玄武盾”。其中白虎令有5个，其他的都是孤品。')
                                           else:
                                                print('钱不够，惊天大情报不可能让你白嫖的')
                                        elif qingbao1==6:
                                            if money>100000:
                                                money=money-100000
                                                print('你花费了100000元，买了一个惊天大情报！')
                                                ls('惊天大情报：我就不信你有这么多钱，除非开挂') 
                                            else:
                                                print('钱不够，惊天大情报不可能让你白嫖的')
                                elif huan=='1':
                                    print('0.返回1.询问老板2.在店里找找有没有什么线索')
                                    huan=input('请输入')
                                    if huan=='1':
                                        print('老板：我们这家店历史悠久，并且并不是全靠四大神兽的庇护而留存下来的，我们本身就有底蕴存在。')
                                    elif huan=='2':
                                        print('你找啊找，找到了一根毛')
                                        print('“神秘而又神奇的毛”已放入背包')
                                        L1.append('神秘而又神奇的毛')
                                    else:
                                        print('老板：欢迎下次光临~')
                                else:
                                    print('输错')
                        else:
                            print('输入错误，请重新输入')
                #
                elif a5=='5':
                    print('1.捕鱼2.猎杀棕熊')
                    aa1=input('请输入选项')
                    if aa1=='1':
                        yujuqing=yujuqing+1
                        if yujuqing==5:
                            print('这一天你和往常一样来捉鱼')
                            time.sleep(1)
                            print('你捉啊捉，捉到了一条红鲤鱼')
                            time.sleep(1)
                            print('“刷拉”，不一会又捉到了一条绿鲤鱼')
                            time.sleep(1)
                            print('你又捉到了一条')
                            time.sleep(1)
                            print('等等，应该是，一头')
                            time.sleep(1)
                            print('驴？')
                            time.sleep(1)
                            print('“儿啊”')
                            time.sleep(1)
                            print('只见驴欢快的叫了你一声。')
                            time.sleep(1)
                            print('你满头黑线，确定了，这确实是一头驴子。')
                            time.sleep(1)
                            print('“啊，对不起啊兄台，我家的驴打扰到你了。”')
                            time.sleep(1)
                            print('一道清新的声音由远及近传了过来。')
                            time.sleep(1)
                            print('“啊，没事”，你回答道，抬头一看，只见来人身高八尺，一身素净的白袍穿在身上显得十分儒雅。')
                            time.sleep(1)
                            print('“那就好”只见来人张口轻轻说道，“我观兄台是在这里抓鱼？”')
                            print('1.对，是的。')
                            print('2.不，不是，我怎么可能在抓鱼呢。')
                            wauhfiudhf=input('')
                            print('“我叫吴形，来自隔壁的一个名为吴泉镇的小村庄，那边的风景比这更好，兄台有时间可以去那里看看”来人自来熟的说道。')
                            time.sleep(1)
                            print('哦，好的，我有空一定会去拜访。')
                            nameyu=input('啊，忘了做自我介绍了，我叫')
                            print('兄台原来叫',nameyu,'啊！幸会幸会。我还有事便先走一步了，有空一定得去我那转转啊！”说着，吴形便带着他的驴走了。小毛驴临走前还欢快的叫了两声，“儿啊，儿啊！”')
                            time.sleep(1)
                        the_number = random.randint(1, 10)
                        print('您已成功进入捕鱼游戏，鱼是很灵敏的一种物种，试试看你能不能成功捉到它吧！')
                        guess = int(input('1-10代表从左到右的顺序，赶紧来猜猜鱼在哪个方位吧: '))
                        while (guess != the_number):
                               if (guess > the_number):
                                   print(guess,'鱼在左边，快去逮住它！')
                               if (guess < the_number):
                                   print(guess,'哎呀，鱼在右边，还不快去捉！')
                               guess = int(input('再来一次：'))
                        print(guess,'恭喜你成功捉到了鱼！')
                        print('一条鱼已放入背包')
                        L1.append('鱼')
                        wjiaowai='10'
                        yuer=random.randint(1, 10)
                        if yuer!=2:
                            print('恭喜您捕鱼途中成功触发暴击，金钱+500')
                            money=money+500
                        if yuer==4:
                            print('您在捕鱼途中被划伤，生命值-5')
                            Lifevalue1=Lifevalue1-5         
                    elif aa1=='2':
                        k='1'
                        while k=='1':
                            k=2
                            print("0.返回1.设置陷阱")
                            aaa1=input("请输入选项：")
                            if aaa1=='1':
                                b='1'
                                while b=='1':
                                    b=2
                                    #
                                    print("0.返回")
                                    print("1.曲树陷阱（制造难度大，需要一颗坚实的树和坚韧的绳子，用竹子做底，辅以木扣和绳套，消耗绳子*2，竹子*3，圆木*2）")
                                    print("2.绳套陷阱（有效,简单却有效，需要一颗粗壮的树枝，一块大石头，主体是绳子，辅以竹子，木材，消耗绳子*3，竹子*1，圆木*1）")
                                    print("3.落井陷阱（较有效非常简单，只需要竹子搭建，挖个坑即可，消耗竹子*3）")
                                    choose=input("请选择陷阱：")
                                    yuanmu=L1.count('圆木')
                                    shengzi=L1.count('绳子')
                                    zhuzi=L1.count('竹子')
                                    if choose=='1':
                                        if zhuzi>=3 and yuanmu>=2 and shengzi>=2:
                                            print("已消耗竹子*3，圆木*2，绳子*2.")
                                            del L1[L1.index('竹子')]
                                            del L1[L1.index('竹子')]
                                            del L1[L1.index('竹子')]
                                            del L1[L1.index('绳子')]
                                            percent=random.randint(65,100)
                                            del L1[L1.index('绳子')]
                                            del L1[L1.index('圆木')]
                                            del L1[L1.index('圆木')]
                                        else:
                                            print("你没有足够的材料")
                                    elif choose=='2':
                                        if zhuzi>=1 and yuanmu>=1 and shengzi>=3:
                                            print("已消耗竹子*1，圆木*1，绳子*3.")
                                            del L1[L1.index('竹子')]
                                            del L1[L1.index('绳子')]
                                            del L1[L1.index('绳子')]
                                            percent=random.randint(60,90)
                                            del L1[L1.index('绳子')]
                                            del L1[L1.index('圆木')]
                                        else:
                                            print("你没有足够的材料")
                                    elif choose=='3':
                                        if zhuzi>=3:
                                            print("已消耗竹子*3.")
                                            del L1[L1.index('竹子')]
                                            del L1[L1.index('竹子')]
                                            percent=random.randint(55,85)
                                            del L1[L1.index('竹子')]
                                        else:
                                            print("你没有足够的材料")
                                    elif choose=='0':
                                        b=2
                                    else:
                                        print("输入错误，默认不选")
                                    print("1.是，鱼 2.否 3.是，猪肉 0.返回")
                                    if choose!='0':
                                       wf='1'
                                    while wf=='1':
                                        wf=2
                                        #棕熊起始血量
                                        Lifebear=300
                                        choose2=input("请设置诱饵：鱼或猪肉，是否设置？（输入选项）")
                                        if choose2=='1':
                                            if '鱼' in L1:
                                                del L1[L1.index('鱼')]
                                                print("你设置了鱼,陷阱威力得到提升")
                                            else:
                                                print("你没有鱼")
                                        elif choose2=='0':
                                            wf=2
                                        elif choose2=='2':
                                            percent=percent-10
                                            print("你没有设置鱼或猪肉")
                                        elif choose2=='3':
                                            if '猪肉' in L1:
                                                del L1[L1.index('猪肉')]
                                                print("你设置了猪肉,陷阱威力得到提升")
                                        else:
                                            print("输入错误，默认不选：")
                                        if percent>=70:
                                            print("你的陷阱抓到了棕熊，对其造成100点伤害！")
                                            Lifebear=Lifebear-100
                                            print("棕熊还剩",Lifebear,"点血量")
                                        else:
                                            print("可恶！被它躲过了陷阱！")
                                        kk='1'
                                        while kk=='1':
                                            print("1.攻击2.道具")
                                            choose3=input("请输入选项:")
                                            if choose3=='1':
                                                #角色的攻击力
                                                damage=random.randint(1, 100)
                                                if dongpo>0:
                                                    dongpo=dongpo-1
                                                    damage=damage+20
                                                if '白虎令' in L1:
                                                    damage = damage*3
                                                if '青龙玉佩'in L1:
                                                    Lifevalue1=Lifevalue1+100
                                                    if Lifevaluelimit<Lifevalue1:
                                                        Lifevalue1=Lifevaluelimit
                                                #棕熊的攻击力
                                                damagebear=random.randint(5, 15)
                                                Lifebear=Lifebear-damage
                                                Lifevalue1=Lifevalue1-damagebear
                                                print("你对棕熊造成伤害",damage,"棕熊还剩",Lifebear,"点血量")
                                                print("棕熊对你造成伤害",damagebear,"你还剩",Lifevalue1,"点血量")
                                                if Lifevalue1<=0:
                                                   Lifevalue1=0
                                                   choose4=input("你死了！已自动使用【还魂丹】（按回车继续）")
                                                   if '还魂丹（三转）' in L1:
                                                           del L1[L1.index('还魂丹（三转）')]
                                                           Lifevalue1=Lifevaluelimit
                                                           if Lifevaluelimit>1000:
                                                               Lifevalue1=1000
                                                               print('三转还魂丹的药效只能坚持将生命值回复至1000')
                                                           else:
                                                               print("成功使用【还魂丹（三转）】，生命值已回满")
                                                   else:
                                                       print('你没有还魂丹，您已死亡，请手动重新打开游戏')
                                                       break
                                                elif Lifebear<=0:
                                                      print("成功捕获！")
                                                      kk=2
                                                      print("1.熊掌2.兽筋3.熊皮")
                                                      drop=input("请选择掉落物：")
                                                      if drop=='1':
                                                          print("获得熊掌一个，价值极高。")
                                                          L1.append('熊掌')
                                                      elif drop=='2':
                                                          print("获得兽筋一条")
                                                          L1.append('兽筋')
                                                      elif drop=='3':
                                                          print("获得熊皮一张")
                                                          L1.append('熊皮')
                                                      kk=0
                                                      wjiaowai='10'
                                                      #
                                            elif choose3=='2':
                                                print("1.东坡肉 2.金疮药")
                                                items=input("请输入选项：")
                                                if items=='2':
                                                    if '金疮药' in L1:
                                                        Lifevalue1=Lifevalue1+60
                                                        del L1[L1.index('金疮药')]
                                                        if Lifevalue1>=Lifevaluelimit:
                                                            Lifevalue1=Lifevaluelimit
                                                        print("你现在的生命值为：",Lifevalue1)
                                                    else:
                                                        print("你没有此道具")
                                                elif items=='1':
                                                    if '东坡肉' in L1:
                                                        dongpo=5
                                                        del L1[L1.index('东坡肉')]
                                                        print("你的体能得到了增强，攻击+20，持续5回合")
                                                    else:
                                                        print('"您没有此道具"')
                            elif aaa1=='0':
                                k=3
                            else:
                                print("输入错误，请重新输入")
                                k='1'
                    else:
                        print("输入错误，请重新输入")
                        wjiaowai='10'
                elif (a5 == '4'):
                    print('突然，一只年兽从旁边的草丛中跳了出来')
                    print('1.驯服(限一次)2.战斗')
                    a6 = input('请输入选项：')
                    if (a6 == '1' and xunfu1==0):
                        xunfu1=xunfu1+1
                        print('年兽：“既然你要驯服我，那我便考考你。”')
                        print('年兽：1+1=？')
                        answer=input('请输入答案')
                        if answer=='2':
                            print('流氓不可怕，就怕流氓有文化')
                        else:
                            print('没文化，真可怕')
                        print('年兽：制作人是个什么样的人？')
                        print('1.好人，大好人 2.大慈善家 3.全能的人 4.我全都要')
                        answer=input('请输入选项：')
                        if answer=='1':
                           Lifevalue1=Lifevaluelimit
                           print('生命已回满')
                        elif answer=='2':
                            money=money+10000
                            print('金钱加10000')
                            Lifevalue1=Lifevalue1-10
                            print('你受到了年兽对你造成的10点伤害')
                        elif answer=='3':
                            print('获得成就点*50')
                            chengjiu=chengjiu+50
                        elif answer=='4':
                            print('因为这是通过此关的正确答案，所以无特殊奖励')
                        print('年兽：李四是干嘛的？')
                        print('1.卖李子的2.情报员3.黑市联络员4.神秘人')
                        answer=input('')
                        print('年兽：张三是个什么人？')
                        print('1.赌徒2.赌徒3.嘿嘿，你猜错了，3不是赌徒。3是赌王，怎么样，没想到吧。')
                        answer=input('')
                        print('年兽已成功被你折服，您已消耗3000金钱将其收服，年兽已自动帮您去看家了~')
                        money=money-3000
                        print('当前金钱：',money)
                        wjiaowai='10'
                    elif (a6 == '2'):
                        # 战斗循环
                        wsidou = '1'
                        while (Lifevalue1 > 0 and Lifevalue2 > 0 and wsidou == '1'):
                            h1 = random.randint(1, 100)
                            if ('辟邪红衣' in L2):
                                # 减伤
                                h1 = (0.5 * h1)
                            Lifevalue1 = (Lifevalue1 - h1)
                            print('你受到了年兽对你造成的', h1, '点伤害，当前生命值为', Lifevalue1)
                            if (Lifevalue1 <= 0):
                                Lifevalue1 = 0
                                if '还魂丹（三转）' in L1:
                                    print('你受到了年兽对你造成的', h1, '点伤害，当前生命值为', Lifevalue1)
                                    Lifevalue1=Lifevaluelimit
                                    del L1[L1.index('还魂丹（三转）')]
                                    if Lifevaluelimit>1000:
                                                               Lifevalue1=1000
                                                               print('三转还魂丹的药效只能坚持将生命值回复至1000')
                                    else:
                                               print('还魂丹已使用，生命值已回满')
                                else:
                                    print('你受到了年兽对你造成的', h1, '点伤害，当前生命值为', Lifevalue1)
                            if (Lifevalue1 == 0):
                                print('你已死亡')
                                break
                            zhandou = '12'
                            while (zhandou == '12'):
                                zhandou = '1'
                                print('1.攻击2.道具3.撤退')
                                z1 = input('请输入选项：')
                                if (z1 == '1'):
                                    h2 = random.randint(1, 100)
                                    Lifevalue2 = (Lifevalue2 - h2)
                                    print('你对年兽造成了', h2, '点伤害，年兽剩余生命值为', Lifevalue2)
                                elif (z1 == '2'):
                                    ww1 = '0'
                                    while (ww1 == '0'):
                                        ww1 = '2'
                                        print('1.爆竹2.精准打击')
                                        attack = input('请输入选项：')
                                        if (attack == '1'):
                                            if ('爆竹' in L1):
                                                del L1[L1.index('爆竹')]
                                                Lifevalue2 = (Lifevalue2 - 500)
                                                print(
                                                    '你点燃了爆竹，朝年兽扔了过去，成功命中！造成了500点伤害，年兽剩余生命值为', Lifevalue2)
                                            else:
                                                print('你的背包里没有爆竹，请重新选择')
                                                ww1 = '0'
                                        elif (attack == '2'):
                                            print('你对年兽施放了精准打击，年兽受到你造成的50点伤害')
                                            Lifevalue2 = (Lifevalue2 - 50)
                                        else:
                                            pass
                                elif (z1 == '3'):
                                    wsidou = '2'
                                    wjiaowai = '10'
                                else:
                                    print('输入错误，请重新输入')
                                    zhandou = '12'
                                if (Lifevalue2 <= 0):
                                    Lifevalue2 = 0
                                    print('(这算附赠的)你点燃了爆竹，朝年兽扔了过去，成功命中！造成了500点伤害，年兽剩余生命值为', Lifevalue2)
                                    print('年兽已死亡')
                                    ww1 = '2'
                                    qwe = random.randint(1, 100)
                                    if (qwe >= 80):
                                        print('你获得掉落物-年兽蛋')
                                        L1.append('年兽蛋')
                                        print('唔，看起来很好吃的样子，不过话说回来，年兽是卵生的？')
                                    if (qwe <= 20):
                                        print('你获得了掉落物-年兽角')
                                        L1.append('年兽角')
                                    if (qwe <= 80 and qwe >= 20):
                                        print('请选择以下掉落物之中的一个：1.汤圆2.年兽之血3.盲盒')
                                        qwe1 = input('请输入选项：')
                                        if (qwe1 == '1'):
                                            L1.append('汤圆10个')
                                            print('汤圆10个已放入背包')
                                            ww1 = '2'
                                            wjiaowai = '10'
                                        elif (qwe1 == '2'):
                                            L1.append('年兽之血')
                                            print('年兽之血已放入背包')
                                            ww1 = '2'
                                            wjiaowai = '10'
                                        else:
                                            qwe = random.randint(1, 3)
                                            if qwe==1:
                                                print('恭喜您获得金钱10000')
                                                money=money+10000
                                            elif qwe==2:
                                                print('恭喜您生命上限+100')
                                                Lifevaluelimit=Lifevaluelimit+100
                                            else:
                                                print('恭喜您获得西街赌坊的秘密！')
                                                print('张三一半的概率赢，若张三是对的，李四50%跟张三一样，25%押大，25%押小。若张三是错的，李四50%押大，50%押小。求李四赢的概率是多少？')


                    else:
                        pass
                elif (a5 == '0'):
                    wjiaowai = '1'
                    w = '1'
                elif (a5 == '1'):
                    print('你进入了这荒废的南苑')
                    time.sleep(1)
                    print('突然从荒废的墙顶跳出了一只饕鬄')
                    time.sleep(1)
                    print('望着这只巨大的饕鬄，你惊讶的发现，你竟然打不过他')
                    time.sleep(1)
                    print('饕鬄张了张嘴，你吓了一跳')
                    time.sleep(1)
                    print('他，他，他不会要吃了我吧。你心中如是想到')
                    time.sleep(1)
                    print('就在这时，未见其人先闻其声.远处悠悠然传来了一道沧桑的歌声')
                    time.sleep(1)
                    print('“明月一轮映九州，情者各处醉感伤。”')
                    time.sleep(1)
                    print('只片刻的工夫，那道声音便由远及近')
                    time.sleep(1)
                    print('“皓皓明月一烛台，忧忧心底满沧澜。”')
                    time.sleep(1)
                    print('这时你才得以看清，那人身着一袭黑衣，背负一把大剑，此时随着脚下的挪移，二指一并，向饕鬄一点。')
                    time.sleep(1)
                    print('“沧海星沙聚空会，地上流萤人间醉。”')
                    time.sleep(1)
                    print('饕鬄进入了眩晕状态，同时防御力大幅度减弱')
                    time.sleep(1)
                    print('那中年剑客随即把背后的大剑拔了出来，终身一跃，向前一斩')
                    time.sleep(1)
                    print('“地满萤火天遍星，所至何处可通冥。”')
                    time.sleep(1)
                    print('饕鬄受到了重创，进入了暴怒状态，朝天大吼')
                    time.sleep(1)
                    print('而那黑衣剑客却浑然不受半点影响')
                    time.sleep(1)
                    print('“十步杀一人，千里不留行”')
                    time.sleep(1)
                    print('饕鬄：可惜我不是人')
                    time.sleep(1)
                    print('“事了拂衣去，深藏功与名”')
                    time.sleep(1)
                    print('饕鬄：？？？')
                    time.sleep(1)
                    print('片刻后，饕鬄应声倒地')
                    time.sleep(1)
                    print('“君莫笑就是我，我就是君莫笑”')
                    time.sleep(1)
                    print('饕鬄：我记住你了，我即便是化作厉鬼也不会放过你')
                    time.sleep(1)
                    print('饕鬄，阵亡')
                    time.sleep(1)
                    print('你正要上前感谢这个仗义出手而又武功高强的正义侠客，谁知那侠客随着几个纵身，早已走远')
                    time.sleep(1)
                    print('你拍了拍身上的灰尘，心想对方真是个好人啊，随手一摸腰带，钱包瘪瘪的')
                    time.sleep(1)
                    print('你：？？？')
                    time.sleep(1)
                    print('你：你偷我钱，我跟你没完！')
                    money = 0
                    print('当前金钱：0')
                    time.sleep(1)
                    print('你好不容易从这满地狼藉里走出去，却见那偷了你钱的中年侠客正在路口，你：')
                    time.sleep(1)
                    print('1.小偷，还我钱')
                    print('2.多谢大侠的救命之恩')
                    print('3.大佬，你是怎么做到从封闭的钱袋里偷钱而不令人察觉的，我想学')
                    suibianw = input('')
                    for i in ('醉卧沙场君莫笑，古来征战几人回。这句话你知道什么意思吗 ，战场是残酷的地方，每个人都不奢求能从战场生还，我能救得了你一次，但不可能一直救你于险境，你终有一日得独立。诺，这是给你的2个包子和一瓶水，足够支撑到你回城了，回去吧，在领悟到这首诗的真谛前，不要回来了。'):
                           print(i, flush=0.03,end='')
                           time.sleep(0.03)
                    print('你心想：真是个很怪的人呢')
                    print('这首诗的真谛你领悟了吗？')
                    suibianla = input('你领悟了什么：')
                    wjiaowai = '1'
                    w = '1'
                    print('恭喜你获得包子')
                    L1.append('包子')
                else:
                    print('输入错误，请重新输入')
                    wjiaowai = '10'
                input("按回车键清屏并继续")
                os.system('cls')
        elif (a2 == '4'):
            break
        elif (a2 == '1'):
            w5 = '0'
            while (w5 == '0'):
                print('大街上依旧熙熙攘攘，人们脸上无不洋溢着幸福……')
                if (rpc == 0):
                    print('11.吃着糖葫芦的小孩')
                print('12.经常往来四市的行人')
                print('0.回去 1.西市 2.东市 3.南市 4.北市 5.中市 6.官方公告')
                print('6.陋巷(2.0版本开放)')
                a21 = input('请输入选项：')
                if (a21 == '0'):
                    w5 = '1'
                    w = '1'
                elif a21=='3':
                    w4='0'
                    print('你来到了渡口，花费了100元交了船费来到了南市')
                    money=money-100
                    time.sleep(1)
                    while w4=='0':
                             print('0.回到大街 1.马家店南市分店（未开放）')
                             a211 = input('请输入选项：')
                             if (a211 == '0'):
                                  w4 = '1'
                             elif a211=='1':
                                  w3=1
                                  while w3!='0':
                                            print('0.返回南市1.辔头：可以使你更有方向感，且更好的驾驭马儿——100元')
                                            print('您当前的金钱为：', money)
                                            a2111 = input('请输入选项：')
                                            if a2111=='1':
                                             money = (money - 100)
                                             print('您已消耗100元，买进辔头。当前剩余金钱为：', money)
                                             print('辔头X1已放入坐骑栏')
                                             L4.append('辔头')
                                             print('当前坐骑栏物品为', L4)
                                             input("按回车键清屏并继续")
                                             os.system('cls')
                                            elif a2111=='0':
                                                os.system('cls')
                                                w3 = '0'
                                            else:
                                                print('输入错误，请重新输入')
                             else:
                                 print('输入错误，请重新输入')
                elif a21=='12':
                    print('行人：北市遥远，需有快马。南市有河，需要渡船。')
                elif a21=='4':
                    w4='0'
                    if '骏马'in L4:
                        print('你骑着骏马，如同闪现一般到了北市')
                    elif '骐骥'in L4:
                        print('骐骥一跃，咻——')
                        time.sleep(1)
                    elif '良马' in L4:
                         print('良马：伯乐何在？')
                         time.sleep(2)
                    elif '驽马' in L4:
                             numa=L1.count('驽马')
                             if numa>=10:
                               print('驽马十驾，功在不舍')
                             else:
                                 print('驽马：啊，你太重了，虐待马啊~')
                    else:
                        print('你目前没有马，正在拼命赶路中，请耐心等待')
                        time.sleep(4)
                    if '鞍鞯'in L4:
                        print('这一路稳稳当当，十分顺利')
                    else:
                        answer=random.randint(1, 2)
                        if answer==1:
                            print('路中颠簸，生命-3')
                            Lifevalue1=Lifevalue1-3
                        else:
                            print('这一路稳稳当当，十分顺利')
                    if '辔头'in L4:
                        print('你的方向感十分准确，一路顺利')
                    else:
                        answer=random.randint(1, 10)
                        if answer==1:
                            print('你一个不小心迷路了，多耽搁了一会（3s）')
                            time.sleep(3)
                        else:
                            print('你的方向感十分准确，一路顺利')
                    print('费劲千辛万苦，你总算风尘仆仆的抵达了北市')
                    while w4=='0':
                             print('0.回到大街 1.马家店北市分店')
                             a211 = input('请输入选项：')
                             if (a211 == '0'):
                                  w4 = '1'
                             elif a211=='1':
                                  w3=1
                                  while w3!='0':
                                            print('0.返回南市1.长鞭：攻击加10。——100元')
                                            print('您当前的金钱为：', money)
                                            a2111 = input('请输入选项：')
                                            if a2111=='1':
                                             money = (money - 100)
                                             print('您已消耗100元，买进长鞭。当前剩余金钱为：', money)
                                             print('长鞭X1已放入坐骑栏')
                                             L4.append('长鞭')
                                             print('当前坐骑栏物品为', L4)
                                             input("按回车键清屏并继续")
                                             os.system('cls')
                                            elif a2111=='0':
                                                os.system('cls')
                                                w3 = '0'
                             else:
                                 print('输入错误，请重新输入')
                elif (a21 == '1'):
                    w4 = '0'
                    #正式版本的概率应该是1-12
                    xishi=random.randint(1, 2)
                    xishicishu=xishicishu+1
                    if xishi==1:
                                       if lianxu2+1==xishicishu:
                                           print('小子，你运气不好啊，你已经连续两次被我们逮到了啊。')
                                           hs1('编者的话：你已经连续两次被他们逮到了，逮到一次是1/12的概率，所以连续两次的概率就是1/144，你这得多倒霉啊，这么点概率都让你碰上了~至于三次的话我就不设置了，应该没有人会倒霉到三次都碰上')
                                       print('你遭遇了西市黑恶势力')
                                       lianxu2=xishicishu
                                       print('1.战斗2.被抢劫')
                                       du=input('请输入选项：')
                                       if du=='2':
                                           print('你被抢走了3000元')
                                           money=money-3000
                                       elif du=='1':
                                           duw='1'
                                           Lifehunhun = 300
                                           while duw == '1':
                                               print('小混混们提起棍子向你走来')
                                               print('1.攻击2.道具')
                                               da=input('请输入选项')
                                               if da=='2':
                                                   print('1.金疮药2.东坡肉3.小还丹')
                                                   daoju=input('请输入选项')
                                                   if daoju=='1':
                                                       if '金疮药'in L1:
                                                           print('您已使用金疮药')
                                                           Lifevalue1=Lifevalue1+60
                                                           del L1[L1.index('金疮药')]
                                                           if Lifevalue1>=Lifevaluelimit:
                                                              Lifevalue1=Lifevaluelimit
                                                           print("你现在的生命值为：",Lifevalue1)
                                                       else:
                                                           print("你没有此道具")
                                                   elif daoju=='2':
                                                      if '东坡肉' in L1:
                                                          dongpo=5
                                                          del L1[L1.index('东坡肉')]
                                                          print("你的体能得到了增强，攻击+20，持续5回合")
                                                      else:
                                                          print('"您没有此道具"')
                                                   elif daoju=='3':
                                                        if '小还丹'in L1:
                                                            Lifevaluelimit=Lifevaluelimit+10
                                                            Lifevalue1=100
                                                            del L1[L1.index('小还丹')]
                                                            print('当前生命值为100')
                                                        else:
                                                            print('"您没有此道具"')
                                               elif da=='1':
                                                   #角色的攻击力
                                                damage=random.randint(1, 100)
                                                if dongpo>0:
                                                    dongpo=dongpo-1
                                                    damage=damage+20
                                                if '白虎令'in L1:
                                                    damage=damage*5
                                                    #西市加成白虎令5倍（本来是3倍）
                                                if '青龙玉佩'in L1:
                                                    qs('青青子衿，悠悠我心')
                                                    qs('青龙玉佩已生效，生命恢复100')
                                                    Lifevalue1 = Lifevalue1+100
                                                    if Lifevaluelimit<Lifevalue1:
                                                        Lifevalue1=Lifevaluelimit
                                                #小混混的攻击力
                                                damagebear=random.randint(1, 15)
                                                Lifehunhun=Lifehunhun-damage
                                                Lifevalue1=Lifevalue1-damagebear
                                                print("你对小混混群体造成伤害",damage,"小混混群体还剩",Lifehunhun,"点血量")
                                                print("小混混甲对你造成伤害",damagebear,"你还剩",Lifevalue1,"点血量")
                                                damagebear=random.randint(5, 6)
                                                Lifevalue1=Lifevalue1-damagebear
                                                print("小混混乙对你造成伤害",damagebear,"你还剩",Lifevalue1,"点血量")
                                                damagebear=random.randint(0, 30)
                                                Lifevalue1=Lifevalue1-damagebear
                                                print("小混混丙对你造成伤害",damagebear,"你还剩",Lifevalue1,"点血量")
                                                if Lifevalue1<=0:
                                                   Lifevalue1=0
                                                   choose4=input("你死了！需要【还魂丹】（按回车继续）")
                                                   if '还魂丹（三转）' in L1:
                                                           del L1[L1.index('还魂丹（三转）')]
                                                           Lifevalue1=Lifevaluelimit
                                                           if Lifevaluelimit>1000:
                                                               Lifevalue1=1000
                                                               print('三转还魂丹的药效只能坚持将生命值回复至1000')
                                                           else:
                                                               print("成功使用【还魂丹（三转）】，生命值已回满")
                                                   else:
                                                            print('你没有还魂丹，您已死亡，请手动重新打开游戏')
                                                            break
                                                elif Lifehunhun<=0:
                                                      print("你成功赶走了小混混！")
                                                      duw=0
                                                      print("功德+1")
                                                      answer=random.randint(1, 10)
                                                      if answer==1:
                                                          print('你很幸运的获得了小混混遗留下来的500元')
                                                          money=money+500
                                                      elif answer==2:
                                                          print('我想你需要去回春堂看看了')
                                                      elif answer==3:
                                                          print('赌场十赌九输，一个不小心还有生命危险，下次不要来了')
                                                      elif answer==4:
                                                          print('你获得了小混混们遗留下来的金疮药')
                                                          L1.append('金疮药')
                                                      elif answer==5:
                                                          print('你获得了小混混们遗留下来的金疮药*3')
                                                          L1.append('金疮药')
                                                          L1.append('金疮药')
                                                          L1.append('金疮药')
                                                      elif answer==6:
                                                          print('你获得了小混混们遗留下来的金疮药*2')
                                                          L1.append('金疮药')
                                                          L1.append('金疮药')
                                                      elif answer==6:
                                                          print('你获得了小混混们遗留下来的竹子*2')
                                                          L1.append('竹子')
                                                          L1.append('竹子')
                                                      elif answer==6:
                                                          print('你获得了小混混们遗留下来的绳子*3')
                                                          L1.append('绳子')
                                                          L1.append('绳子')
                                                          L1.append('绳子')
                    print('0.回到大街1.西街赌坊2.马家店西市分店3.回春堂4.林老先生茶馆（暂未营业） 5.不起眼的杂货铺')
                    print('6.老铁铁匠铺')
                    a211 = input('请输入选项：')
                    if (a211 == '0'):
                        w4 = '1'
                    elif a211=='5':
                        w3=1
                        while w3!='0':
                            print('0.返回西市1.竹子——100元2.绳子——50元3.木材')
                            print('您当前的金钱为：', money)
                            a2111 = input('请输入选项：')
                            if a2111 == '0':
                                os.system('cls')
                                w3 = '0'
                            elif a2111=='1':
                                money = (money - 100)
                                print('您已消耗100元，买进竹子。当前剩余金钱为：', money)
                                print('竹子X1已放入背包')
                                L1.append('竹子')
                                print('当前背包物品为', L1)
                                input("按回车键清屏并继续")
                                os.system('cls')
                                print('0.返回西市 1.竹子——100元2.绳子——50元3.木材')
                            elif a2111=='2':
                                money = (money - 50)
                                print('您已消耗50元，买进绳子。当前剩余金钱为：', money)
                                print('绳子X1已放入背包')
                                L1.append('绳子')
                                print('当前背包物品为', L1)
                                input("按回车键清屏并继续")
                                os.system('cls')
                                print('0.返回西市 1.竹子——100元2.绳子——50元3.木材')
                            elif a2111=='3':
                                print('0.返回（本来想试试强买强卖的，这回放过你了）1.圆木——50元2.白杨木——100元3.红木——500元4.沉香木（限购1个）——10000元')
                                aa21=input('请输入选项')
                                if aa21=='1':
                                    money = (money - 50)
                                    print('您已消耗50元，买进圆木。当前剩余金钱为：', money)
                                    print('圆木X1已放入背包')
                                    L1.append('圆木')
                                    print('当前背包物品为', L1)
                                    input("按回车键清屏并继续")
                                    os.system('cls')
                                elif aa21=='2':
                                    money = (money - 100)
                                    print('您已消耗100元，买进白杨木。当前剩余金钱为：', money)
                                    print('白杨木X1已放入背包')
                                    L1.append('白杨木')
                                    print('当前背包物品为', L1)
                                    input("按回车键清屏并继续")
                                    os.system('cls')
                                elif aa21=='3':
                                    money = (money - 500)
                                    print('您已消耗500元，买进红木。当前剩余金钱为：', money)
                                    print('红木X1已放入背包')
                                    L1.append('红木')
                                    print('当前背包物品为', L1)
                                    input("按回车键清屏并继续")
                                    os.system('cls')
                                elif aa21=='4':
                                     chenxiang=chenxiang+1
                                     if chenxiang==1:
                                          money = (money - 10000)
                                          print('您已消耗10000元，买进沉香木。当前剩余金钱为：', money)
                                          print('沉香木X1已放入背包')
                                          L1.append('沉香木')
                                          print('当前背包物品为', L1)
                                          input("按回车键清屏并继续")
                                          os.system('cls')
                                     else:
                                         print('人不可以太贪心呦~')
                                else:
                                    print('输入错误')
                            else:
                                print('输入错误，请重新输入')
                    elif (a211 == '3'):
                        w3 = 1
                        while (w3 != '0'):
                            print('0.返回西市 1.就诊2.买药')
                            print('您当前的金钱为：', money)
                            a2111 = input('请输入选项：')
                            if a2111=='2':
                                w3=1
                                while w3!='0':
                                       print('0.返回1.金疮药：出行必备，使用后生命恢复60点——100元2.还魂丹（三转）（限购1个）：死亡后或生命值小于等于0时自动使用，将生命回满——1000元3.小还丹：使用后生命回复至100点，且生命上限增加10——1000元')
                                       print('您当前的金钱为：', money)
                                       a2111 = input('请输入选项：')
                                       if (a2111 == '1'):
                                           money=money-100
                                           L1.append('金疮药')
                                           print('您已消耗100元，买进金疮药。当前剩余金钱为：', money)
                                           print('当前背包物品为', L1)
                                           input("按回车键清屏并继续")
                                           os.system('cls')
                                       elif a2111=='2':
                                           huanhundan=huanhundan+1
                                           if huanhundan>1:
                                               print('已经没货了')
                                           else:
                                               money=money-1000
                                               L1.append('还魂丹（三转）')
                                               print('您已消耗1000元，买进还魂丹（三转）。当前剩余金钱为：', money)
                                               print('当前背包物品为', L1)
                                               input("按回车键清屏并继续")
                                               os.system('cls')
                                       elif a2111=='3':
                                            money=money-1000
                                            L1.append('小还丹')
                                            print('您已消耗1000元，买进小还丹。当前剩余金钱为：', money)
                                            print('当前背包物品为', L1)
                                            input("按回车键清屏并继续")
                                            os.system('cls')
                                       elif (a2111 == '0'):
                                               os.system('cls')
                                               w3 = '0'
                                       else:
                                            print('输入错误，请重新输入')
                                            os.system('cls')
                            elif (a2111 == '1'):
                                if (Lifevalue1 <= 0.25 * Lifevaluelimit):
                                    w3883 = (Lifevaluelimit - Lifevalue1)
                                    print('你被切了下脉，你需要花费', w3883, '金钱来回复', w3883, '血量。目前已自动扣除并治疗')
                                    money = (money - w3883)
                                    Lifevalue1 = Lifevaluelimit
                                    qie = 1
                                elif (Lifevalue1 <= 0.5 * Lifevaluelimit):
                                    w3883 = (Lifevaluelimit - Lifevalue1)
                                    print('你被问了几个问题，你需要花费', w3883, '金钱来回复', w3883, '血量。目前已自动扣除并治疗')
                                    money = (money - w3883)
                                    Lifevalue1 = Lifevaluelimit
                                    wen2 = 1
                                elif (Lifevalue1 <= 0.75 * Lifevaluelimit):
                                    w3883 = (Lifevaluelimit - Lifevalue1)
                                    print('你被听了下心跳，你需要花费', w3883, '金钱来回复', w3883, '血量。目前已自动扣除并治疗')
                                    money = (money - w3883)
                                    Lifevalue1 = Lifevaluelimit
                                    wen = 1
                                elif (Lifevalue1 <= Lifevaluelimit):
                                    w3883 = (Lifevaluelimit - Lifevalue1)
                                    print('你被看了下气色，你需要花费', w3883, '金钱来回复', w3883, '血量。目前已自动扣除并治疗')
                                    money = (money - w3883)
                                    Lifevalue1 = Lifevaluelimit
                                    wang = 1
                                #
                                elif Lifevalue1<0:
                                    qs('老仙医：你知道吗，我把店开在这就是为了拯救那些在西市垂死的人，这样的话，那些人还有救。其实我本不是西市人，我是东市青龙一脉，来到这为的是守护。')
                                #
                                else:
                                    pass
                                print('当前剩余金钱为：', money)
                                print('当前血量为', Lifevalue1)
                                wwwwwwww = input('按回车键清屏并继续')
                                os.system('cls')
                            elif (a2111 == '0'):
                                if (wen == 1 and wang == 1 and wen2 == 1 and qie == 1 and wangyici==0):
                                    print('恭喜你达成“望闻问切”成就，成就点+50')
                                    wangyici=wangyici+1
                                    chengjiu = (chengjiu + 50)
                                w3 = '0'
                            else:
                                print('输入错误，请重新输入')
                    elif (a211 == '2'):
                        w3 = 1
                        print('0.返回西市 1.鞍鞯——100元')
                        while (w3 != '0'):
                            n998 = 0
                            print('您当前的金钱为：', money)
                            a2111 = input('请输入选项：')
                            if (a2111 == '1'):
                                money = (money - 100)
                                print('您已消耗100元，买进鞍鞯。当前剩余金钱为：', money)
                                print('鞍鞯X1已放入坐骑栏')
                                L4.append('鞍鞯')
                                print('当前坐骑栏物品为', L4)
                                input("按回车键清屏并继续")
                                os.system('cls')
                                print('0.返回西市 1.鞍鞯——100元')
                            elif (a2111 == '0'):
                                os.system('cls')
                                w3 = '0'
                            else:
                                print('输入错误，请重新输入')
                                os.system('cls')
                    elif (a211 == '1'):
                        w3 = 1
                        while (w3 != '0'):
                            if (money == 0):
                                print('你被敲打了一下，“没有钱也来玩？”')
                                print('生命值-10')
                                Lifevalue1 = (Lifevalue1 - 10)
                            print('0.返回西市 1. 好运骰子')
                            a2111 = input('请输入选项：')
                            if (a2111 == '1'):
                                hs1('东家：相信大家都知道规则了，那我们就开始吧')
                                print('你：？？？')
                                touzi = random.randint(1, 16)
                                if (touzi > 8):
                                    touzi = '大'
                                elif (touzi < 8):
                                    touzi = '小'
                                else:
                                    touzi = '豹子'
                                touzi3 = random.randint(1, 10)
                                if (touzi3 <= 5):
                                    touzizhang = touzi
                                else:
                                    touzizhang = random.randint(1, 2)
                                    if (touzizhang == 1):
                                        touzizhang = '小'
                                    else:
                                        touzizhang = '大'
                                hs1('只见东家把手上的骰子向上一扔，拿起骰盅当空一划，罩住骰子后在空中摇了两下，接儿落地。')
                                print('张三：我押', touzizhang)
                                touzi4 = random.randint(1, 2)
                                if (touzi4 == 1):
                                    touzili = touzizhang
                                else:
                                    touzili = random.randint(1, 5)
                                    if (touzili == 5):
                                        touzili = '豹子'
                                    elif (touzili <= 2):
                                        touzili = '小'
                                    else:
                                        touzili = '大'
                                print('李四：嘿嘿，那我就押', touzili, '吧')
                                print('1.大2.小3.豹子')
                                touzis = input('请选择：')
                                print('结果是', touzi)
                                if (touzis == '1'):
                                    if (touzi == '大'):
                                        print('恭喜你猜对了，金钱+1000')
                                        money = (money + 1000)
                                        print('当前金钱：', money)
                                    else:
                                        print('恭喜你猜错了，金钱-1000')
                                        money = (money - 1000)
                                        print('当前金钱：', money)
                                elif (touzis == '2'):
                                    if (touzi == '小'):
                                        print('恭喜你猜对了，金钱+1000')
                                        money = (money + 1000)
                                        print('当前金钱：', money)
                                    else:
                                        print('恭喜你猜错了，金钱-1000')
                                        money = (money - 1000)
                                        print('当前金钱：', money)
                                else:
                                    if (touzi == '豹子'):
                                        print('恭喜你猜对了，金钱+9999')
                                        money = (money + 9999)
                                        print('当前金钱：', money)
                                    else:
                                        print('恭喜你猜错了，金钱-666')
                                        money = (money - 666)
                                        print('当前金钱：', money)
                                input("按回车清屏并继续")
                                os.system('cls')
                            elif (a2111 == '0'):
                                if (money <= 0):
                                    print('恭喜你达成成就“血本无归”，成就点+50,金钱刷新为起始状态')
                                    money = 6666
                                    chengjiu = (chengjiu + 50)
                                if money<=3000:
                                    du = random.randint(1, 3)
                                    if du==2:
                                       print('你遭遇了赌场黑恶势力')
                                       print('1.战斗2.被抢劫')
                                       du=input('请输入选项：')
                                       if du=='2':
                                           print('你身上仅有的',money,'被抢得一干二净')
                                           money=0
                                       elif du=='1':
                                           duw='1'
                                           Lifehunhun = 350
                                           while duw == '1':
                                               print('小混混们提起棍子向你走来')
                                               print('1.攻击2.道具')
                                               da=input('请输入选项')
                                               if da=='2':
                                                   print('1.金疮药2.东坡肉3.小还丹')
                                                   daoju=input('请输入选项')
                                                   if daoju=='1':
                                                       if '金疮药'in L1:
                                                           print('您已使用金疮药')
                                                           Lifevalue1=Lifevalue1+60
                                                           del L1[L1.index('金疮药')]
                                                           if Lifevalue1>=Lifevaluelimit:
                                                              Lifevalue1=Lifevaluelimit
                                                           print("你现在的生命值为：",Lifevalue1)
                                                       else:
                                                           print("你没有此道具")
                                                   elif daoju=='2':
                                                      if '东坡肉' in L1:
                                                          dongpo=5
                                                          del L1[L1.index('东坡肉')]
                                                          print("你的体能得到了增强，攻击+20，持续5回合")
                                                      else:
                                                          print('"您没有此道具"')
                                                   elif daoju=='3':
                                                        if '小还丹'in L1:
                                                            Lifevaluelimit=Lifevaluelimit+10
                                                            Lifevalue1=100
                                                            del L1[L1.index('小还丹')]
                                                            print('当前生命值为100')
                                                        else:
                                                            print('"您没有此道具"')
                                               elif da=='1':
                                                   #角色的攻击力
                                                damage=random.randint(1, 100)
                                                if dongpo>0:
                                                    dongpo=dongpo-1
                                                    damage=damage+20
                                                if '白虎令'in L1:
                                                    damage=damage*5
                                                #西市白虎令加成5倍，白虎令原先是3倍
                                                if '青龙玉佩'in L1:
                                                    qs('青青子衿，悠悠我心')
                                                    qs('青龙玉佩已生效，生命恢复100')
                                                    Lifevalue1=Lifevalue1+100
                                                    if Lifevaluelimit<Lifevalue1:
                                                        Lifevalue1=Lifevaluelimit
                                                #小混混的攻击力
                                                damagebear=random.randint(3, 10)
                                                Lifehunhun=Lifehunhun-damage
                                                Lifevalue1=Lifevalue1-damagebear
                                                print("你对小混混群体造成伤害",damage,"小混混群体还剩",Lifehunhun,"点血量")
                                                print("小混混甲对你造成伤害",damagebear,"你还剩",Lifevalue1,"点血量")
                                                damagebear=random.randint(3, 10)
                                                Lifevalue1=Lifevalue1-damagebear
                                                print("小混混乙对你造成伤害",damagebear,"你还剩",Lifevalue1,"点血量")
                                                damagebear=random.randint(3, 10)
                                                Lifevalue1=Lifevalue1-damagebear
                                                print("小混混丙对你造成伤害",damagebear,"你还剩",Lifevalue1,"点血量")
                                                damagebear=random.randint(0, 3)
                                                Lifevalue1=Lifevalue1-damagebear
                                                print("小混混丁对你造成伤害",damagebear,"你还剩",Lifevalue1,"点血量")
                                                if Lifevalue1<=0:
                                                   Lifevalue1=0
                                                   choose4=input("你死了！需要【还魂丹】（按回车继续）")
                                                   if '还魂丹（三转）' in L1:
                                                           del L1[L1.index('还魂丹（三转）')]
                                                           Lifevalue1=Lifevaluelimit
                                                           if Lifevaluelimit>1000:
                                                               Lifevalue1=1000
                                                               print('三转还魂丹的药效只能坚持将生命值回复至1000')
                                                           else:
                                                               print("成功使用【还魂丹（三转）】，生命值已回满")
                                                   else:
                                                            print('你没有还魂丹，您已死亡，请手动重新打开游戏')
                                                            break
                                                elif Lifehunhun<=0:
                                                      print("你成功赶走了小混混！")
                                                      duw=0
                                                      print("功德+1")
                                                      answer=random.randint(1, 10)
                                                      if answer==1:
                                                          print('你很幸运的获得了小混混遗留下来的500元')
                                                          money=money+500
                                                      elif answer==2:
                                                          print('我想你需要去回春堂看看了')
                                                      elif answer==3:
                                                          print('赌场十赌九输，一个不小心还有生命危险，下次不要来了')
                                                      elif answer==4:
                                                          print('你获得了小混混们遗留下来的金疮药')
                                                          L1.append('金疮药')
                                                      elif answer==5:
                                                          print('你获得了小混混们遗留下来的金疮药*3')
                                                          L1.append('金疮药')
                                                          L1.append('金疮药')
                                                          L1.append('金疮药')
                                                      elif answer==6:
                                                          print('你获得了小混混们遗留下来的金疮药*2')
                                                          L1.append('金疮药')
                                                          L1.append('金疮药')
                                                      elif answer==6:
                                                          print('你获得了小混混们遗留下来的竹子*2')
                                                          L1.append('竹子')
                                                          L1.append('竹子')
                                                      elif answer==7:
                                                          print('你获得了小混混们遗留下来的绳子*4')
                                                          L1.append('绳子')
                                                          L1.append('绳子')
                                                          L1.append('绳子')
                                                          L1.append('绳子')
                                w3 = '0'
                            else:
                                print('输入错误，请重新输入')
                    elif a211=='6':
                        m='1'
                        while m=='1':
                            m=2
                            hs1("老铁匠：“客官，需要我提供什么帮助吗？”")
                            print("0.返回 1.铸造武器 2.卖材料")
                            option=input("请输入选项：")
                            if option=='1':
                                print("0.返回 1.高强度合金劲长弓 2.玄铁长剑 3.白焊金长刀 4.狂战士战斧")
                                kuangshi=L1.count('矿石')
                                baiyangmu=L1.count('白杨木')
                                shenzi=L1.count('绳子')
                                zhuzi=L1.count('竹子')
                                choose5=input("请输入选项：")
                                if choose5=='1':
                                    print("老铁匠：“小伙子要求很高啊，制造这把弓需要很大的力气。”")
                                    print("需要耗材：白杨木*1，矿石*7，绳子*2")
                                    print("选择你要支付老铁匠多少钱（这会影响成功率）。")
                                    print("1.500 2.1000 3.2000")
                                    pay=input("请输入选项：")
                                    if kuangshi>=7 and baiyangmu>=1 and shenzi>=2:
                                        del L1[L1.index('白杨木')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('绳子')]
                                        del L1[L1.index('绳子')]
                                        success=random.randint(1,100)
                                        if pay=='1':
                                            print("老铁匠：“现在的年轻人真是吝啬啊”")
                                            money=money-500
                                            print("你消耗了500金钱,还剩",money,"金钱")
                                        elif pay=='2':
                                            print("老铁匠：“好！这就给你来造一件！”")
                                            money=money-1000
                                            print("你消耗了1000金钱,还剩",money,"金钱")
                                            success=success+15
                                        elif pay=='3':
                                            print("老铁匠：“客官大气！我愿尽全力帮你造好”")
                                            money=money-2000
                                            print("你消耗了2000金钱,还剩",money,"金钱")
                                            success=success+30
                                        if 50<=success<=90:
                                            print("成功铸造！")
                                            L2.append('高强度合金劲长弓')
                                        elif success>90:
                                            print("完美！将返还多余材料")
                                            L1.append('矿石')
                                            L1.append('矿石')
                                            L1.append('矿石')
                                            L1.append('绳子')
                                            L2.append('高强度合金劲长弓')
                                        else:
                                            print("铸造失败！将返还一部分材料")
                                            L1.append('矿石')
                                            L1.append('矿石')
                                            L1.append('绳子')
                                    else:
                                       print("你没有足够材料")
                                    m='1'
                                elif choose5=='2':
                                    print("老铁匠：“小伙子有眼光！这把玄铁剑造起来可是很难得！”")
                                    print("需要耗材矿石*6，白杨木*1")
                                    print("选择你要支付老铁匠多少钱（这将影响铸造成功率）")
                                    print("1.500 2.1000 3.2000")
                                    pay2=input("请输入选项")
                                    if kuangshi>=6 and baiyangmu>=1:
                                        del L1[L1.index('白杨木')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        success=random.randint(1,100)
                                        if pay2=='1':
                                            print("老铁匠：“你其实可以给我更多钱的”")
                                            money=money-500
                                            print("你消耗了500金钱,还剩",money,"金钱")
                                        elif pay2=='2':
                                            print("老铁匠：“有干劲了！”")
                                            money=money-1000
                                            print("你消耗了1000金钱,还剩",money,"金钱")
                                            success=success+15
                                        elif pay2=='3':
                                            print("老铁匠：“这就来！”")
                                            money=money-2000
                                            print("你消耗了2000金钱,还剩",money,"金钱")
                                            success=success+30
                                        if 45<=success<=90:
                                            print("成功铸造！")
                                            L2.append('玄铁长剑')
                                        elif success>90:
                                            print("完美！将返还多余材料")
                                            L1.append('矿石')
                                            L1.append('矿石')
                                            L2.append('玄铁长剑')
                                        else:
                                            print("铸造失败！将返还一部分材料")
                                            L1.append('矿石')
                                    else:
                                        print("你没有足够的材料")
                                    m='1'
                                elif choose5=='3':
                                    print("小伙子看得准！这个是一名异国使者给我的配方，全国上下估计都没几个人有！")
                                    print("需要耗材矿石*5，竹子*2")
                                    print("请选择你要支付老铁匠多少钱（这将影响成功率）")
                                    print("1.400 2.900 3.1600")
                                    pay3=input("请输入选项:")
                                    if kuangshi>=5 and zhuzi>=2:
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('竹子')]
                                        del L1[L1.index('竹子')]
                                        success=random.randint(1,100)
                                        if pay3=='1':
                                            print("老铁匠：“造好刀可不容易啊！”")
                                            money=money-400
                                            print("你消耗了400金钱,还剩",money,"金钱")
                                        elif pay3=='2':
                                            print("老铁匠：“我看行！”")
                                            money=money-900
                                            print("你消耗了900金钱,还剩",money,"金钱")
                                            succcess=success+15
                                        elif pay3=='3':
                                            print("老铁匠：“给你一把绝世好刀！”")
                                            money=money-1600
                                            print("你消耗了1600金钱,还剩",money,"金钱")
                                            succcess=success+30
                                        if 40<=success<=90:
                                            print("成功铸造！")
                                            L2.append('白焊金长刀')
                                        elif success>90:
                                            print("完美！将返还多余材料")
                                            L1.append('矿石')
                                            L1.append('竹子')
                                            L2.append('白焊金长刀')
                                        else:
                                            print("铸造失败！将返还一部分材料")
                                            L1.append('矿石')
                                    else:
                                        print("你没有足够的材料")
                                    m='1'
                                elif choose5=='4':
                                    print("小伙子有胆量！则斧头可不是一般人控制得了的！")
                                    print("需要耗材矿石*4，白杨木*2")
                                    print("请选择你要支付老铁匠多少钱（这将影响成功率）")
                                    print("1.400 2.900 3.1600")
                                    pay4=input("请输入选项:")
                                    if kuangshi>=4 and baiyangmu>=2:
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('矿石')]
                                        del L1[L1.index('白杨木')]
                                        del L1[L1.index('白杨木')]
                                        success=random.randint(1,100)
                                        if pay4=='1':
                                            print("老铁匠：“这可没那么好造！”")
                                            money=money-400
                                            print("你消耗了400金钱,还剩",money,"金钱")
                                        elif pay4=='2':
                                            print("老铁匠：“好胆量！”")
                                            money=money-900
                                            print("你消耗了900金钱,还剩",money,"金钱")
                                            success=success+15
                                        elif pay4=='3':
                                            print("老铁匠：“有力！有力!”")
                                            money=money-1600
                                            print("你消耗了1600金钱,还剩",money,"金钱")
                                            success=success+30
                                        if 40<=success<=90:
                                            print("成功铸造！")
                                            L2.append('狂战士战斧')
                                        elif success>90:
                                            print("完美！将返还多余材料")
                                            L1.append('矿石')
                                            L1.append('白杨木')
                                            L2.append('狂战士战斧')
                                        else:
                                            print("铸造失败！将返还一部分材料")
                                            L1.append('矿石')
                                    else:
                                        print("你没有足够的材料")
                                    m='1'
                    else:
                        print('输入错误，请重新输入')
                        w4 = '4'
                elif (a21 == '5'):
                    w4 = '0'
                    while (w4 == '0'):
                        h991 = random.randint(1, 5)
                        if h991 == 2 or h991 == 3: 
                            print('友情提示：在天台输入“个人”可查看个人信息')
                        elif h991==4:
                            qigai1='1'
                            while qigai1=='1':
                                  print('你路过的时候眼睛余光看到了个人，面前有一个碗')
                                  print('你：1.走人2.施舍1文钱 3.给他100个铜板 4.赠予他千两白银 5.给他万两黄金')
                                  qigai=input('你：')
                                  if qigai=='2':
                                     qs('乞丐：给1文钱打发叫花子呢')
                                     money=money-1
                                     tao2=2
                                  elif qigai=='1':
                                      qigai1='2'
                                      if tao1==2 and tao2==2 and tao3==3 and tao4==2 and taoyici==0:
                                          print('恭喜您完成算命所有篇章，成就点+50')
                                          taoyici=taoyici+1
                                          chengjiu=chengjiu+50
                                  elif qigai=='3':
                                      qs('算命人：我是算卦的')
                                      money=money-100
                                      print('当前剩余金钱：',money)
                                      tao1=2
                                  elif qigai=='4':
                                      qs('算命人：草，大凶')
                                      money=money-1000
                                      print('当前剩余金钱：',money)
                                      tao3=2
                                  elif qigai=='5':
                                      qs('算命人：在买到装备之前别去郊外长满荒草的地方')
                                      money=money-10000
                                      print('当前剩余金钱：',money)                                   
                                      tao4=2
                        elif (h991 == 5):
                            print('21.（恭喜你巧遇）说书人')
                            h9911 = input('请输入（按回车键跳过该选择）：')
                            if (h9911 == '21'):
                                shu = (shu + 1)
                                print('只见说书人庄重说道：“正所谓‘天下没有免费的午餐’”说书人随后画风一转：“不过你放心，我这说书是免费的，毕竟说书是一项高尚的事业，你且听我与你娓娓道来……”')
                                if (shu == 1):
                                    print('从前有座书山，山上有座叶庙，庙里有个学生在写作业，写的是什么呢，写的是……')
                                    print('你：……')
                                    print('1.还真是在说书……')
                                    print('2.你怕不是对说书这职业有什么误解……')
                                    print('3.我竟无言以对')
                                    hjfhasgfdfy = input('同时你心里在想：')
                                    print('说书人：“对了，说了这么久竟然还忘了做自我介绍，真是失敬失敬，我叫吴长青，你称呼我为吴书生就行。对了，谈了这么久还不知道你名字呢？')
                                    name1 = input('这位兄台，你的名字是：')
                                    print('吴书生：“奥，原来是', name1, '呀，久仰久仰。红尘滚滚，事务繁多，吾先告辞了。下次见到兄台估计就是另一番故事了吧。')
                                elif (shu == 2):
                                    print('吴书生：“哎呀，谁撞我。”吴书生捂着他那被撞痛的头，一看。“原来是', name1, '啊，好久不见，甚是想念。自上次一别，兄台向来可好？')
                                    print('你：“还好，不过你这么急干嘛去啊？”')
                                    print('吴书生：“其实也说不上什么急事，就是我说书正说到阿方的时候，有人不信我有阿方的木雕，于是我回家准备拿给他们看。”')
                                    print('你：“原来是这样啊，不过阿方是谁啊”')
                                    print('吴书生一听到这个，正欲说时，却见他的客户余老九跑过来催：“吴先生，麻烦快一点，大伙还在等着呢。吴书生说：“那这样吧，你跟我走一趟也就差不多知道个大概了”')
                                    print('于是你跟吴书生到家里拿了木雕后又转到大街上。面对着前方的观众，吴书生举起了手中的木雕，抬着从左转到右，又从右转到左，说道“都看到了吧，这可是货真价实的阿方亲手雕刻的木雕，我没骗你们吧，当时我恰好从阿方买了一个，我也敢保证，我这故事绝对真实，绝对可信。”')
                                    print('周围的观众一看吴书生手上这木雕，赫然是真品，连忙说道：“行了行了，故事的真实我们当然毫不怀疑，毕竟能让林老先生那样的人挂念的人，必然是个很好的人。我们当时只是不信你恰好有现在市场上价值千金的阿方的木雕而已，现在才知道，原来你当时还有这层缘故，如此，阿方的木雕在你手里就毫不奇怪了。')
                                    print('吴书生：“那么我便继续讲下去了：……')
                                elif shu==3:
                                    for i in ('吴书生：“又见面了呀，朋友。相逢即是缘，如果你想听听我的故事的话，就请先坐下来，喝完茶歇歇。因为我要讲的故事很长，很长。那是一场梦幻般的故事……'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('那是一年夏，繁花似锦的夏，知了在树上不厌其烦的叫着，而我，此时正在一个凉亭里读书。她，则在一旁安心画画。就这样，我读书，她画画，很好，真希望时间静止在那一刻。'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('她画画画的很好，仿佛自然自然而然投影进去的。她很爱大自然，爱大自然里的一花一木，一草一树。她有一次放下画笔，看向凉亭外的风景时曾对我说，"一花一世界，一草一树木，一叶一菩提。大自然是美妙的，我想把这一切都画下来。"'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('然后她便转过头来问我：“你呢，长青，你的志向是什么呢”'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('我不好意思的挠了挠头：“我，我的志向是，是，是成为一个大书生，读万卷书，行万里路。”'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('“哦，就这些吗？”她歪着头看向我。“那便祝愿我俩一起成功吧！”'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('“恩，初心不改，细水长流”'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('然而，那年冬天，她因病而逝，她没告诉我，她得了绝症，我也从没察觉到。等到我知道消息时，一切都晚了。我当时痛苦，懊悔，乃至一切的一切之悲痛。'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('从那以后，我一直遵守着承诺，同时也时常用另一种眼光来看待这个世界，这个世界纵有点点瑕疵，但依旧美好，不是吗？'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('我的故事也许你听得无聊了吧，不过这就是我的故事，我也将不忘初心，一直走下去。'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('来日方长，我们有缘再相见。'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                else:
                                    pass
                            input("按回车键清屏并继续")
                            os.system('cls')
                        else:
                            pass
                        print('0.回到大街1.成就兑换点2.天字一号店3.花市4.新春专卖铺（仅此开放）')
                        a211 = input('请输入选项：')
                        if (a211 == '0'):
                            w4 = '1'
                        elif a211=='3':
                            print('去年元夜时')
                            aa1=input('请输入下一句话')
                            if aa1=='花市灯如昼':
                                w3 = 1
                                while (w3 != '0'):
                                    print('0.返回中市1.花市老板娘 2.路人甲 3.花铺一（未开发） 4.三叶草园（未开发）')
                                    a2111 = input('请输入选项：')
                                    if (a2111 == '1'):
                                        print('不管你是什么人，花市里总有你想要的东西。')
                                    elif a2111=='4':
                                        print('')
                                        #一叶代表祈求 二叶代表希望 三叶代表爱情 四叶代表幸福
                                    elif a2111=='3':
                                        print('0.返回1.彼岸花2.曼陀罗3.黑玫瑰4.罂粟花5.虞美人')
                                    elif a2111 == '2':
                                        if jia==0:
                                            jia=jia+1
                                            print('\033[1;31m我在等一个人……\033[0m')
                                            wwwwwwww = input('按回车清屏并继续')
                                            os.system('cls')
                                        elif jia==1:
                                            print('\033[1;31m你：还在等吗？\033[0m')
                                            time.sleep(1)
                                            print('\033[1;31m恩\033[0m')
                                            jia=jia+1
                                        elif jia==2:
                                            jia=jia+1
                                            print('\033[1;31m你在等谁？\033[0m')
                                            time.sleep(1)
                                            print('\033[1;31m等一个很重要的人\033[0m')
                                            time.sleep(1)
                                            print('\033[1;31m有多重要\033[0m')
                                            time.sleep(1)
                                            print('\033[1;31m说不出来的重要\033[0m')
                                            time.sleep(1)
                                        elif jia==3:
                                            jia = jia+1
                                            print('\033[1;31m夜已深，何不归\033[0m')
                                            time.sleep(1)
                                            print('\033[1;31m只因未能人等至\033[0m')
                                            time.sleep(1)
                                            print('\033[1;31m夜半已过，有约亦当别\033[0m')
                                            time.sleep(1)
                                            print('\033[1;31m君不见，天上之明月\033[0m')
                                            time.sleep(1)
                                            print('\033[1;31m一如依旧，吾何当离？\033[0m')
                                            time.sleep(1)
                                            #有待清屏
                                    elif (a2111 == '0'):
                                              w3 = '0'
                                    else:
                                        print('输入错误，请重新输入')
                        elif (a211 == '4'):
                            w3 = 1
                            while (w3 != '0'):
                                print('0.返回中市 1.烟花：观赏性极强，晚宴必备——100元1箱 2.爆竹:可对年兽造成500点伤害——100元1串 3.辟邪红衣：可减弱年兽等对你造成的50%的伤害——100元1件 4.“福”倒：可为你的晚宴布景加分——100元10张')
                                print('您当前的金钱为：', money)
                                a2111 = input('请输入选项：')
                                if (a2111 == '2'):
                                    money = (money - 100)
                                    print('您已消耗100元，买进爆竹1串。当前剩余金钱为：', money)
                                    print('爆竹一串已放入背包')
                                    L1.append('爆竹')
                                    print('当前背包物品为', L1)
                                elif (a2111 == '3'):
                                    money = (money - 100)
                                    # 这里要改
                                    print('您已消耗100元，买进辟邪红衣1件。当前剩余金钱为：', money)
                                    print('辟邪红衣1件已放入背包，检测到您没有装备，已自动放入装备栏')
                                    L2.append('辟邪红衣')
                                    print('当前背包物品为', L1)
                                elif (a2111 == '0'):
                                    w3 = '0'
                                else:
                                    print('输入错误，请重新输入')
                                input("按回车清屏并继续")
                                os.system('cls')
                        else:
                            print('输入错误，请重新输入')
                            w4 = '4'
                elif (a21 == '11'):
                    rpc = (rpc + 1)
                    print('吃着糖葫芦的小孩：“你好，我叫天才，你呢？”')
                    time.sleep(3)
                    print('天才：“好了，不和你说了，我哥哥还在明堂等着我呢”')
                    time.sleep(2)
                    print('陋巷里，一道黑色的身影，嘴角勾起一抹弧度：“真是个有趣的小孩呢”')
                    time.sleep(3)
                elif (a21 == '2'):
                    w45 = '0'
                    while (w45 == '0'):
                        h991 = random.randint(1, 5)
                        if h991 == 2 or h991==3:
                            print('友情提示：在天台输入“个人”可查看个人信息')
                        elif h991==4:
                            qigai1='1'
                            while qigai1=='1':
                                  print('你路过的时候眼睛余光看到了个人，面前有一个碗')
                                  print('你：1.走人2.施舍1文钱 3.给他100个铜板 4.赠予他千两白银 5.给他万两黄金')
                                  qigai=input('你：')
                                  if qigai=='2':
                                     qs('乞丐：给1文钱打发叫花子呢')
                                     money=money-1
                                     tao2=2
                                  elif qigai=='1':
                                      qigai1='2'
                                      if tao1==2 and tao2==2 and tao3==3 and tao4==2 and taoyici==0:
                                          print('恭喜您完成算命所有篇章，成就点+50')
                                          taoyici=taoyici+1
                                          chengjiu=chengjiu+50
                                  elif qigai=='3':
                                      qs('算命人：我是算卦的')
                                      money=money-100
                                      print('当前剩余金钱：',money)
                                      tao1=2
                                  elif qigai=='4':
                                      qs('算命人：草，大凶')
                                      money=money-1000
                                      print('当前剩余金钱：',money)
                                      tao3=2
                                  elif qigai=='5':
                                      qs('算命人：在买到装备之前别去郊外长满荒草的地方')
                                      money=money-10000
                                      print('当前剩余金钱：',money)                                  
                                      tao4=2
                        elif (h991 == 5):
                            print('21.（恭喜你巧遇）说书人')
                            h9911 = input('请输入（按回车键跳过该选择）：')
                            if (h9911 == '21'):
                                shu = (shu + 1)
                                print('只见说书人庄重说道：“正所谓‘天下没有免费的午餐’”说书人随后画风一转：“不过你放心，我这说书是免费的，毕竟说书是一项高尚的事业，你且听我与你娓娓道来……”')
                                if (shu == 1):
                                    print('从前有座书山，山上有座叶庙，庙里有个学生在写作业，写的是什么呢，写的是……')
                                    print('你：……')
                                    print('1.还真是在说书……')
                                    print('2.你怕不是对说书这职业有什么误解……')
                                    print('3.我竟无言以对')
                                    hjfhasgfdfy = input('同时你心里在想：')
                                    print('说书人：“对了，说了这么久竟然还忘了做自我介绍，真是失敬失敬，我叫吴长青，你称呼我为吴书生就行。对了，谈了这么久还不知道你名字呢？')
                                    name1 = input('这位兄台，你的名字是：')
                                    print('吴书生：“奥，原来是', name1, '呀，久仰久仰。红尘滚滚，事务繁多，吾先告辞了。下次见到兄台估计就是另一番故事了吧。')
                                elif (shu == 2):
                                    print('吴书生：“哎呀，谁撞我。”吴书生捂着他那被撞痛的头，一看。“原来是', name1, '啊，好久不见，甚是想念。自上次一别，兄台向来可好？')
                                    print('你：“还好，不过你这么急干嘛去啊？”')
                                    print('吴书生：“其实也说不上什么急事，就是我说书正说到阿方的时候，有人不信我有阿方的木雕，于是我回家准备拿给他们看。”')
                                    print('你：“原来是这样啊，不过阿方是谁啊”')
                                    print('吴书生一听到这个，正欲说时，却见他的客户余老九跑过来催：“吴先生，麻烦快一点，大伙还在等着呢。吴书生说：“那这样吧，你跟我走一趟也就差不多知道个大概了”')
                                    print('于是你跟吴书生到家里拿了木雕后又转到大街上。面对着前方的观众，吴书生举起了手中的木雕，抬着从左转到右，又从右转到左，说道“都看到了吧，这可是货真价实的阿方亲手雕刻的木雕，我没骗你们吧，当时我恰好从阿方买了一个，我也敢保证，我这故事绝对真实，绝对可信。”')
                                    print('周围的观众一看吴书生手上这木雕，赫然是真品，连忙说道：“行了行了，故事的真实我们当然毫不怀疑，毕竟能让林老先生那样的人挂念的人，必然是个很好的人。我们当时只是不信你恰好有现在市场上价值千金的阿方的木雕而已，现在才知道，原来你当时还有这层缘故，如此，阿方的木雕在你手里就毫不奇怪了。')
                                    print('吴书生：“那么我便继续讲下去了：……')
                                elif shu==3:
                                    for i in ('吴书生：“又见面了呀，朋友。相逢即是缘，如果你想听听我的故事的话，就请先坐下来，喝完茶歇歇。因为我要讲的故事很长，很长。那是一场梦幻般的故事……'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('那是一年夏，繁花似锦的夏，知了在树上不厌其烦的叫着，而我，此时正在一个凉亭里读书。她，则在一旁安心画画。就这样，我读书，她画画，很好，真希望时间静止在那一刻。'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('她画画画的很好，仿佛自然自然而然投影进去的。她很爱大自然，爱大自然里的一花一木，一草一树。她有一次放下画笔，看向凉亭外的风景时曾对我说，"一花一世界，一草一树木，一叶一菩提。大自然是美妙的，我想把这一切都画下来。"'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('然后她便转过头来问我：“你呢，长青，你的志向是什么呢”'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('我不好意思的挠了挠头：“我，我的志向是，是，是成为一个大书生，读万卷书，行万里路。”'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('“哦，就这些吗？”她歪着头看向我。“那便祝愿我俩一起成功吧！”'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('“恩，初心不改，细水长流”'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('然而，那年冬天，她因病而逝，她没告诉我，她得了绝症，我也从没察觉到。等到我知道消息时，一切都晚了。我当时痛苦，懊悔，乃至一切的一切之悲痛。'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('从那以后，我一直遵守着承诺，同时也时常用另一种眼光来看待这个世界，这个世界纵有点点瑕疵，但依旧美好，不是吗？'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('我的故事也许你听得无聊了吧，不过这就是我的故事，我也将不忘初心，一直走下去。'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                    for i in ('来日方长，我们有缘再相见。'):
                                        print(i, flush=0.03,end='')
                                        time.sleep(0.03)
                                else:
                                    pass
                        print('0.回到大街1.马家店东市分店2.李四的李子店（李四的情报店1.2版本开放）3.糖堆专卖店（未开发）4.王老五猪肉铺')
                        a224 = input('请输入选项：')
                        if (a224 == '0'):
                            w45 = '1'
                        elif (a224 == '2'):
                            ls('李四：欢迎光临')
                            print('1.谢谢惠顾2.新年好3.除夕晚上来我家吗')
                            ict = input('你：')
                            if (ict == '2'):
                                ls('李四：“新年好呀，新年好呀，祝福大家新年好……”')
                            elif (ict == '3'):
                                ls('李四：“好呀，不过我还得把这些剩下的李子处理完，晚点再到贵府拜访吧”')
                            elif (ict == '1'):
                                ls('李四：“恩，接头暗号答对了，看来是熟客了。最近看得紧，nang,这是九九归一令，拿好了”')
                                print('九九归一令已放入收藏栏')
                                L5.append('九九归一令')
                                print('九九归一令：黑市的出入凭证（在大街上输入“99=1”即可进入黑市”')
                            else:
                                print('输入错误')
                            w3 = 1
                            while (w3 != '0'):
                                #
                                print('0.返回东市 1.李子：李家一绝，不容错过——10元2.酸甜李子汤：酸酸甜甜好滋味——300元3.霸王李：李四家的信物，具有无上的功效——10000元')
                                print('您当前的金钱为：', money)
                                a2111 = input('请输入选项：')
                                if a2111=='3':
                                  if money>=10000:
                                    money=money-10000
                                    print('您已消耗10000元，买进霸王李一颗。当前剩余金钱为：', money)
                                    print('霸王李一颗已放入背包')
                                    L1.append('霸王李')
                                    print('当前背包物品为', L1)
                                    lizi = random.randint(1, 2)
                                    if (lizi == 1):
                                       print( '\033[1;33m李四：白虎令本来有5个，现在只余下来了3个。当时四大神兽都留下了东西，但白虎主杀伐，认为他的后人不能被欺负，故留下了5个，同时白虎令在西市使用还有加持作用。为什么白虎令会少了2个呢，不是失传，而是自爆。\033[0m', end='')
                                       print('\033[1;33m是的，白虎令可自爆。那2个少的就是被人自爆的。行有行规，现在西市那边为了保护白虎令，订下了规矩，不可为自己的私事而自爆白虎令。这也算是不幸中的万幸了吧。据说现存的3个白虎令，1个在黑市，一个在西市黑帮老大手里。\033[0m')
                                    elif lizi == 2:
                                        print('\033[1;33m李四：朱雀宝珠蕴含了变数，据说是朱雀以命炼制的，当初四大神兽撤走的急。朱雀宝珠尚未完善，朱雀急忙进去完善。然而那一夜朱雀失踪了，连带着失踪的还有朱雀宝珠。\033[0m')
                                  else:
                                      print('你的金额不足，别想来白嫖情报！')
                                      #
                                elif a2111=='2':
                                    money=money-300
                                    print('您已消耗300元，买进酸甜李子汤一碗。当前剩余金钱为：', money)
                                    print('酸甜李子汤一碗已放入背包')
                                    L1.append('酸甜李子汤')
                                    print('当前背包物品为', L1)
                                    lizi = random.randint(1, 7)
                                    if (lizi == 1):
                                        ls('李四：吴形和吴长青似乎有点关系')
                                    elif lizi==5:
                                        ls('李四：“知道小混混丁为什么叫小混混丁吗？嘿嘿，因为他最弱啊。4个人不是400血的原因就是因为有小混混丁在拖后腿啊。”说着李四办了个鬼脸')
                                    elif lizi==2 or lizi==3 or lizi==4:
                                        ls('李四：西市不太平，西市是治安最差的一个地方，如果你必须去回春堂看病的话，建议多买点金疮药。金疮药在天台上也可以使用，在天台输入“金疮药”即可。')
                                elif (a2111 == '1'):
                                    money = (money - 10)
                                    print('您已消耗10元，买进李子一个。当前剩余金钱为：', money)
                                    print('李子一个已放入背包')
                                    L1.append('李子')
                                    print('当前背包物品为', L1)
                                    lizi = random.randint(1, 7)
                                    if (lizi == 1):
                                        ls('李四：“听说张三有一手高超的赌术，在赌坊跟着他混准没错”')
                                        u1 = '1'
                                    elif (lizi == 2):
                                        ls('李四：“听说在天台输入“个人”可以查看个人信息呦”')
                                        u2 = '1'
                                    elif (lizi == 3):
                                        ls('李四：“当你回到大街上时，如果你的金钱数目为负，则你会扣血，如果你的生命值为0及以下，则你会死亡”')
                                        u3 = '1'
                                    elif (lizi == 4):
                                        ls('李四：“我敢打包票，本游戏的制作人绝对是个帅哥”')
                                        u4 = '1'
                                    elif (lizi == 5):
                                        ls('李四：“据说四大街市相互联系，而中市则是它们的核心。”')
                                        u5 = '1'
                                    elif (lizi == 6):
                                        ls('李四：“阿方是个好人，可惜他就这么走了……什么？你问阿方是谁？你去林老先生茶馆逛一圈也就差不多知道了。”')
                                        u6 = '1'
                                    elif lizi==7:
                                        ls('李四：“在天台输入‘小还丹’或‘金疮药’即可使用~”')
                                        u7='1'
                                    else:
                                        pass
                                elif (a2111 == '0'):
                                    if (u1 == '1' and u2 == '1' and u3 == '1'and u7=='1' and u4 == '1' and u5 == '1' and u6 == '1' and u100 == 1):
                                        print('系统消息：恭喜你达成收集完李四的七大情报，达成“情报小能手”成就，成就点+30')
                                        chengjiu = (chengjiu + 30)
                                        u100 = (u100 + 1)
                                    w3 = '0'
                                else:
                                    print('输入错误，请重新输入')
                        elif (a224 == '4'):
                            w3 = 1
                            while (w3 != '0'):
                                print('王老五：“您好，客官，您要点什么？”')
                                print('0.返回东市 1. 猪肉：普通的猪肉，无毒无害无注水——50元2.东坡肉：苏轼的肉【手动滑稽】，吃一口长生不老，吃两口永不烦恼，吃三口没完没了——100元 3.猪头一个：…… 给你个猪头，你自己想吧——50元4.王老五秘制辟邪狗血一份：？？？——200元')
                                print('您当前的金钱为：', money)
                                a2111 = input('请输入选项：')
                                if (a2111 == '2'):
                                    money = (money - 100)
                                    print('您已消耗100元，买进东坡肉。当前剩余金钱为：', money)
                                    print('东坡肉已放入背包')
                                    L1.append('东坡肉')
                                    print('当前背包物品为', L1)
                                elif (a2111 == '3'):
                                    money = (money - 50)
                                    print('您已消耗50元，买进猪头一个。当前剩余金钱为：', money)
                                    print('猪头一个已放入背包，')
                                    L1.append('猪头')
                                    print('当前背包物品为', L1)
                                elif (a2111 == '1'):
                                    money = (money - 50)
                                    print('您已消耗50元，买进猪肉。当前剩余金钱为：', money)
                                    print('猪肉已放入背包，')
                                    L1.append('猪肉')
                                    print('当前背包物品为', L1)
                                elif (a2111 == '4'):
                                    money = (money - 200)
                                    print('您已消耗200元，买进王老五秘制辟邪狗血一份。当前剩余金钱为：', money)
                                    print('王老五秘制辟邪狗血一份已放入背包，')
                                    dogblood = (dogblood + 1)
                                    L1.append('王老五秘制辟邪狗血一份')
                                    print('当前背包物品为', L1)
                                elif (a2111 == '0'):
                                    w3 = '0'
                                    if (dogblood >= 5):
                                        print('王老五看到你如此钟爱于他的秘制狗血后差点感动哭了，连忙从店里追了出来，塞给你一个包裹')
                                        print('你打开一看，包裹里装着王老五秘制狗血的配方')
                                        print('系统消息：恭喜你喜获民间五大奇货之一的秘制狗血配方，集齐所有即可召唤小神龙【手动滑稽】')
                                        L5.append('王老五秘制狗血的配方')
                                        print('王老五秘制狗血的配方已放入收藏栏')
                                else:
                                    print('输入错误，请重新输入')
                            input("按回车键清屏并继续")
                            os.system('cls')
                        elif (a224 == '1'):
                            w3 = 1
                            n998 = 0
                            print('0.返回东市 1.驽马——10元2.良马——100元3.骐骥——200元4.骏马——300元')
                            while (w3 != '0'):
                                print('您当前的金钱为：', money)
                                a2111 = input('请输入选项：')
                                if (a2111 == '2'):
                                    money = (money - 100)
                                    print('您已消耗100元，买进良马一匹。当前剩余金钱为：', money)
                                    print('良马一匹已放入坐骑栏')
                                    L4.append('良马')
                                    print('当前坐骑栏物品为', L4)
                                elif (a2111 == '3'):
                                    money = (money - 200)
                                    print('您已消耗200元，买进骐骥一匹。当前剩余金钱为：', money)
                                    print('骐骥已放入坐骑栏，')
                                    L4.append('骐骥')
                                    print('当前坐骑栏物品为', L4)
                                elif (a2111 == '1'):
                                    money = (money - 10)
                                    print('您已消耗10元，买进劣马一匹。当前剩余金钱为：', money)
                                    print('驽马已放入坐骑栏，')
                                    L4.append('驽马')
                                    n998 = (n998 + 1)
                                    n889 = (n889 + 1)
                                    print('当前坐骑栏物品为', L4)
                                elif (a2111 == '4'):
                                    money = (money - 300)
                                    print('您已消耗300元，买进骏马一匹。当前剩余金钱为：', money)
                                    print('骏马已放入坐骑栏，')
                                    L4.append('骏马')
                                    print('当前坐骑栏物品为', L4)
                                elif (a2111 == '0'):
                                    if (n998 == 9):
                                        print('恭喜你达成成就‘功亏一篑’成就点+10')
                                        chengjiu = (chengjiu + 10)
                                    if (n889 == 10):
                                        print('恭喜你达成成就‘功在不舍’成就点+10')
                                        chengjiu = (chengjiu + 10)
                                    w3 = '0'
                                else:
                                    print('输入错误，请重新输入')
                            input("按回车键清屏并继续")
                            os.system('cls')
                        else:
                            print('输入错误，请重新输入')
                            w45 = '0'
                elif (a21 == '6'):
                    hs('官方公告：1.0版本开放5大市场，目前版本0.66（青龙复兴） 官方QQ群：439394084')
                    w5 = '0'
                else:
                    print('输入错误，请重新输入')
                    w5 = '0'
        else:
            w = '1'
            print('输入错误，请重新输入')

if (Lifevalue1 == 0):
    pass
print('游戏尚未制作完善，敬请期待')
