from random import choice




#sujetos

#no incluí género/pronombres no binarios (sea x o e) 
#porque me pareció una pesadilla agregarlo siendo que
#la mayoría sino todas las personas que hago referencia
#acá son hombres o mujeres

proper_m = ['Felipe Solá', 'Larreta', 'Roberto Navarro', 
    'Darío Sztajnszrajber', 'Luis Zamora', 'Samid', 'Javier Milei', 'Massa', 'Del Caño', 
    'Mauricio Macri', 'Jorge Lanata', 'Eduardo Feinmann', 
    'Aníbal Fernández', 'Alberto Fernández', 'Axel Kicillof', 
    'Nisman', 'Máximo Kirchner'
    ]

proper_f = ['Elisa Carrió', 'Mirta Legrand', 'Moria Casán', 'Ofelia Fernández', 
        'Susana Giménez', 'Myriam Bregman', 'Cristina Kirchner', 'Soledad Acuña', 
        'Patricia Bullrich', 'Eugenia Vidal', 'Gabriela Michetti'
        ]

past_proper_m = ['Juan Domingo Perón',  
        'el juez Bonadío', 'Hipólito Yrigoyen', 'Jorge Rafael Videla', 'Carlos Saul Menem', 'Fernando De la Rua', 
        'Néstor Kirchner'
        ]

past_proper_f = ['Eva Perón', 'Isabel Perón'
        ]

Colective_m = ['el feminismo', 'el frente de izquierda', 'el frente de todos', 
        'juntos por el cambio', 'el oficialismo', 'TN', 'c5n', 'el transactivismo', 
        'el progresismo', 'el feminismo radical', 'el patriarcado', 'el comunismo', 
        'el sindicalismo', 'el trotskismo', 'el anarquismo', 'el peronismo', 'el gobierno', 
        'el nuevo orden mundial', 'el Estado', 'el macrismo', 'el radicalismo', 
        'el capitalismo', 'el socialismo', 'el partido justicialista', 'el kirchnerismo', 
        'el oficialismo', 'el sector público', 'el sector privado'
        ]

Colective_f = ['la izquierda', 'la UCR', 'la casta política', 'la UADE', 
        'la CGT', 'la franja morada', 'la corte suprema', 'la comunidad LGBTTTQIA+', 
        'la burguesía', 'la oposición', 'la iglesia', 'la patria', 'la clase media', 
        'la clase trabajadora', 'la clase alta', 'la derecha', 'la nueva izquierda'
        ]

Plural_m = ['los piqueteros', 'los planeros', 
        'los inmigrantes', 'los libertarios', 'los provida', 'los narcos', 
        'los gays', 'los políticos', 'los troskos', 'los peronistas', 
        'los anarquistas', 'los macristas', 'los kirchneristas', 'los milicos', 
        'los machitos', 'los hombres cis heterosexuales', 
        'los grandes empresarios', 'los pequeños empresarios'
        ]

Plural_f = ['las feministas', 'las feminazis', 'las aborteras', 
        'las radfems', 'las prostitutas', 'las travas', 'las maricas', 'las trabajadoras sexuales'
        ]

Plural_Col_m = ["los movimientos sociales", "los bancos", "los sindicatos", "los partidos políticos"]

Plural_col_f = ["las pymes", "las grandes empresas", "las entidades financieras", "las petroleras", "las inmobiliarias"]

#inicio
choose = choice([proper_m, proper_f, Colective_m, Colective_f, Plural_m, Plural_f])
someone = choice(choose)
todobien = ['Todo bien con ', 'Me cae bien ', 'No soy fan de ']
todobiencon = choice(todobien) + someone + ", pero"

inicio_afirmacion = ['Creo que', 'Ahre que', 'Resulta que', 'Les recuerdo que', 
        'No es por parecer facho, pero', 'Como defensor de los derechos humanos, creo que',
         'Seguro me linchan por esto, pero', 
         'Seamos sinceros,', 'Es simple lógica,', 'voy a decir esto una sola vez,', 
         'A ver si lo entienden de una vez,', 'Aparentemente', 'estoy 100% seguro de que', 
         'lo peor de todo esto es que', 'es increible como nadie habla de que', 'La verdad salió a la luz,', 
         'Siempre supe que', 'No tengo dudas de que', 'No se olviden de que', 'Según un nuevo informe por un periodista independiente,', 
         'Okey, pero si te parás cinco segundos a pensarlo,', 'Esta confirmado que', 'Como ciudadano argentino no puedo callarme ante esto,', 
         'No se por qué nadie habla de que', 'Opinión políticamemte incorrecta:', 'Cada día estoy más seguro de que', 
         'Según mis propias investigaciones,', 'Nadie quiere aceptar que', 'Creo que hoy presenciamos todos en primera persona que', 
         'Hoy ví en las noticias que', 'Ya nadie puede ocultar que', 'Increible, pero', 'Los medios no quieren que sepas que', 
         'no me canso de repetirlo,', 'Se cayó la careta,', todobiencon
         ]

