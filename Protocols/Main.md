# Communication Protocols
## First stage 
In this stage the agents which are going to communicate to each other are from the same community. Cross-Community communicaction will be on the Second Stage.
The communication protocol in the first stage is as follows:
- Select a community at random
    - Select the hearer agent and the speaker agent of the selected community at random.
    - Select an object at random.
    - If the speaker doesn't have any word for the object it generates one based on his rule of generating a word.
    - The speaker takes the word in his memory which it heared the most.
    - If the hearer doesn't have the word for the object in his memory it learns it.
    - If the hearer has this word in his memory:
        - It increments the frequency counter of the word.
        - He reduces the counter of the other words, if any goes down to zero it gets out of its memory.
## Second Stage
In this stage all communities have converged in a word for each object. It's time for the ambassadors to form the council and decide the definitive word for each object.
In this stage the communication protocol is as follows:
- Take the speaker ambassador at random.
- The speaker will communicate to all other ambassador, with each the communication will be as follows:
    - Select the object to speak about at random.
    - The speaker communicates it word.
    - The hearer Evaluates the word and decides which he prefers the most (the one which resemble more to its generation rule).
- After all ambassadors have communicated its words, each ambassadors remove all their words from their memories except of their favourite.
- Each ambassador communicates with each other ambassador.
    - They save the frequency of each word they hear.
    - In this communication all embassadors will end up with the same list of words and with the same frequencies.
    - Each ambassador chose for each object the most frequent word.
- Each ambassador communicate with each other non-ambassador agent in their community.
- Finally all Agents will have the same list of words, each refferring to each object.