#Libraries
import tkinter as tk
from turtle import window_height
import requests
from PIL import Image, ImageTk
import os
import urllib.request

root = tk.Tk()

#Basic Templet

root.title("Weather App")
root.geometry("600x500")

# Openweather API info
# key: 64f28e8b4911b51b3ee1ca8ad43692d1
# Api URL: https://api.openweathermap.org/data/2.5/weather

#Functionalities

def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City:%s\nCondition:%s\nTemperature:%s'%(city,condition,temp)
    except:
        final_str = "Problem while retrieving this information !!"
    return final_str    
 
    
def get_weather(city):
    weather_keys = '64f28e8b4911b51b3ee1ca8ad43692d1'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_keys,'q':city,'units':'metric'}
    response = requests.get(url,params)
    #print(response.json())
    weather = response.json()
    
    #print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])
    
    result['text'] = format_response(weather)
    
    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)
    
def open_image(icon):
    size = int(frame_two.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size,size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image=img

#Background Image
   
img = Image.open("background_img.jpg")
img = img.resize((600,500))
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

#Heading

heading_title = tk.Label(bg_lbl,text='Earth Including Over 2,00,000 Cities!',fg='red',bg='#79BAEC',font=('times new roman',20,'bold'))
heading_title.place(x=80,y=18)

#1st frame
frame_one = tk.Frame(bg_lbl,bg="#4682B4",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)

txt_box = tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='W')

#Get weather button

btn = tk.Button(frame_one,text='Get Weather',fg='green',font=('times new roman',16,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=13)

#2nd frame

frame_two = tk.Frame(bg_lbl,bg="#82CAFF",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result = tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

#Bottom canvas

weather_icon = tk.Canvas(result,bg='white',bd=0,highlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)

#Assign icons to weather

day = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13n.png', '50d.png']
night = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']

base_url = 'https://openweathermap.org/img/w/'
img_dir = './img/'
if not os.path.exists(img_dir):
	os.makedirs(img_dir)

for name in day:
	file_name = img_dir+name
	if not os.path.exists(file_name):
		urllib.request.urlretrieve(base_url+name, file_name)

for name in night:
	file_name = img_dir+name
	if not os.path.exists(file_name):
		urllib.request.urlretrieve(base_url+name, file_name)


root.mainloop()