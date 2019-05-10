# coding=utf-8
import jieba.analyse  # 导入结巴jieba相关模块

output = open('words.csv', 'w')
output.write('词语,词频,词权\n')
stopkeyword = [line.strip() for line in open('stop.txt').readlines()]  # 将停止词文件保存到列表
text = open(r"new.txt", "r", encoding="utf-8").read()  # 导入需要计算的内容
zidian = {}
fenci = jieba.cut_for_search(text)
for fc in fenci:
    if fc in zidian:
        zidian[fc] += 1
    else:
        # zidian.setdefault(fc,1)   #字典中如果不存在键，就加入键，键值设置为1
        zidian[fc] = 1
# 计算tfidf
tfidf = jieba.analyse.extract_tags(text, topK=30, withWeight=True)

# 写入到csv
for word_weight in tfidf:
    print(word_weight)
    if word_weight in stopkeyword:
        pass
    else:  # 不存在的话就输出
        print
        word_weight[0], zidian.get(word_weight[0], 'not found'), str(int(word_weight[1] * 100)) + '%'
        output.write('%s,%s,%s\n' % (
        word_weight[0], zidian.get(word_weight[0], 'not found'), str(int(word_weight[1] * 100)) + '%'))