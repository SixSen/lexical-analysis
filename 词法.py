def lexical_analysis(src):
    """
    词法分析
    """
    # src = src.replace("\r", " ")
    # src = src.replace("\b", " ")
    # src = src.strip("\n")       # 去除每行结尾的换行符
    # unit = src.split()          # 根据空格进行分割为不同单元
    print("分析结果:")
    for unit in src:
        print("=============================== line:", src.index(unit)+1)
        for sentence in unit:
            index = unit.index(sentence)
            cur = 0
            sentence = sentence + " "   # 结尾加入空格以防止进行:=判断时发生访问地址越界
            while cur < len(sentence) - 1:
                if sentence[cur] == '+':
                    print("+    加号")
                    cur = cur + 1
                elif sentence[cur] == '(':
                    print("(    左括号")
                    cur = cur + 1
                elif sentence[cur] == ')':
                    print(")    右括号")
                    cur = cur + 1
                elif sentence[cur] == ';':
                    print(";    分号")
                    cur = cur + 1
                elif sentence[cur] == ',':
                    print(",    逗号")
                    cur = cur + 1
                elif sentence[cur] == '=':
                    print("=    错误的赋值号(应为 := )")
                    cur = cur + 1
                elif sentence[cur] == ':':
                    if sentence[cur + 1] == '=':
                        cur = cur + 2
                        print(":=   赋值号")
                    else:
                        cur = cur + 1
                        print(":    冒号")
                elif sentence[cur] == '0':
                    temp = ""
                    while 'a' <= sentence[cur] <= 'z' or sentence[cur].isdigit():
                        temp = temp + sentence[cur]
                        cur = cur + 1
                    print(temp, "错误的词法(数字或符号不能以0开头)")

                elif sentence[cur].isdigit():
                    err_flag = 0
                    temp = ""
                    while 'a' <= sentence[cur] <= 'z' or sentence[cur].isdigit():
                        if 'a' <= sentence[cur] <= 'z':
                            err_flag = 1
                        temp = temp + sentence[cur]
                        cur = cur + 1
                    if err_flag:
                        print(temp, "错误的词法(数字串中不能出现字母)")
                    else:
                        print(temp, "数字串")
                elif 'a' <= sentence[cur] <= 'z':
                    if sentence[cur:cur + 3] == 'var':
                        if sentence[cur + 3].isalnum():
                            temp = ""
                            err_flag = 0
                            while sentence[cur].isalnum():
                                if 'A' <= sentence[cur] <= 'Z':
                                    err_flag = 1
                                temp = temp + sentence[cur]
                                cur = cur + 1
                            if err_flag:
                                print(temp, "错误的标识符(不得包含大写字母)")
                            else:
                                print(temp, "标识符")
                        else:
                            cur = cur + 3
                            print("var  变量定义关键字")
                    else:
                        if 'a' <= sentence[cur] <= 'z' or sentence[cur].isdigit():
                            temp = ""
                            while 'a' <= sentence[cur] <= 'z' or sentence[cur].isdigit():
                                temp = temp + sentence[cur]
                                cur = cur + 1
                            print(temp, "标识符")
                elif 'A' <= sentence[cur] <= 'Z':
                    temp = ""
                    while sentence[cur].isalnum():
                        temp = temp + sentence[cur]
                        cur = cur + 1
                    print(temp, "错误的标识符(不得包含大写字母)")
                else:
                    print("非法的符号：", sentence[cur])
                    cur = cur + 1


if __name__ == "__main__":
    """
    主程序
    """
    program = []
    line = input("请输入源程序(输入':q'开始分析):\n")
    while line != ':q':
        line = line.strip("\n")  # 去除每行结尾的换行符
        words = line.split()  # 根据空格进行分割为不同单元
        program.append(words)
        line = input()
    lexical_analysis(program)
    input()
