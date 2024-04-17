# ANSI
---

### ASCII编码表
    | 二进制 |  十进制 | 十六进制 | 字符/缩写 | 解释 |
    | ------|---------|----------|----------|------|
    | 00000000 | 0 | 00 | NUL (NULL) | 空字符 |
    | 00000001 | 1 | 01 | SOH (Start Of Headling) | 标题开始 |
    | 00000010 | 2 | 02 | STX (Start Of Text) | 正文开始 |
    | 00000011 | 3 | 03 | ETX (End Of Text) | 正文结束 |
    | 00000100 | 4 | 04 | EOT (End Of Transmission) | 传输结束 |
    | 00000101 | 5 | 05 | ENQ (Enquiry) | 请求 |
    | 00000110 | 6 | 06 | ACK (Acknowledge) | 回应/响应/收到通知 |
    | 00000111 | 7 | 07 | BEL (Bell) | 响铃 |
    | 00001000 | 8 | 08 | BS (Backspace) | 退格 |
    | 00001001 | 9 | 09 | HT (Horizontal Tab) | 水平制表符 |
    | 00001010 | 10 | 0A | LF/NL(Line Feed/New Line) | 换行键 |
    | 00001011 | 11 | 0B | VT (Vertical Tab) | 垂直制表符 |
    | 00001100 | 12 | 0C | FF/NP (Form Feed/New Page) | 换页键 |
    | 00001101 | 13 | 0D | CR (Carriage Return) | 回车键 |
    | 00001110 | 14 | 0E | SO (Shift Out) | 不用切换 |
    | 00001111 | 15 | 0F | SI (Shift In) | 启用切换 |
    | 00010000 | 16 | 10 | DLE (Data Link Escape) | 数据链路转义 |
    | 00010001 | 17 | 11 | DC1/XON (Device Control 1/Transmission On) | 设备控制1/传输开始 |
    | 00010010 | 18 | 12 | DC2 (Device Control 2) | 设备控制2 |
    | 00010011 | 19 | 13 | DC3/XOFF (Device Control 3/Transmission Off) | 设备控制3/传输中断 |
    | 00010100 | 20 | 14 | DC4 (Device Control 4) | 设备控制4 |
    | 00010101 | 21 | 15 | NAK (Negative Acknowledge) | 无响应/非正常响应/拒绝接收 |
    | 00010110 | 22 | 16 | SYN (Synchronous Idle) | 同步空闲 |
    | 00010111 | 23 | 17 | ETB (End of Transmission Block) | 传输块结束/块传输终止 |
    | 00011000 | 24 | 18 | CAN (Cancel) | 取消 |
    | 00011001 | 25 | 19 | EM (End of Medium) | 已到介质末端/介质存储已满/介质中断 |
    | 00011010 | 26 | 1A | SUB (Substitute) | 替补/替换 |
    | 00011011 | 27 | 1B | ESC (Escape) | 逃离/取消 |
    | 00011100 | 28 | 1C | FS (File Separator) | 文件分割符 |
    | 00011101 | 29 | 1D | GS (Group Separator) | 组分隔符/分组符 |
    | 00011110 | 30 | 1E | RS (Record Separator) | 记录分离符 |
    | 00011111 | 31 | 1F | US (Unit Separator) | 单元分隔符 |
    | 00100000 | 32 | 20 | (Space) | 空格 |
    | 00100001 | 33 | 21 | ! | | |
    | 00100010 | 34 | 22 | " | | |
    | 00100011 | 35 | 23 | # | | |
    | 00100100 | 36 | 24 | $ | | |
    | 00100101 | 37 | 25 | % | | |
    | 00100110 | 38 | 26 | & | | |
    | 00100111 | 39 | 27 | ' | | |
    | 00101000 | 40 | 28 | ( | | |
    | 00101001 | 41 | 29 | ) | | |
    | 00101010 | 42 | 2A | * | | |
    | 00101011 | 43 | 2B | + | | |
    | 00101100 | 44 | 2C | , | | |
    | 00101101 | 45 | 2D | - | | |
    | 00101110 | 46 | 2E | . | | |
    | 00101111 | 47 | 2F | / | | |
    | 00110000 | 48 | 30 | 0 | | |
    | 00110001 | 49 | 31 | 1 | | |
    | 00110010 | 50 | 32 | 2 | | |
    | 00110011 | 51 | 33 | 3 | | |
    | 00110100 | 52 | 34 | 4 | | |
    | 00110101 | 53 | 35 | 5 | | |
    | 00110110 | 54 | 36 | 6 | | |
    | 00110111 | 55 | 37 | 7 | | |
    | 00111000 | 56 | 38 | 8 | | |
    | 00111001 | 57 | 39 | 9 | | |
    | 00111010 | 58 | 3A | : | | |
    | 00111011 | 59 | 3B | ; | | |
    | 00111100 | 60 | 3C | < | | |
    | 00111101 | 61 | 3D | = | | |
    | 00111110 | 62 | 3E | > | | |
    | 00111111 | 63 | 3F | ? | | |
    | 01000000 | 64 | 40 | @ | | |
    | 01000001 | 65 | 41 | A | | |
    | 01000010 | 66 | 42 | B | | |
    | 01000011 | 67 | 43 | C | | |
    | 01000100 | 68 | 44 | D | | |
    | 01000101 | 69 | 45 | E | | |
    | 01000110 | 70 | 46 | F | | |
    | 01000111 | 71 | 47 | G | | |
    | 01001000 | 72 | 48 | H | | |
    | 01001001 | 73 | 49 | I | | |
    | 01001010 | 74 | 4A | J | | |
    | 01001011 | 75 | 4B | K | | |
    | 01001100 | 76 | 4C | L | | |
    | 01001101 | 77 | 4D | M | | |
    | 01001110 | 78 | 4E | N | | |
    | 01001111 | 79 | 4F | O | | |
    | 01010000 | 80 | 50 | P | | |
    | 01010001 | 81 | 51 | Q | | |
    | 01010010 | 82 | 52 | R | | |
    | 01010011 | 83 | 53 | S | | |
    | 01010100 | 84 | 54 | T | | |
    | 01010101 | 85 | 55 | U | | |
    | 01010110 | 86 | 56 | V | | |
    | 01010111 | 87 | 57 | W | | |
    | 01011000 | 88 | 58 | X | | |
    | 01011001 | 89 | 59 | Y | | |
    | 01011010 | 90 | 5A | Z | | |
    | 01011011 | 91 | 5B | [ | | |
    | 01011100 | 92 | 5C | \ | | |
    | 01011101 | 93 | 5D | ] | | |
    | 01011110 | 94 | 5E | ^ | | |
    | 01011111 | 95 | 5F | _ | | |
    | 01100000 | 96 | 60 | ` | | |
    | 01100001 | 97 | 61 | a | | |
    | 01100010 | 98 | 62 | b | | |
    | 01100011 | 99 | 63 | c | | |
    | 01100100 | 100 | 64 | d | | |
    | 01100101 | 101 | 65 | e | | |
    | 01100110 | 102 | 66 | f | | |
    | 01100111 | 103 | 67 | g | | |
    | 01101000 | 104 | 68 | h | | |
    | 01101001 | 105 | 69 | i | | |
    | 01101010 | 106 | 6A | j | | |
    | 01101011 | 107 | 6B | k | | |
    | 01101100 | 108 | 6C | l | | |
    | 01101101 | 109 | 6D | m | | |
    | 01101110 | 110 | 6E | n | | |
    | 01101111 | 111 | 6F | o | | |
    | 01110000 | 112 | 70 | p | | |
    | 01110001 | 113 | 71 | q | | |
    | 01110010 | 114 | 72 | r | | |
    | 01110011 | 115 | 73 | s | | |
    | 01110100 | 116 | 74 | t | | |
    | 01110101 | 117 | 75 | u | | |
    | 01110110 | 118 | 76 | v | | |
    | 01110111 | 119 | 77 | w | | |
    | 01111000 | 120 | 78 | x | | |
    | 01111001 | 121 | 79 | y | | |
    | 01111010 | 122 | 7A | z | | |
    | 01111011 | 123 | 7B | { | | |
    | 01111100 | 124 | 7C | | | | |
    | 01111101 | 125 | 7D | } | | |
    | 01111110 | 126 | 7E | ~ | | |
    | 01111111 | 127 | 7F | DEL (Delete) | 删除 |

### ANSI escape code日常用法
1. 常用语法格式

    常用的ansi escape code的语法看起如下：
    ```
    0x1B + "[" + <zero or more numbers, separated by ";"> + <a letter>
    ```
    加号将语法分为了几部分，阅读语法的方式：

    最前面的0x1B 是ansi escape code开始的标准
    接着的 `[` 已经说过了，是CSI (Control Sequence Introducer)
    中间部分的` <zero or more numbers, separated by ";"> `由0个或者多个数字组成，是函数的参数，多个参数之间由分号进行分割。
    最终部分的` <a letter> `是一个字母，是ansi escape code需要调用的函数名
    CSI (Control Sequence Introducer) 各部分的字符范围如下(简单了解即可)：

    | 组成部分 | 字符范围 | ASCII |
    | ------- | ------- |------ |
    | 参数字节 | 0x30–0x3F | 0–9:;<=>? |
    | 中间字节 | 0x20–0x2F | 空格、!"#$%&’()*+,-./ |
    | 最终字节 | 0x40–0x7E | @A–Z[]^_`a–z{ |
    如果您看到`\x1b[0;1;34m`，您可以这样阅读：
    ```
    \x1b[  # call a CSI function
    0;1;34 # function arguments (0, 1, 34)
    m      # function name
    ```
    因此: 上面这句话可以理解为m(0, 1, 34); 同样，\x1b[A 可以理解为: A()。

2. 可用的函数  
    |   | name                         | signature  | description |
    | --| ---------------------------- |----------- | ----------- |
    | A | Cursor Up                    | (n=1)      | Move cursor up by n 【将光标向上移动n行】 |
    | B | Cursor Down                  | (n=1)      | Move cursor down by n 【将光标向下移动n行】 |
    | C | Cursor Forward               | (n=1)      | Move cursor forward by n 【将光标向前移动n个字符】 |
    | D | Cursor Back                  | (n=1)      | Move cursor back by n 【将光标向后移动n个字符】 |
    | E | Cursor Next Line             | (n=1)      | Move cursor to the beginning of the line n lines down【将光标向下移到到n行的行首】 |
    | F | Cursor Previous Line         | (n=1)      | Move cursor to the beginning of the line n lines up【将光标向上移到到n行的行首】 |
    | G | Cursor Horizontal Absolute   | (n=1)      | Move cursor to the the column nwithin the current row 【将光标移动到当前行中的第n列】 |
    | H | Cursor Position              | (n=1, m=1) | Move cursor to row n, column m, counting from the top left corner |
    | J | Erase in Display             | (n=0)      | Clear part of the screen. 0, 1, 2, and 3 have various specific functions |
    | K | Erase in Line                | (n=0)      | Clear part of the line. 0, 1, and 2 have various specific functions |
    | S | Scroll Up                    | (n=1)      | Scroll window up by n lines 【将窗口向上滚动到n行】 |
    | T | Scroll Down                  | (n=1)      | Scroll window down by n lines 【将窗口向下滚动到n行】 |
    | s | Save Cursor Position         | ()         | Save current cursor position for use with u |
    | u | Restore Cursor Position      | ()         | Set cursor back to position last saved by s |
    | f | …                            | …          | (same as G) |
    | m | SGR                          | (*)        | Set graphics mode. More below |

3. 单独介绍SGR(Set graphics mode)
    | value | name / description |
    | ----- | ------------------ |
    | 0 | Reset: turn off all attributes 【重置：关闭所有属性】 |
    | 1 | Bold (or bright, it’s up to the terminal and the user config to some extent) 【粗体】 |
    | 3 | Italic 【斜体】 |
    | 4 | Underline 【下划线】 |
    | 5 | 缓慢闪烁 |
    | 6 | 快速闪烁 |
    | 7 | 反显 |
    | 8 | 隐藏 |
    | 9 | 划除 |
    | 10 | 主要(默认)字体 |
    | 11-19 | 替代字体 |
    | 20 | 尖角体 |
    | 21 | 关闭粗体或双下划线 |
    | 22 | 正常颜色或强度 |
    | 23 | 非斜体、非尖角体 |
    | 24 | 关闭下划线 |
    | 25 | 关闭闪烁 |
    | 27 | 关闭反显 |
    | 28 | 关闭隐藏 |
    | 29 | 关闭化除 |
    | 30–37 | Set text colour from the basic colour palette of 0–7 【从0-7的基本颜色板中设置文本颜色,即前景色】 |
    | 38;5;n | Set text colour to index n in a 256-colour palette(e.g. \x1b[38;5;34m)【前景色】 |
    | 38;2;r;g;b | Set text colour to an RGB value (e.g. \x1b[38;2;255;255;0m)【前景色】 |
    | 39 | 默认前景色 |
    | 40–47 | Set background colour 【从0-7的基本颜色板中设置背景色】 |
    | 48;5;n | Set background colour to index n in a 256-colour palette 【背景色】 |
    | 48;2;r;g;b | Set background colour to an RGB value 【背景色】 |
    | 49 | 默认背景色 |
    | 51 | Framed |
    | 52 | Encircled |
    | 53 | 上划线 |
    | 54 | Not framed or encircled |
    | 55 | 关闭上划线 |
    | 60 | 表意文字下划线或右边线 |
    | 61 | 表意文字双下划线或双右边线 |
    | 62 | 表意文字上划线或左边线 |
    | 63 | 表意文字双上划线或双左边线 |
    | 64 | 表意文字着重标志 |
    | 65 | 表意文字属性关闭 |
    | 90–97 | Set text colour from the bright colour palette of 0–7 |
    | 100–107 | Set background colour from the bright colour palette of 0–7 |

4. 基本颜色面板 Colour Palettes
    - 颜色面板
        | value | name / description |
        | ----- | ------------------ |
        | 0 | Black |
        | 1 | Red |
        | 2 | Green |
        | 3 | Yellow |
        | 4 | Blue |
        | 5 | Magenta |
        | 6 | Cyan |
        | 7 | White |

    - 颜色显示位置
        | value | name / description |
        | ----- | ------------------ |
        | 30 | Foreground(前景字体颜色) |
        | 40 | Background(背景色) |
        | 90 | ForegroundBright(字体颜色高亮) |
        | 100 | BackgroundBright(背景颜色高亮) |
    
    - 显示类型
        | value | name / description |
        | ----- | ------------------ |
        | 0 | 终端默认设置（黑底白字） |
        | 1 | 高亮显示 |
        | 4 | 使用下划线 |
        | 5 | 闪烁 |
        | 7 | 反白显示 |
        | 8 | 不可见 |

5. 其他有用的转义
    | value | name / description |
    | ----- | ------------------ |
    | \x1b[?25h | 显示光标 |
    | \x1b[?25l | 隐藏光标 |

### 颜色
| 格式 | 描述 |
| ----- | ------------------ |
| \x1b[31m | \x1b和\033都是ANSI中的ESC，一个是十六进制，一个是八进制；31表示红色，m表示SGR函数 |
| \x1b[0;32m | 0;30 第一个表示显示类型, 32表示字体颜色 |
| \x1b[0;40;32m | 0;40;30 第一个表示显示类型，40表示背景颜色，32表示字体颜色；所有数字可以调整顺序，通过取值确认配置项 |
| \x1b[38;5;nm | 固定设置前景色颜色的方式，n取值是0-255 |
| \x1b[38;2;r;g;bm | 固定设置前景色颜色的RGB方式，r,g,b取值是0-255 |
| \x1b[48;5;nm | 固定设置前景色颜色的方式，n取值是0-255 |
| \x1b[48;2;r;g;bm | 固定设置前景色颜色的RGB方式，r,g,b取值是0-255 |

### 鼠标控制
| 格式 | 描述 |
| ----- | --- |
| \x1b[nA | 光标上移n行 |
| \x1b[nB | 光标下移n行 |
| \x1b[nC | 光标右移n列 |
| \x1b[nD | 光标左移n列 |
| \x1b[y;xH | 设置光标位置（y行,x列） |
| \x1b[2J | 清屏 |
| \x1b[K | 清除从光标到行尾的内容 |
| \x1b[s | 保存光标位置 |
| \x1b[u | 恢复光标位置 |
| \x1b[?25h | 隐藏光标 |
| \x1b[?25l | 显示光标 |

### 参考文献
1. [ASCII码一览表](http://c.biancheng.net/c/ascii/)
2. [ASCII码一览表](https://zhuanlan.zhihu.com/p/570148970)
3. [github_ansi](https://github.com/tehmaze/ansi)