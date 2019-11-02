# Council-based Strategy Naming Game 
This is an implementation of the minimal Naming Game proposed by Baronchelli. We propose an innovative process for deciding the final name of an object in a set of objects, where each object will receive a name. The process is as follows:

* A set of agents is created and they are organized in a set of communities.
* Each community implements a set of rules for generating a word for a given object.
* Each member of the community proposes a word and a final "community word" is chosen.
* An ambassador is chosen in each community to attend a "council" where a definitive word for the object is decided.
* The process for communicating the words is based on the preference rules of each ambassador. We define a threshold of  50% for deciding if an agent adopts a foreign word. For example:
	* A1 and A2 share words.
	* A1 has a preference for A2's word of 20% and A2 has a preference for A1's word of 75%. Thus, A2 will adopt A1's word as its own. 

**Restrictions**
* Se pide analizar la influencia de los parámetros N, C, O, y los protocolos de comunicación
en cada una de estas variables, especialmente en el tiempo de convergencia Tconv.
* N = 10, 20, 50, 71, 80, 100, 200
* O = 2, 4, 7, 8, 16
* C = 2, 4, 7, 8, 16
* (optional) Forgetness Factor = 2, 4, 7, 8, 16 
* (optional) Variations in protocols = Add some probality distribution in random selections
* (optional) Try with the parameters found by http://iridia.ulb.ac.be/irace/

**TODO:**
* Defining set of rules for generating words (Explain it)
* Define communication protocol (Explain it)
* Define mechanism of word analysis according to a set of rules (Explain GetPreference)
* Get Stats:
	- Tconv: tiempo que tarda el sistema en ponerse de acuerdo. (Tiempo en numero de pasos de tiempo, es decir comunicaciones peer to peer)
	- Tmax: momento de la computación en que hay un mayor número de palabras totales
en el sistema.
	- Wmax: número máximo de palabras totales.
	- Wdif: número máximo de palabras diferentes.
* Get Graphs from stats
* Write technical report
* Write presentation