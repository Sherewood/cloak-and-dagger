
import time
import sys
import math
import random

TALK="You attempt to make small talk with anyone who would listen, but to no avial."
PICKUP="Pickup what?"
ATTACK="You usually work with a 'speak softly and carry a big stick' philosophy. No one here is a threat"
USE="There's no point here"
Passcode="11215"
Riddle="NOTHING"
part=1
MgWords="ABBACADABA"
TASK="Asking around town, you learn that today is the festival of the broken sun, and that all revelers are free enter the castle"
CASK="Asking around the castle, you find that most are either too busy or too drunk to properly respond."
PASK="Finding anyone in the prison who is still capaable of rational speech is hard.It appears anyone who was sound was dragged off by guards and...looking into the eyes of those who are left, you can guess."
DASK="You look into the darkness and ask yourself what it is. Prehaps a more magical hand can help"
rng=10
##

#ITEMS or Event triggers. Some of theses are not items you can get in game and use but they still need the same format
##
class Score():
    points=0
class MC():
    Healed=False
    BlackBlade=False
class Town_guard():
    type="EN"
    name="TOWN_GUARD"
    onspot="A Town_guard spots you and begins to approach you!"
    defeated=False
    dmessage="A guard lays on the ground, unconscious"
    following=False
    follow="the guard is still advancing behind you! He continues to slash"
    damage=10
    grace=True
    chance=8
    health=2
class Castle_guard():
    type="EN"
    name="CASTLE_GUARD"
    onspot="Standing to your left is a sole Castle_guard who appears to realize you aren't a reveler!He approaches with his sword drawn"
    defeated=False
    following=False
    dmessage="You see the unconcious guard being slowly pushed by serfs. You note that, while you see servants going to and fro, they don't seem to be going left..."
    damage=20
    grace=True
    chance=6
    health=3
    follow="The guard gives chase, striking and slashing at you!"
class Prison_guard():
    type="EN"
    name="PRISON_GUARD"
    following=False
    onspot="Much to your dismay, you are not alone in this room! a Prison_guard wakes at the sound of your entrance and readies his hammer."
    defeated=False
    dmessage="The prison guard is silent. With the helmet on his head lowered, it almost appears that he is sleeping."
    follow="Like a dog, the prison guard continues to nip at your heels. He lands a hit!"
    damage=10
    grace=True
    chance=5
    health=4



class Black_Blade():
    type="ITEM"
    name="BLACKBLADE"
    onspot="A blade as dark as a moonless night. As you hold it, you hear whispers and see shadows dancing around you"
    pickup="Despreate times call for despreate measures. As you take the knife, you hear laughter coming from everywhere yet nowhere."
    held=False
    changeLocal=False
    keyDesc="The room is empty now, but the air feels lighter. As if spirits have left the room."
    hasMor=False
    usepoints=0
    picp=103
    disposable=False
    droppable=False
    examine="You look deeper into the dark blade, yet you do not see your reflection. Instead, you see the history of the blade. So many sacrifices done in secret, only to be discarded. After which, you see your reflection and feel the blade getting warm, as if it were seething"
class healing():
    type="ITEM"
    name="SPRING"
    pickup="Mearly dropping your toes within the spring fills you with life and health!"
    keyDesc="The spring bubbles from a wall within the hidden chamber. The waters invite you"
    held=False
    changeLocal=False
    hasMor=False
    usepoints=107
    picp=0
    disposable=False
    droppable=False
    #Since you can't take this one, it has no examine
class Knife():
    type="ITEM"
    name="KNIFE"
    onspot="A solid Blade, nothing too special yet nothing too weak"
    pickup="You take your dagger and place it in the bag, then run like the wind!"
    changeLocal=True
    whereTo="Town_Center"
    held=False
    keyDesc=""
    hasMor=False
    usepoints=0
    picp=50
    droppable=True
    drop="You let the blade fall to the ground"
    onground="There is a knife on the ground"
    examine="A blade given to you by your master when you became an assasin. This knife has been with you for a while."
    disposable=False

class Poison():
    type="ITEM"
    name="POISON"
    onspot="A mainstay for your trade, this poison is undetectable yet strong"
    pickup="Being careful not to spill, you take the poison and put it in your bag, then hop out the window"
    changeLocal=True
    whereTo="Town_Center"
    held=False
    Used=False
    keyDesc=""
    hasMor=False
    usepoints=100
    picp=50
    droppable=True
    drop="You place the vial on the ground"
    onground="You notice a small vial of poison on the ground"
    examine="You remember your friend Gary giving this to you. 'Can drop a 7ft tall man in an instant!' he advertized. You hope he was right"
    disposable=True

 
class Costume():
    type="ITEM"
    name="COSTUME"
    onspot="A set of colorful cloths worn by the Troop in town"
    pickup="Being careful not to wake the drunk, you pocket the costume"
    Unlock="CASTLE_BRIDGE"
    held=False
    changeLocal=False
    hasMor=False
    keyDesc="The castle bridge has quieted somewhat and, in the silence, the guard stands silently. As you get closer, however, you hear a snore. It appears the Kings guard has been...overworked"
    usepoints=100
    picp=50
    droppable=True
    drop="Realizing that the grime is exactly what you think it is, you quickly drop the cosutme."
    onground="On the ground lies a costume"
    examine="It's a fine costume and in your size. Just ignore the grim on the bottom.'It's not vomit, it's not vomit,' you mutter as you place back the cosutme"
    disposable=True
class Rope():
    type="ITEM"
    name="ROPE"
    onspot="It's a long piece of rope, While it may not look like much, You've climbed up buildings with a swing of this thing"
    pickup="You pick up the rope and attach it to your hip. You then hop out the window"
    changeLocal=True
    whereTo="Town_Center"
    held=False
    keyDesc="You walk the path until the path vanishes, leaving you in the wilds with only the castle as reference. You stop when you notice a large open window into the castle.\n there is a rope hanging from the window"
    hasMor=False
    usepoints=100
    picp=50
    droppable=True
    disposable=True
    drop="You place the rope on the ground"
    onground="You notice some rope on the ground"
    examine="A long piece of rope you carry around with you. It's capable of reaching the top of your hometown abby and you're fairly certain that it was a really big abby"
