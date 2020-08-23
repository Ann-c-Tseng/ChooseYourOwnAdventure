print("Welcome to this Game of Choices: ")

name = input("What do you want to be called? ")

print("Hello ", name, ".", " Now that we are ready, lets play...", sep="")

health = 10
print("You are starting with", 10, "health.", "Use your health wisely!")
print("")
print("You find yourself returning to consciousness in a field. You see a path before you branching out into the left or right: ")
left_or_right = input("Do you go left or right (left/right)? ")
if left_or_right == "left":
  print("")
  ans = input("You choose the left side, following the path until you reach a lake. Do you swim across or go around (across/around)? ")
  if ans == "around":
    print("")
    print("You went around smoothly without meeting any wild animals and reached the other side.")
  elif ans == "across":
    print("")
    print("You managed to get across but was bit by a fish. You lost 5 health.")
    health -= 5
    print("Your health is now at", 5)

  ans = input("You notice a house and a river. Which do you go to (house/river)? ")
  if ans == "house":
    print("")
    print("You go to the the dilapidated house, and an unfriendly looking man comes out weilding a club. As you tried to dodge his blows and escape, you get hit by the club and lose 5 health")
    health -= 5
    print("Your health is now at", health)
    if health <= 0:
      print("")
      print("You have lost too much health!", "Your health is currently at", health, "and you have died.")
    else:
      print("")
      print("You evaded the man and are now at the back of the house without him noticing. You were about to leave the place when you see two eyes looking at you from a gap between two wooden planks making up the backyard's shed.")
      ans = input("Do you go towards the eyes (yes/no)? ")
      if ans == "yes":
        print("You decided to move towards the shed to take a look at what is in it. The eyes dissapeared into the shed as you make your way over.")
        print("You hear footsteps and presume that the man with the club is coming. Without a second thought, you bring yourself into the shed and closed the door")
        print("")
        print("Your eyes adjust to the darkness and you were surprised at how big the shed is from the inside. Looking to your right you see a bunch of basic gardening tools, and to your left you see the owner of the eyes you saw while you were in the backyard.")
        print("")
        print("Hello? - You said")
        print("")
        print("The girl stared at you in fright. To your surprised, she then said - ", name, "? You were about to ask her how she knew your name, when you feel a sudden thud against the back of your head. A moment later, all went black.", sep="")
        print("")
        print("")
        print("Thank you for playing... this game is continuing to be updated and lengthened. Thank you for your time, and feel free to replay to see what other roads you could've taken!")

      else:
        print("")
        print("You decide to leave the backyard and the errie situation, but as you were leaving, the man with the club came into the backyard and saw you. He brought out his club and slammed his weapon onto the back of your head. You lost", health, "health and died.")

  else:
    print("")
    print("You followed the river, but as you were walking along the riverbank, you were bit by a snake. You tried to mitigate the venom but was unsuccessful. You died as the venom consumes your body.")

else:
  print("")
  print("You went to the right... and landed in quick sand. You struggled to escape but the sand pulled you further under. You died suffocating to death")
