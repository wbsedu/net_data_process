import matplotlib.pyplot as plt;
import matplotlib as mpl;
import numpy as np;
#import matplotlib.font_manager as fm;

def plot_delay(write_delay,read_delay):
    for i in range(0,10,1):
        read_delay[i]=read_delay[i]*1000;
        write_delay[i]=write_delay[i]*1000;
    plt.rcParams['font.sans-serif'] = ['SimSun']
    front={'family' : 'SimSun',
    'weight' : 'normal',
    'size' : 23,
    }
    x=np.linspace(1,10,10)
    plt.figure() 
    plt.xlabel("注入率N(读写请求比例N:1)",front)
    plt.ylabel("延时(cycle)",front)

    plt.xticks([0, 1, 2,3, 4, 5, 6, 7, 8, 9, 10, 11])
    plt.tick_params(labelsize=23)
    plt.plot(x,write_delay, marker='o',label="写请求平均延时")
    plt.plot(x,read_delay, marker='>',label="读请求平均延时")
    plt.legend(loc="upper right",prop=front)
    #plt.legend(handles=[A, B], prop=font1)
    plt.grid()
    return
write_delay0=[0.08093980731172294, 0.08005124226267564, 0.08123909412070483, 0.08019906056273003, 0.08087770926699475, 0.0807572891220627, 0.0816036899142997, 0.0792655693829403, 0.08028884105713889, 0.0799108093354074]
read_delay0=[0.12083912818922715, 0.1172939994448928, 0.1154752395096662, 0.11488506117171972, 0.11462419395932043, 0.11425210195545539, 0.11395959080113116, 0.11420309292602479, 0.11378531757025209, 0.11378657321459684]
write_delay1=[0.08093980731172294, 0.08005124226267564, 0.08123909412070483, 0.08019906056273003, 0.08087770926699475, 0.0807572891220627, 0.0816036899142997, 0.0792655693829403, 0.08028884105713889, 0.0799108093354074]
read_delay1=[0.12083912818922715, 0.1172939994448928, 0.1154752395096662, 0.11488506117171972, 0.11462419395932043, 0.11425210195545539, 0.11395959080113116, 0.11420309292602479, 0.11378531757025209, 0.11378657321459684]
plot_delay(write_delay0,read_delay0)
plot_delay(write_delay1,read_delay1)
plt.show()