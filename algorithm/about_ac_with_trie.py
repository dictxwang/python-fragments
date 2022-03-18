# -*- coding: utf8 -*-
__author__ = 'wangqiang'


"""
trie的使用：实现多模字符串的匹配（类AC自动机）
"""

import re
import about_trie


def make_trie(keywords_file):
    """
    构建trie树
    :param keywords_file: 关键词文件
    :return:
    """
    trie = about_trie.Trie()
    fp = open(keywords_file, mode="r", encoding="utf8")
    for line in fp.readlines():
        line = line.strip("\r\n").strip("\n")
        line = line.strip()
        trie.insert(line)
    fp.close()
    return trie


def make_keywords_file(input, output):
    """
    通过一段英文文本生成词表文件
    :param input:
    :param output:
    :return:
    """
    all_words = set()
    fp = open(input, mode="r", encoding="utf8")

    # 预编译正则表达式，提升效率
    regex = re.compile(r"[;|,|:|\(|\)|\+|\-|\"|'|\[|\]|\.|“|”]*")
    regex_html = re.compile(r"(</?\s*.+>)*", re.IGNORECASE)
    for line in fp.readlines():
        line = line.strip("\r\n").strip("\n")
        line = line.strip()
        line = re.sub(regex_html, "", line)
        words = line.split(" ")
        for word in words:
            word = re.sub(regex, "", word)
            if word:
                all_words.add(word)
    fp.close()
    ofp = open(output, mode="w", encoding="utf8")
    for w in all_words:
        ofp.write(w + "\n")
        ofp.flush()
    ofp.close()


def search_match_words(trie, text):
    """
    查找命中的关键词，以及对应命中的下标位置
    :param trie:
    :param text:
    :return: 同时返回命中词和位置
    """
    def nfa_match(current_node, text, start_index=0, matched_prefix="", first_level=False):
        """
        非确定型有穷自动机（Non-determinism Finite Automate, NFA）匹配模式
        带回溯的模式，当发生匹配失败阻断时，需要将已匹配的字符回溯
        :param current_node: trie的当前节点
        :param text: 待匹配的文本
        :param start_index: text起始匹配位置
        :param matched_prefix: 已配的文本前缀
        :param first_level: 是否是第一层匹配
        :return:
        """
        words_with_pos = []
        # text匹配到末尾
        if start_index >= len(text):
            return words_with_pos
        text_current_char = text[start_index]
        if text_current_char == " " or current_node.get_key() != text_current_char:
            # 当前字符是分隔符或当前位置不匹配并且当前是第一层匹配（当前节点的父节点是root节点）；
            # 将text前进一位继续匹配（这里需要将已匹配的前缀丢掉）
            if first_level:
                words_with_pos.extend(nfa_match(current_node, text, start_index=start_index+1,
                                                matched_prefix="", first_level=True))
        else:
            if current_node.get_key() == text_current_char:
                # 如果匹配成功且当前节点是word结束点，追加到结果中
                if current_node.get_is_word():
                    words_with_pos.append((matched_prefix + text_current_char, start_index - len(matched_prefix)))
                # 继续递归匹配当前节点的子节点
                # 这里不需要匹配所有子节点，选取其中key和下一个位置一致的匹配即可
                for key, child in current_node.get_children().items():
                    if start_index + 1 < len(text) and key == text[start_index + 1]:
                        words_with_pos.extend(nfa_match(child, text, start_index=start_index+1,
                                                        matched_prefix=matched_prefix+text_current_char))

        return words_with_pos

    wps = []
    if text:
        root = trie.get_root()
        for index in range(len(text)):
            for child in root.get_children().values():
                wps.extend(nfa_match(child, text, start_index=index, matched_prefix="", first_level=True))

    # 结果去重并排序
    words = []
    exists = []
    for wp in wps:
        key = f"{wp[0]}_{wp[1]}"
        if key not in exists:
            words.append(wp)
            exists.append(key)
    # 按命中位置排序
    words.sort(key=lambda x: x[1])
    return words


if __name__ == '__main__':

    keywords_file = "data/for_trie_keywords.txt"

    # 创建keywords文件
    # keywords_source_file = "data/trie_keywords_source.txt"
    # make_keywords_file("data/trie_keywords_source.txt", "data/for_trie_keywords.txt")

    # 构建trie树
    trie = make_trie(keywords_file)
    # 查找
    print(trie.search("士農工商"))

    # 匹配
    print(search_match_words(trie, "士農工商"))
    print(search_match_words(trie, "123士農工商"))
    print(search_match_words(trie, "士農工商xyz"))
    print(search_match_words(trie, "123Historians are now turning to local gazetteers of Ming China for clues that would show consistent growth in population."))
