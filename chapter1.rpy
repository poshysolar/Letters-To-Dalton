image bg rylies_bedroom = "images/RyliesBedroom.jpg"
image bg rylies_bathroom = "images/RBathroom.jpg"
image bg staircase = "images/Staircase.jpg"
image bg kitchen = "images/Kitchen.jpg"
image bg FarmYard = "images/FarmYard.jpg"
image bg ChickenBG = "images/ChickenBG.jpg"
image bg PigPen = "images/PigPen.jpg"

image russell = "images/Russell.png"
image piper = "images/Piper.png"

define russell = Character("Russell", who_color="#c8c8c8", what_color="#ffffff")
define piper = Character("Piper", who_color="#c8c8c8", what_color="#ffffff")
define rylie = Character("Rylie", who_color="#c8c8c8", what_color="#ffffff")
define e = Character("Earl", who_color="#c8c8c8", what_color="#ffffff")

label start:
    scene bg rylies_bedroom
    with fade
    
    play music "audio/C1Audio.mp3" volume 0.35 loop fadein 5.0
    play sound "audio/BirdEffect.mp3" volume 0.5 loop
    
    "She’s awake before the alarm, and it’s not the peaceful kind of waking up."
    
    "More like being pulled up out of deep water, chest tight and eyes already open and staring at the ceiling before she even registers where she is."
    
    "{i}The dream again.{/i}"
    
    "She doesn't try to hold onto it. {i}She never does.{/i}"
    
    "She just breathes, slow and steady, and lets the images dissolve at the edges until they fade away completely."
    
    "She focuses on that sound until her heartbeat settles back to something reasonable."
    
    "She rolls over and reaches into the nightstand drawer, fingers finding the worn cover of her diary without needing to look."
    
    "She's been keeping it going on five months now."
    
    "Not out of boredom, but because the dreams kept coming back on a cycle, and she wanted to track it."
    
    "Look for the pattern. Find the thing that explains it."
    
    "She hasn't found it yet, but she keeps writing."
    
    "She opens to the current page and writes the date. {i}Just the date.{/i}"
    
    "Underneath it, three words:"
    
    "{i}the dream returned...{/i}"
    
    "She closes it, slides it back in the drawer, and lies there another minute listening to the morning settle in around her."
    
    "The light is coming through the thin curtains now, pale gold, laying itself across the wall of her small room."
    
    "She pulls the sheet over her face. It doesn't do much."
    
    "After a minute of knowing she’s awake and morning is already here, she sits up."
    
    "Feet hit the cool floor."
    
    "She rolls her shoulders once."
    
    stop sound  # Stops the looping BirdEffect.mp3
    
    scene bg rylies_bathroom
    with fade
    
    "The bathroom is small and plain, just exactly what it needs to be."
    
    "There's a cracked tile at the base of the sink that was already broken when she arrived."
    
    "She runs the water cold and washes her face first."
    
    "Cold water is the only thing that actually cuts through the fog the dream leaves behind."
    
    "Her uniform is on the hook behind the door where she put it the night before, plain work dress, housemaid apron folded over the top."
    
    "She dresses without rushing, making sure everything is tucked and right."
    
    "She takes her time with her hair, patting her afro into shape, getting it neat."
    
    "Brushes her teeth slow, rinses, and then finally looks at the mirror."
    
    "Her face is calm. It usually is."
    
    "Like calm means empty. Like calm means she isn't paying attention."
    
    "She lets them think that."
    
    "She turns off the light and heads for the stairs."
    
    scene bg staircase
    with fade
    
    "The third step creaks."
    
    "She skips over it without thinking, weight shifting before her foot even makes contact,"
    
    "the way she's done every single morning since her second week here."
    
    "The smell of coffee is already rising up from the kitchen."
    
    "She can hear the newspaper, the slow, deliberate sound of a page being turned."
    
    "Russell is already at the table."
    
    "She takes the last few steps down and turns toward the kitchen."
    
    stop music fadeout 2.0
    
    scene bg kitchen
    with fade
    
    show russell at center
    with dissolve
    
    "Russell sits at the head of the table, his newspaper spread flat, both big hands holding it down."
    
    "His coffee cup sits empty at his right."
    
    "He doesn't look up when she comes in, and she doesn't expect him to."
    
    hide russell
    show piper at center
    with dissolve
    
    "Piper is at the other end, chin propped in one hand,"
    
    "wearing the face she always wears in the morning like the day has already personally wronged her just by arriving."
    
    "She gives Rylie a quick, disinterested glance when she comes in, then looks back at the table."
    
    hide piper
    
    "Rylie crosses to the counter, picks up the coffee pot, and pours Russell's cup."
    
    "She sets it beside his hand without a sound."
    
    show russell at center
    with dissolve
    
    play sound "audio/RAudio01.mp3"
    russell "Mornin'."
    
    "Rylie gives a small nod and begins setting out the rest of the breakfast table."
    
    hide russell
    show piper at center
    with dissolve
    
    "Piper is dragging her spoon in slow, lazy circles inside her bowl"
    
    play sound "audio/PAudio01.mp3"
    piper "The chickens were loud half the night. Woke me up twice. I couldn't get back to sleep for an hour."
    
    "She says it like she’s filing a complaint, not to anyone in particular.... just letting it out"
    

    hide piper
    show russell at center
    with dissolve
    
    play sound "audio/RAudio02.mp3"
    russell "Chickens make noise, Piper. It's what they do."
    
    russell "You're not gonna grow up on a farm and act surprised every time an animal acts like an animal."
    
    hide russell
    show piper at center
    with dissolve
    
    play sound "audio/PAudio02.mp3"
    piper "I'm not surprised, I'm tired. There's a difference."
    
    piper "And it wasn't just regular noise... it was frantic, like something was wrong with them."
    
    hide russell
    show russell at center
    with dissolve
    
    play sound "audio/RAudio03.mp3"
    russell "If somethin' was wrong with 'em, Rylie woulda found it by now. Isn't that right."
    
    "He says it flatly, not quite a question"
    
    "He just expects the answer to be yes, so he doesn't bother inflecting it like he's waiting on one."
    
    rylie "I'll check on them first thing this morning, sir."
    
    play sound "audio/RAudio04.mp3"
    russell "See, Piper. You ought to worry about somethin' worth worrying about."
    
    "He takes a slow, satisfied sip of his coffee."
    
    hide russell
    show piper at center
    with dissolve
    
    play sound "audio/PAudio03.mp3"
    piper "It's not that serious, I just said I couldn't sleep—"
    
    hide piper
    show russell at center
    with dissolve
    
    play sound "audio/RAudio05.mp3"
    russell "And I just told ya it's handled. So that's the end of it."
    
    "He sets the cup back down and glances up just far enough to make sure the conversation is over."
    
    "Piper presses her lips together and goes back to her bowl."
    
    "Russell turns another page."
    
    play sound "audio/RAudio06.mp3"
    russell "Good and hot this mornin', Rylie. Thank ya."
    
    "Rylie gives a small nod."
    
    "She finishes at the table, moves to the back door, pulls on her work boots, and laces them up."
    
    hide russell
    show piper at center
    with dissolve
    
    "Behind her, Piper starts dragging that spoon again, slow and pointless,"
    
    hide piper
    with dissolve
    
    "Rylie steps outside."
    
    jump c2_scene