class Vanished():
    type="ITEM"
    name="GOD"
    onspot="The blessing of a dark god. The tides have turned in your favor."
    held=False
    changeLocal=False
    hasMor=False
    Exist=True
    usepoints=100
    picp=50
    droppable=False
    examine="Think less like your holding a god and think more that a god owes you a favor."
    disposable=True
class Masters_Message():
    type="ITEM"
    name="MASTERS_MESSAGE"
    pickup="This is never going to be used but I'm writing for the sake of writing"
    onspot="You read the decciphered message of Your master: Important case, meet at inn with man and tell him 11215"
    held=True
    changeLocal=False
    keyDesc=""
    hasMor=False
    usepoints=100
    picp=50
    disposable=False
    droppable=False
    examine="You never made out your master to be a delegator of task. If she was called, she would simply go. But prehaps it's because she's begun to see your talent that you were given this task."
class MAGIC():
    type="ITEM"
    name="MAGIC"
    pickup="You take the rune off the ground and, on touch, the rune slides onto your hand. You feel an energy surging through you!"
    onspot="A magical rune, capable of allowing you to use a MAGICAL solution. Now if only you had some magical problems"
    held=False
    changeLocal=False
    keyDesc="You see a nice and clean staircase going up an old tower"
    hasMor=False
    usepoints=100
    picp=50
    droppable=False
    examine="A magic rune appears on your hand. If it were any other day, this would be the best day of your life"
    disposable=False
class FOOD():
    type="ITEM"
    name="FOOD"
    pickup="You take the plate of food, now fully decorated and hold it in your hands"
    onspot="A plate of delicous food which may be the last thing the king ever eats lies on the table"
    held=False
    changeLocal=False
    whereTo=False
    bomb="Prison"
    hasMor=True
    keyDesc="You enter the throne room once more to find it dark. No one appears to be here, It could be that the king has something more important."
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":CASK}
    usepoints=200
    picp=100
    droppable=False
    examine=onspot
    disposable=False
class PoisonFood():
    type="ITEM"
    name="POI_FOOD"
    pickup="You take the plate of food and slather it in poison. You now have some Poi_food instead of normal food"
    held=False
    changeLocal=False
    whereTo=False
    bomb="Prison"
    hasMor=True
    keyDesc="You enter the throne room once more to find it dark. No one appears to be here, It could be that the king has something more important."
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK, "ASK":CASK}
    usepoints=200
    picp=100
    disposable=False
    droppable=False
    examine=FOOD.onspot
    disposable=False
class Gold_Leaf():
    type="ITEM"
    name="GOLDLEAF"
    onspot="Ornate gold woven together forms the leaf in your hands. Used for almost all decorations"
    pickup="you pry the gold leaf off the wall and place it in your pocket"
    held=False
    changeLocal=False
    keyDesc="Things have cooled down a bit now that the main course is ready. Most of the serfs still here are in smaller rooms, having their own dinners. The Pig on the plate is still at the back."
    hasMor=True
    Utrigger="Being though, you give the Pig a maranade of poison before you head out."
    USE={"POISON":Utrigger}
    PICKUP={"FOOD":FOOD}
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK, "ASK":CASK}
    usepoints=100
    picp=50
    disposable=True
    droppable=True
    drop="Fearing it might shatter, you look towards a wall and place the goldleaf wherever it can fit."
    onground="You see a piece of gold leaf hung loosly on the wall"
    examine="An ornate piece of gold shaped like a maple leaf. Used in decorations and presentation"
class Rod_Of_Babble():
    type="ITEM"
    name="ROD"
    onspot=" You hold in you hand a large Iron rod. Carved into it is a great deal of ornate designs. You note there is a missing piece at the bottom"
    pickup="You take the rod and put it in your pocket, the cold steel sending a shiver down your spine"
    held=False
    changeLocal=False
    keyDesc="The Room is now darkend once again. You note now the walls chared"
    hasMor=False
    usepoints=100
    picp=50
    disposable=True
    droppable=True
    drop="You place the rod on the ground."
    onground="There is a rod on the ground"
    examine="An sleek, black, metal rod. Looking deeper, you notice that the rod is also carved, showing multiple runes on either side"
class KeyRing():
    type="ITEM"
    name="KEYRING"
    onspot="A set of keys beloning to the Keysmith."
    pickup="You take the keyring off the corpse and cover the body with a blanket. You then curse the king for his ruthlessness"
    held= False
    changeLocal=False
    usepoints=100
    picp=50
    droppable=True
    drop="You place the keyring on the ground"
    onground="You see a keyring on the ground"
    disposable=True
    examine="It's a keyring for almost any house in the Town. The keymaster was the appointed Locksmith of the realm, who was arrested for dissenting against the king."
    hasMor=True
    ATrig="As you ask about the king, the wizards eyes darken.'They say, many years ago, the King's ancestor was a wizard. That wizard was able to imprisson a god who then helped him take over the kingdom.' they say every festival of the broken sun, the king will sacrifice prisoners to keep the protection.\nBut, when i was a young lad, I snuck up to the ancient wizard tower in the castle and found the altar holding the god in.\nIf one were to open the lock, then the king would no longer be protected.'\nThe wizard then puts a pipe in his mouth,'But you didn't hear this from me. I don't want to end up like the keymaster.\n"
    talkTrig="Welcome, as thanks for helping me inside. I will show you some of what I've learned. Using this MAGIC rune on the ground, you will be able to use magic! This may help you in your quest...whatever it is."
    PICKUP={"MAGIC":MAGIC}
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":talkTrig,"ATTACK":ATTACK,"ASK":ATrig}   
    keyDesc="Tomes line the wall as you enter the hut of the wizard. Upon the ground lies a massive rune which the wizard has taken to call MAGIC! the wizard himself welcomes you inside."
