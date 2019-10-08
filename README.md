# Council-based Strategy Naming Game 
This is an implementation of the minimal Naming Game proposed by Baronchelli. We propose an innovative process for deciding the final name of an object in a set of objects, where each object will receive a name. The process is as follows:

* A set of agents is created and they are organized in a set of communities.
* Each community implements a set of rules for generating a word for a given object.
* Each member of the community proposes a word and a final "community word" is chosen.
* An ambassador is chosen in each community to attend a "council" where a definitive word for the object is decided.
* The process for communicating the words is based on the preference rules of each ambassador. We define a threshold of  50% for deciding if an agent adopts a foreign word. For example:
	* A1 and A2 share words.
	* A1 has a preference for A2's word of 20% and A2 has a preference for A1's word of 75%. Thus, A2 will adopt A1's word as its own. 


**TODO:**
* Defining set of rules for generating words
* Define communication protocol
* Define mechanism of word analysis according to a set of rules