# 代码解析：
# 我们定义了一个名为josephus的函数，该函数接受一个参数n，表示人数。
# 在函数内部，我们首先创建一个包含1到n的人员列表people。
# 初始化索引index和报数计数器count为0。
# 使用循环来模拟报数和淘汰的过程，直到只剩下一人。每次报数到3时，将当前人员从列表中移除。
# 如果还有多余的人员，则更新索引和计数器。
# 最后，返回列表中剩下的唯一一个人的编号作为最后留下的结果。
# 在主程序中，定义输入的人数n。
# 调用josephus函数，将n作为参数传递，并将返回的结果存储在result变量中。
# 最后，打印输出最后留下的人的编号。

def josephus(n):
    # 创建人员列表
    people = list(range(1, n+1))

    # 初始化索引和报数计数器
    index = 0
    count = 0

    while len(people) > 1:
        count += 1
        # 报数到3时淘汰当前人员
        if count == 3:
            people.pop(index)
            count = 0
        else:
            index = (index + 1) % len(people)

    return people[0]

# 输入人数
n = int(input())

# 调用函数计算最后留下的人的编号
result = josephus(n)

# 输出结果
print(result)
