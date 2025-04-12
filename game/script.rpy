define sm = Character("Spider-Man")
define t = Character ("Teléfono", color= "#aaaaaaff")
define im = Character ("Iron-Man", color= "#ff0000")
define dv = Character ("Duende Verde", color= "#00ff00")
define hg = Character ("Hermano Gemelo")
define n = Character ("Narrador", color= "#ffffff")
label start:

    scene opening scene

    sm "Ah…"

    sm "Qué maravillosa vista de la ciudad"

    play sound "ringing.mp3"

    t "RING, RING, RING"

    show exclamation_mark at Transform(zoom=0.35, xalign=0.595, yalign=0.5)
    show question_mark at Transform(zoom=0.25, xalign=0.625, yalign=0.5)

    sm "¡¿Qué es eso?!"

    hide question_mark
    hide exclamation_mark

    sm "Oh, solo es un mensaje de Tony Stark"

    sm "Espera un momento…"

    show question_mark at Transform(zoom=0.25, xalign=0.6075, yalign=0.5)

    sm "¿Por qué me estará mandando un mensaje?"

    hide question_mark

    sm "Supongo que puede ser algo importante"

    sm "Mejor lo leo antes de que algo explote"

    show screen tony_message
    $ renpy.pause(0.1, hard=False)

    sm "Parece que es importante"

    show question_mark at Transform(zoom=0.25, xalign=0.6075, yalign=0.5)

    sm "¿Debería aceptar la misión?"
    
    hide question_mark

    menu:

        "Sí":
            sm "Hora de ponerse a trabajar"
            $ renpy.movie_cutscene("spider-man_song.webm")
            jump mission

        "No":   
            sm "De todas maneras, quería descansar"

            show question_mark at Transform(zoom=0.25, xalign=0.6075, yalign=0.5)

            sm "¿Qué es es-"

            hide question_mark

    return

label mission:
    
    scene mission

    show question_mark at Transform(zoom=0.35, xalign=0.2075, yalign=0.235)

    sm "¿Qué pasó?"

    hide question_mark

    im "Invadieron el edificio de Oscorp, necesitamos tu ayuda"

    show question_mark at Transform(zoom=0.35, xalign=0.2075, yalign=0.235)

    sm "¿Los ayudo?"

    hide question_mark

    menu:

        "Sí":

            show exclamation_mark at Transform(zoom=0.50, xalign=0.2075, yalign=0.235)

            sm "¡Vamos!"

            hide exclamation_mark

            sm "Tal vez encuentro a mi gemelo perdido o algo así, ja ja"
            $ renpy.movie_cutscene("spider-man_song.webm")
            jump end

        "Ir al cine":   

            show exclamation_mark at Transform(zoom=0.50, xalign=0.2075, yalign=0.235)

            sm "¡Siii!"

            hide exclamation_mark

            $ renpy.movie_cutscene("spider-man_song.webm")
            $ renpy.movie_cutscene("spider-man_song.webm")
            $ renpy.movie_cutscene("spider-man_song.webm")

            sm "Aunque el mundo explote, todo valió la pena..."

    return

label end:

    scene green goblin encounter

    dv "Decidiste venir..."

    dv "Te voy a revelar algo que nunca esperaste..."

    scene black
    play sound "vine-boom.mp3"

    dv ""

    scene green goblin plot twist

    hg "Soy tu hermano gemelo."

    $ renpy.movie_cutscene("spider-man meme scene.webm")

    scene black

    n "La historia continuara..."

    return
