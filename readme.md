<h1 style="text-align:center">Eta Multi-FX Unit</h1>

### Abstract

*This project aims to provide a cheaper alternative to commercially available multi-fx units for guitar players. Through the use of an Arduino microcontroller and a Raspberrypi single board computer, it is possible to build a simple yet inexpensive Mutli-FX unit.*



## Introduction

<div style="text-align: justify">One of the most fun parts of playing guitar is the ability to mix and match different effect together in order to achieve your own unique sound. One way of  generating these different effects in order to alter one's guitar sound is through the use of a Multi-Effects Unit. These units provide a vast amount of different effects in a single package that allows you to mix and match to your heart's content. The main drawback however to these multi effects units is that their price is not within lots of guitar player's budgets. The Eta Multi-FX unit aims to address this problem by providing guitar players with a cheaper alternative.</div>



### Specifications



#### Brief overview

The Eta Multi-FX unit uses both an Arduino microcontroller as well as a Raspberrypi to act as the brains of the operation. While the Raspberrypi is responsible for user interactions such as displaying the GUI or reading in button presses etc. the Arduino is used for Real time processing of the incoming signal. The Arduino and Raspberrypi communicate with each other via a 23LCV1024 SRAM from Microchip. The reason for the use of the intermediate device in the communication chain is to prevent interruptions to the Arduino's real time processing of the signal. By using this device, the Arduino can read the required information once it has time available. The main data that will be communicated between the two devices will be what effects the Arduino needs to apply to the incoming signal, which can easily be stored on the SRAM.



#### Arduino

As mentioned previously, the Arduino is responsible for the real time processing of the signal. The decision for using an Arduino microcontroller for this task was made for a couple of reasons which most importantly include the following two reasons: The Arduino's superior performance during time critical operations, even though the RaspberryPi has vastly superior computational performance, its use of an operating system where background tasks and other forms of interrupts mean it is difficult to perform real time or even near real time processing of a signal. The second reason is the large amount of resources and documentation available pertaining to the use of Input and Output pins on the Arduino platform, whilst resources covering a similar topic for applied to the raspberry pi, seem few and far between.



#### Arduino Code Execution

<img src="Documentation\Images\Arduino_Code_Execution.jpeg" width="50%" height="50%" align="center"/>
