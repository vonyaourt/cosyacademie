
image skip_very_smallI = im.FactorScale("Assets/skip_btn_idle.png", .10)
image skip_very_smallH = im.FactorScale("Assets/skip_btn_hover.png", .10)

screen skip_von_very_small:
    vbox :
        imagebutton:
            idle "skip_very_smallI" 
            hover "skip_very_smallH"
            action [Skip()]

image skip_smallI = im.FactorScale("Assets/skip_btn_idle.png", .25)
image skip_smallH = im.FactorScale("Assets/skip_btn_hover.png", .25)

screen skip_von_small:
    vbox :
        imagebutton:
            idle "skip_smallI" 
            hover "skip_smallH"
            action [Skip()]

image skip_mediumI = im.FactorScale("Assets/skip_btn_idle.png", 0.5)
image skip_mediumH = im.FactorScale("Assets/skip_btn_hover.png", 0.5)

      
screen skip_von_medium:
    vbox :
        imagebutton:
            idle "skip_mediumI" 
            hover "skip_mediumH"
            action [Skip()]


image skip_bigI = im.FactorScale("Assets/skip_btn_idle.png", 0.75)
image skip_bigH = im.FactorScale("Assets/skip_btn_hover.png", 0.75)

screen skip_von_big:
    vbox :
        imagebutton:
            idle "skip_bigI" 
            hover "skip_bigH"
            action [Skip()]

screen skip_von_huge:
    vbox :
        imagebutton:
            idle "Assets/skip_btn_idle.png"
            hover "Assets/skip_btn_hover.png"
            action [Skip()]

