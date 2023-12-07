---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

<style>
a:link {
  text-decoration: none;
}

a:visited {
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

a:active {
  text-decoration: underline;
}
</style>

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
<!-- <h2>Research project</h2> -->

<!-- I am working on the following projects: -->

<!-- * Automatic Training Data Search and Model Evaluation by Measuring Domain Gap -->

<!-- * Human action recognition in videos -->

<!-- * Industrial research project -->
<!--   * Human-related anomaly detection in surveillance videos -->
<!--   * Research student: [Supasun Khumpraphan](https://micsupasun.github.io/) -->

I always look for motivated and hardworking students who are interested in doing research with me. However, applicants must possess good mathematical and computational skills, preferably with prior experience in machine learning and/or computer vision. Strong programming skills in Python, Matlab, and/or TensorFlow are essential, and hands-on deep learning expertise is important as well. Additionally, integrity, honesty, the ability to work under pressure, and the capacity to explore while adhering to strict directions are all essential qualities.

<h2>Industry Research Sponsorship for Students</h2>

I annually organize multiple industry research awards to support promising research candidates (Bachelor's, Honours, and Master's Students) interested in my research areas. 

Please note that only students from the Group of Eight (Go8) Australian universities are considered.

**The Active Intelligence Research Challenge Award** was established by Mr. Lei Wang and Mr. Francis Williams to honor individuals who have demonstrated exceptional dedication, expertise, and a commitment to excellence in the field of Artificial Intelligence and Machine Learning. 

The Award includes a cash prize (up to $5,000) along with a research internship (6-12 months full-time). These awards are provided by Active Intelligence Corporation LLC.

The Awards are granted solely on merit and are not subject to quotas. Typically, four candidates can receive awards from a pool of 20 candidates (with a minimum GPA of 6.75/7), resulting in an approximate acceptance rate of 20%, based on the 2023-2024 results.

This year marks the 1st Annual Active Intelligence Research Challenge.

For more information regarding the application and award process, please contact the awarded candidates before reaching out to me.

- <font color="blue"> 2023-2024 awarded ANU international students are:</font>
  -  [Mr. Arjun Raj](https://www.linkedin.com/in/ar4152/?originalSubdomain=in) <font color="blue"> (Bachelor of Advanced Computing (Research and Development) (Honours)),</font>
  -  [Mr. Liyun Zhu](https://www.linkedin.com/in/liyun-zhu-b8755328b/) <font color="blue"> (Master of Machine Learning and Computer Vision),</font>
  -  [Mr. Liwen Luo](https://luoshanji99.github.io/) <font color="blue"> (Master of Machine Learning and Computer Vision), and </font>
  -  [Mr. Qixiang Chen](https://www.linkedin.com/in/qixiang-chen-23ab2826b/) <font color="blue"> (Bachelor of Advanced Computing (Honours)). </font>

<!-- - <font color="blue"> Visiting student: </font>
  - <font color="blue"> Mr. Zerui Wang (The University of Western Australia, Bachelor of Science), 16/06/2023 - 19/07/2023.</font> -->



<h2>ANU Summer Research Scholars Program</h2>

ANU offers Summer Research Scholarships (SRS) and Summer Research Internships (SRI). External (non-ANU) students from Australia and New Zealand are eligible to apply for a Summer Research Scholarship. Current ANU students are eligible to apply for a Summer Research Internship. 

The SRS scholarship includes board and on-campus accommodation for 9 weeks (run between Monday 20 Nov 2023 to Friday 19 Jan 2024), including the Christmas shutdown period. Candidates are awarded a stipend of \\$150 per week, along with a travel allowance of up to \\$1,000 for students relocating from interstate or from New Zealand. The SRI scholarship provides a stipend of \\$400 per week to assist with the cost of living during the program. All students participating in the program will be invited to a variety of shared social events, workshops and seminars during the summer period.

For more details, please refer to [Summer Research Scholarships](https://cecc.anu.edu.au/current-students/research-opportunities/summer-research-scholarships). You can find my research projects by visiting [2023-2024 ANU CECC SRS Projects Page](https://cecc.anu.edu.au/current-students/research-opportunities/summer-research-projects-2023), get in touch if you are interested.

- <font color="blue"> 2023-2024 awarded ANU domestic student: </font>
  - [Mr. Xiuyuan (Jack) Yuan](https://jackyuanx.github.io) <font color="blue"> (Bachelor of Advanced Computing). </font> <font color="red"> Thanks to the ANU School of Computing for providing research funding.</font>


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


<h2>Bachelor & Honours Research Project</h2>

I am a [registered ANU Higher Degree Research (HDR) supervisor](https://services.anu.edu.au/research-support/hdr-supervision-development/hdr-supervision-registration-and-renewal/hdr-1).

If you are an ANU undergraduate seeking an Honors research project, please note that I typically accept a maximum of two Honors students each year to ensure high-quality supervision, and I prefer 24-unit projects.

If you are an ANU master's student seeking individual projects, I require candidates to have a solid research background, a strong GPA, and proficient coding skills. Additionally, it is important that you have adequate time available for research.


<h2>Research Grant / Funding</h2>

* The NCI National AI Flagship Merit Allocation Scheme
  * I am a **Lead CI** (2024/01/01-2024/06/30).
  * Project Title: Robust anomaly detection in human-centric videos
  * This project aims at developing advanced computer vision and deep learning techniques to identify and characterise anomalies in video data where humans are central. The project leverages cutting-edge technology to enhance security, safety, and surveillance systems, making them more effective in detecting unusual behaviours and events, which may range from security breaches and accidents to rare medical conditions in healthcare applications.
  * The significance of this project lies in its unique focus on human-centric videos. While anomaly detection in videos is an established field, the novelty emerges from its specialised applications in situations where human activity is central. The innovative aspects include (i) Robustness: The project seeks to develop highly reliable models capable of detecting anomalies in complex, real-world scenarios, where human interactions and activities can vary significantly. (ii) Real-time analysis: By applying these methods to real-time video streams, the project addresses the demand for timely responses to anomalies in security, industrial, and healthcare settings. (iii) Ethical considerations: The project incorporates ethical considerations, such as ensuring privacy and avoiding bias in the identification of anomalies, thereby making the technology responsible and trustworthy.
  * Beyond its academic contributions, this project has the potential to make significant contributions to the economy, society, environment, and culture.

* Research grant: Review of Xailient’s technical pipeline of facial recognition
  * I am a **Co-Investigator (Co-I)** (**AU$50,815**, 2023/10/30‐2023/12/22)
  * Personnel: Dr. Liang Zheng and I are the main personnel for this project. Prof. Stephen Gould, a world-level expert in optimization and computer vision will provide additional advice.
  * Scope: The ANU team will review Xailient’s technical pipeline of facial recognition. There are many components in this pipeline, such as face detection, alignment, facial recognition, and matching score determination, model/architecture selection, loss function, hyperparameters, training data cleaning, learning strategies, and speed/accuracy optimization.
  * The ANU team will conduct an in-depth review of some of them (as mutually agreed between Xailient and ANU, also depending on how much time each will take), identify gaps, and provide technical advice and guidance to improve their real-world efficacy.
  * The advice given by the ANU team will be based on technologies available in public domains that can benefit and improve Xailient products.
 
  
* NCI Adaptater Scheme Q4 2023 (HPC funding scheme)
  * I am a **Chief Investigator (CI)** / **Delegated lead CI** (2023/10/01‐2023/12/31). <!-- The Lead CI is Dr. Liang Zheng, and another CI is [Dr. Yunzhong Hou](https://hou-yz.github.io/). -->
  * Project Title: Towards building general-purpose multimodal foundation models
  * Scope: Vision-language pre-training (VLP) has attracted rapidly growing attention in both computer vision and NLP communities due to the emergence of large-scale multimodal foundation models like Contrastive Language-Image Pre-training (CLIP). It is very encouraging to see that many Vision-Language (VL) systems have been deployed in industry. For example, iPhone can generate image captions read by VoiceOver for vision-impaired users. Although multimodal intelligence has been applied in many areas including image-text, core computer vision and video-text tasks, there are still many factors to be considered including robustness to new domains, fairness and responsible AI issues.
  * Aim: One common theme stands out is how to build a general-purpose multi-modal foundation model. We aim to build a foundation model that is stable and generalisable, and can be readily adopted to various downstream tasks, ranging from image-level vision tasks (e.g., image classification, retrieval, and captioning), region-level vision tasks (e.g., object detection and phrase grounding), to pixel-level vision tasks (e.g., segmentation and image generation). In order to build a
general-purpose foundation model, we need a unified model architecture that can be readily scaled up; and when being pre-trained at scale, it can be readily adopted to various downstream computer vision and VL tasks. 

* Grant / Project Award from Oracle for Research
  * **Oracle Cloud credits award** (**AU$48,000**, 2023/07/26‐2024/07/25) <!-- for 366 days -->
  * Research project: Automatic, large-scale screening of failure cases in autonomous driving
  <!-- * Computer perception techniques have been widely used in real-world applications such as autonomous vehicles. While the state-of-the-art methods achieve impressive system accuracy, their real-world robustness is often hindered by corner cases, e.g., a pedestrian partially occluded by an umbrella on a dark day.Instead of letting such cases happen during deployment, in this project, we aim to develop a protocol which can detect potential failure cases through screening millions of different test scenarios via simulation. The identified corner cases are then used to understand system vulnerability and improve accuracy and safety in the end. -->
  * Automotive AI is rapidly replacing human drivers by enabling autonomous vehicles that use sensors to gather data about their surroundings. State-of-the-art methods achieve impressive system accuracy; however, technology is not always perfect, and this imperfection might be magnified  when it comes to safety-critical applications like autonomous driving. Potential failure cases include severe occlusions, extreme weather, low lighting conditions, strange human appearances and poses, which will compromise system performance and even lead to undesirable consequences.
  * In this research project, we aim to build a scalable simulator and diffusion models to generate millions of different test scenarios from which we detect potential failure cases of existing pedestrian and vehicle detection systems. This is to understand the vulnerability of driverless systems, and finally to improve its accuracy and safety through another round of training with these corner cases. The test scenarios cover all possible potential failure cases by varying scene and/or street layout, weather and lighting conditions, human body sizes, visual appearances of human subjects, different levels of occlusions, different levels of sensor noise, etc. More complicated test scenarios are produced by a mixture of several aforementioned individual test scenarios. These different test scenarios are able to reflect the real and sometimes unpredictable driving scenarios on the road. After being identified by running our pedestrian and/or vehicle detectors, failure cases are then summarised and analysed, and the possible reasons why the model is vulnerable to them are identified. Similar failure environments are further explored to find more closely related failure cases. Finally, we fine-tune our pedestrian and vehicle detectors to improve their robustness against difficult test scenarios.

* Research grant: Sharing early insights for more resilient communities
  * I am a **Co-Investigator (Co-I)** (**AU$71,089**, 2023/04/19‐2023/10/31)
  * Research Assistant: [Saswat Panda](https://biology.anu.edu.au/people/professional-staff/saswat-panda) (ANU)
  * This project is a joint initiative with the Southern NSW Drought Resilience Adoption and Innovation Hub and forms part of the Australian Government’s Agricultural Innovation Hubs Program.
  * The project is being conducted by the University of Canberra, Australian National University, Charles Sturt University, and University of Wollongong.
  * The project is to develop and test ‘early warning’ indicators for loss of resilience following challenging climate-related events. These indicators will be used to develop a resource that can be used to by the wide range of organisations and services to identify communities in the early stages of resilience loss and provide targeted support to agricultural communities.
  * Through understanding early warning signs that individuals and communities are at risk of resilience loss, we could inform policy and support service interventions earlier. This would provide communities with the necessary support to mitigate wider and longer lasting resilience loss related to the impacts of a climate events, which in turn, would reduce the overall harm to lives and livelihoods and facilitate resilience building across physical, psychological, social, economic, domains.

* Industry research sponsorship (Active Intelligence Corp.): Detecting anomalies in video footage (round 2)
  * I am a **Principal Investigator** / **Project Lead** (**AU$60,060**, 2022/07/01‐2023/06/30)
  * Project: Human‐related anomaly detection in surveillance videos (round 2)
  * In the second round of our project on human-related anomaly detection in surveillance videos, we aim to enhance the technology's capabilities. This involves refining normal behavior modeling for adaptability across diverse environments and incorporating feedback from the first round. We will implement state-of-the-art anomaly detection algorithms, leveraging machine learning for continuous improvement and heightened sensitivity.
  * The project also includes the development of robust event classification mechanisms, real-time alert systems, and features for in-depth post-event analysis and reporting. Special attention will be given to tailoring the technology for specific scenarios, such as shoplifting detection in retail, identification of unauthorized personnel, and improved fall detection in elderly care facilities.
  * Additionally, we will explore the integration of sensor data, including audio and environmental inputs, to augment video-based anomaly detection and provide a more comprehensive understanding of complex situations. These enhancements aim to further advance the technology's applications in retail security, secure areas monitoring, elderly care facilities, and public safety in crowded places. Rigorous testing and validation will ensure the reliability and robustness of the system, reinforcing its role in enhancing security, safety, and situational awareness in modern surveillance systems.
 
* Industry research sponsorship (Active Intelligence Corp.): Detecting anomalies in video footage
  * I am a **Principal Investigator** / **Project Lead** (**AU$123,368**, 2021/07/01‐2022/06/30)
  * Project: Human‐related anomaly detection in surveillance videos
  * Human-related anomaly detection in surveillance videos is a technology used to identify unusual or suspicious behavior involving people within a monitored environment. It is a subfield of video analytics and computer vision that aims to automatically detect deviations from normal human behavior in real-time or from recorded video footage. The primary goal of human-related anomaly detection is to enhance security, safety, and situational awareness in various applications, such as public safety, retail, transportation, and critical infrastructure protection.
  * Key components of human-related anomaly detection in surveillance videos include: normal behavior modeling, anomaly detection algorithms, event classification, real-time alerts, post-event analysis, adaptability, etc.
  * Human-related anomaly detection can be applied in various scenarios, such as identifying potential shoplifting in retail stores, spotting unauthorized personnel in secure areas, detecting accidents or falls in elderly care facilities, or monitoring crowded places for public safety. The technology relies on a combination of machine learning, computer vision, and sensor data to make these determinations, and it plays a vital role in enhancing security and safety in modern surveillance systems.

 

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
