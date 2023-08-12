import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
# text ="""The short story is a crafted form in its own right. Short stories make use of plot, resonance, and other dynamic components as in a novel, but typically to a lesser degree. While the short story is largely distinct from the novel or novella/short novel, authors generally draw from a common pool of literary techniques.[citation needed] The short story is sometimes referred to as a genre.[2]

# Determining what exactly defines a short story has been recurrently problematic.[3] A classic definition of a short story is that one should be able to read it in one sitting, a point most notably made in Edgar Allan Poe's essay "The Philosophy of Composition" (1846).[4] H.G. Wells described the purpose of the short story as "The jolly art, of making something very bright and moving; it may be horrible or pathetic or funny or profoundly illuminating, having only this essential, that it should take from fifteen to fifty minutes to read aloud."[5] According to William Faulkner, a short story is character-driven and a writer's job is to "...trot along behind him with a paper and pencil trying to keep up long enough to put down what he says and does."[6]

# Some authors have argued that a short story must have a strict form. Somerset Maugham thought that the short story "must have a definite design, which includes a point of departure, a climax and a point of test; in other words, it must have a plot".[5] Hugh Walpole had a similar view: "A story should be a story; a record of things happening full of incidents, swift movements, unexpected development, leading through suspense to a climax and a satisfying denouement."[5]

# This view of the short story as a finished product of art is however opposed by Anton Chekov, who thought that a story should have neither a beginning nor an end. It should just be a "slice of life", presented suggestively. In his stories, Chekov does not round off the end but leaves it to the readers to draw their own conclusions.[5]

# Sukumar Azhikode defined a short story as "a brief prose narrative with an intense episodic or anecdotal effect".[3] Flannery O'Connor emphasized the need to consider what is exactly meant by the descriptor short.[7] Short story writers may define their works as part of the artistic and personal expression of the form. They may also attempt to resist categorization by genre and fixed formation.[5]"""


def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    # print(stopwords)
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(rawdocs)
    # print(doc)
    token = [token.text for token in doc]
    # print(token)
    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] =1
            else:
                word_freq[word.text]+=1
    # print(word_freq)
    max_freq = max(word_freq.values())
    # print(max_freq)
    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq
    # print(word_freq)
    sent_token=[sent for sent in doc.sents]
    #print(sent_token)
    sent_scores={}
    for sent in sent_token:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]
    # print(sent_scores)
    select_len =int(len(sent_token) *0.4)
    print(select_len)
    summary = nlargest(select_len,sent_scores,key=sent_scores.get)
    # print(summary)
    final_summary = [word.text for word in summary]
    summary = " ".join(final_summary)
    # print(text)
    # print("\n*****************\n")
    # print(summary)
    # print("length if original text ",len(text.split(' ')))
    # print("length of  summary text ",len(summary.split(' ')))

    return summary,doc,len(rawdocs.split(' ')),len(summary.split(' '))

