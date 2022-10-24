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
    

 

    p.setup = setup
  
      
myp5 = window.p5.new(sketch)
