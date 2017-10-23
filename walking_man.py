
# Created by : Younes Elfeitori
# Created on : Oct 2017
# Created for : ICS3U
# This program shows a walking man

import ui
import time
@ui.in_background

def walking_man_touch_up_inside(sender):
    
   
    #variables 
    generated_number = 0
    counter = 10
    
    
    while counter > generated_number:
          
          if generated_number == 0:             
              view['walkingman_image'].image = ui.Image.named('./assets/sprites/walkingman_1.BMP')
              generated_number = generated_number + 1                             
    
          elif generated_number == 1: 
              time.sleep(0.10)             
              view['walkingman_image'].image = ui.Image.named('./assets/sprites/walkingman_2.BMP')                                                                                              
              generated_number = generated_number + 1                              
    
          elif generated_number == 2:
              time.sleep(0.10)
              view['walkingman_image'].image = ui.Image.named('./assets/sprites/walkingman_3.BMP')
              generated_number = generated_number + 1                             
    
          elif generated_number == 3:
              time.sleep(0.10)
              view['walkingman_image'].image = ui.Image.named('./assets/sprites/walkingman_4.BMP')
              generated_number = generated_number + 1                             
    
          elif generated_number == 4:
              time.sleep(0.10)
              view['walkingman_image'].image = ui.Image.named('./assets/sprites/walkingman_5.BMP')
              generated_number = generated_number + 1                              
    
          elif generated_number == 5:
              time.sleep(0.10)
              view['walkingman_image'].image = ui.Image.named('./assets/sprites/walkingman_6.BMP')
              generated_number = generated_number + 1                           
    
          elif generated_number == 6:
              time.sleep(0.10)
              view['walkingman_image'].image = ui.Image.named('./assets/sprites/walkingman_7.BMP')
              generated_number = generated_number + 1                              
    
          elif generated_number == 7:
              time.sleep(0.10)
              view['walkingman_image'].image = ui.Image.named('./assets/sprites/walkingman_8.BMP')
              generated_number = generated_number + 1                              
    
          elif generated_number == 8:
              time.sleep(0.10)
              view['walkingman_image'].image = ui.Image.named('./assets/sprites/walkingman_9.BMP')
              generated_number = generated_number + 1                             
    
          elif generated_number == 9:
              time.sleep(0.10)
              view['walkingman_image'].image = ui.Image.named('./assets/sprites/walkingman_10.BMP')
              generated_number = 0                            
     
view = ui.load_view()
view.present('sheet')
