# Language identifier

The objetive of this project it to identify the language of a text file, ou some source code.

We will use the W2C corpus for training http://ufal.mff.cuni.cz/~majlis/w2c/download.html 

The algorithm that we will be using the algorithm described in Cavnar, Bill and Trenkle, John [http://odur.let.rug.nl/vannoord/TextCat/textcat.pdf] 

 [//]: # Comment consider use the LIBSVM[https://www.csie.ntu.edu.tw/~cjlin/libsvm/].

Modules of this project:
- N-Grammar computer (removing punctuation and numbers)
- Trainer (uses the n-grammar from a base training set to compute the top n-gramms)
- Vector comparer (to several languages)
