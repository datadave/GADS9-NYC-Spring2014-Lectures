###What's the importance of the Naive Bayes Equation -- what do we need to know?
   * **Why Naive? It assumes all inputs (categories, predictors) are independent**: In the case of text: ts blind to word context and meaning: 
   * **Naivete helps because negligible information is required** -- simply word counting and that's it -- faster testing and very simple construction on ANY text.  Naivete doesn't hurt because correctness is based on classification, not prediction.
   * **Good Predictor, (possibly) Bad Estimator:** NB chooses among possible categories to find the one that is the greatest.  The associated probability assigned is not necessarily accurate.  For example -- it might predict an email is Spam at 80%, but the true value might be 95% -- this doesn't matter, since its just choosing the category, anything over 50% will give it a perfect score. So while good estimation means good prediction,  good prediction doesn't necessarily mean good estimation.
   * **Bayes Theorem is Easily Derivable**: The best method I've found is Venn diagrams via [Oscar Bonilla](http://oscarbonilla.com/2009/05/visualizing-bayes-theorem/) ![](http://note.io/1nf77lD).  These two steps, clear from the diagram above, can do it:
       * P(AB) = |AB| / |U| 
       * P(A|B) = |AB| / |B|
       ...
       * P(B|A) = P(AB)P(B) / P(A)
         
         
  * **Prior Knowledge is a Shortcut to Prediction** This is the philosophical element of Bayes that is important -- it uses prior knowledge.  That's the whole point of the "A given B" element of it.
    

### How does TF-IDF Work?
  * TF is simple multinomial method - how many times is the term in the doc?
  * IDF adds weights for rarity -- how rare is the term overall?
  * TF-IDF scoring system with number of terms in document and overall rarity of terms factored in.
    
    
###What's the difference between Multinomial and Bernoulli Naive Bayes?
   * Try Bernoulli when your dictionary of words and document length is small.
   * With Bernoulli, you may add in additional non-word features easily
   * Multinomial usually performs better, takes into account frequency vs. presence
   * Consider the probability for the prior of the term "the" -- Bernoulli: 100%; Multinomial 5%



