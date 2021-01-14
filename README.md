# COVID-19-Markov-Chain-Digression

***Introduction***

Mandating the use of masks is almost regarded as a universal protocol responding to the COVID-19 pandemic due to its ability to prevent the expulsion of bodily fluids that potentially contain viruses. However, although it is conventionally known that masks contribute to the prevention of COVID-19 transmission based on theory, the actual variance of COVID-19 transmission rates depending on the percentage of the population wearing masks is unknown to many. To enlighten the public on the huge difference between wearing a mask and choosing not to, I have created a program that simulates the transmission of the virus among a given population of 50 using the SEIR model and the Markov Chain Model, with results varying depending on the percentage of population wearing masks, the types of people interacted with, and the level of civic awareness.

***How to Use***

Download any programming application that supports python using your browser. Once that has been completed, reference the links below that will redirect you to my GitHub pages containing the projects. Download and open them in the application. To see changes in the transmission rates, modify the variables listed at the top of the file entitled human.py. Here are the list of the variables and what they represent:

* FRIENDS_MEET: The chance that two friends will meet
* JUST_MEET: The chance that any two random strangers will meet
* SYMPTOM_MASK: The chance that a person with visible symptoms wears a mask
* NO_SYMPTOM_MASK: The chance that a person with no visible symptoms wears a mask
* CIVIC_AWARENESS: The overall ‘level’ of protective awareness among the community 
* MASK_INF_OUT: The chance that an infected person wearing a mask will transmit the virus 
* NO_MASK_INF_OUT: The chance that an infected person without a mask will transmit the virus 
* MASK_SUS_IN: The chance that a susceptible person wearing a mask will receive the virus 
* NO_MASK_SUS_IN: The chance that a susceptible person without a mask will receive the virus 

Noticeable changes in the simulated transmission rates will change as these variables are altered, especially those directly related to mask-wearing statuses.
