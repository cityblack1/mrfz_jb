#!/usr/bin/python

import win32com.client
import win32gui
import time

dm = win32com.client.Dispatch('dm.dmsoft')
#current version
print(dm.Ver())

class Ops(object):
    def __init__(self, enable_front=True):
        """hwnd 整形数: 指定的窗口句柄

display 字符串: 屏幕颜色获取方式 取值有以下几种

"normal" : 正常模式,平常我们用的前台截屏模式

"gdi" : gdi模式,用于窗口采用GDI方式刷新时. 此模式占用CPU较大.

"gdi2" : gdi2模式,此模式兼容性较强,但是速度比gdi模式要慢许多,如果gdi模式发现后台不刷新时,可以考虑用gdi2模式.

"dx2" : dx2模式,用于窗口采用dx模式刷新,如果dx方式会出现窗口所在进程崩溃的状况,可以考虑采用这种.采用这种方式要保证窗口有一部分在屏幕外.win7或者vista不需要移动也可后台.此模式占用CPU较大.

"dx3" : dx3模式,同dx2模式,但是如果发现有些窗口后台不刷新时,可以考虑用dx3模式,此模式比dx2模式慢许多. 此模式占用CPU较大.

"dx" : dx模式,等同于BindWindowEx中，display设置的"dx.graphic.2d|dx.graphic.3d",具体参考BindWindowEx
注意此模式需要管理员权限

mouse 字符串: 鼠标仿真模式 取值有以下几种

"normal" : 正常模式,平常我们用的前台鼠标模式

"windows": Windows模式,采取模拟windows消息方式 同按键自带后台插件.

"windows2": Windows2 模式,采取模拟windows消息方式(锁定鼠标位置) 此模式等同于BindWindowEx中的mouse为以下组合
"dx.mouse.position.lock.api|dx.mouse.position.lock.message|dx.mouse.state.message"
注意此模式需要管理员权限

"windows3": Windows3模式，采取模拟windows消息方式,可以支持有多个子窗口的窗口后台.

"dx": dx模式,采用模拟dx后台鼠标模式,这种方式会锁定鼠标输入.有些窗口在此模式下绑定时，需要先激活窗口再绑定(或者绑定以后激活)，否则可能会出现绑定后鼠标无效的情况.此模式等同于BindWindowEx中的mouse为以下组合
"dx.public.active.api|dx.public.active.message|dx.mouse.position.lock.api|dx.mouse.position.lock.message|dx.mouse.state.api|dx.mouse.state.message|dx.mouse.api|dx.mouse.focus.input.api|dx.mouse.focus.input.message|dx.mouse.clip.lock.api|dx.mouse.input.lock.api|dx.mouse.cursor"
注意此模式需要管理员权限

"dx2"：dx2模式,这种方式类似于dx模式,但是不会锁定外部鼠标输入.
有些窗口在此模式下绑定时，需要先激活窗口再绑定(或者绑定以后手动激活)，否则可能会出现绑定后鼠标无效的情况. 此模式等同于BindWindowEx中的mouse为以下组合
"dx.public.active.api|dx.public.active.message|dx.mouse.position.lock.api|dx.mouse.state.api|dx.mouse.api|dx.mouse.focus.input.api|dx.mouse.focus.input.message|dx.mouse.clip.lock.api|dx.mouse.input.lock.api| dx.mouse.cursor"
注意此模式需要管理员权限

keypad 字符串: 键盘仿真模式 取值有以下几种

"normal" : 正常模式,平常我们用的前台键盘模式

"windows": Windows模式,采取模拟windows消息方式 同按键的后台插件.

"dx": dx模式,采用模拟dx后台键盘模式。有些窗口在此模式下绑定时，需要先激活窗口再绑定(或者绑定以后激活)，否则可能会出现绑定后键盘无效的情况. 此模式等同于BindWindowEx中的keypad为以下组合
"dx.public.active.api|dx.public.active.message| dx.keypad.state.api|dx.keypad.api|dx.keypad.input.lock.api"
注意此模式需要管理员权限

"""
        self.enable_front = enable_front
        self.real_init()

    def real_init(self):
        hd = dm.EnumWindow(0, 'TheRender', 'RenderWindow', 3)
        dm.BindWindow(int(hd), 'normal', 'windows', 'windows', 0)
        self.hd = int(hd)
        self.setFront()

    def setFront(self):
        if self.enable_front:
            win32gui.SetForegroundWindow(self.hd)

    def sleep_a_while(self, t=None):
        time.sleep(t or 0.1)

    def get_color(self, x, y):
        self.setFront()
        self.sleep_a_while()
        re = dm.GetColor(x, y)
        # print(re)
        return re

    def get_current_post(self):
        _, x, y = dm.GetCursorPos
        return x, y

    def click(self, x, y):
        dm.MoveTo(x, y)
        self.sleep_a_while()
        dm.LeftClick()


if __name__ == '__main__':
    # print(Ops.right_click())
    o = Ops()
    import time
    print(o.get_color(767,464))
    o.click(767,464)