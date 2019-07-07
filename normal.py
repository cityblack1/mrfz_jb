# coding: utf-8

from base import Ops, dm


class MyOps(Ops):
    def run(self):
        self.setFront()
        self.sleep_a_while(1)
        # 1181,638 and 1182,656 是『开始行动』按钮的两个点
        need_click = dm.GetColor(1181,638) == '0094d6' and dm.GetColor(1182,656) == 'fdffff'
        if need_click:
            # 1214,38 是编队界面右上角的垃圾箱图标
            while self.get_color(1214,38) != '7d0000':
                self.click(1181,638)
                self.sleep_a_while(1)
        # 1210,55 是战斗界面右上角的暂停图标
        # 1126,468 是编队界面的『开始行动』图标
        while self.get_color(1210,55) != 'ffffff':
            self.click(1126,468)
            self.sleep_a_while(1)

        # 现在应该进入战斗
        while not (dm.GetColor(1181, 638) == '0094d6' and dm.GetColor(1182, 656) == 'fdffff'):
            self.click(*JINGYAN5)
            self.sleep_a_while(4)

def main():
    o = MyOps()
    # while True:
    for i in range(10):
        o.run()

LONGMEN5 = (927,168)
JINGYAN5 = (928,170)
JIAOMIE = (844,482)
M4_6 = (562,341)
M1_6 = (550,344)
M1_7 = (534,227)
PRB2 = (845,250)
if __name__ == '__main__':
    import  time
    time.sleep(5)
    main()

# 龙门比5： 927,168
# 经验 5 ： 928,170
# 剿灭作战：844,482