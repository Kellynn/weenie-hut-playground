# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Roxanne")
define b = Character("Boo")

transform boo_float:
    pos (0.6, 0.5)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bookstore

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show roxanne

    # These display lines of dialogue.

    r "Wow! What a beautiful bookstore"

    r "I could spend all day in here"

    hide roxanne

    "Roxanne meandered around the bookstore looking at every cover that caught her eye. There were books of all types, old and new. A true reader's paradise."

    "She happily browsed until she heard a sudden sound from underfoot. To her horror, she had stepped in a puddle of blood."

    show roxanne

    r "Aaaaahhh!!"

    r "I was looking for historical fiction, not a murder mystery!"

    "She looked around to try and ascertain where the blood came from. Underneath the table on her left was a body, completely still and bloody."

    "She looked around for anyone else in the store, but found herself completely alone."

    r "Um....hello? Are you ok?"

    "Nothing responded....but only for a moment."

    show roxanne at left

    show boo scared at boo_float

    b "Oh no!!"

    # This ends the game.

    return
