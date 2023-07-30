---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

<!-- Skills
====== -->

<!-- * Programming languages
  * Python
  * Matlab
  * C/C++
  * LATEX
  * Unix shell scripts

* Machine learning libraries
  * Pytorch
  * Scikit-learn
  * TensorFlow
  * MatConvNet -->



<!-- * Action recognition
* Anomaly detection
* Video image processing
* One- & few-shot learning
* Deep learning
* Tensor learning
* Domain adaptation -->
<!-- <p>&nbsp;</p> -->
<h2>Research project</h2>

<!-- I am working on the following projects: -->

* Automatic Training Data Search and Model Evaluation by Measuring Domain Gap

* Human action recognition in videos

* Industrial research project
  * Human-related anomaly detection in surveillance videos
<!--   * Research student: [Supasun Khumpraphan](https://micsupasun.github.io/) -->

<h2>Research grant / award / funding</h2>

* Sharing early insights for more resilient communities
  * I am a Co-Investigator (Co-I).
  * Research Assistant: [Saswat Panda](https://biology.anu.edu.au/people/professional-staff/saswat-panda) (ANU)
  * This project is a joint initiative with the Southern NSW Drought Resilience Adoption and Innovation Hub and forms part of the Australian Government’s Agricultural Innovation Hubs Program. 
  * The project is being conducted by the University of Canberra, Australian National University, Charles Sturt University, and University of Wollongong.
  * The project is to develop and test ‘early warning’ indicators for loss of resilience following challenging climate-related events. These indicators will be used to develop a resource that can be used to by the wide range of organisations and services to identify communities in the early stages of resilience loss and provide targeted support to agricultural communities.
  * Through understanding early warning signs that individuals and communities are at risk of resilience loss, we could inform policy and support service interventions earlier. This would provide communities with the necessary support to mitigate wider and longer lasting resilience loss related to the impacts of a climate events, which in turn, would reduce the overall harm to lives and livelihoods and facilitate resilience building across physical, psychological, social, economic, domains.
 
* Grant / Project Award from Oracle for Research
  * Oracle Cloud credits award (AU$48,000 for 366 days)
  * Research project: Automatic, large-scale screening of failure cases in autonomous driving
  <!-- * Computer perception techniques have been widely used in real-world applications such as autonomous vehicles. While the state-of-the-art methods achieve impressive system accuracy, their real-world robustness is often hindered by corner cases, e.g., a pedestrian partially occluded by an umbrella on a dark day.Instead of letting such cases happen during deployment, in this project, we aim to develop a protocol which can detect potential failure cases through screening millions of different test scenarios via simulation. The identified corner cases are then used to understand system vulnerability and improve accuracy and safety in the end. -->
  * Automotive AI is rapidly replacing human drivers by enabling autonomous vehicles that use sensors to gather data about their surroundings. State-of-the-art methods achieve impressive system accuracy; however, technology is not always perfect, and this imperfection might be magnified  when it comes to safety-critical applications like autonomous driving. Potential failure cases include severe occlusions, extreme weather, low lighting conditions, strange human appearances and poses, which will compromise system performance and even lead to undesirable consequences.
  * In this research project, we aim to build a scalable simulator and diffusion models to generate millions of different test scenarios from which we detect potential failure cases of existing pedestrian and vehicle detection systems. This is to understand the vulnerability of driverless systems, and finally to improve its accuracy and safety through another round of training with these corner cases. The test scenarios cover all possible potential failure cases by varying scene and/or street layout, weather and lighting conditions, human body sizes, visual appearances of human subjects, different levels of occlusions, different levels of sensor noise, etc. More complicated test scenarios are produced by a mixture of several aforementioned individual test scenarios. These different test scenarios are able to reflect the real and sometimes unpredictable driving scenarios on the road. After being identified by running our pedestrian and/or vehicle detectors, failure cases are then summarised and analysed, and the possible reasons why the model is vulnerable to them are identified. Similar failure environments are further explored to find more closely related failure cases. Finally, we fine-tune our pedestrian and vehicle detectors to improve their robustness against difficult test scenarios. 


<h2>ANU Summer Research Scholars Program</h2>

ANU offers Summer Research Scholarships (SRS) and Summer Research Internships (SRI). External (non-ANU) students from Australia and New Zealand are eligible to apply for a Summer Research Scholarship. Current ANU students are eligible to apply for a Summer Research Internship. 

The SRS scholarship includes board and on-campus accommodation for 9 weeks (run between Monday 20 Nov 2023 to Friday 19 Jan 2024), including the Christmas shutdown period. Candidates are awarded a stipend of \\$150 per week, along with a travel allowance of up to \\$1,000 for students relocating from interstate or from New Zealand. The SRI scholarship provides a stipend of \\$400 per week to assist with the cost of living during the program. All students participating in the program will be invited to a variety of shared social events, workshops and seminars during the summer period.

For more details, please refer to [Summer Research Scholarships](https://cecc.anu.edu.au/current-students/research-opportunities/summer-research-scholarships). You can find my research projects by visiting [2023-2024 ANU CECC SRS Projects Page](https://cecc.anu.edu.au/current-students/research-opportunities/summer-research-projects-2023), get in touch if you are interested.

<!-- * Project 1: Video dynamics distillation -->

<!--  Video captures motions such as natural dynamics and human actions. Various research works have been dedicated in learning and extracting spatio-temporal features from videos for human action recognition, anomaly detection, and scene understanding tasks. 
Nowadays, video data have been pre-processed to a variety of data formats using either machine learning tools / computer vision algorithms or physical sensors (e.g., Microsoft Kinect camera with OpenNI framework), for example, optical flows that highlight the video dynamics, depth videos that segment the
foreground objects and human subjects, and skeleton sequences that focus on human poses evolving in time, for better video understanding. 
However, videos contain very redundant information, which hinders the effectiveness and efficiency in extracting the motions of interest, and forces the computer vision community works hard in various large-scale pre-training for downstream video processing tasks. 
Until now, video processing still highly relies on 3D CNNs, and it still suffers from the darkness of large and complicated models. In this research project, we aim to develop more lightweight video data formats which are able to efficiently distill the motions at different granular levels by removing redundant information while focusing on the core dynamics. 
We also explore the acceleration of training and testing while reducing the amount of video data for storage, and answer a scientific question `How much information is contained in the video data and in what format?'.
Many downstream video processing tasks will benefit from our video dynamic distillation process, towards making video understanding much easier and more efficient. This also opens up a new research direction in exploring better video data representations for more lightweight cutting-edge video models. -->

<!-- * Project 2: Training video data optimisation -->

<!--  We live in a world where most of our actions are constantly captured by cameras. Video cameras are spread almost everywhere: in smartphones, computers, drones, surveillance systems, cars, robots, intercoms, etc.
The quality of video data highly affects the performance of video models in its massive useful applications.
Video data optimisation aims to improve the quality of video data being feed into the model for training hence improving the model performance, e.g., recognition accuracy and generalisation abilities. 
However, videos are more challenging due to the extra introduced temporal signals, which makes video understanding hard. 
Compared to image domain, videos suffer from much more serious data quality issues. 
Moving cameras, challenging natural dynamics e.g., rainy, snowy, reflection, etc., background dynamics e.g., tree waving, camera noise and camera shaking issues degrade the video model performance when trained on these unstable and noisy videos. 
Further challenging issues including the label errors and noisy ground truths, and the labeling process for video contents is even more labor-intensive and tedious.
Many video data optimisation methods have been proposed in the literature for training robust video models, for example, video data augmentation is widely used in video model training. Generic video augmentation uses some basic video transformations such as geometric, color space, temporal, erasing and mixing, e.g., video data augmentation via temporal cropping. However, these augmentation methods are still unable to address the video data quality issues as they simply create a large number of diverse video contents with different focuses which still highly rely on the quality of original video data.
In this research project, we aim to explore video data optimisation techniques that are able to improve the model performance for downstream video processing tasks such as human action recognition and anomaly detection. We also explore (i) the influence of training videos on the prediction of a test video (ii) how each individual training video affect the generalisation ability of a model and (iii) do we need all the video data in the training set or shall we drop unfavorable video samples and how. -->

<!-- <h2>Personal statement</h2> -->

<!-- I am a hardworking, passionate and self-disciplined researcher. -->
  
<!-- I have worked with the <font color="blue">large-scale volumetric</font> action recognition datasets which are bigger by several orders of magnitude compared to ImageNet.  -->

<!-- I have learnt to deal efficiently with complex projects given <font color="blue">limited computational resources</font> (albeit HPC-based). -->

<!-- I have a solid background to work on <font color="blue">cross-dataset problems</font>, I understand very well (i) concepts of distribution shift between datasets (ii) issues with generalization to new class concepts (iii) issues underpinning model failures due to out-of-distribution situations (iv) issues resulting from low sample counts, and so forth.  -->

<!-- My knowledge gained from past research experience span several <font color="blue">computer vision and machine learning disciplines</font> including camera projective geometry, graph neural networks, and optimal transportation (apart from action recognition and few-shot learning). -->

<!-- I have delivered a number of strong scientific ideas as witnessed by my (i) academic outputs (papers in high quality venues) and (ii) practical knowledge of action recognition / anomaly detection systems (patents). -->

<!-- <p>&nbsp;</p> -->
<!-- <h2>Research interests</h2> -->

<!-- My interests include action recognition in videos, anomaly detection, video image processing, one- and few-shot learning, deep learning, tensor learning and domain adaptation. -->