class Star_Of_Babble():
    type="ITEM"
    name="STAR"
    onspot="In your hands you hold a star made from Human flesh. Despite being old, you feel it beating in your hands"
    pickup="You pick up the star and almost drop it. It feels..fleshy. You eventually place it in your pocket"
    changeLocal=False
    examine="You'd rather not, the star is composed of human skin and feels warm.You feel any more details and you'll no longer be able to contain your lunch"
    held=False
    keyDesc="The altar has now lit up, bloods red lights fly from to the ceiling. The star still needs to be pushed"
    hasMor=True
    Utrigger="You begin pushing in the rod. As you do so, the light in the room becomes unbearable and blinding. Finally, as you push the rod as far it will go, the light dies. You fall back winded and see a shadow coming from the altar. It reaches out and touches you.'Simply USE me, a god, and i shall destroy your enenmies....'He then dissapates..."
    Actions={"USE":{"ROD":Utrigger}, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":"There's nothing here now"}
    usepoints=100
    picp=50
    disposable=True





# NODES CLASSES. 
class Commence():
    isLocked=False
    description="Welcome to Cloak and dagger.\nMovement is handled with North,South,East,West,Up and down being represented by n,s,e,w,u,d.\nuse items by using use<item>, pickup with pickup<item>, talk with talk, and attack with attack<person>.\nEnter yes to continue."
class Intro():
    description="You enter a packed tavern. You are an assasin and you've been sent here by your master to meet your client.\n Looking north, you think you see an old man drinking alone.\n Upstairs is your room and, to the south, is the town center."
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":TASK}
    isLocked=False
    failsafe=None
    Events=[]

class Upstairs():
    description="this is upstairs, You head to your room and open a bag.\nInside are your tools: poison, a long sting of rope and your trusty knife.\nSuddenly, You hear noises outside. The Town guard!\nLooks like you'll need to sneak through the north window if you want to survive.\n Unfortunatley, you don't have time to get your bag through, so it looks like you can only take one thing!"
    items={"KNIFE":Knife, "POISON":Poison,"ROPE":Rope}
    Actions={"USE":USE, "PICKUP":items, "TALK":TALK,"ATTACK":ATTACK,"ASK":TASK}
    isLocked=False
    failsafe=None
    Events=False
class Old_man():
    description="Tis an old man in a cloak, when you try and talk to him, he simply turns and grunts.\nIf only he knew you knew who he was...Wonder if you have anything to prove who you are"
    UTrigger="The Old man looks up from his brew and looks you dead in the eye as you say it. 'So, you're the Assasin they've sent' he says quietly, offering you a space a the table.\n 'Was expecting a Lady,' he says while you reassure him that you are the one sent by your Master. \n 'Doesn't matter, I don't want no more noise with this. listen, the King's a tyrnat and he needs to be stopped! So sneak into the castle and end him.' The old man looks back to his brew, it appears you know what your doing now."
    Actions={"USE":{"11215": UTrigger} , "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":TASK}
    isLocked=False
    failsafe=None
    Events=[]

class Town_Center():
    description="You are now in the center of town.\nFrom the west come hunters from the woods. The Eastern path is caked with people in Bright costumes. It appears there's a fair in town.\n Southwards you see the gates of the castle and north brings you back to the tavern"
    isLocked=False
    failsafe="S" # because S is also locked for the castle entrance, This is a failsage to use just in case
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":TASK}
    Events=[]
class Town_East():
    description="The streets are lined with tightly packed houses which are either locked or abandoned.\n from the north, you catch the sight of a tight alleyway but, to the East, you see a bizzare hut. "
    isLocked=False
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":TASK}
    failsafe=None
    Events=[]
class Alley():
    description="As you get closer to the Alley, all you can smell is unpleasant odors.Looking in, you see the culprit; a drunken performer passed out on the boxes, his costume taken off and neatly folded on a box nearby. You'd laugh but you're afraid you'd inhale more of the smell."
    isLocked=False
    items={"COSTUME":Costume}
    Actions={"USE":USE, "PICKUP":items, "TALK":TALK,"ATTACK":ATTACK,"ASK":"There's no one here who can talk"}
    failsafe=None
    Events=[Costume]
class Wizard():
    isLocked=False
    USE={"KEYRING":KeyRing}
    talkTrig="You go up to the old man and ask what's wrong.\n 'Oh, it's nothing,' he replies,'I've been locked out of my home and the only other key belongs to the keymaster.He's gone now, imprissoned by the king. So Now i'm stuck.'\n He sighs and continues sitting down."
    description="You see an oddly large, small looking, hut. In front of it sits an elderly man"
    useTrig="You take the keymaster's keys and pop open the door to the hut. The wizard looks at you in amazement and walks inside.'Come, I have somthing in thanks' he says as he heads inside"
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":talkTrig,"ATTACK":ATTACK,"ASK":talkTrig}    
    failsafe=None
    Events=[]
class Town_West():
    description="A lesser building density than eastside, the westward path gives way to the royal woods."
    isLocked=False
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":TASK}
    failsafe=None
    Events=[]
class Forest():
    isLocked=True
    LockedMsg="U"
    Lockedprint="You look up to the window and, oh boy, it's high up. Almost impossible to climb by hand, you'd need somthing to help you up there"
    description="You walk the path until the path vanishes, leaving you in the wilds with only the castle as reference. You stop when you notice a large open window into the castle."
    UTrigger="With a flick of the wrist and years of muscle training, you toss the rope all the way up to the window. A path now opens to get into the castle!"
    USE={"ROPE":UTrigger}
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK": "You ask the birds if there are any kings nearby. Naturally, the fly away towards the north"}
    failsafe=None
    Events=[Town_guard]
class Castle_Bridge():
    isLocked=True
    description="The castle Bridge is packed with performers and revelers, yet the guardsman at the front is staunch in his vigiliance.\nYou see him force away all non-revelers and prevent their entry.\nYou imagine the same would happen so long as you continue South"
    LockedMsg="S"
    Lockedprint="You try and pass the gate but to no avail. The guard is too strong to defeat, there must be a way to sneak past, or maybe jump in"
    Utrigger="You fade into the crowds and put on the suit. Soon afterwards, You head to the gate in a colorful suit and mask. The guard moves away"
    Actions={"USE":{"COSTUME":Utrigger}, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":CASK}
    failsafe=None
    Events=[]
class Castle_Center():
    description="The main area of the Castle is populated with partiers, servants and guards.\nTo the East, you see servants mill about the Eastern Corridor.\nWestwards, you see very little precense with the exception of guardsmen.\nSouth, you see the entrance to the kings court...blocked by the largest Soldier you've ever seen! "
    isLocked=True
    UTrigger="With the plate of food in your hands, the guardsman moves back and allows you to pass"
    LockedMsg="S"
    Lockedprint="You find yourself looking into the kings court and seeing a bulk of steel armor in front of you. This is the biggest guard You've ever seen and the thickest armor as well. Prehaps, some scheadenfrued is needed to unlock the chamber"
    Actions={"USE":{"FOOD":UTrigger}, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":CASK}
    failsafe=None
    Events=[]
class Castle_Left():
    description="The Western side of the castle is barren, save for a few guards."
    isLocked=False
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":CASK}
    failsafe=None
    Events=[Castle_guard]
class Castle_Left_in():
    description="At a certain point, you notice the paths diverge. To the East, you see where the line of servants start as many serfs head towards the kitchens. South, however, appears to be a darker corridor."
    isLocked=False
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":CASK}
    failsafe=None
    Events=[]
class Kitchen():
    isLocked=True
    failsafe=None
    LockedMsg="I can just use this as a comment"
    description="You look into the kitchen to see an orgy of noise.\nSerfs preapare and move wines, breads and meats while, in the back, a routund chief is screaming in a foreign language.\n In front of him, you see a large plate of Food, decorated perfectly with spices and additional Gold Leaf at the side.\nYou can't help but notice the platter looks like it could use one more gold leaf decoration"
    Utrigger="You raise the gold Leaf over head the the cheif looks immeditaly. With unexpected speed he snatches it from your hands and places it on the plate.\n '💣︎⍓︎ ♑︎□︎●︎♎︎ ●︎♏︎♋︎♐︎✏︎ ⍓︎□︎◆︎ ♒︎♋︎❖︎♏︎ ⧫︎♒︎♏︎ ♒︎□︎■︎□︎❒︎⬧︎ □︎♐︎ ♌︎❒︎♓︎■︎♑︎♓︎■︎♑︎ ♓︎⧫︎ ⧫︎□︎ ⧫︎♒︎♏︎ 🙵♓︎■︎♑︎ 🙵♓︎■︎♎︎ ⬧︎♏︎❒︎♐︎📬︎ 💣︎♏︎✍︎ ♓︎🕯︎❍︎ ♑︎□︎■︎■︎♋︎ ♑︎□︎ ⬧︎●︎♏︎♏︎◻︎📬︎' he says as he points to the platter.\n Your windings is rusty but you can assume he thinks your a serf.\nWith that, he leaves the room and you are left with a platter to carry."
    USE={"GOLDLEAF":Utrigger}
    TALK="You pass by the shuffling serfs and try to talk to the chief.\nHe looks at you and says, '🕈︎♒︎♏︎❒︎♏︎ ♓︎⬧︎ ❍︎⍓︎ ♑︎□︎●︎♎︎ ●︎♏︎♋︎♐︎✏︎!' to which you say 'Pardon?' to which he replies,'☝︎□︎●︎♎︎ ●︎♏︎♋︎♐︎!!!!' You back off after this riviting conversation." 
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":TALK}
    Events=[]
class Wizard_Tower_Ent():
    description="You reach the end of the hallway to see a sprialing staircase in front of you.Unfortunatley, it appears the stairs are covered in somthing...slimey"
    isLocked=True
    UTrigger="Using the power of MAGIC! You cast a spell to dry the sheened stairs, It appears you can go up it now"
    LockedMsg="U"
    Lockedprint="Look look up the stairs and begin to walk up. To your surprise, you fall down immeditatley!Looking up, you see a shimmering sheen cover the stairs. You might need to see a wizard..."
    Actions={"USE":{"MAGIC":UTrigger}, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":CASK}
    failsafe=None
    Events=[]
class Court():
    description="You enter the Court of your target. A golden interior meets you as you see a crowd of people galavanting and celebrating.\n At the center of the commotion sits the kings, who you catch chinking his cup with...your Master?!"
    isLocked=False
    Betrayal="As you raise your voice to speak, a knife swipes your face on the right.\n'There he is!' Cries your master, 'That is the would-be Assasin!' You watch as she touches goblets with the king as the guards swarm you..."
    Vengence="You are able to drop the platter onto the table before a knife stabs you in the hand.\nYou look up to see the smiling face of your master as she turns towards everyone.'This right here is the would be ass....' Her voice cuts off as she sees the king slumped over in his food, Dead. You begin to laugh as the guards swarm you..."
    Usage={"FOOD":Betrayal, "POI_FOOD":Vengence}
    Actions={"USE":Usage, "PICKUP":PICKUP, "TALK":Betrayal,"ATTACK":ATTACK,"ASK":CASK}
    failsafe=None
    Events=[]
class Castle_right():
    description="The left side of the castle is modest, walking by you are servants doing their duties. You Look southward to see down the hallway"
    isLocked=False
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":CASK}
    failsafe=None
    Events=[]
class Castle_right_in():
    description="As you continue deeper, you see an old picure embroidden with a golden portrait.\n In the picture, you see a monsterous demon being buffeted by an old man with a large rod with a star at it's end."
    isLocked=False
    items={"GOLDLEAF":Gold_Leaf}
    Actions={"USE":USE, "PICKUP":items, "TALK":TALK,"ATTACK":ATTACK,"ASK":CASK}
    failsafe=None
    Events=[Gold_Leaf]

class Over_Prison():
    description="There's not much here, but all you can hear are whispers coming from what appears to be below you."
    isLocked=False
    TALK="HELLO!? Your cry out into the darkness. You are met with nothing but a small voice:'Nothing...'"
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":CASK}
    failsafe=None
    Events=[]

class Prison():
    description="You wake from your hammer induced nap to find yourself in a stone Prison.\nA few people mill about but most simply lay along the walls, giving up and awaiting death.\nLooking to the East, you see a room with blood training from it and a northern passage smells like true death.\nAdditioanlly, as you look southward to the sound of running water you see an old face: your contact!"
    isLocked=False
    TALK="Heading over towards your contact, you catch him turning and seeing you. His eyes darken and he looks down sullen.'They've got you as well huh? The Lady that was next to the king backstabbed your entire organisation.'\n 'BUT' he looks up quickly, 'You cannot fail this! Listen, i know a secret way out through the stream, all you need to do is USE ABBACADABA and a door will open. You'll most likely find the king and his goons in the woods somewhere.' He tries to continue talking but the guards see him and begin dragging him off. He looks back at you and nods."
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":PASK}
    failsafe=None
    Events=[]

class Torture():
    description="Evil works this place, and your an assasin. What you see before you is a room meant for...Interrogations. As you walk the room, you hear whispers and screams closeby."
    isLocked=False
    TALK="You try and talk back to the whispers but all you get back is laughter."
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":PASK}
    failsafe=None
    Events=[]

class Corpse():
    description="As you walk northern, you are greated to the stench of death. It appears this is the prisons mourge and they have a resident. \n A half decayed man lays on a steel slate. You can barely recognize who it is util you see a set of keys next to him. It appears to be the keymaster"
    isLocked=False
    TALK="You utter a small prayer for the keymaster"
    Actions={"USE":USE, "PICKUP":{"KEYRING":KeyRing}, "TALK":TALK,"ATTACK":ATTACK,"ASK":PASK}
    failsafe=None
    Events=[KeyRing]

class Escape(): 
    description="You enter a more earthen room. Looking at the ground, you see a small stream passing under the prison floors and past a grate leading to the outside world."
    isLocked=True

    LockedMsg="S"
    Lockedprint="It would be embarrising if it were that easy. No, the stream is too shallow for you to swim in and, aside from that, the rest of the room is blank wall. If only someone knew a way..."
    failsafe=None
    UTrigger="ABBACADABA! You say with a quiet voice. Your attempts at stealth are in vain for, as you say the words the earthen wall begins to flicker and fade, becoming somewhat of a translucent carpet. You feel like the room may look the same, but at least now you know you can pass the wall!"
    Actions={"USE":{"ABBACADABA":UTrigger}, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":PASK}
    Events=[Prison_guard]

class Wizard_Tower():
    description="After what appears to be an eternity, you ascend into a large cicular room covered in cobwebs.The ceiling is covered in stars and the walls filled with strings of spells. \nEastward lies another room and North a smaller one. "
    isLocked=False
    Actions={"USE":USE, "PICKUP":{"ROD":Rod_Of_Babble}, "TALK":TALK,"ATTACK":ATTACK,"ASK":DASK}
    failsafe=None
    Events=[Rod_Of_Babble]

class Altar():
    description="You see a multitude of written spells on the wall leading up to what appears to be an altar. At the center, lays a large statue with a star shaped hole in it."
    isLocked=False
    Utrigger="You press the star into it's whole and the entire room lights up. Red light now floods the air and you can hear a voice. 'Child, release me so that i may go back to my plane. Do so and i shall grant you my favor....'"
    Actions={"USE":{"STAR":Utrigger}, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":DASK}
    failsafe=None
    Events=[]
class Vault():
    description="You enter what appears to be a study area. Looking around, you see a vault built into the wall. Locked by a code, you look around the room once more and see an ancient script along the wall. Almost physically impossible to read."
    isLocked=True
    LockedMsg="ROD"
    Decipher="Magic flow forth and you read the inscription: Name The sole thing the wealthy would want from a wretch and take the reward to my chamber"
    Deciphered="You remain absolutly quiet, wondering what it all meant, when you hear a small click as the vault opens quietly"
    Actions={"USE":{"MAGIC":Decipher, "NOTHING": Deciphered} , "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":DASK}
    failsafe=None
    Events=[]
class Spring():
    description="Feeling the wall, You stumble upon a loose brick. pressing it, the wall gives way and you are revealed an area of untold beauty. By chance, you have found a spring of healing within such an evil place."
    isLocked=False
    Utrigger="Mearly dropping your toes within the spring fills you with life and health"
    Actions={"USE":{"SPRING", Utrigger}, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":"Why is this here? Prehaps the king's family was not always so evil..."}
    failsafe=None
    Events=[]
class Blade():
    description="Following the whispers, you find an attic like opening in the chamber. Heading upwards, you see a small room caked in blood with, in what appears to be a stone body, a black blade with a golden hilt."
    isLocked=False
    Actions={"USE":USE, "PICKUP":{"BLACKBLADE":Black_Blade}, "TALK":TALK,"ATTACK":ATTACK,"ASK":"Why is this here? You ask. Maybe the King's line is evilier than you thought..."}
    failsafe=None
    Events=[]
class Ritual():
    description="Entering the woods, you move through the thick vines and bramble. Eventually, you see just West of where you are a circle with stones surrounding it. Within it, several figures stand in a circle chanting."
    isLocked=True
    failsafe=None
    LockedMsg="W"
    Lockedprint="In an attempt to enter the circle, you are bounced back by a magical force. When you recover, you note the skies reveal a cloudy figure, with a cloudy hand covering the stone circle.Prehaps you need to find a way to dispell a spirit"
    Usage="Looking up, you see the cloud shaking and eventually dissipate. There's no turning back now."
    Actions={"USE":{"GOD":Usage}, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":DASK}
    Events=[]
class RitualSite():
    description="You walk into earthen grounds, quenched with blood.\nWhile the sacrifices have happenend, no evil will come from this.\nYour targets lay in front of you, whimpering. You make quick work of felling your targets, what with your abilities honed to the teeth.\nYet, your master is nowhere to be seen"
    isLocked=False
    failsafe=None
    TALK="'Where are you hiding....' you call out into the shadows to find the traitor. All that you hear back is wind going North"
    USE="You feel the dirt around you. Some have been upheaved going North"
    PICKUP="Feeling the bodies, you notice that all their purses have been cut, You then look and find a trail of coins going North."
    ATTACK="There's nothing here to attack, not yet..."
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":ATTACK,"ASK":DASK}
    Events=[]
class END():
    description="Trudging east, you end up on a side road heading out of the kingdom.\nYou see your master loading a cart full of treasure.'I never thought you would make it this far' she says, as if she sensed your precense.\n'I must have trained you well, but this ends NOW!' she turns and unsheaths her dagger.\n"
    isLocked=None
    theEnd="Honed is you blade, you do not feel it hesitate in finishing off the traitor. After the deed is done, You simply sit down and think about what's happened. Maybe it's time to retire."
    Actions={"USE":USE, "PICKUP":PICKUP, "TALK":TALK,"ATTACK":{"MASTER":theEnd},"ASK":"Why? you ask. Your master turns to you and says, 'There is no honor amoungst theives and killers. He offered me riches, I offered him an organization. You should've known better to trust me.After all, I thought you to trust no one."}
    failsafe=None
    Events=[]

#METHODS: Note that a few options were hardcoded becuase it garuntees it works
def pickup(Player,items,x,choice):
    #print(Score)
    if (len(choice.split())>1):

        choice=choice.split()[1].upper()
        if (Player[0][1].Events):
            for ground in Player[0][1].Events:
                if (ground.type=="ITEM"):
                    if (choice==ground.name):
                        print(ground.pickup)
                        items.append(ground)
                        ground.held=True
                        return"0"
        for check in range(len(items)):
            if (choice== items[check].name and items[check].held ):
                print("You are already holding this")
                return "0"
        for itm in Player[0][1].Actions["PICKUP"]:
            if (choice.strip=="BLACKBLADE"):
                print(Player[0][1].Actions["PICKUP"][choice].pickup)
                items.append(Player[0][1].Actions["PICKUP"][choice])
                Player[0][1].Actions["PICKUP"][choice].held=True
                Score.points+=items[check].picp
                Player[0][1].description=Black_Blade.keyDesc
                return"0"
            #print(itm)
            #print(choice)
            if (choice==itm):
                print(Player[0][1].Actions["PICKUP"][choice].pickup)
                items.append(Player[0][1].Actions["PICKUP"][choice])
                Player[0][1].Actions["PICKUP"][choice].held=True
                Score.points+=items[check].picp
                if (Player[0][1].Actions["PICKUP"][choice].changeLocal):
                    if(Player[0][1].Actions["PICKUP"][choice].whereTo !=False):
                        choice = Player[0][1].Actions["PICKUP"][choice].whereTo
                        #print(choice)
                       
                        return  choice
                return "0"
  
        print("You cannot use that there")

    else:
       print("pickup what?")
       return "0"



    return "0"
def Inventory(items):
    print("You have: \n")
    for i in range( len(items)):
        print(items[i].name)
    return "0"
def Use(Player, choice, items, Score,Health):
        #print(Score.points)
        if (len(choice.split())>1):
            choice=choice.split()[1].upper()

            if (choice=="POISON"):
                for h in range (len(items)):
                    if (items[h].name=="POISON"):
                        for k in range (len(items)):
                            if (items[k].name=="FOOD"):
                                print(PoisonFood.pickup)
                                items.append(PoisonFood)
                                Score.points+=items[k].usepoints
                                items.remove(Poison)
                                return "0"
            for itm in (Player[0][1].Actions["USE"]):

                if itm !=None:
                    if (choice=="GOD"):
                        Ritual.isLocked=False
                        print(Player[0][1].Actions["USE"]["GOD"])
                        return "0"
                    if(choice=="SPRING"):
                        Health=100
                        MC.healed=True
                        Player[0][1].description=healing.keyDesc
                        Score.points+=healing.usepoints
                        print(healing.pickup)
                        return "0"
                    if (choice==Passcode or choice== Riddle):
                        print(Player[0][1].Actions["USE"][choice])
                        if (choice==Riddle):
                            Player[0][1].description="You enter what appears to be a study area. Looking around, you see a vault built into the wall. Locked by a code, you look around the room once more and see an ancient script along the wall. Almost physically impossible to read."
                            Player[0][1].Actions={"USE":USE, "PICKUP":{"STAR":Star_Of_Babble}, "TALK":"The air here makes it hard to even talk", "ATTACK":ATTACK}
                            Score.points+=100
                        return "0"
                    elif (choice==MgWords):
                        print(Player[0][1].Actions["USE"][choice])
                        Score.points+=20
                        Player[0][1].isLocked=False
                    elif (choice==Rod_Of_Babble.name):
                        Score.points+=100
                        print(Player[0][1].Actions["USE"][choice])
                        items.append(Vanished)
                        items.remove(Rod_Of_Babble)
                        return"0"
                    for check in range(len(items)):
                        if (choice== items[check].name ):
                            if (items[check].changeLocal==True):
                                if (items[check].whereTo==False):
                                    print(Player[0][1].Actions["USE"][choice])
                                    choice = items[check].bomb
                                    print(choice)
                                    Player[0][1].description=items[check].keyDesc
                                    if items[check].hasMor:
                                        Player[0][1].Actions=items[check].Actions
                                    Score.points+=items[check].usepoints
                                    return  choice
                            if (items[check].name=="FOOD"):
                                items[check].changeLocal=True
                                print(Player[0][1].Actions["USE"][choice])
                                Player[0][1].isLocked=False
                                Castle_Center.description="The main area of the Castle is populated with partiers, servants and guards.\nTo the East, you see servants mill about the Eastern Corridor.\nWestwards, you see very little precense with the exception of guardsmen.\nSouth, you see the entrance to the kings court. " # This is to ensure it changes 
                                Score.points+=items[check].usepoints
                                return "0"
                            if(items[check].name=="POI_FOOD"):
                                print(Player[0][1].Actions["USE"][choice])
                                Score.points+=items[check].usepoints
                                return False
                            print(Player[0][1].Actions["USE"][choice])
                            Player[0][1].isLocked=False
                            Player[0][1].description=items[check].keyDesc
                            if items[check].hasMor:
                                Player[0][1].Actions=items[check].Actions
                            Score.points+=items[check].usepoints
                            if (items[check].disposable):
                                items.remove(items[check])
                            return "0"
                    else:
                        print("That's actually a good idea. Now, if only you had that")
                        return "0"
            print("You cannot use that there")

            return "0"
        else:
            print("Use What")
            return "0"
def Talk(Player):
    print(Player[0][1].Actions["TALK"])
    return "0"
def Look(Player, item, choice):
    if (len(choice.split())>1):
        choice=choice.split()[1].upper()
        for search in range (len(item)):
            if (choice.strip()==item[search].name):
                print(item[search].onspot)
                return "0"
    else:
        print(Player[0][1].description)
        return "0"
def Examine(items, choice):
    if (len(choice.split())>1):
        choice=choice.split()[1].upper()
        for search in range (len(items)):
            if (choice.strip()==items[search].name):
                print(items[search].examine)
                return "0"
    else:
        print("Examine what? You can examine surroundings with just LOOK")
        return "0"
def Ask(Player):
    print(Player[0][1].Actions["ASK"])
    return "0"
def Attack(Player, choice, Game_state,Enemies,Health):
    Battle=True
   
    if (len(choice.split())>1):
        choice=choice.split()[1].upper()
        for a in Player[0][1].Actions["ATTACK"]:
            if (a==choice):
              if (MC.Healed):
                  print("The battle rages. You match her jab for jab, slash for slash.\n But in the end, Endurance was on your side and the traitor falls to your feet. ")
                  print(END.theEnd)
                  return False
              elif (Black_Blade.held):
                  print("With one clean strike, your masters blade is chopped into two pieces by your new shiny weapon.")
                  print(END.theEnd)
                  return False
              else:
                  death=3
                  while(death>0):
                     combat=input("You square off! You can PUNCH, KICK or THROW. else, you could just use a weapon...")
                     if (death==3):
                         print("Try as you'd like, a master is still a master. You are thrown back fatigued, but keep trying!")
                         death-=1
                     elif(death==2):
                         print("another attempt sends you sprawling backwards.'Oh? is that all my failure of a student can muster?' says your master as she approaches with knives out. You can feel the magic surging in you...")
                         death-=1
                     elif(death==1):
                         print("Even if you tried to prepare magic, you were too slow and find yourself pinned and on death's doorstep.\nBut, if you're going down...\n Magic begins surging out of your body.\nAt least, you'll take the traitor with you...\nOne large explosion of mana is seen that night as your tale goes into legend.\nTHE END.")
                         death-=1
                  return False

        for che in Enemies:
          if (choice==che.name):
             while(Battle):
               combat=input("You square off! You can PUNCH, KICK or THROW. else, you could just use a weapon...")
               combat=combat.upper().replace(" ","")
               if ( combat=="USEKNIFE" and Knife.held or combat=="USEBLACKBLADE" and Black_Blade.held):
                   print("Using you knife, you put a swift end to this brawl")
                   che.defeated=True
                   Player[0][1].Events.append(che)
                   Enemies.remove(che)
                   Battle=False
               elif (combat=="PUNCH"):
                    atk=random.randint(0,10)
                    if (atk-che.chance<=0):
                        print ("HIT! You lay a haymaker onto the guard!")
                        che.health-=1
                        if che.health==0:
                            print("The guard succumbs to his injuries and falls down. Your not sure if their dead but you can't imagine them getting back up.")
                            che.defeated=True
                            Player[0][1].Events.append(che)
                            Enemies.remove(che)
                            Battle=False
                    else:
                        print("MISS! You punch misses and you are open! The guard strikes!")
                        atk=random.randint(0,10)
                        if (atk-che.chance>=0):
                            print ("The guard lays out a strike, but misses.")
                        else:
                            print("You take a stab from the guard!")
                            Health-=che.damage
                            if (Health<=50 and Health>25):
                                print("You're feeling dizzy")
                            elif(Health<=25 and Health>0):
                                print("Your breathing heavliy. You've lost a lot of blood")
                            elif (Health<=0):
                                print("You've tried to continue, but you've become too weak at this point. You pass out and the last thing you see is a swarm of guards...\n GAME OVER")
                                Game_State=False

               elif (combat=="KICK"):
                    atk=random.randint(0,10)
                    if (atk-che.chance<=0):
                        print ("HIT! You land your foot straight into the guards jaw!")
                        che.health-=1
                        if che.health==0:
                            print("The guard succumbs to his injuries and falls down. Your not sure if their dead but you can't imagine them getting back up.")
                            che.defeated=True
                            Player[0][1].Events.append(che)
                            Enemies.remove(che)
                            Battle=False
                    else:
                        print("MISS! You kick misses and you are open! The guard strikes!")
                        atk=random.randint(0,10)
                        if (atk-che.chance>=0):
                            print ("The guard lays out a strike, but misses.")
                        else:
                            print("You take a stab from the guard!")
                            Health-=che.damage
                            if (Health<=50 and Health>25):
                                print("You're feeling dizzy")
                            elif(Health<=25 and Health>0):
                                print("Your breathing heavliy. You've lost a lot of blood")
                            elif (Health<=0):
                                print("You've tried to continue, but you've become too weak at this point. You pass out and the last thing you see is a swarm of guards...\n GAME OVER")
                                Game_State=False
               elif (combat=="THROW"):
                    atk=random.randint(0,10)
                    if (atk-che.chance<=0):
                        print ("HIT! You find a smooth rock and, with an precise hand, land a rock into the eye of the guard!")
                        che.health-=1
                        if che.health==0:
                            print("The guard succumbs to his injuries and falls down. Your not sure if their dead but you can't imagine them getting back up.")
                            che.defeated=True
                            Player[0][1].Events.append(che)
                            Enemies.remove(che)
                            Battle=False
                    else:
                        print("MISS! You throw a rock but misses and you are open! The guard strikes!")
                        atk=random.randint(0,10)
                        if (atk-che.chance>=0):
                            print ("The guard lays out a strike, but misses.")
                        else:
                            print("You take a stab from the guard!")
                            Health-=che.damage
                            if (Health<=50 and Health>25):
                                print("You're feeling dizzy")
                            elif(Health<=25 and Health>0):
                                print("Your breathing heavliy. You've lost a lot of blood")
                            elif (Health<=0):
                                print("You've tried to continue, but you've become too weak at this point. You pass out and the last thing you see is a swarm of guards...\n GAME OVER")
                                Game_State=False
        if (Battle):
            print("You cannot find that enemy")
            return "0"


                    
    else:
        print("who are you fighting?")
        return "0"

    return "0"
def drop(Player, choice, items):
        if (len(choice.split())>1):
            choice=choice.split()[1].upper()
            for i in items:
                if (i.name==choice):
                    if (i.droppable):
                        i.held=False
                        Player[0][1].Events.append(i)
                        print(i.drop)
                        items.remove(i)
                        return"0"
                    else:
                        print("This...Is a bit too important to drop")
                        return"0"
        else:
            print("drop what?")
            return"0"

def main():
    items=[MAGIC]
    Enemies=[]
    items.append(Masters_Message)
    numitms=1
    Health=100
   

    BoardState={"Commence": [("",Commence), ("YES", Intro)],
                "Intro":[("", Intro), ("N", Old_man),("U", Upstairs),("S",Town_Center)],
                "Old_man":[("", Old_man), ("S", Intro)],
                "Upstairs":[("",Upstairs),("N", Town_Center)],
                "Town_Center":[("",Town_Center), ("E", Town_East), ("W",Town_West), ("S", Castle_Bridge),("N",Intro)],
                "Town_East":[("",Town_East),("N",Alley),("W",Town_Center),("E",Wizard)],
                "Alley":[("",Alley), ("S",Town_East)],
                "Wizard":[("",Wizard),("W",Town_East)],
                "Town_West":[("",Town_West),("E",Town_Center),("W",Forest)],
                "Forest":[("",Forest),("E",Town_West), ("U",Castle_right),("N",Ritual)],
                "Castle_Bridge":[("",Castle_Bridge), ("N",Town_Center),("S",Castle_Center)],
                "Castle_Center":[("",Castle_Center), ("N",Castle_Bridge),("S",Court),("E",Castle_Left),("W",Castle_right)],
                "Court":[("",Court),("ATTACK", Prison)],
                "Castle_right":[("",Castle_Left),("W", Spring),("S",Castle_right_in),("E",Castle_Center)],
                "Castle_right_in":[("",Castle_right_in),("N",Castle_right),("S", Wizard_Tower_Ent)],
                "Wizard_Tower_Ent":[("",Wizard_Tower_Ent), ("U",Wizard_Tower),("N",Castle_right_in)],
                "Castle_Left":[("",Castle_right),("W",Castle_Center),("S",Castle_Left_in)],
                "Castle_Left_in":[("",Castle_Left_in),("N",Castle_Left),("E",Kitchen),("S",Over_Prison)],
                "Kitchen":[("",Kitchen),("W",Castle_Left_in)],
                "Over_Prison":[("",Over_Prison),("N",Castle_Left_in)],
                "Prison":[("",Prison),("E",Torture),("N",Corpse),("S",Escape)],
                "Torture":[("",Torture), ("W",Prison),("U", Blade)],
                "Corpse":[("",Corpse),("S",Prison)],
                "Escape":[("",Escape),("D",Forest)],
                "Blade":[("",Blade),("D",Torture)],
                "Spring":[("",Spring),("E",Castle_right)],
                "Wizard_Tower":[("",Wizard_Tower),("N",Altar),("E",Vault),("D",Wizard_Tower_Ent)],
                "Altar":[("",Altar),("S",Wizard_Tower)],
                "Vault":[("",Vault),("W",Wizard_Tower)],
                "Ritual":[("",Ritual),("W",RitualSite),("S",Forest)],
                "RitualSite":[("",RitualSite),("E",Ritual),("N",END)],
                "END":[("",END)]}
    choice=""
    Game_State=True
    Zone="Commence"
    found=False
    special=False
    Player=BoardState[Zone]
    print(Player[0][1].description)

    while(Game_State):
        found=False
        special=False
        choice=input("Please enter your next choice here>" )
        #print(Player[0][0])
        if not choice=="":
            if (choice.upper().split()[0]=="DROP"):
                choice= drop(Player, choice, items)
                found=True
            elif (choice.upper().split()[0]=="ASK"):
                choice= Ask(Player)
                found=True 
            elif (choice.upper().split()[0]=="EXAMINE"):
                choice=Examine(items, choice)
                found=True
            elif (choice.upper().split()[0]=="ATTACK"):
                choice= Attack(Player,choice, Game_State,Enemies,Health)
                found=True
            elif (choice.upper().split()[0]=="TALK"):
                choice= Talk(Player)
                found=True
                special=True
            elif (choice.upper().split()[0]=="PICKUP"):
                choice= pickup(Player, items, numitms,choice)
                found=True
                special=True
            elif (choice.upper().strip()=="INVENTORY"):
                choice=Inventory(items)
                found=True
            elif(choice.upper().strip()=="QUIT"):
                Game_State=False
                break
            elif (choice.upper().split()[0]=="USE"):
                choice=  Use(Player, choice, items, Score,Health)
                found=True
            elif (choice.upper().split()[0]=="LOOK"):
                choice= Look(Player,items,choice)
                found=True
                special=True
            if(choice==False):
                Game_State=False
                break
            elif (found and choice!="0"):
                Zone= choice
                Player=BoardState[Zone]


            else:
                for search in range(len(Player)):
                    if choice.upper()==Player[search][0]:
                        if Player[0][1].isLocked:
                            if Player[0][1].LockedMsg==Player[search][0]:
                                print(Player[0][1].Lockedprint)
                                found=True
                                break
                            elif Player[0][1].failsafe!=None:
                               Zone=str(Player[search][1]).split(".")[1].split("'")[0]
                               Player=BoardState[Zone]
                               found=True


                               break

                       # print("you made it in")
                        Zone=str(Player[search][1]).split(".")[1].split("'")[0]
                        Player=BoardState[Zone]


                        found=True
                        break
            
            if (found and not special):
                print(Player[0][1].description)
                if (Player[0][1].Events):
                    #print (Player[0][1].Events)
                    for extra in Player[0][1].Events:
                        #print(extra)
                        if extra.type=="ITEM" and extra.droppable:
                            if not extra.held:
                                print(extra.onground)

                        elif not extra.following:
                            print(extra.onspot)
                            extra.following=True
                            Enemies.append(extra)
                            Player[0][1].Events.remove(extra)
                        elif extra.defeated:
                            print(extra.dmessage)
                if (len(Enemies)>0):
                    for dam in Enemies:
                        if not dam.following:
                            Enemies.remove(dam)
                        else:
                            print(dam.follow)
                            if (dam.grace):
                                print("You are able to dodge the blow, but you fear further attacks")
                                dam.grace=False
                            else:
                                print("The weapon grazes you!")
                                Health-=dam.damage
                                if (Health<=50 and Health>25):
                                    print("You're feeling dizzy")
                                elif(Health<=25 and Health>0):
                                    print("Your breathing heavliy. You've lost a lot of blood")
                                elif (Health<=0):
                                    print("You've tried to continue, but you've become too weak at this point. You pass out and the last thing you see is a swarm of guards...\n GAME OVER")
                                    Game_State=False
            elif (not found):
                print("I Don't know what you said")
            print("")
            print(" CLOAK AND DAGGER                       SCORE: ", Score.points)
        
    print("AND SO ENDS YOUR RUN OF CLOAK AND DAGGER. Total points:",Score.points)
    rank={"Initiate:":(1,"Inexpirienced, probably not the best canadate"),"Hitman:":(500,"Rough, but you get the job done"),"Ghost:":(1000,"Highly effective, you've made sure all your bases have been checked"), "Legend:":(2000, "VENI, VIDI,VICI! You've come of this not as a meer assasin but as a magical legend!")}
    for v in rank:
        #print(rank[v])
        if (Score.points/rank[v][0]>=1):
            print("RANKING: ",v,rank[v][1])
            break

        

       



if __name__ == "__main__":
        main()
