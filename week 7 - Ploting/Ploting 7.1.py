# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 21:51:33 2018

@author: Reda
"""

import pylab as plt

my_sample = []
my_linear = []
my_quadratic = []
my_cubic = []
my_exponential = []

for i in range(30):
    my_sample.append(i)
    my_linear.append(i)
    my_quadratic.append(i**2)
    my_cubic.append(i**3)
    my_exponential.append(1.5**i)


##1st way
#plt.plot(my_sample, my_linear)    
#plt.plot(my_sample, my_quadratic) #(x, y)
#plt.plot(my_sample, my_cubic)
#plt.plot(my_sample, my_exponential)

##2nd way
#plt.figure('lin')
#plt.plot(my_sample, my_linear)
#plt.figure('quad')    
#plt.plot(my_sample, my_quadratic) #(x, y)
#plt.figure('cube')
#plt.plot(my_sample, my_cubic)
#plt.figure('expo')
#plt.plot(my_sample, my_exponential)

##3rd way
#plt.figure('lin')
#plt.xlabel('Sample points')
#plt.ylabel('Linear function')
#plt.plot(my_sample, my_linear)
#plt.figure('quad')                  #this one here
#plt.plot(my_sample, my_quadratic) #(x, y)
#plt.figure('cube')
#plt.plot(my_sample, my_cubic)
#plt.figure('expo')
#plt.plot(my_sample, my_exponential)
#plt.figure('quad')                  #reopen the quad figure
#plt.ylabel('quadratic function')
##reopen all the figures
#plt.figure('lin')
#plt.title('Linear')
#plt.figure('quad')
#plt.title('Quadratic')
#plt.figure('cube')
#plt.title('Cubic')
#plt.figure('expo')
#plt.title('Exponential')

#4th way
#.clf() == clear the frame
#plt.figure('lin')
#plt.clf() 
#plt.plot(my_sample, my_linear)
#plt.figure('quad')
#plt.clf()
#plt.plot(my_sample, my_quadratic)
#plt.figure('cube')
#plt.clf()
#plt.plot(my_sample, my_cubic)
#plt.figure('expo')
#plt.clf()
#plt.plot(my_sample, my_exponential)
#
#plt.figure('lin')
#plt.title('Linear')
#plt.figure('quad')
#plt.title('Quadratic')
#plt.figure('cube')
#plt.title('Cubic')
#plt.figure('expo')
#plt.title('Exponential')
    
##CHANGING LIMITS ON AXES
#plt.figure('lin')
#plt.clf()
#plt.ylim(0,1000) #limit on y axis
#plt.plot(my_sample, my_linear)
#plt.figure('quad')
#plt.clf()
#plt.ylim(0,1000) #limit on y axis
#plt.plot(my_sample, my_quadratic)
#plt.figure('lin')
#plt.title('Linear')
#plt.figure('quad')
#plt.title('Quadratic')
    
##OVERLAYING PLOTS
#plt.figure('linquad')
#plt.title('Linear vs. Quadratic')
#plt.clf()
#plt.plot(my_sample, my_linear)
#plt.plot(my_sample, my_quadratic)
#
#plt.figure('cube exp')
#plt.title('Cubic vs. Exponential')
#plt.clf()
#plt.plot(my_sample, my_cubic)
#plt.plot(my_sample, my_exponential)


##ADDING MORE DOCUMENTATION
#plt.figure('linquad')
#plt.title('Linear vs. Quadratic')
#plt.clf()
#plt.plot(my_sample, my_linear, label = 'linear')
#plt.plot(my_sample, my_quadratic, label = 'quadratic')
#plt.legend(loc= 'upper left') #loc == location
#
#plt.figure('cube exp')
#plt.title('Cubic vs. Exponential')
#plt.clf()
#plt.plot(my_sample, my_cubic, label = 'cubic')
#plt.plot(my_sample, my_exponential, label = 'exponential')
#plt.legend()  #plt do it otomatically


##CHANGING DATA DISPLAY
#plt.figure('lin quad')
#plt.title('Linear vs. Quadratic')
#plt.clf()
#plt.plot(my_sample, my_linear, 'b-', label = 'linear', linewidth= 2.0)  #color b- = blue
#plt.plot(my_sample, my_quadratic,'r', label = 'quadratic', linewidth= 3.0) # r == red
#plt.legend(loc= 'upper left')
#
#plt.figure('cube exp')
#plt.title('Cubic vs. Exponential')
#plt.clf()
#plt.plot(my_sample, my_cubic, 'g--', label = 'cubic', linewidth= 4.0) #green dashed line
#plt.plot(my_sample, my_exponential, 'r',label= 'exponential', linewidth= 5.0)
#plt.legend()

##USING SUBPLOTS
plt.figure('linquad')
plt.title('Linear vs. Quadratic')
plt.clf()
plt.subplot(211)
plt.ylim(0,900)
plt.plot(my_sample, my_linear, 'b-', label = 'linear', linewidth= 2.0)
plt.subplot(212)
plt.ylim(0,900)
plt.plot(my_sample, my_quadratic,'r', label = 'quadratic', linewidth= 3.0)
plt.legend(loc= 'upper left')


plt.figure('cube exp')
plt.title('Cubic vs. Exponential')
plt.clf()
plt.subplot(121)
plt.ylim(0, 140000)
plt.plot(my_sample, my_cubic, 'g--', label = 'cubic', linewidth= 4.0)
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(my_sample, my_exponential, 'r',label= 'exponential', linewidth= 5.0)
plt.legend()