label club_rando:

    play music wonderful    

    scene black
    image name_club_rando = Text("{size=80}Chapitre 6 :\nLe club de Rando", text_align=0.5)
    window hide
    show name_club_rando:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide name_club_rando
    window auto

    scene rando with fade

    show Von PoseSpeciale Sourire Yeuxfermes
    von "C’est bon, tout le monde est là ? Alors bienvenue au club de randonnée !"
    von "Ici on marche pour se détendre, entretenir le corps mais aussi cultiver l’esprit."
    von "Un seul mot d’ordre : bonne humeur obligatoire."
    pov "Et on va où exactement ?"
    show Von PoseSpeciale Sourire Yeuxfermes
    von "[povname] tu vois le haut de cette montagne ?"
    von "Et bien c’est là que nous allons, ce sera l’affaire d’une heure ou deux."
    von "Et pendant que nous marchons, on pourra en profiter pour étudier la nature et réviser l’histoire de nos régions…"
    show Foulk PoseGauche Sourire Yeuxfermes at left with dissolve
    foulk "Et on pourra récolter des plantes sauvages !"
    show Von PoseDroite Colere
    von "Foulk, je t’ai déjà dit que le club de randonnée n’était pas destiné à remplacer le club d’herboristerie !"
    show Foulk PoseGauche Triste
    foulk "C’est pas de ma faute si Lock l’a fait fermer !"
    von "Ah et c’est la faute de qui alors ?"
    foulk "De dieuv’, il a menacé de crever des peuneus si on touchait à ses champis…" 
    show Foulk PoseGauche Sourire Rougit
    foulk "Mais bon, grâce à ton club de rando on peut enfin reprendre la construction de notre \"herbier\" sans se faire déranger par les fli… les pions."
    show Von PoseDroite Degoute
    von "Hmmpf… ça ne sert à rien que je vous demande de vous arrêter j’imagine. D’ailleurs, il est où dieuv ?"
    show Foulk PoseGauche Sourire
    foulk "Je crois qu’il est déjà en train de cueillir des champis dans la forêt, on le trouvera en chemin."
    pov "A propos de chemin, il y a un éboulement qui nous barre la route sur le sentier, là…"
    hide Foulk
    hide Von
    show Von Standard Badboy at center
    von "Vous en avez assez de cette bande de rocailles ?"
    show Von PoseSpeciale Badboy
    von "Et bien on va vous en débarrasser." 
    pov "Mais pourquoi il dit \"vous\" en parlant de lui ?"
    show Foulk PoseGauche Sourire at left
    foulk "Ne t’inquiète pas, au bout d’un moment tu n’y feras plus gaffe. En attendant, il a vraiment dégagé la route, ce cong…"
    show Dieuvomi PoseSpeciale Colere at right
    dieuv "Qui a démoli mon barrage ? Il était là pour arrêter les cyclistes, que je puisse leur CREVER LES PEUNEUS !"
    show Von Standard Colere
    von "C’est moi dieuv ! On est en pleine randonnée là !"
    von "Déjà que foulk nous ralentit en ramassant la moitié des fleurs sauvages sur le bas-côté, faut que tu crées des éboulements par-dessus le marché !"
    show Dieuvomi PoseGauche Sourire Yeuxfermes Rougit
    dieuv "Désolé, je ne savais pas que vous passeriez par ici, si j’avais su je serais venu dès le début avec vous, c’est le dernier club qui me permet de récolter mes psilocybes."
    show Von PoseSpeciale Colere Rougit
    von "Je vous ai déjà dit d’arrêter de collecter des plantes pendant les randos !"
    show Foulk PoseSpeciale Sourire Yeuxfermes
    foulk "Et qu’est-ce qui te dérange là-dedans ? On se contente de s’en servir pour agrémenter notre terrasse, c’est prof Mickey qui nous l’a demandé."
    show Von PoseDroite Degoute
    von "Ce qui me dérange, c’est que vos plantes empestent à trois kilomètres et que vous n’arrêtez pas de hurler dès que vous trouvez le moindre truc qui a l’air comestible !"
    foulk "T’es en train de dire que ce qui te dérange c’est…"
    show Von PoseDroite Colere
    von "Parfaitement, l’odeur et le bruit !"
    show Dieuvomi Standard Sourire Yeuxfermes
    dieuv "WOW foulk REGARDE J’AI TROUVE UN CHAMPI, TAING’"
    show Von Standard Triste
    von "Allez les gars, le club de randonnée c’est pour marcher, mais c’est pas pour vos errements prophylactiques à base de pharmacopée hallucinogène…"
    show Foulk PoseGauche Badboy
    foulk "Heing ?"
    show Dieuvomi PoseGauche Badboy
    dieuv "Quoi ?"
    show Von Standard Sourire
    von "Le club de randonnée c’est surtout pour admirer les merveilles de notre terroir, la beauté de nos paysages ! C’est ressentir l’atavisme qui coule dans nos veines ! C’est vouloir défendre son patrimoine et ses valeurs !"
    foulk "Ah ouais, Jacques Atavisme, j’en ai entendu parler"
    hide Dieuvomi with dissolve
    hide Foulk with dissolve
    show Von BrasCroises Badboy at center
    von "Allez, passons aux choses sérieuses. C’est l’heure du… questionnaire d’histoire ! Vous ne croyiez tout de même pas que vous alliez vous en tirer sans vous cultiver !"


    python:
        von_monologue_tags = "{fast}"
    
    menu:
        von "Première question : où est né Jean II le Bon, roi de France de 1350 à 1364 ?"
        
        "A Blois, ville royale et d’une importance culturelle et historique majeure.":
            show Von PoseSpeciale Badboy
            von "Ce n’est pas la bonne réponse."

        "Au Mans, capitale des rillettes, c’est déjà pas mal.":
            show Von PoseSpeciale Sourire Yeuxfermes Rougit
            von "C’est la bonne réponse !"
    
    show Von BrasCroises Triste

    show screen skip_von_very_small

    von "Jean II Le Bon n’était malheureusement pas digne d’être né à Blois.[von_monologue_tags]"
    von "Il a été un mauvais roi, appauvrissant un royaume confronté à la peste et à la guerre contre les Anglais, perdant plusieurs batailles, notamment celle de Poitiers en 1356.[von_monologue_tags]"

    hide screen skip_von_very_small
    show screen skip_von_small

    von "C’est lors de cet événement qu’il est fait prisonnier, puis conduit à Londres où il mourra huit ans plus tard après être revenu en France et reparti en Angleterre pour verser la rançon demandée pour sa libération, cédant au passage un tiers du royaume.[von_monologue_tags]"
    von "Pendant la vacance du pouvoir, c’est le prévôt des marchands de Paris, Etienne Marcel, qui en tant que délégué du tiers état lors des états généraux convoqués en 1355, 1356 et 1357, devient le chef du mouvement réformateur, et donc à la tête de l’opposition au pouvoir royal.[von_monologue_tags]"


    hide screen skip_von_small
    show screen skip_von_medium    


    von "Ce qui lui vaudra la sienne, de tête. On se demande bien pourquoi, d’ailleurs, on nomme des stations de métro d’après ce genre de personnages, d’ailleurs, mais passons, Lorent Deustch, grand historien, a déjà fait un livre sur le sujet.[von_monologue_tags]"
    von "Je disais donc que Jean II Le Bon ne méritait pas d’être né à Blois. Blois est une ville d’importance, capitale du comté de Blois avant qu’elle ne soit intégrée au duché d’Orléans en 1397.[von_monologue_tags]"


    hide screen skip_von_medium
    show screen skip_von_big        

    von "De nombreuses personnalités y sont nées ou mortes, car la ville était un centre culturel majeur à la fin du Moyen-Age et à la Renaissance, comme le prouve son château.[von_monologue_tags]"
    von "Né des vestiges d’une forteresse, le château royal est aujourd’hui composé de trois ailes possédant chacun un style distinct :[von_monologue_tags]"
    
    hide screen skip_von_big
    show screen skip_von_huge

    von "L’aile Louis XII, roi de France né à Blois et admiré du peuple et des historiens...[von_monologue_tags]"
    von "L’aile François 1er, grand roi qui a souvent déplacé la cour au château de Blois...[von_monologue_tags]"
    von "Et l’aile Gaston d’Orléans, dans un style gothique typique du XVIIe siècle.[von_monologue_tags]"
    von "C’est un joyau architectural unique que chaque personne de goût se doit de visiter au moins une fois dans sa vie ![von_monologue_tags]"
    von "Un témoignage unique de la richesse d’une ville dont on dit qu’elle était tellement raffinée qu’elle était l’hôte de quarante-sept horlogers simultanément sous Gaston d’Orléans.[von_monologue_tags]"
    
    hide screen skip_von_huge
    menu:
        von "Quarante-sept, tu te rends compte ? C’est fou ! Mais d’ailleurs, en parlant d’horlogerie, quelle heure est-il ?"

        "...":
         jump after_skip
        
        "Voilà, je crois qu’on est enfin arrivés au sommet ! Qu’est-ce qu’on fait désormais, on redescend ?":
         jump after_skip

    label after_skip:
        show Von PoseDroite Sourire Yeuxfermes
        von "Non, attends, c’est l’heure d’enfiler nos doudounes, il fait froid !"
        show Foulk PoseGauche Degoute at left
        foulk "Elles sont bleues…"
        von "Parfaitement ! Et si vous croisez un troll d’ébène, dites-le-moi, on le reconduira à la frontière ensemble."
        pov "…"
        show Foulk PoseGauche Colere 
        foulk "C’est n’importe quoi !"
        show Dieuvomi PoseSpeciale Colere at right
        dieuv "C’est moyen malin tout ça ! Venez, on se casse !"

    hide Dieuvomi with dissolve
    hide Foulk with dissolve
    hide Von with dissolve

    innerpov "J'ai essayé tous les clubs qu'on m'a conseillé... Je vais retourner voir Metalice, elle aura suremment une idée !"

    jump conseil_eleves
    return