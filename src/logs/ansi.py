from enum import Enum
from typing import Union


class Graphic:
    def __init__(self, values: Union[str, int, list]):
        if isinstance(values, list):
            self.values = values
        elif isinstance(values, str):
            self.values = [values]
        elif isinstance(values, int):
            self.values = [str(values)]
        elif isinstance(values, Graphic):
            self.values = values.values
        else:
            raise TypeError('Graphic 类型必须是str, int, Graphic, list')

    def __add__(self, other: Union[str, int, "Graphic"]):
        """Graphic支持多个"""
        g = Graphic(values=[])
        g.values.extend(self.values)
        if isinstance(other, str):
            g.values.append(other)
        elif isinstance(other, int):
            g.values.append(str(other))
        elif isinstance(other, Graphic):
            g.values.extend(other.values)
        return g

    def __str__(self) -> str:
        return ';'.join([value for value in self.values]) + 'm'


class SGR:
    # select Graphic Rendition 选择图像再现
    RESET = Graphic(0)  # 关闭所有属性
    NORMAL = Graphic(0)  #
    BOLD = Graphic(1)  # 加粗
    INCREASE_INTENSITY = Graphic(1)  # 增强强度
    FAINT = Graphic(2)  # 小字号
    DECREASE_INTENSITY = Graphic(2)  # 减弱强度
    ITALIC = Graphic(3)  # 斜体
    UNDERLINE = Graphic(4)  # 下划线
    BLINK_SLOW = Graphic(5)  # 缓慢闪烁
    BLINK_RAPID = Graphic(6)  # 快速闪烁
    BLINK_FAST = Graphic(6)  # 快速闪烁
    NEGATIVE = Graphic(7)  # 反显
    CONCEAL = Graphic(8)  # 隐藏
    CROSSED_OUT = Graphic(9)  # 划除
    FONT_DEFAULT = Graphic(10)  # 默认字体
    FONT_1 = Graphic(11)  # 字体1
    FONT_2 = Graphic(12)  # 字体2
    FONT_3 = Graphic(13)  # 字体3
    FONT_4 = Graphic(14)  # 字体4
    FONT_5 = Graphic(15)  # 字体5
    FONT_6 = Graphic(16)  # 字体6
    FONT_7 = Graphic(17)  # 字体7
    FONT_8 = Graphic(18)  # 字体8
    FONT_9 = Graphic(19)  # 字体9
    BLACKLETTER = Graphic(20)  # 黑体
    UNDERLINE_DOUBLE = Graphic(21)  # 关闭粗体或双下划线
    NOT_BOLD = Graphic(21)  # 关闭粗体或双下划线
    NORMAL_INTENSITY = Graphic(22)  # 正常颜色或强度
    NOT_ITALIC = Graphic(23)  # 非斜体、非黑体
    NOT_BLACKLETTER = Graphic(23)  # 非黑体
    NOT_UNDERLINE = Graphic(24)  # 关闭下划线
    NOT_BLINKING = Graphic(25)  # 关闭反显
    STEADY = Graphic(25)  # 关闭闪烁
    NOT_REVERSED = Graphic(27)  # 关闭反显
    REVEAL = Graphic(28)  # 关闭隐藏
    NO_CROSSED_OUT = Graphic(29)  # 关闭化除
    FRAMED = Graphic(51)  # Framed
    ENCIRCLED = Graphic(52)  # Encircled
    OVERLINED = Graphic(53)  # 上划线
    NOT_FRAMED = Graphic(54)  # Not framed or encircled
    NOT_ENCIRCLED = Graphic(54)  # Not framed or encircled
    NOT_OVERLINED = Graphic(55)  # 关闭上划线

    ################################
    ######## color desc
    # 默认颜色是black, red, green, yellow, blue, magenta, cyan, white
    # 但是white默认对应的是gray
    # 以Foreground color举例
    # BLACK = 0;30 除了white，其他颜色都是只在暗色调情况下的颜色
    # DRAK_GRAY = 1;30
    # GRAY = 0;37  WHITE=1;37

    # Foreground color
    BLACK = Graphic(30)  # Black(=0) + Foreground(=30)
    RED = Graphic(31)  # Red(=1) + Foreground(=30)
    GREEN = Graphic(32)  # Green(=2) + Foreground(=30)
    YELLOW = Graphic(33)  # Yellow(=3) + Foreground(=30) = RED | GREEN
    BLUE = Graphic(34)  # Blue(=4) + Foreground(=30)
    MAGENTA = Graphic(35)  # Magenta(=5, 品红) + Foreground(=30) = RED | BLUE
    CYAN = Graphic(36)  # Cyan(=6, 青色) + Foreground(=30)   = GREEN | BLUE
    GRAY = Graphic(37)  # White(=7) + Foreground(=30)
    BIT = Graphic(38)  # Bit(=8, 8bit和24bit多位颜色表示的SGR) + Foreground(=30)
    DEFAULT = Graphic(39)  # Default(=9, 默认颜色) + Foreground(=30)
    DRAK_GRAY = INCREASE_INTENSITY + BLACK  # 1;30
    LIGHT_RED = INCREASE_INTENSITY + RED
    LIGHT_GREEN = INCREASE_INTENSITY + GREEN
    LIGHT_YELLOW = INCREASE_INTENSITY + YELLOW
    LIGHT_BLUE = INCREASE_INTENSITY + BLUE
    LIGHT_MAGENTA = INCREASE_INTENSITY + MAGENTA
    LIGHT_CYAN = INCREASE_INTENSITY + CYAN
    WHITE = INCREASE_INTENSITY + GRAY

    # ForegroundBright color
    BRIGHT_BLACK = Graphic(90)  # Black(=0) + ForegroundBright(=90)
    BRIGHT_RED = Graphic(91)  # Red(=1) + ForegroundBright(=90)
    BRIGHT_GREEN = Graphic(92)  # Green(=2) + ForegroundBright(=90)
    BRIGHT_YELLOW = Graphic(93)  # Yellow(=3) + ForegroundBright(=90)
    BRIGHT_BLUE = Graphic(94)  # Blue(=4) + ForegroundBright(=90)
    BRIGHT_MAGENTA = Graphic(95)  # Magenta(=5, 品红) + ForegroundBright(=90)
    BRIGHT_CYAN = Graphic(96)  # Cyan(=6, 青色) + ForegroundBright(=90)
    BRIGHT_GRAY = Graphic(97)  # White(=7) + ForegroundBright(=90)
    BRIGHT_DRAK_GRAY = INCREASE_INTENSITY + BRIGHT_BLACK  # 1;90
    BRIGHT_LIGHT_RED = INCREASE_INTENSITY + BRIGHT_RED
    BRIGHT_LIGHT_GREEN = INCREASE_INTENSITY + BRIGHT_GREEN
    BRIGHT_LIGHT_YELLOW = INCREASE_INTENSITY + BRIGHT_YELLOW
    BRIGHT_LIGHT_BLUE = INCREASE_INTENSITY + BRIGHT_BLUE
    BRIGHT_LIGHT_MAGENTA = INCREASE_INTENSITY + BRIGHT_MAGENTA
    BRIGHT_LIGHT_CYAN = INCREASE_INTENSITY + BRIGHT_CYAN
    BRIGHT_WHITE = INCREASE_INTENSITY + BRIGHT_GRAY

    # Background color
    BLACK_BG = Graphic(40)  # Black(=0) + Background(=40)
    RED_BG = Graphic(41)  # Red(=1) + Background(=40)
    GREEN_BG = Graphic(42)  # Green(=2) + Background(=40)
    YELLOW_BG = Graphic(43)  # Yellow(=3) + Background(=40)
    BLUE_BG = Graphic(44)  # Blue(=4) + Background(=40)
    MAGENTA_BG = Graphic(45)  # Magenta(=5, 品红) + Background(=40)
    CYAN_BG = Graphic(46)  # Cyan(=6, 青色) + Background(=40)
    GRAY_BG = Graphic(47)  # White(=7) + Background(=40)
    BIT_BG = Graphic(48)  # Bit(=8, 8bit和24bit多位颜色表示的SGR) + Foreground(=30)
    DEFAULT_BG = Graphic(49)  # Default(=9, 默认颜色) + Background(=40)
    DRAK_GRAY_BG = INCREASE_INTENSITY + BLACK_BG  # 1;40
    LIGHT_RED_BG = INCREASE_INTENSITY + RED_BG
    LIGHT_GREEN_BG = INCREASE_INTENSITY + GREEN_BG
    LIGHT_YELLOW_BG = INCREASE_INTENSITY + YELLOW_BG
    LIGHT_BLUE_BG = INCREASE_INTENSITY + BLUE_BG
    LIGHT_MAGENTA_BG = INCREASE_INTENSITY + MAGENTA_BG
    LIGHT_CYAN_BG = INCREASE_INTENSITY + CYAN_BG
    WHITE_BG = INCREASE_INTENSITY + GRAY_BG

    # BackgroundBright color
    BRIGHT_BLACK_BG = Graphic(100)  # Black(=0) + BackgroundBright(=100)
    BRIGHT_RED_BG = Graphic(101)  # Red(=1) + BackgroundBright(=100)
    BRIGHT_GREEN_BG = Graphic(102)  # Green(=2) + BackgroundBright(=100)
    BRIGHT_YELLOW_BG = Graphic(103)  # Yellow(=3) + BackgroundBright(=100)
    BRIGHT_BLUE_BG = Graphic(104)  # Blue(=4) + BackgroundBright(=100)
    BRIGHT_MAGENTA_BG = Graphic(105)  # Magenta(=5, 品红) + BackgroundBright(=100)
    BRIGHT_CYAN_BG = Graphic(106)  # Cyan(=6, 青色) + BackgroundBright(=100)
    BRIGHT_GRAY_BG = Graphic(107)  # White(=7) + BackgroundBright(=100)
    BRIGHT_DRAK_GRAY_BG = INCREASE_INTENSITY + BRIGHT_BLACK_BG  # 1;100
    BRIGHT_LIGHT_RED_BG = INCREASE_INTENSITY + BRIGHT_RED_BG
    BRIGHT_LIGHT_GREEN_BG = INCREASE_INTENSITY + BRIGHT_GREEN_BG
    BRIGHT_LIGHT_YELLOW_BG = INCREASE_INTENSITY + BRIGHT_YELLOW_BG
    BRIGHT_LIGHT_BLUE_BG = INCREASE_INTENSITY + BRIGHT_BLUE_BG
    BRIGHT_LIGHT_MAGENTA_BG = INCREASE_INTENSITY + BRIGHT_MAGENTA_BG
    BRIGHT_LIGHT_CYAN_BG = INCREASE_INTENSITY + BRIGHT_CYAN_BG
    BRIGHT_WHITE_BG = INCREASE_INTENSITY + BRIGHT_GRAY_BG


