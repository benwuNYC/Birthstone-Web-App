from flask import render_template, request, redirect
from app import app
from app.models import model, formopener

birthstones = {
    "january" : "Garnet", 
    "february" : "Amethyst",
    "march" : "Aquamarine",
    "april" : "Diamond",
    "may" : "Emerald",
    "june" : "Pearl or Alexandrite or Moonstone",
    "july" : "Ruby",
    "august" : "Peridot",
    "september" : "Sapphire",
    "october" : "Tourmaline or Opal",
    "november" : "Topaz or Citrine",
    "december" : "Tanzanite, Zircon or Turquoise",
}
birthstone_descriptions = {
    "january" : "Garnet, the birthstone of January, is mined in a rainbow of colors. From the fiery orange of Mandarin Garnet to the rich green of Tsavorite Garnet and to the most widely recognized color of Pyrope Garnet, it is considered a great gift to symbolize friendship and trust.", 
    "february" : "Amethyst, the birthstone of February, is a variety of Quartz that carries a spectacular purple color that ranges from a blend of deep violet and red to a lighter lilac hue. Ancient Greeks believed that the stone protected the wearer from drunkenness and enabled them to keep a balanced mindset.",
    "march" : "Aquamarine, the birthstone of March, has a rich color and has long been a symbol of youth, health and hope. Its mesmerizing color ranges from pale to deep blue and are reminiscent of the sea. A perfect birthstone for March, the Aquamarine creates a beautiful accent to spring and summer wardrobes.",
    "april" : "Diamonds, the birthstone of April, are commonly associated with love which make it the perfect gift for a loved one. While white diamonds are most common, fancy colored diamonds can be found in various colors including yellow, blue, pink and a variety of others as well.",
    "may" : "Emerald, the birthstone of May, carries the rich green color of Spring and radiates a beautiful vivid tone. They are considered to be a symbol of rebirth and love. Emeralds are the rarest gemstones and are typically mined in Colombia, Brazil, Afghanistan and Zambia.",
    "june" : "June birthdays claim three birthstones; pearl, moonstone and Alexandrite. Pearls have been wildly popular in jewelry for centuries because of their natural beauty. Alexandrite gemstones are extremely rare and desirable since they change color based on the lighting. Named for its glowing color sheen that resembles the moonlight, Moonstone can belong to several different members of the feldspar group and they display a unique play of color known as adularescence. ",
    "july" : "Rubies, the birthstone of July, are considered the king of gems and represent love, health and wisdom. It was believed wearing a fine red Ruby bestowed good fortune on its owner. A Ruby is the most valuable gemstone and its value increases based on its color and quality.",
    "august" : "August is the latest month to claim Peridot. Peridot, with it’s signature lime green color, is believed to instill power and influence in the wearer.",
    "september" : "Sapphire, the birthstone of September, is most desired in its pure, rich blue color but is present in almost every color including pink, yellow and green. In the Middle Ages the gem was believed to protect those close to you from harm and also represented loyalty and trust.",
    "october" : "October also has two birthstones; Tourmaline and Opal. Tourmaline is a favorite gemstone for many because it’s available in a rainbow of beautiful colors. Opal gemstones are truly unique because each individual gem is adorned with a one-of-a-kind color combination.",
    "november" : "November birthdays are associated with two gems; Citrine and Topaz. The warm color of Citrine is said to be a gift from the sun and it’s believed to be a healing gemstone. Topaz is most desired in its rich orange Imperial Topaz color but it is found in a variety of rich colors like blue, pink and yellow.",
    "december" : "December birthdays have claim to three gemstones; Zircon, Tanzanite and Turquoise. Each of these gemstones carries a unique blue tone making it a perfect birthstone for Minnesota’s frigid December winters. Zircon can be found in a variety of colors, but blue is the overwhelming favorite.",    
}
birthstone_pictures = {
    "january" : "static/january-birthstone.jpg",
    "february" : "static/february-birthstone.jpg",
    "march" : "static/march-birthstone.jpg",
    "april" : "static/april-birthstone.jpg",
    "may" : "static/may-birthstone.png",
    "june" : "static/june-birthstone.jpg",
    "july" : "static/july-birthstone.jpg",
    "august": "static/august-birthstone.jpg",
    "september" : "static/september-birthstone.jpg",
    "october" : "static/october-birthstone.jpg",
    "november" : "static/november-birthstone.jpg",
    "december": "static/december-birthstone.jpg",
}

@app.route('/')
@app.route('/index')
def index():
    birthday = {}
    return render_template('index.html', birthday = birthday)
@app.route('/sendBirthstone', methods = ['GET','POST'])
def birthStone():
    if request.method == "GET": #If we get the page, it gives one; else if it posts(Sends info) it returns else 
        return  "Stop refreshing the page!"
    else:
        user_data = request.form 
        month = user_data["month"].lower()
        birthday = {"month" : month, "stone" : birthstones[month], "description" : birthstone_descriptions[month], "picture" : birthstone_pictures[month]}
        return render_template('results.html', birthday = birthday )
        #birthstones[month] + "\n" + birthstone_descriptions[month]
        