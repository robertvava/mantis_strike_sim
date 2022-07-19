# mantis_strike_sim
## Modelling the decision-making process of a praying mantis (Tenodera Augustipennis) hunting behavior. 

Decisions are the most fundamental property of intelligent behavior. Intelligent agents
are faced with making decisions all the time. Sometimes, intelligence can arise as an
emergent property of a collective of decisional agents, like an ant colony choosing a new
nest, or an aggregation of generic decision-making units, such as neurons in a brain. The
study of collective decision making can have applications in many fields, and has been
gaining tremendous interest in the research community over the past few decades. In
particular, natural occurrence of decision making has been studied. Empirical and
computational studies have shown that different high-level properties of a decision-making
collective system can alter the overall capacity of system to make the best choices. For
instance, in ant colonies choosing a new nest, diverse acceptance thresholds were shown to
influence the rate of correct decisions, both empirically and computationally (Robinson et.
al., 2013; Masuda et. al., 2015).

Similarly, general-purpose models of collective decision-making were also studied. In
a computational simulation, Hasegawa et. al. (2017) explored a scenario of generic decisionmaking units faced with multiple options of different qualities to choose from. Their paper included multiple versions of the model, exploring how input variations would take effect in
the final decisional output. They found that that threshold variance, as well as number of
decision units allocated to each option, has a great effect on the proportion of correct choices.
Moreover, an interesting finding was that a quorum decision becomes superior when the
variability of allocated units is large, while it becomes less effective otherwise. Collective
decision-making like Hasegawa et. al. were used in various areas and it was shown that,
combined with other methods, they can contribute significantly to adaptive behavior in
artificial systems (Soorati et. al., 2019). In nature, collective decision making is present in
many higher-level systems (made of several decision units, such as ants or bees), but they can
also occur in less seemingly unintelligent agents. Biological neural networks can be
conceptualized as an instance of a higher-level system made of lower-level, unintelligent
decisional agents (i.e. neurons). Thus, the brain can be seen as a perfect example of a system
producing emergent intelligence through its enormous number of decisional units. As will be
shown in this paper, disproportionate allocation of decisional units with various thresholds
can lead to better decisions, and with the human brain’s 86 billion neurons (and 85 billion
non-neuronal cells), the property of intelligence in humans, and generally, in mammals,
might be yet another example of a collective decision-maker.

In this paper, a model for the decision-making process of strike/no-strike of the
praying mantis Tenodera Augustipennis inspired by Hasegawa et. al.’s model is
implemented. The aim of the paper is to apply this computational model into a novel scenario
and observe the overarching behavior. Another important aspect is understanding whether the
claim that their model can be used as a computational simulation of the brain’s decisionmaking process. The current model includes the idea of “clusters”, representing a parallel tobiological neural networks that are theoretically responsible for assessing different individual
factors in terms of yes/no outputs, escalated by the weights associated to the factors. 
The choice of factors to be included have been pulled from existing research on praying mantis
behavior. Particularly, 5 factors are included: size, contrast to background, speed, direction
and distance. These factors, along with 5 others, were shown to be the main stimuli that lead
to the praying mantis’ decision to strike or not to strike their prey (Bertsch et. al., 2019). In
this paper, the other 5 factors were eliminated for two reasons: (1) They would have been
harder to implement and somehow distinct from the chosen ones, and (2) Additional factors
would not have added additional value relative to the purpose of the paper. Normally, praying
mantises were observed to have two hunting strategies: Stalk and pursue (type 1), and wait
and ambush (type 2). In this paper, type 2 was modelled. Within the literature, it is also well
known that satiety level is an important factor that influences the hunting strategies and the
decision making process of Tenodera. However, this factor is also omitted from the model,
because the results of higher levels of hunger would be easily predicted and wouldn’t add any
new information.

In this simulation, the mantis is presented with a prey exhibiting the characteristics
mentioned above. To emulate a real world situation, these characteristics are changing at
random over time. The simulated praying mantis (or more accurately, the simulated brain that
makes the decisions for the praying mantis), is presented with many time step of various
qualities, having the task to decide when would be a good time to strike. In this context,
“quality” describes a high likelihood of catching the prey. The “real” time frame for making
the choice is 10 seconds, similar to empirical studies in the field of praying mantis behavior
(Yamawaki, 2017). However, in the simulation, each time step represents a potential time to
strike for the decision-maker. Naturally, there would be more time steps that could be
considered “best” choices.

Overall, the current simulation failed to produce substantial conclusions, but if the
limitations are given enough consideration, the results can be interpreted with caution. The
conclusions drawn from Hasegawa et. al. paper were mildly reproduced in this paper, and the
limitations could account for the differences. At the same time, many aspects present in the
original paper were not accounted for in the current simulation.

### Methods

