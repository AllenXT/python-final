from hashtable import Hashtable
import math

HASH_CELLS = 57
TOO_FULL = 0.5
GROWTH_RATIO = 2

class Markov:
    def __init__(self, k, text, use_hashtable):
        """
        Construct a new k-order markov model using the text 'text'.
        """
        self.k = k
        # use_hashtable is true -> Hashtable
        # use_hashtable is false -> the built in dict data structure
        self.model = Hashtable(HASH_CELLS, 0, TOO_FULL, GROWTH_RATIO) if use_hashtable else {}
        self._alphabet = set()
        self._build(text)
       
        
    def _getStrings(self, idx, str):
        # get strings with length k & k+1
        kstr = str[idx:idx + self.k]
        k1str = str[idx:idx + self.k + 1]
        
        # handle the wrap around
        if len(kstr) < self.k:
            kstr += str[0:self.k - len(kstr)]
        if len(k1str) < self.k + 1:
            k1str += str[0:self.k + 1 - len(k1str)]
        
        return kstr, k1str
      
        
    def _build(self, text):
        for i in range(len(text)):
            # get each string in the text
            kstr, kplus1str = self._getStrings(i, text)
            # print(kstr, kplus1str)
            
            # build the hashtable
            self.model[kstr] = self.model.get(kstr, 0) + 1
            self.model[kplus1str] = self.model.get(kplus1str, 0) + 1
            self._alphabet.update(kstr, kplus1str)
        
             
    def log_probability(self, s):
        """
        Get the log probability of string "s", given the statistics of
        character sequences modeled by this particular Markov model
        This probability is *not* normalized by the length of the string.
        """
        # log((M + 1)/(N + S))
        S = len(self._alphabet)
        log_prob = 0
        
        for i in range(len(s)):
            # get each string in the text
            kstr, kplus1str = self._getStrings(i, s)
            # print(kstr, kplus1str)
            
            # find the freq in the hashtable and apply Laplace smoothing
            M = self.model.get(kplus1str, 0)
            N = self.model.get(kstr, 0)
            
            # compute the log prob
            log_prob += math.log((M + 1)/(N + S))
            
        return log_prob
        
            
def identify_speaker(speech1, speech2, speech3, k, use_hashtable):
    """
    Given sample text from two speakers (1 and 2), and text from an
    unidentified speaker (3), return a tuple with the *normalized* log probabilities
    of each of the speakers uttering that text under a "order" order
    character-based Markov model, and a conclusion of which speaker
    uttered the unidentified text based on the two probabilities.
    """
    model1 = Markov(k, speech1, use_hashtable)
    model2 = Markov(k, speech2, use_hashtable)
    
    # apply the *normalized* log probabilities
    prob1 = model1.log_probability(speech3) / len(speech3)
    prob2 = model2.log_probability(speech3) / len(speech3)
    
    # output the result and analyze the likelihood
    speaker = 'A' if prob1 >= prob2 else 'B'
    return (prob1, prob2, speaker)