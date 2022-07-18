# mantis_strike_sim
Modelling the decision-making process of a praying mantis (Tenodera Augustipennis) hunting behavior. 


The current paper summarizes an experiment focused on an adaptive agent to a dynamic environment. A robot’s objective is to end up “hugging” a light source with the highest brightness, out of multiple lights (typically 5 others than the highest brightness one). A significant disturbance is inserted at a certain disturbance time within a simulation run. The robot can be said that it adapted successfully if it can still find and hug the brightest light during until the end of the simulation. The adaptive strategy entails a random searching state which is turned on or off depending on whether the robot detected the highest brightness in the environment, which in turn makes the robot go towards the source of the light. This strategy has proven to be unsuccessful. A possible explanation is the fact that several important factors are disregarded, such as the actual relationship between the robot’s sensory inputs and the light. 

Introduction 
		
	The word adaptive encompasses a range of requirements for it to be attached to a system. An adaptive system must be described in relation to at least two components: a successful behavior of the system and a dynamic environment which, at some point, or over a period of time, would significantly change its properties so that the initial successful behavior of the system would be disrupted (Holland, 1992). A system adapts when the successful behavior is still achieved after the significant disruption in the environment. 
Software-based robotics is a field that offers tremendous opportunities for exploring adaptive systems due to the flexibility of the experimental setup. Both the environment and the adaptive agents (or robots) can be changed easily with the purpose of testing different experimental conditions. In this paper, a simulation of a light-seeking robot was produced for exploring adaptation strategies of the robot in a changing environment. A controller has been implemented for integrating the adaptive strategy. The focus of the simulation was to test the performance of the adaptive strategy implemented in the controller, when faced with a significant disruption in the environment. Ultimately, the adaptation strategy failed to produce a successful behavior, which was the result of an under-engineered controller. 
Modern methods for adaptation include Artificial Neural Networks (ANNs), hill climber algorithms, feedback control loops, and many others were shown to lead to successful adaptation in different situations (De Nicola, Jahnichen & Wirsing, 2020). In some cases, simple adaptation strategies are sufficient for solving specific tasks. In the current experiment, a non-standard adaptive strategy was used for the experiment. 

Methods
	SituSim (University of Sussex) was used for setting up the simulation. The experiment consists of the following: a controller, a disturbance, and the light sources. The aim of the robot is to explore the space and find the light source with the highest brightness. The robot has successfully adapted if, after the disturbance happened, it is still able to find and “hug” the brightest light source. The code is provided in the attached files. 

Light Sources
	There is one main source (represented as green), which will have a higher brightness than the secondary light sources (represented as yellow) at all times. The secondary light sources spawn at random, while the main source will always be at point (0, 0) (middle). 

 

Disturbance Class 
	A custom-made disturbance was created (BrightnessDisturbance). At a given disturbance time, the brightness of all lights will suffer a gradual or drastic change. The main light will have a sudden drop in brightness at disturbance time, while the secondary lights will have a decreasing brightness over time, starting at disturbance time. 

Adaptive Controller
	The controller contains the instructions given to the motors of the robot, effectively determining the behavior. Thus, the controller is the most important element, which produces the useful data to be examined. In this experiment, the controller has interchangeable states that are determined by the inputs that the robot receives. The controller schematics can be found in Figure 2. 		

 
 
![](images/Adaptive%20Controller.png)



Arena
	The arena was implemented for keeping a limited search space. 





Results and Analyses 
	The successful behavior was quantified by the final position of the robot (“hugging” the main light at the end of the simulation). Data from 100 runs was obtained. 
	Out of 100 runs, the robot achieved the target only 7 times. This suggests that the adaptive strategy failed to be consistent. Moreover, the successful runs are more likely a result of random chance rather than an intended adaptation. 
	A sample trajectory can be observed in Figure 3. In this figure, the random search stance is exemplified throughout the whole simulation. In this particular run, the robot ends up “hugging” the main light only for a brief time close to the end of the simulation. Thus, it can be classified as a potential false positive.


![](images/Sample%20Trajectory.png)


Discussion 
	Adaptive strategies face the challenge of complexity. Some strategies are prone to overengineering, significantly increasing the resources needed for implementation, and sometimes even leading to non-optimal results (Mobius, 2022). On the other side, simple strategies can sometimes prove to be too simple, failing to achieve desired outcomes. In the current paper, the strategy utilized for adaptation led to unsuccessful adaptation, which stemmed from the under-engineering of the adaptive controller. 
	A possible explanation for why the strategy fails is the agnosticism to the relationship between the sensory inputs of the robot and the lights. In essence, the inputs are determined not only by the distance from the light to the sensors, but also the angle of the sensors to the lights. This factor greatly influences the final sensory input, and needs to be taken into account for designing adaptive strategies (although depending on the tasks). In the controller, there has been no regard for the angle between the sensor and the light sources. Moreover, perceiving more lights will lead to higher inputs, affecting the overall perceived brightness. The unsuccessful behavior is most probably resulting from disregarding important factors like the abovementioned ones. Also, it could mean that the nature of the strategy itself might have been inappropriate for this problem. A more popular solution for search problems, like the hill climber, might have proved to be a better strategy. This idea could be explored in future experiments. 
	Simple solutions are in fact a good standard for engineering problems, and can prove to be the most efficient, as compared to more complex solutions. A fundamental question is how to come up with the best solution before experimentation. This is particularly important for the field of Artificial Intelligence (A.I.). There are numerous examples where the objective function of an A.I. system was achieved, but the solution was too radical or simply inappropriate. For instance, a French chatbot that was supposed to help people with their mental health was recorded to suggest “suicide” as an option (Vaidyam et. al., 2019). 
	This highlights the importance of defining a good objective function that could not be “misinterpreted” by the system. In the current paper, the objective function was not optimal for the actual objective of the system. A better objective function could have been to measure not only the final position of the robot, but also the time spent “hugging” the light source, assigning a certain threshold value for the said time. 
	In science and engineering, failure is an opportunity to make better designs and acquire a better understanding of nature or man-made systems. The shortcomings of this experiment can be treated as good warning points for future similar experiments, contributing to the long-term development of the theory and practice of adaptive systems. 









References 

Mobus G.E. (2022) Principles of Systems Science. In: Systems Science: Theory, Analysis, Modeling, and Design. Springer, Cham. https://doi.org/10.1007/978-3-030-93482-8_2
Holland, J.H., 1992. Complex adaptive systems. Daedalus, 121(1), pp.17-30.
Vaidyam, A.N., Wisniewski, H., Halamka, J.D., Kashavan, M.S. and Torous, J.B., 2019. Chatbots and conversational agents in mental health: a review of the psychiatric landscape. The Canadian Journal of Psychiatry, 64(7), pp.456-464.
