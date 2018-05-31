# CDT Software Course - TMCS 2018

Tues 16th - Fri 19th, May 2017.

Lars Andersen Bratholm (LAB), Mike O'Connor (MOC), Silvia Amabilino (SA), David Glowacki (DRG)

## Timetable

Tuesday 29th May (DRG)

* 10:00 Introduction and Overview
* 10:15 Getting Started with Python
    * [A simple Python Program](outlines/gettingStarted.md)
* 10:45 A simple live demo for debugging in PyCharm (DRG)
    * [This video also provides a nice outline of how to debug in PyCharm](https://www.youtube.com/watch?v=BBPoInSOiOY)
    
* 11:00 Learning more about Python
    * [A Python Framework for Simple Game Mechanics](outlines/I-pyGlet-GameMechanics.md)
    * Basic Python features
      * [containers, lists, and dictionaries](python/1_lists_and_dictionaries.md)
      * [functions & modules](python/2_functions_and_modules.md)
      * [documenting Code](python/3_documenting_code.md)
    * [Basic Principles of Object-Oriented Programming](python/4_object_orientation.md)
    * Other Potentially useful stuff 
      * [Python tutorial](https://docs.python.org/3/tutorial/index.html) (use as a reference, not an actual tutorial) 
      * Already a python expert? Try some [Project Euler](https://projecteuler.net/) challenges.    

* 11:30 coffee
* 13:00 Lunch
* 14:00 [Scipy and NumPy](python/5_numpy.md)
* 15:15 Coffee 
* 15:30 [Experiment & Play: Use what you've learned to hack-your-own game mechanics](outlines/II-pyGlet-GameMechanics.md)
* 17:30 Finish 

Wednesday 30th May (LAB, MOC, SA, DRG)

* 10:00 [Experiment & Play: Use what you've learned to hack-your-own game mechanics](outlines/II-pyGlet-GameMechanics.md)
* 11:15 coffee
* 11:30 Version Control 
    * [Part 1: Basic git - structure & commands](outlines/git-outline.md#git-and-version-control) - LAB
* 12:30 Lunch
* 13:30 Version Control 
    * [Part 2: Remote repos & GIT GUIs](outlines/git-outline.md#part-2) - LAB
    * live code example: how to upload your game projects onto github using gitkraken
* 14:30 coffee
* 14:45 [Testing software and catching errors](testing/README.md) ([slides](testing/slides.pdf)) - LAB/DRG
* 15:15 A REALLY Quick overview of machine learning & data science (DRG)
* 15:45 coffee
* 16:00 Overview of the three hackathon projects
    * LAB - Learning with TensorFlow - [slides](https://gitpitch.com/larsbratholm/boot-camps/master?p=tf_tutorial/presentation)
    * SA  - Machine learning potential energy surfaces
    * MOC - Machine learning hand pose for interactive molecular simulation in VR
* 16:30 coffee
* 16:45 The data science pipeline [slides](https://gitpitch.com/larsbratholm/boot-camps/master?p=pipeline) - LAB
    * [jupyter notebook](pipeline/data_science_pipeline.ipynb)
* 17:45 Pub. Students should take this opportunity to organize themselves into their project groups

Thursday 31st May (LAB, MOC, SA, DRG)

* 10:00 - 18:00 hackathon
    * group 1 led by LAB - tutorial [here](tf_tutorial/README.md)
    * group 2 led by SA - repository [here](https://bitbucket.org/SilviaAmAm/tmcs_2018/src/master/)  
    * group 3 led by MOC - repository [here](https://github.com/mikeoconnor0308/tensorglove)
* 12:00 - 13:00 guest lecture: Clare Macrae (developer @Cambridge Crystallographic Data Centre)
    * [download link for Clare's ppt slides: professional software development](proSoftwareDev2018.pptx)
* 18:00 - 19:00 pizza/wine party!

Friday 1st Jun (LAB, MOC, SA, DRG)
 
* 11:00 - 16:00 hackathon
* 16:00 - 17:00 show and tell


## Hints and tips

[Hints and tips](outlines/hints_and_tips.md) on common Bash and editor commands.

Beginners guide to using the [shell](shell/README.md)
## Before you arrive...

We recommend that you bring your own laptop to work on (so 
that you can easily continue to use the same tools for the hackathon!).

You should test your installation using our testing scripts. To access these start a shell and run the 
commands:

    git clone https://github.com/larsbratholm/boot-camps.git
    cd boot-camps/setup

before following [these instructions](setup/README.md).

You also need to create a free individual account on 
[GitHub](https://github.com/join). Make sure 
you know your username and password when you arrive

We recommend that you to work through this short tutorial on 
[Beginning Python](http://chryswoods.com/beginning_python) to refresh yourself on Python. 

## Acknowledgements 

Much of this workshop borrows from the great resource that is [Software Carpentry](https://software-carpentry.org/).
