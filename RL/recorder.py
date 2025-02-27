#!/usr/bin/env python
import rospy #importar ros para python
from std_msgs.msg import String, Int32 #importa mensajes de ROS tipo String y Int32
import cv2 # importar libreria opencv
import os     
from sensor_msgs.msg import Image # importar mensajes de ROS tipo Image
from cv_bridge import CvBridge # importar convertidor de formato de imagenes

class Template(object):
	def __init__(self, args):
		super(Template, self).__init__()
		self.args = args
		#modificar en la linea 14 la subscripción de la cámara
		self.Sub_Cam = rospy.Subscriber("/duckiebot/camera_node/image/rect", Image, self.tomar_img)
		self.i = 0
		
	#def publicar(self, msg):
		#self.publi.publish(msg)

	def tomar_img(self, msg):
		bridge = CvBridge()
		image = bridge.imgmsg_to_cv2(msg, "bgr8") 
		#Se declara la carpeta donde se guardaran las imagenes (crear en la misma ruta que se encuentra recorder.py)
        path = 'duckietown/catkin_ws/src/desafios_2022/src'
        #Se escribe la imagen en la caperta del path
        nombre = "imagen"+str(self.i)+".jpg"
        cv2.imwrite(nombre, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        self.i+=1

#Crear una forma de guardar las velocidades lineales y angulares de las ruedas

def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
