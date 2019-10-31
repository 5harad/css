# MS&E 231 Discussion Section: Text Processing and NLP

This discussion section will provide a brief introduction to a few different aspects of text processing and NLTK. There is an incredible wealth of information and software out there to make your life easier and accomplish a wide variety of language-related tasks, but today we'll be looking at just a small subset, via three notebooks:

* Text processing and topic modeling (`TopicModeling.ipynb`)
  * using [NLTK](https://nltk.org) + [gensim](https://radimrehurek.com/gensim/index.html) 
* Document vector representation and toxic comment classification (`ToxicCommentLearning.ipynb`)
  * using [scikit-learn](https://scikit-learn.org/)
* Word embedding visualization (`WordEmbeddingViz.ipynb`)
  * using [GloVe](https://nlp.stanford.edu/projects/glove/) word vectors and gensim (again)

## Prereqs

Install `nltk`, `gensim`, and `scikit-learn` (e.g. using `pip3 install`).

Once installed, `nltk` requires a further step to download corpora; i would recommend simply grabbing everything with `nltk.download('all')`.

Let's get started!

## Further NLP resources

We just scratched the surface in lab, and looked at these packages:

* [gensim](https://radimrehurek.com/gensim/index.html)  (widely used in NLP)
* [NLTK](https://nltk.org) (so, so many features)
* [scikit-learn](https://scikit-learn.org/) (not text-specific)

There are many other great pieces of software, among them:

* [spaCy](https://spacy.io/) (does too many things to name)
* [MALLET](http://mallet.cs.umass.edu/) (document classificiation, topic modeling, sequence tagging)

If you're working with sentiment analysis of online speech, you might consider the [Perspective API](https://perspectiveapi.com/).

One Stanford course with many more resources to check out is [CS 224N](http://web.stanford.edu/class/cs224n/).

Some of the state-of-the-art language understanding methods (as of this writing), if you're interested in keeping up with these sorts of things, are [BERT](https://arxiv.org/abs/1810.04805) and [XLNet](https://arxiv.org/abs/1906.08237).