inicio_pregunta = ['Por qué los medios no hablan de como', 
        'Estamos todos de acuerdo con que', 'Me están jodiendo? Que no ven que', 
        'Por qué no despiertan y se dan cuenta de que', 'No se dan cuenta de que', 
        'Cuántas veces hay que repetir que', 'Che, nadie notó antes que', 'No es gracioso como',
        'Qué parte no entienden de que']



#predicados

choose_per = choice([proper_m, proper_f, Colective_m, Colective_f, Plural_m, Plural_f])
alguien = choice(choose_per)
worksfor = ['trabaja para ', 'tiene una alianza con ', 'encubre a ', 'tiene un romance secreto con ',
            'sobornó a ']
trabaja_para = choice(worksfor) + alguien

proper_predicate_n = ['tiene que renunciar', 'evade impuestos', 'es antisemita',
            'le roba a los jubilados', 'va a sacar adelante a la nación', 'es narco', 
            'es comunista', 'tiene que ir en cana','es una amenaza para la familia tradicional',
            trabaja_para]

proper_predicate_m = ['es un corrupto', 'es un pedófilo', 'es un genio', 'es un héroe', 'es totalitario', 
            'es extranjero', 'tiene que ser llevado a la justicia', 'está cancelado', 'es un chorro', 
            'es trolo en secreto', 'es un populista', 'es un macho', 'es un fascista', 'es un drogadicto'
            ]

proper_predicate_f = ['es una corrupta', 'es una chorra', 'es una heroina', 'es una genia', 'tiene que ser llevada a la justicia', 
            'es trola', 'es un travesti', 'es una populista', 'es una feminazi', 'es una fascista', 'es misógina', 'es una terf'
            ]


proper_predicate_past_n = ['evadía impuestos', 'era antisemita', 'no hizo nada malo', 
            'le robaba a los jubilados', 'iba a sacar adelante a la nación', 'era narco'
            ]

proper_predicate_past_m = ['era un corrupto', 'era un pedófilo', 'era un terrorista', 
            'era un héroe', 'era extranjero', 'está cancelado', 'era un chorro', 
            'era trolo en secreto', 'era un populista', 'era un macho', 'era un fascista',
            'era un guerrillero', 'era un drogadicto'
            ]

proper_predicate_past_f = ['era una corrupta', 'era una chorra', 'era una heroina', 'era trola', 
            'era un travesti', 'era una populista', 'era una feminazi', 'era una fascista', 
            'era misógina', 'era una terf'
            ]

proper_predicate_col_n = ['es una moda', 'es punitivista', 'es yuta', 
                    'planea un golpe de Estado', 'es racista', 
                    'es un rejunte de vagos', 'es antiderechos', 
                    'es parte del lobby LGTB', 'es antipopular', 
                    'es terrorista', 'es imperialista', 'es una farsa', 
                    'está en contra de la familia', 'tranza con los narcos', 
                    'es vendepatria', 'es de putos', 'es la verdadera derecha'
                    ]

proper_predicate_col_m = ['es guerrillero', 'es financiado por george soros', 
                    'tiene que ser abolido', 'es antidemocrático', 'es patriarcal', 'es misógino'
                    ]

proper_predicate_col_f = ['es terrorista', 'es guerrillera', 'es corrupta', 
                    'está llena de adolescentes mantenidos', 'esta formada por vagos'
                    ]


proper_predicate_plur_n = ['son delincuentes', 'son marionetas políticas', 'manejan la economía', 
            'compraron a los medios', 'deberían dejarse de joder y ponerse a laburar', 
            'viven sin trabajar', 'son ilegales', 'solo buscan lo mejor para el país', 
            'planean derrocar al gobierno', 'venden droga', 'tienen que ir en cana', 
            'quieren corromper a nuestros hijos', 'vinieron a saquear el país', 
            'van a liderar la próxima revolución', 'son indispensables para la sociedad', 
            'son salvajes'
            ]

proper_predicate_plur_m = ['son financiados por el Estado', 'son antiargentinos', 
            'son enfermos mentales', 'son unos incompetentes', 'son antidemocráticos', 
            'son unos ladrones'
            ]

proper_predicate_plur_f = ['son financiadas por el Estado', 'son antidemocráticas', 'son violentas'
            ]

