import string
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word={}
        # translator=string.maketrans("","",string.punctuation)
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        # paragraph=paragraph.translate(translator)
        banned=[i.lower() for i in banned]
        for i in range(len(paragraph)):
            q=paragraph[i].lower()
            a=[]
            for char in q:
                if char not in punctuations:
                    a.append(char)
            q="".join(a)
            print(q)
            if  q not in banned:
                if q not in word:
                    word[q]=1
                else:
                    word[q]+=1
        word = sorted(word.items(), key=operator.itemgetter(0))
        print(word)
        return (next(iter(word)) )
                
s=Solution()
paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
banned=["hit"]
s.mostCommonWord(paragraph,banned)