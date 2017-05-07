# coding:utf-8
def load_blocked():
    global blocked_words
    with open('game.py') as f:
         blocked_words = [l.strip for l in f if f]
 
 
 
 def words_filter(name,charocter = 'utf-8',symbal = '*'):
     
