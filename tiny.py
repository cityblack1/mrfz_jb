# coding: utf-8

from base import Ops, dm

"""tiny 是 540 × 960 分辨率"""

class MyOps(Ops):
    def run(self, click_pos):
        # self.setFront()
        self.sleep_a_while(1)
        # 1181,638 and 1182,656 是『开始行动』按钮的两个点
        need_click = dm.GetColor(832,480) == '0093d5' and dm.GetColor(857,490) == 'ffffff'
        if need_click:
            # 1214,38 是编队界面右上角的垃圾箱图标
            while self.get_color(913,33) != '7d0000':
                self.click(832,480)
                self.sleep_a_while(1)
        # 1210,55 是战斗界面右上角的暂停图标
        # 1126,468 是编队界面的『开始行动』图标
        while self.get_color(893,36) != 'ffffff':
            self.click(822,369)
            self.sleep_a_while(1)

        # 现在应该进入战斗
        while not (dm.GetColor(832,480) == '0093d5' and dm.GetColor(857,490) == 'ffffff'):
            print('inhere')
            self.click(*click_pos)
            self.sleep_a_while(3)


if __name__ == '__main__':
    o = MyOps()
    while True:
        o.run((348, 387))