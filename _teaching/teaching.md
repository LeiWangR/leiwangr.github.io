---
layout: archive
title: "Teaching"
permalink: /teaching/
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

<h2>Teaching@Griffith</h2>

* 2026 Trimester 2, Brisbane City (South Bank) - In Person: **Course Convenor**
  * School of Information and Communication Technology, Griffith University
  * [1811ICT Programming Principles](https://www.griffith.edu.au/study/courses/programming-principles-1811ICT?location=dom#trimester-2-brisbane-city-south-bank)
  * View [course profiles](https://leiwangr.github.io/files/1811ICT.pdf)
  * About this course:
    * Programming is a foundational skill for all computing disciplines. This course develops skills and concepts that are essential to good programming practice and problem solving. It covers fundamental programming concepts, object-oriented programming, basic data structures, and algorithmic processes.
    * Incompatible: must not have completed 2807ICT Programming Principles


Welcome to the course! This semester, you will learn Python by building your own *Mission Control Panel*, a program that monitors mission data, checks system conditions, analyses information, and helps operators make decisions.
You will not build it all at once. Starting with a simple control panel in Week 1, you will add new capabilities week by week as you learn new Python concepts. Each new topic gives you another tool to make your system smarter, more capable, and more complete: (i) *Lectures:* Discover the Python concepts and problem-solving techniques behind each capability. (ii) *Workshops:* Put those concepts into action by upgrading your *Mission Control Panel* from one version to the next.


| Week | Lecture materials | Workshop materials |
|:---:|:---|:---|
| 1 | [Introduction](https://leiwangr.github.io/files/1811ICT/w01lec-introduction.pdf) | [v1.0](https://leiwangr.github.io/files/1811ICT/workshop01-v1.pdf): Building the Basic Mission Control Panel [[Code]](https://leiwangr.github.io/files/1811ICT/mission_control.py)|
| 2 | [Variables, Assignment Statements, Input and Output](https://leiwangr.github.io/files/1811ICT/w02lec-strings-variables-input-and-output.pdf) | [v2.0](https://leiwangr.github.io/files/1811ICT/workshop02-v2.pdf): Variables, User Input and Program Output [[Code]](https://leiwangr.github.io/files/1811ICT/mission_control_v2.py) |
| 3 | [Booleans and Conditional Statements](https://leiwangr.github.io/files/1811ICT/w03lec-booleans-and-decisions.pdf) | [v3.0](https://leiwangr.github.io/files/1811ICT/workshop03-v3.pdf): Making Decisions with Conditions and Boolean Logic [[Code]](https://leiwangr.github.io/files/1811ICT/mission_control_v3.py) |
| 4 | [Loops (Iterations)](https://leiwangr.github.io/files/1811ICT/w04lec-loops-and-repetition.pdf) | [v4.0](https://leiwangr.github.io/files/1811ICT/workshop04-v4.pdf): Repeating Tasks with Loops [[Code]](https://leiwangr.github.io/files/1811ICT/mission_control_v4.py) |
|  | *Student Vacation Week — No Teaching* | *Student Vacation Week — No Teaching* |
| 5 | [Functions](https://leiwangr.github.io/files/1811ICT/w05lec-functions.pdf) | [v5.0](https://leiwangr.github.io/files/1811ICT/workshop05-v5.pdf): Organising Programs with Functions [[Code]](https://leiwangr.github.io/files/1811ICT/mission_control_v5.py) |
| **Quiz 1** | Quiz 1 [solutions](https://leiwangr.github.io/files/1811ICT/quiz1-solutions.pdf) | Q1-Q6: Solutions and explanations |
| 6 | [Lists & Tuples](https://leiwangr.github.io/files/1811ICT/w06lec-lists-and-tuples.pdf) | [v6.0](https://leiwangr.github.io/files/1811ICT/workshop06-v6.pdf): Storing and Processing Data with Lists and Tuples [[Code]](https://leiwangr.github.io/files/1811ICT/mission_control_v6.py) |
| 7 | [More About Strings](https://leiwangr.github.io/files/1811ICT/w07lec-strings.pdf) | [v7.0](https://leiwangr.github.io/files/1811ICT/workshop07-v7.pdf): Working with Strings and Text Data [[Code]](https://leiwangr.github.io/files/1811ICT/mission_control_v7.py) |
| 8 | Files and Error Handling | Workshop 8 |
| 9 | Sets and Dictionaries | Workshop 9 |
| 10 | Object-Oriented Programming | Workshop 10 |
| 11 | Modules & Libraries | Workshop 11 |
| 12 | Revision & Exam Information | No Workshop |

* 2026 Trimester 2, Online: **Course Convenor**
  * School of Information and Communication Technology, Griffith University
  * [3006ICT Robotics and Computer Vision](https://www.griffith.edu.au/study/courses/robotics-and-computer-vision-3006ICT?location=dom#trimester-2-online)
  * View [course profiles](https://leiwangr.github.io/files/3006ICT.pdf)
  * About this course:
    * This course introduces the principles and methods that enable robots to perceive and understand the physical world using cameras and vision-based sensing. It covers coordinate frames, image formation, camera calibration, geometric vision, feature extraction, motion estimation, depth perception, object perception, visual localisation, mapping, and vision-guided robotic operation. Students learn how computer vision supports embodied intelligence in mobile robots, robot manipulators, and other autonomous systems, and how perception modules are integrated into complete robotic pipelines. The course emphasises robotics-specific computer vision rather than general machine learning or generic image classification. Students will develop the conceptual and practical foundations needed to design perception pipelines for tasks such as localisation, mapping, tracking, grasping, navigation, and autonomous operation in real-world environments. Students must be enrolled in either 1534 Bachelor of Computer Science or 1585 B Engineering (Hon)/BComp Science.
    * Pre-requisites: must have completed 2801ICT Computing Algorithms AND must have completed 2802ICT Intelligent Systems


*How does a robot see, understand, and act in the world?* In these hands-on workshops, you will build the answer step by step. You will learn how cameras turn the 3D world into images, how robots recover geometric and depth information, how visual features reveal motion, and how modern vision models detect and understand objects. You will then bring these techniques together for tasks such as visual tracking, motion estimation, SLAM, navigation, and robotic manipulation. Along the way, you will develop practical skills in Python, OpenCV, computer-vision algorithms, deep learning, visualisation, experimentation, debugging, and engineering evaluation, learning not only how a method works, but also when it works, when it fails, and how to use it responsibly in a robotic system.

| Week | Practical focus | Workshop materials |
|:---:|:---|:---|
| 1 | **Introduction to Vision-Enabled Robotics**<br>Build a simple vision-to-action pipeline: load and inspect images, extract a visual target, estimate its image location, and use that information to make a basic robot-relevant decision. | Chapter 1: Getting Started with Vision-Enabled Robotics |
| 2 | **Camera Models, Coordinate Systems and Robot Geometry**<br>Explore how 3D points are projected into image pixels, how camera intrinsics affect projection, and how depth enables reasoning back from pixels to 3D points. | Chapter 2: Camera Geometry — From 3D Points to Image Pixels and Back |
| 3 | **Classical Computer Vision for Robotic Perception**<br>Extract distinctive visual features, track features between frames, estimate image motion, and investigate how classical vision methods behave under different conditions. | Chapter 3: Feature Detection, Optical Flow and Visual Tracking |
| 4 | **Deep Learning for Robotic Vision**<br>Adapt a pretrained visual model to a new task, compare frozen and fine-tuned models, evaluate performance, and investigate robustness under visual changes. | Chapter 4: Transfer Learning, Fine-Tuning and Robustness |
|  | *Student Vacation Week — No Teaching* | *Student Vacation Week — No Teaching* |
| 5 | **Object Detection and Semantic Segmentation for Robotics**<br>Use pretrained vision models to detect objects, interpret bounding boxes and confidence scores, evaluate predictions, and connect visual perception to simple robot decisions. | Chapter 5: Object Detection and Robotic Decision Making |
| | *Individual Project Available*<br>Detection-Assisted Visual Tracking: Apply concepts from the earlier workshops to develop a complete detection-assisted visual-tracking system. | Submission: 23:59, Sunday Week 7 (No presentation requirement) |
| 6 | **Depth Estimation, RGB-D Vision and 3D Scene Understanding**<br>Explore how depth information can extend image-based perception into 3D, and investigate how visual information can support spatial understanding and robotic tasks. | Chapter 6 & Individual Project |
| 7 | **Visual Motion Estimation and SLAM Concepts**<br>Build a visual-motion pipeline using feature correspondences, geometric verification, relative camera motion, visual odometry, keyframes, and loop-closure concepts. | Chapter 7: Visual Odometry and Visual SLAM |
| | *Group Project Available*<br>Integrate robotics and computer-vision techniques into a larger team-based project. | Submission: 23:59, Sunday Week 11 (Team presentation: Week 12) |
| 8 | **Vision-Based Robot Navigation**<br>Apply visual perception to navigation problems and consider how information extracted from images can support robot movement and decision-making. | Workshop 8 |
| 9 | **Vision for Planar Object Grasping**<br>Explore how visual information about planar objects can support localisation and manipulation, connecting perception with robotic grasping tasks. | Workshop 9 |
| 10 | **Learning-Based Robot Control**<br>Investigate how learned visual representations can be connected to robot control and decision-making, with attention to practical performance and reliability. | Workshop 10 |
| 11 | **Foundation Models for Robotics: Vision-Language-Action and Embodied AI**<br>Explore emerging approaches that combine visual perception, language understanding, learning, and action for more capable robotic systems. | No Workshop |
| 12 | *Group Project Presentation*<br>Present and reflect on the completed group project, including the problem, approach, results, and practical robotics insights. | *Group Project Presentation* |

<h2>Teaching@ANU</h2>

* *22 July 2024 - 25 Oct 2024*: **TechLauncher Examiner**
  * School of Computing, The Australian National University (ANU)
  * [ANU TechLauncher](https://comp.anu.edu.au/TechLauncher/), co-taught courses: [COMP3500 - Software Engineering Project](https://programsandcourses.anu.edu.au/course/comp3500), [COMP4500 - Software Engineering Practice](https://programsandcourses.anu.edu.au/2023/course/COMP4500), [COMP8715 - Computing Project](https://programsandcourses.anu.edu.au/course/comp8715)
  * Course Convener: [A/Prof. Charles Gretton](https://researchers.anu.edu.au/researchers/gretton-co) & [A/Prof. Liang Zheng](https://zheng-lab-anu.github.io/)
  * <font color="red">My Student Experience of Learning and Teaching (<strong>SELT</strong>) teacher survey results: $4.11\pm0.80$ (on a 5-point scale, 413 enrollments)</font>
  * Duties:
    * Assess submissions from students, provide feedback, and contribute to determining final grades based on specified criteria and standards
    * Participate in quality control processes, ensuring consistency across evaluations, investigating deviations in assessments, and considering inputs from various sources to ensure fairness
    * Uphold ANU policies on academic integrity, plagiarism, late submissions, and appeals, ensuring that evaluations are conducted in accordance with established academic standards and guidelines

* *19 Feb 2024 - 24 May 2024*: **TechLauncher Examiner**
  * School of Computing, The Australian National University (ANU)
  * [ANU TechLauncher](https://comp.anu.edu.au/TechLauncher/), co-taught courses: [COMP3500 - Software Engineering Project](https://programsandcourses.anu.edu.au/course/comp3500), [COMP4500 - Software Engineering Practice](https://programsandcourses.anu.edu.au/2023/course/COMP4500), [COMP8715 - Computing Project](https://programsandcourses.anu.edu.au/course/comp8715)
  * Course Convener: [A/Prof. Charles Gretton](https://researchers.anu.edu.au/researchers/gretton-co) & [A/Prof. Liang Zheng](https://zheng-lab-anu.github.io/)
  * <font color="red">My Student Experience of Learning and Teaching (<strong>SELT</strong>) teacher survey results: $4.60\pm0.80$ (on a 5-point scale, 313 enrollments)</font>

<h2>Teaching@UWA</h2>

* *26 Feb 2018 - 1 June 2018*: **Teaching Assistant**
  * Department of Computer Science and Software Engineering (CSSE), The University of Western Australia (UWA)
  * [CITS5508 Machine Learning](https://handbooks.uwa.edu.au/unitdetails?code=CITS5508)
  * Unit Coordinator(s): [Assoc. Prof. Du Huynh](https://research-repository.uwa.edu.au/en/persons/du-huynh) & [Prof. Mark Reynolds](https://research-repository.uwa.edu.au/en/persons/mark-reynolds)
  * Job Duties:
    * Set assignment questions
    * Supervise laboratory classes
    * Help with assignment marking