class Opr:
    def __init__(self, command: str, arg_num: int = 0):
        """
        指令信息
        Args:
            arg_num (int, optional): 质量需要的参数，默认是0个
        """
        self.command = command
        self.arg_num = arg_num
        self.params = []

    def add_params(self, args: list):
        self.params.extend([str(item) for item in list(args)])

    def __str__(self) -> str:
        if len(self.params) != self.arg_num:
            raise ValueError(f'当前命令需要{self.arg_num}个参数，传入{len(self.params)}个参数')
        return ';'.join(self.params) + self.command


class Cursor:
    UP = Opr('A', 1)  # 光标上移n行  nA
    DOWN = Opr('B', 1)  # 光标下移n行  nB
    FORWARD = Opr('C', 1)  # 光标右移n行  nC
    RIGHT = Opr('C', 1)  # 光标右移n行  nC
    BACK = Opr('D', 1)  # 光标左移n行  nD
    LEFT = Opr('D', 1)  # 光标左移n行  nD
    NEXT_LINE = Opr('E', 1)  # 下n行       nE
    PREV_LINE = Opr('F', 1)  # 上n行       nF
    GOTO_X = Opr('G', 1)  # 光标水平移动到第n列 nG
    GOTO = Opr('H', 2)  # 设置光标位置  y;xH
    ERASE = Opr('2J', 0)  # 清屏
    ERASE_LINE = Opr('K', 0)  # 清除从光标到行尾的内容
    SCROLL_UP = Opr('S', 0)  # 向上滚动 nS
    SCROLL_DOWN = Opr('T', 0)  # 向下滚动 nT
    SAVE_CURSOR = Opr('s', 0)  # 保存光标位置
    LOAD_CURSOR = Opr('u', 0)  # 恢复光标位置
    SHOW = Opr('?25h', 0)  # 隐藏光标
    HIDE = Opr('?25l', 0)  # 显示光标


