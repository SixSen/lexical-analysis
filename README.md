# Lexical-analysis
应用Python完成类FORTRAN/Pascal语言的词法分析

- 用于编译原理的学习
- 能够分辨变量定义与使用
- 对于变量的重复定义有错误提示



#### 运行结果
```
请输入源程序(输入':q'开始分析):
var ab,ke,vark,varD,0av,vark,MAT12
ab = vark;
ke := (3429 + 12）;
\ ls
vark：=0923
:q
分析结果:
=============================== line: 1
var  变量定义关键字
ab 标识符
,    逗号
ke 标识符
,    逗号
vark 标识符
,    逗号
varD 错误的标识符(不得包含大写字母)
,    逗号
0av 错误的词法(数字或符号不能以0开头)
,    逗号
vark 错误的标识符(重复定义)
,    逗号
MAT12 错误的标识符(不得包含大写字母)
=============================== line: 2
ab 使用标识符
=    错误的赋值号(应为 := )
vark 使用标识符
;    分号
=============================== line: 3
ke 使用标识符
:=   赋值号
(    左括号
3429 数字串
+    加号
12 数字串
)    右括号
;    分号
=============================== line: 4
非法的符号： \
ls 未定义的标识符(错误)
=============================== line: 5
vark 使用标识符
非法的符号： ：
=    错误的赋值号(应为 := )
0923 错误的词法(数字或符号不能以0开头)
```
