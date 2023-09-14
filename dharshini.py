classplayer:
 defplay(self):
   print("The player is playing cricket")
 classBatsman(player):
    defplay(self):
     print("The Batsman is batting.")
classBowler(player):
  defplay(self):
   print("The Bowler is bowling.")
#creating objects of the

Batsman andBowler classes
batsman=Batsman()
bowler=Bowler()
#calling the play()method for each object
batsman.play()
bowler.play()
