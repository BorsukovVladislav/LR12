#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check_skobki(s, skobki=0):
    if skobki < 0:
        return False
    if s:
        if s[0] == '(':
            skobki += 1
        elif s[0] == ')':
            skobki -= 1
        return check_skobki(s[1:], skobki)
    return skobki == 0


if __name__ == '__main__':
    if check_skobki(input("Введите строку: ")):
        print("Скобки раставлены правильно")
    else:
        print("Скобки раставлены не правильно")
