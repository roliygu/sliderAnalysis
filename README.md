sliderAnalysis
==============
这个project主要功能是从字幕文件中划分出单词，并判断是新单词或旧单词
input文件是新的字幕文件；
oldoutput是已认识的单词库；
每次更新的单词都会输出到output.txt；
然后在output.txt每个分析，认识的单词分到oldoutput.txt，不认识的转到output1.txt；分析完之后output.txt是空的。output2作为临时存储。