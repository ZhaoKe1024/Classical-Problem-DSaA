# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2025-02-07 19:00
class TuringMachine:
    def __init__(self, tape):
        self.tape = tape  # 纸带，用一个列表表示
        self.head = 0  # 指针位置
        self.state = 'q0'  # 初始状态

    def move_head(self, direction):
        if direction == 'R':
            self.head += 1
            if self.head == len(self.tape):  # 如果指针超出纸带范围，扩展纸带
                self.tape.append('0')
        elif direction == 'L':
            self.head -= 1
            if self.head < 0:  # 如果指针超出左边界，扩展纸带
                self.tape.insert(0, '0')
                self.head = 0
        else:
            pass

    def write(self, symbol):
        self.tape[self.head] = symbol

    def read(self):
        return self.tape[self.head]

    def run(self):
        while self.state != 'halt':
            current_symbol = self.read()
            if self.state == 'q0':
                if current_symbol == '1':
                    self.move_head('R')  # 向右移动，直到找到第一个数字的末尾
                elif current_symbol == '0':
                    self.write('1')
                    self.state = 'q1'  # 找到第一个数字的末尾，进入状态q1
                    self.move_head('R')  # 跳过空白符，开始处理第二个数字
            elif self.state == 'q1':
                if current_symbol == '1':
                    self.move_head('R')  # 向右移动，直到找到第二个数字的末尾
                elif current_symbol == '0':
                    self.state = 'q2'  # 找到第二个数字的末尾，进入状态q2
                    self.move_head('L')  # 回到第二个数字的起始位置
            elif self.state == 'q2':
                if current_symbol == '1':
                    self.write('0')  # 将第二个数字的1改为B
                    # self.state = 'halt'
                elif current_symbol == '0':
                    self.state = 'halt'  # 找到第二个数字的起始位置，进入状态q3

    def display_tape(self):
        return ''.join(self.tape).lstrip('B').rstrip('B')  # 去掉前导和后导的B


if __name__ == '__main__':
    tape = ['1', '1', '1', '1', '0', '1', '1', '1', '0']  # 用B表示空白符
    tm = TuringMachine(tape)
    tm.run()
    print("加法结果：", tm.display_tape())