The current simulation was adapted from Hasegawa et. al. (2017) general-purpose
collective decision-making model. The simulated environment was a scenario in which a
praying mantis (assumed to have sufficiently high levels of hunger) utilizing a type 2 hunting
strategy (wait and ambush) is faced with a prey of 5 different characteristics: size, contrast to
background, distance, direction and speed.
For making this decision, each factor (characteristic) of the prey is assigned a
decisional cluster contributing to the final range of decisions. The range of decisions is
represented by time-steps over a period of 10 seconds (typically, in nature, the striking would
occur between 5 and 20 seconds from sighting). In this simulation, the time period is
irrelevant, while the number of time steps represent the range of “options” with which the
mantis is faced. The overall quality of an option is computed as the average of the real
“opportunity” quality of each time step. Perceived quality was also computed based on the
real qualities.

Each cluster is made of m decision units, and assigned a certain weight. A range of
normally distributed thresholds (with mean μ, and σ standard deviation) are assigned to the
decision units assigned to each cluster. Therefore, there are 5 clusters deciding “strike/nostrike” for each time step in the simulation. A visualization can be found in Figure 1. 
Thefinal decisions are computed based on the weighted average for each time step. In this
simulation, there are multiple potential time steps (options) from which the mantis could
choose. The model assumes that any choice is perceived to lead to a successful strike. A
correct choice is considered the one that is above the value of μ(real_quality) +
σ(real_quality) over the entire distribution.
Figure 1. A typical output of the quality over time
The graph represents a distribution of objective quality over time. The violet bars represent a “strike” decision.
Results and Analysis
The descriptive statistics are summarized in Table 1. The simulation was ran 1000
times for each configuration. A summary of the different configurations can be found in
Table 2. The model did prove to choose the time moments with the highest probability of
success, significantly more than 50% of the time, depending on the initial conditions and the
configurations.
It is important to note that in almost 40% of the cases, aside from Config. 3, the final
decision was “not strike” (depicted in Figure 1) at any moment, regardless of the
configuration (unless the quality distribution is very low). Typical outputs for each
configuration are shown in Figure 2. Configuration 3 led to significantly lower proportion of
successful strikes, because they were (1) overly selected and (2) the initial conditions were
highly varied. Configurations 1 and 2 showed relatively good performance, however, there is
a significant difference between the performance from Hasegawa et. al. paper. This might be
due to the nature of the current model, which was adapted to other conditions.
The number of decision units has been kept proportional and consistent for the three
configurations. An extra configuration has been considered and analyzed, maintaining the
parameters of Config 1, but altering the number of allocated decision units. The changed
allocation of units and the results were shown in Table 3. Interestingly, compared to Config 1
with proportionally allocated units, in this configuration, the results were significantly better,
leading to a higher rate of correctly chosen options. Another observation is that the mean
“rating” of the choices was also significantly higher, standing at 2.91, 1.26 higher than the
standard Config 1.
Table 1. Configurations 1, 2 and 3
Config 1 Config 2 Config 3
Mean 1.65 2.08 1.63
Standard Deviation 0.43 0.22 0.45
% of correct choices 60% 61% 26%
Table 2. Decision Units and Weights array order match the factors order (top to bottom) in the table.
Config 1 Config 2 Config 3
Decision Units (m)
[20, 20, 20, 20, 20] [20, 20, 20, 20, 20] [20, 20, 20, 20, 20]
Weights [0.40, 0.10, 0.10, 0.20, 0.20] [0.45, 0.09, 0.35, 0.11, 0.20] [0.35, 0.15, 0.20, 0.10, 0.10]
Size 70 60 90
Contrast to Background 65 70 55
Speed 65 85 50
Direction 60 65 73
Distance 87 75 68
Means [87, 85, 89, 80, 83] [85, 80, 81, 80, 90] [75, 80, 85, 89, 79]
Standard Deviations [1, 2, 4, 2.5, 2] [4, 2.3, 1.7, 3.2, 5] [4.1, 2.7, 1.2, 3, 2]
Table 3. Configuration 1 with disproportionate allocation of units
Allocation of Units: [40, 10, 20, 15, 15]
Mean 2.91
Standard Deviation 0.37
% of correct choices 73%
Discussion
The praying mantis was a subject of interest within the research community for many
of its design properties such as the ability to extend their limbs and catch prey at a very rapid
phase, making it the perfect “assassin” (Markle, 2007). Most study of the praying mantis
behavior was based on empirical studies. Computational modelling the praying mantis natural
designs were focused on its 3D stereotactic vision (Nityananda et. al., 2018) in order to
further understand how 3D vision arises in nature. As far as the research for this paper goes,
there were no computational models of the praying mantis decision-making process for when
to strike and capture their prey. In this paper, a collective decision-making mechanism has
been adapted (Hasegawa et. al., 2017) for studying this aspect of the praying mantis behavior.
Figure 2. Typical outputs for Config 1, 2, 3
Top left = Configuration 1; Top right = Configuration 2; Bottom = Configuration 3.
In their paper, Hasegawa et. al. mention how different properties of the decision making
mechanism, such as threshold variation, can alter the success rate of the responses. They
suggest that the brain is a good example of a suitable natural collective decision-maker to
which their model could be applied to. The current model is one example of such an
application, simulating the decision-making process occurring in the praying mantis
(Tenodera augustipennis) brain when faced with the decision of strike/no-strike over a period
of time.
Several initial conditions (scenarios) were explored in order to understand the
behavior of the model and correlate it with real-world empirical data. Some observation made
by Hasegawa et. al. were confirmed in the current model. In particular, threshold variation
was strongly correlated with better decision-making. However, there were several violations
of the predicted behavior of the current model, which were most likely a by-product of the
limitations of this study. First, the model itself was highly simplified and adapted for the
praying mantis predatory behavior scenario. In the original study by Hasegawa et. al., there
were several versions of the model being explored, one of which was including a quorum in
the decision-making process. In previous studies of collective decision-makers, it was shown
that introducing quorum leads to better decisions in certain conditions. The number of
allocated decision-making units to a certain option will have a great effect on the final
decision, because the model is agnostic to proportionality. To correct this limitation, the
current model had a “weight” assigned to each factor influencing the final decisions.
Consequently, the results of the extra simulation in which the number of allocated units was
altered for Configuration 1 showed better performance than the standard Configuration. This
confirms Hasegawa et. al. observations. Qualitatively, this difference should make no
difference, but quantitatively, it leads to better decisions. In nature, this could be a parallel to
the amount of “power” or energy allocated for more computationally difficult factors to
weight into a final decision.
The current model’s results generally matched the empirical data. Naturally,
eliminating 5 out of 10 factors mentioned in Bertsch et. al. (2019) led to a fundamental
difference in the real-world and simulated scenarios. However, in both real and simulated
scenarios, distance was the most important factor, which led to a sufficient similarity in the
final responses. Overall, the results of this simulation highlights how the general-purpose
decision-making process implemented by Hasegawa et. al. can be applied in many situation,
and even when adapted to different conditions, such as utilizing the model for multiple
decision clusters which would then lead to a final range of decisions (as per the current
simulation), the properties of the model still holds. In regards to research related to praying
mantis behavior, a separate empirical experiment would be necessary to draw sensible
conclusions. Thus, all comparable results between the current simulation and previous
empirical studies should be treated cautiously.
Further analysis could have been made on this simulation. Only 3 scenarios were
analyzed, but plenty of different configuration could have led to more consistent conclusions.
A quorum decision model could have offered insights into the limitations of the current
mechanism. In the original Hasegawa et. al. paper, there were three versions of the model,
which could have been similarly explored in this paper. This could be a good opportunity for
a future improved model of the praying mantis decision-making process. Another
improvement of the current simulation would be to choose a more accurate selection process.
Currently, the selection is based on a meta-threshold chosen arbitrarily, which can greatly
affect the end results. This has not been tested in the current paper and thus the results must
be treated cautiously.
References
Bertsch, D.J., Martin, J.P., Svenson, G.J. and Ritzmann, R.E., 2019. Predatory behavior changes with
satiety or increased insulin levels in the praying mantis (Tenodera sinensis). Journal of Experimental
Biology, 222(11), p.jeb197673.
Hasegawa, E., Mizumoto, N., Kobayashi, K., Dobata, S., Yoshimura, J., Watanabe, S., Murakami, Y.
and Matsuura, K., 2017. Nature of collective decision-making by simple yes/no decision
units. Scientific reports, 7(1), pp.1-11.
Markle, S., 2007. Praying mantises: hungry insect heroes. LernerClassroom.
Masuda, N., Shea-wheller, T. A. O., Doran, C. & Franks, N. R. Computational model of collective nest
selection by ants with heterogeneous acceptance thresholds. R. Soc. Open Sci. 2, 140533 (2015).
Nityananda, V., Tarawneh, G., Henriksen, S., Umeton, D., Simmons, A. and Read, J.C., 2018. A
novel form of stereo vision in the praying mantis. Current Biology, 28(4), pp.588-593.
Robinson, E. J. H., Franks, N. R., Ellis, S., Okuda, S. & Marshall, J. A. R. A simple threshold rule is
sufcient to explain sophisticated collective decision-making. PLoS One 6, e19981 (2011).
Shea-wheller, T. A. O., Masuda, N., Sendova-franks, A. B. & Franks, N. R. Variability in individual
assessment behaviour and its implications for collective decision-making. Proc. R. Soc. B 284, 1–7
(2017).
Soorati, M.D., Heinrich, M.K., Ghofrani, J., Zahadat, P. and Hamann, H., 2019. Photomorphogenesis
for robot self-assembly: adaptivity, collective decision-making, and self-repair. Bioinspiration &
biomimetics, 14(5), p.056006.
Yamawaki, Y., 2017. Decision-making and motor control in predatory insects: a review of the praying
mantis. Ecological Entomology, 42(s1), pp.39-50.
Appendix
model.py
import numpy as np
def decision(t, randnum, size, c2b, speed
