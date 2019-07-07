# coding: utf-8

"""执行多个游戏客户端"""
import win32gui
from base import Ops, dm


class Base(Ops):
    def real_init(self):
        hds = []
        check_list = ['雷电模拟器-1-2-3', '雷电模拟器-1-2', '雷电模拟器-1', '雷电模拟器']
        for ch in check_list:
            hds_ = dm.EnumWindow(0, ch, 'LDPlayerMainFrame', 3)
            if hds_:
                hds_ = map(int, hds_.split(','))
                for hd in hds_:
                    if hd not in hds:
                        hds.insert(0, int(hd))
        hds = [int(dm.EnumWindow(hd, 'TheRender', 'RenderWindow', 3)) for hd in hds]
        self.orders = hds
        self.bind(self.orders[0])

    def check_no_mental(self):
        self.sleep_a_while(1)
        is_used = self.get_color(801,396) == '731010' and self.get_color(424,393) == '0b0b0b'
        if is_used:
            hd = self.hd
            self.switch()
            self.remove(hd)
            return True
        return False

    def bind(self, hd):
        self.hd = hd
        dm.BindWindow(hd, 'normal', 'windows', 'windows', 0)
        win32gui.SetForegroundWindow(hd)

    def switch(self):
        index = self.orders.index(self.hd)
        if index != len(self.orders) - 1:
            next_index = index + 1
        else:
            next_index = 0
        self.bind(self.orders[next_index])

    def main(self, click_pos, round_times, name=''):
        time.sleep(0.5)
        print(name)
        click = click_pos
        for i in range(round_times):
            self.setFront()
            self.sleep_a_while(0.5)
            # 1181,638 and 1182,656 是『开始行动』按钮的两个点
            need_click = dm.GetColor(832, 480) == '0093d5' and dm.GetColor(857, 490) == 'ffffff'
            if need_click:
                # 1214,38 是编队界面右上角的垃圾箱图标
                while self.get_color(913, 33) != '7d0000':
                    self.click(832, 480)
                    if self.check_no_mental():
                        print("{} :理智用完".format(name))
                        return True
                    self.sleep_a_while(1)
                    self.switch()
                    yield
            # 1210,55 是战斗界面右上角的暂停图标
            # 1126,468 是编队界面的『开始行动』图标
            while self.get_color(893, 36) != 'ffffff':
                self.click(822, 369)
                self.sleep_a_while(1)
                self.switch()
                yield

                # 现在应该进入战斗
            while not (dm.GetColor(832, 480) == '0093d5' and dm.GetColor(857, 490) == 'ffffff'):
                print(name)
                if self.check_no_mental():
                    print("{} :理智用完".format(name))
                    return True
                self.click(*click)
                self.sleep_a_while(0.5)
                self.switch()
                yield
                self.sleep_a_while(0.5)
        yield True

    def remove(self, hd):
        self.orders.remove(hd)

    def run(self, gs):

        assert len(gs) == len(self.orders)
        gss = [False for g in gs]
        while True:
            if all(gss):
                break
            for i, g in enumerate(gs):
                if gss[i]:
                    continue
                try:
                    next(g)
                except StopIteration:
                    print('{} stop'.format(str(g)))
                    gss[i] = True


CE5 = (696,131)
M1_7 = (438,168)
M4_4 = (406,250)
M4_9 = (416,257)
JIAO_MIE = (582,409)
XIN_PAIN2 = (627,195)


if __name__ == '__main__':
    import time
    time.sleep(3)
    b = Base(enable_front=True)
    gs = [
        b.main(M1_7, 100, "官服号"),
        b.main(CE5, 100, "b服凛寒"),
        b.main(XIN_PAIN2, 100, "b服柠檬sweet")
    ]
    b.run(gs)
