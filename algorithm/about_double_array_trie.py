#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = "wangqiang"

'''
有关双数组trie树的实现
    用两个数组（base和check）来表示trie，兼容空间和时间负责度；当存储的词量很大时，存储空间和查询效率都优于trie树。
    两个数组的规则： base[i] + code(x) = j, check[j] = i
    在实现过程中，实际上还需要一个存储结构，用于保存所有节点的编码值。
'''


class DoubleArrayTrie:
    def __init__(self, words):
        self._char_code = None  # 保存所有的单字及其编码
        self._array_length = 0  # base与check数组的长度
        self._base_array = None
        self._check_array = None

        self._parse_words(words)  # 生成单字的编码
        self._init_base_check()  # 初始化base和check数组
        self._build_trie(words)  # 构建trie树

    def _build_trie(self, words):
        self._build_base_array(words)
        self._build_check_array()

    def _build_check_array(self):
        for index in range(len(self._check_array)):
            if index == 0:
                self._check_array[index] = -1
            elif self._base_array[index] is None:
                self._check_array[index] = None
            elif len(self._base_array[index][0]) == 1:
                self._check_array[index] = 0  # 根节点位置始终是0
            else:
                prefix = self._base_array[index][0]
                parent_prefix = prefix[:len(prefix) - 1]
                for base_index in range(len(self._base_array)):
                    base = self._base_array[base_index]
                    if base is not None and base[0] == parent_prefix:
                        break
                self._check_array[index] = base_index

    def _build_base_array(self, words):
        '''
        构建trie树，需要逐层构建
        '''
        level = 1
        while True:
            current_level_prefix = set()  # 记录当前层所有的前缀
            if level == 1:
                current_level_prefix.add("")
            else:
                for w in words:
                    if len(w) >= level:
                        current_level_prefix.add(w[0: level - 1])
            if len(current_level_prefix) == 0:
                break

            # 依次处理每个前缀
            for prefix in current_level_prefix:
                # 找到前缀的信息
                prefix_info = None
                for info in self._base_array:
                    if info is not None and info[0] is not None and info[0] == prefix:
                        prefix_info = info
                        break
                if not prefix_info:
                    break

                exists = set()
                for word in words:
                    if (prefix == "" or word.startswith(prefix)) and len(word) >= level:
                        ch = word[level - 1: level]
                        if ch in exists:
                            continue  # 已经在数组中，跳过即可
                        current = prefix + ch
                        current_index = prefix_info[1] + self._char_code[ch]
                        is_word = len(word) == level
                        if not self._base_array[current_index]:
                            # 位置未被占用，直接写入
                            self._base_array[current_index] = [current, prefix_info[1], is_word]
                        else:
                            # 位置已被占用，需要调整prefix的base值，再重新计算位置
                            prefix_base = prefix_info[1]
                            while True:
                                prefix_base += 1  # 尝试重新设置前缀的base值
                                # 需要将已经放置好的单字，用新的base值再计算一遍，判断是否有位置冲突
                                ch_all_index = []
                                has_conflict = False  # 记录是否有冲突
                                for ch_exist in exists:
                                    ch_new_index = prefix_base + self._char_code[ch_exist]
                                    ch_all_index.append(ch_new_index)
                                    if self._base_array[ch_new_index] is not None:
                                        has_conflict = True
                                        break
                                if has_conflict:
                                    # 出现冲突，需要对前缀base再+1，重新计算
                                    continue

                                # 尝试计算当前单字的位置
                                current_index = prefix_base + self._char_code[ch]
                                if current_index in ch_all_index or self._base_array[current_index] is not None:
                                    # 当前单字位置出现冲，需要对前缀base再+1，重头开始重新计算
                                    continue
                                else:
                                    # 位置没有重头，跳出循环
                                    break

                            # 先替换原有单字的位置
                            for ch_exist in exists:
                                old_index = prefix_info[1] + self._char_code[ch_exist]
                                new_index = prefix_base + self._char_code[ch_exist]
                                old_info = self._base_array[old_index]
                                self._base_array[old_index] = None
                                self._base_array[new_index] = [prefix + ch_exist, prefix_base, old_info[2]]

                            # 再设置当前单字的位置
                            self._base_array[prefix_base + self._char_code[ch]] = [current, prefix_base, is_word]

                            # 重置前缀的base
                            prefix_info[1] = prefix_base

                        exists.add(ch)
            level += 1

    def _parse_words(self, words):
        code_current = 0
        char_count = 0
        char_code_dict = {}
        for word in words:
            for ch in word:
                char_count += 1
                if ch not in char_code_dict:
                    code_current += 1
                    char_code_dict[ch] = code_current
        self._char_code = char_code_dict
        self._array_length = char_count

    def _init_base_check(self):
        self._base_array = [None] * self._array_length
        self._base_array[0] = ["", 1, False]  # 将root记录到index=0的位置 [prefix, base, is_word]
        self._check_array = [None] * self._array_length

    def contains(self, word):
        '''
        判断是否包含word
        '''
        prefix_index = 0
        base_value = 1
        last_info = None
        for ch in word:
            if ch not in self._char_code:
                # 存在trie树以外的单字，直接返回失败
                return False
            index = base_value + self._char_code[ch]
            check_value = self._check_array[index]
            if check_value != prefix_index:
                return False

            # 变更前缀信息，继续遍历
            prefix_index = index
            base_value = self._base_array[index][1]

            # 记录最后一轮的base信息，用于判断是否构成词组
            last_info = self._base_array[index]

        # 判断是否是完整的词
        return last_info[2]


if __name__ == '__main__':

    data = ["清华", "清华大学", "清新", "中华", "华人", "北京", "北京天安门", "北京的金山", "金山光芒", "光芒照四方"]
    dat = DoubleArrayTrie(data)
    print(dat._char_code)
    print(dat._base_array)
    print(dat._check_array)

    print(dat.contains("北京天安门"))
    print(dat.contains("光芒照四方"))
    print(dat.contains("北京的金山上"))
