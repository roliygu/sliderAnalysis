sliderAnalysis
==============
这个project主要功能是从字幕文件中划分出单词，并判断是新单词或旧单词
input文件是新的字幕文件；
oldoutput是已认识的单词库；
output是input - oldouput的的生词库（当然不是绝对的，依然有一部分是不存在认识库的认识单词）；
新加了output1和output2作为临时存储库，output1=input-oldput，也就是更（四声）新字幕与已有认识库做比较的新单词（与output库不同）；output2=output1-output，也就是在output基础上的新词（这里面的单词包括了一部分新词和一部分不属于认识库的单词）。
现在已经把3.txt更新完毕。