# ANSI转义序列中以 ESC [ 开头的叫作 Control Sequence Introducer，简写为 CSI
# 十六进制是\x1b, 八进制是\033
CSI = '\x1b['
# OSC 代表的是 Operating System Controls, 主要是拷贝，以\a结尾
OSC = '\x1b]'
# OSC 结束符
BEL = '\a'


def sequence(letter: Union[str, "Opr", "Graphic"]):
    """
    letter: 命令
        在SGR中，是数字列表+m  1;30m
        在Cursor中，是指令A,B,C,D等
    """

    def _sequence(*args: Union[str, int, "Opr", "Graphic"]) -> str:
        """args：主要是指Cursor中的参数"""
        params = [str(item) for item in list(args)]
        # 在每一个颜色设置后，添加重置效果
        RESET = ' \x1b[' + str(SGR.RESET)
        if isinstance(letter, Graphic):
            if len(params) > 0:
                content = ' '.join(params)
                if content.strip() == '':
                    return ''
                command_content = str(letter) + content
                # print(f'SGR:{command_content+RESET}')
                return CSI + command_content + RESET
            return ''
            # raise ValueError('SGR需要配置显示内容')
        elif isinstance(letter, Opr):
            if len(params) > 0:
                letter.add_params(params)
            command_content = str(letter)
            # print(f'cursor:{command_content}')
            # 对于鼠标Opr，无需配置RESET
            return CSI + command_content
        else:
            if len(params) == 0:
                command_content = str(letter)
            else:
                command_content = ';'.join(params) + str(letter)
            # print(f'default:{command_content+RESET}')
            return CSI + command_content + RESET

    return _sequence


# if __name__ == '__main__':
#     # import os
#     # # windows需要执行，linux可以不用执行
#     # os.system('')
#
#     # SGR使用方式
#     black = sequence(SGR.BLACK)  # 定义Graphic
#     print(black('hello world'))  # 赋值在文本上并执行
#     # Cursor使用方式
#     up = sequence(Cursor.UP)  # 定义Cursor
#     print(up(1))  # 赋值操作并执行
