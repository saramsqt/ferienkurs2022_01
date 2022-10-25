from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(700, 410)

        #change color by changing rgb
        #diesen übergegebenen Wert = Parameter
        #die runden klammern die diesen Wert umschliessen = Parameterlisten
        p.background(248, 241, 174)
        p.rectMode(p.CENTER)
      
        #(x,y,a,b) x&y= coordinaten a&b = seiten
        p.rect(350,205,300,200) #mitte

        # (x,y,d) x&y= cordinaten d= durchmesser =grösse
        p.circle(350,205,50)  #mitte
        # p.circle(700,0,50) ecke
        # p.circle(650,50,50) ecke (sichbar)
        p.circle(350,205,40)
        p.circle(350,205,30)
        p.circle(350,205,20)
        p.circle(350,205,10)
       
    p.setup = setup
  
      
myp5 = window.p5.new(sketch)
