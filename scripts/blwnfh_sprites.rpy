init 2:

    python:

        ##    Спрайты    ##

        # Эмоции спрайтов старых персонажей и их отношение к позе

        emotion_to_pose = {
            'dv': {
                'cry': 1, 'scared': 1, 'shocked': 1, 'surprise': 1, 'grin': 2, 'guilty': 3, 'shy': 3, 'sad': 3, 'laugh': 4, 'normal': 4, 'smile': 4, 'angry': 5, 'rage': 5,
            },
            'mz': {
                'bukal': 1, 'normal': 1, 'laugh': 1, 'amazed': 1, 'fun': 1,  'hope': 1, 'sad': 1, 'sceptic': 1, 'smile2': 2, 'cry': 2, 'shyangry': 2,'angry': 2, 'rage': 2, 'confused': 3, 'excitement': 3, 'shy': 3, 'smile': 3,
            },
            'mt': {
                'normal': 1, 'sad': 1, 'smile': 1, 'surprise': 1, 'angry': 2, 'rage': 2, 'grin': 3, 'laugh': 3,
            },
            'sh': {
                'laugh': 1, 'scared': 1, 'smile': 1, 'upset': 1, 'cry': 2, 'normal_smile': 2, 'rage': 2, 'normal': 3, 'serious': 3, 'surprise': 3,
            },
            'un': {
                'angry': 1, 'evil_smile': 1, 'normal': 1, 'shy': 1, 'smile': 1, 'smile2': 1, 'cry': 2, 'cry_smile': 2, 'sad': 2, 'scared': 2, 'shocked': 2, 'surprise': 2, 'angry2': 3, 'grin': 3, 'laugh': 3, 'rage': 3, 'serious': 3, 'smile3': 3, 'draws_normal': 4, 'draws_smile': 4,
            },
            'us': {
                'grin': 1, 'laugh': 1, 'laugh2': 1, 'normal': 1, 'sad': 1, 'smile': 1, 'angry': 2, 'calml': 2, 'dontlike': 2, 'fear': 2, 'upset': 2, 'cry': 3, 'cry2': 3, 'shy': 3, 'shy2': 3, 'surp1': 3, 'surp2': 3, 'surp3': 3,
            },
            'cs': {
                'normal': 1, 'shy': 1, 'smile': 1,
            },
            'mi': {
                'cry': 1, 'dontlike': 1, 'laugh': 1, 'shocked': 1, 'scared': 1, 'shy': 1, 'surprise': 1, 'cry_smile': 2, 'grin': 2, 'happy': 2, 'sad': 2, 'smile': 2, 'angry': 3, 'normal': 3, 'rage': 3, 'serious': 3, 'upset': 3,
            },
            'kat': {
                'grin': 1, 'normal': 1, 'sad': 1, 'shocked': 1, 'akhegao': 2, 'angry': 2, 'fuk': 2, 'happy': 2, 'normal2': 2, 'scared': 2, 'shy': 2, 'guilty': 3, 'nepon': 3, 'obida': 3, 'rock': 3, 'sad2': 3, 'shy2': 3,
            },
            #'uv': {
            #    'pidontlike': 1, 'pirage': 1, 'pisad': 1, 'pishocked': 1, 'pinormal': 2, 'pismile': 2, 'pigrin': 3, 'pilaugh': 3, 'pisurprise2': 3, 'piguilty': 4, 'pisurprise': 4, 'piupset': 4,
            #},
        }

        distance_to_position = {
            "far": (630, 1080),
            "normal": (900, 1080),
            "close": (1050, 1080),
            "background": (1920, 1080)
        }

        def _sprite_for_all_times(full_sprite_name, composite_image):
            """
            Объявляем спрайт для всех времен суток
            """
            renpy.image(
                full_sprite_name,
                ConditionSwitch(
                    "persistent.sprite_time == 'sunset'", im.MatrixColor(composite_image, blwnfh_tint["sunset"]),
                    "persistent.sprite_time == 'night'", im.MatrixColor(composite_image, blwnfh_tint["night"]),
                    True, composite_image,
                )
            )

        def _sepia_sprite(full_sprite_name, composite_image):
            """
            Спрайт, окрашенный в сепию
            """
            renpy.image(full_sprite_name, im.Sepia(composite_image))

        def _dark_sprite(full_sprite_name, composite_image):
            """
            Спрайт в темноте
            """
            renpy.image(full_sprite_name, im.MatrixColor(composite_image, im.matrix.brightness(-0.99)))

        # Генератор новых спрайтов для персонажей из оригинального БЛ

        def make_sprites_for(character, sprite_name, layers, emotions=None, distances=None, exclude=None, sprite_define_func=None, default=True):
            """
            Позволяет объявить почти любой спрайт, состоящий из нескольких слоев,
            каждый слой может идти либо из мода, либо из оригинала.
            Картинки должны класться в папки строго как в оригинале, чтобы это работало.
            """

            if emotions is None:
                emotions = emotion_to_pose[character].keys()
            if distances is None:
                distances = distance_to_position.keys()
            if sprite_define_func is None:
                sprite_define_func = _sprite_for_all_times

            for emotion in emotions:
                if exclude and emotion in exclude:
                    continue

                pose = emotion_to_pose[character][emotion]

                for distance in distances:
                    # Получаем название спрайта, например dv angry blwnfh_sport far
                    full_sprite_name = '%s %s %s' % (character, emotion, sprite_name)
                    if not sprite_name:
                        full_sprite_name = '%s %s' % (character, emotion)  # Не у всех есть одежда
                    if distance != 'normal':
                        full_sprite_name += ' ' + distance

                    # Комбинируем изображение
                    image_parts = [distance_to_position[distance]]
                    for layer in layers:
                        source, file_name = layer.split(':')
                        base_path = blwnfh_IMAGES if source == 'mod' else blwnfh_IMAGES
                        if default:
                            image_path = base_path + "sprites/%s/%s/%s_%s_%s.png" % (
                                distance, character, character, pose, file_name if file_name != '<emotion>' else emotion,
                            )
                        else:
                            image_path = base_path + "sprites/%s/%s/old/%s_%s_%s.png" % (
                                distance, character, character, pose, file_name if file_name != '<emotion>' else emotion,
                            )
                        image_parts += [(0, 0), image_path]
                    composite_image = im.Composite(*image_parts)

                    # Объявляем спрайт
                    sprite_define_func(full_sprite_name, composite_image)


        def make_sprites_with_custom_emotions(custom_emotions, *args):
            """
            Удобно, когда нужно объявить новую эмоцию
            """
            args = list(args)
            assert args[-1][-1] == 'es:<emotion>'
            make_sprites_for(*args, exclude=custom_emotions)
            args[-1][-1] = 'mod:<emotion>'
            make_sprites_for(*args, emotions=custom_emotions)


        # Объявляем спрайты
        ## Новые персонажи
        make_sprites_for('kat', 'pioneer', ['mod:body', 'mod:pioneer', 'mod:<emotion>'])
        make_sprites_for('kat', 'casual', ['mod:body', 'mod:casual', 'mod:<emotion>'])
        make_sprites_for('kat', 'casual shirt', ['mod:body', 'mod:casual', 'mod:<emotion>', 'mod:shirt'])
        make_sprites_for('kat', 'swim', ['mod:body', 'mod:swim', 'mod:<emotion>'])
        make_sprites_for('mz', 'pioneer', ['mod:body', 'mod:pioneer', 'mod:<emotion>'])
        make_sprites_for('mz', 'pioneer', ['mod:body', 'mod:pioneer', 'es:<emotion>'])
        make_sprites_for('mz', 'pioneer glasses', ['mod:body', 'mod:pioneer', 'mod:<emotion>', 'es:glasses'])
        make_sprites_for('mz', 'pioneer glasses', ['mod:body', 'mod:pioneer', 'es:<emotion>', 'es:glasses'])
        
        ## Фоновые спрайты
        make_sprites_for('un', 'draws', ['mod:draws', 'mod:<emotion>'])
        #make_sprites_for('dv', 'bkrr_sport', ['mod:sport', 'es:<emotion>'])
        #make_sprites_for('dv', 'bkrr_swim', ['es:body', 'es:swim', 'es:<emotion>'], exclude=('angry', 'guilty', 'rage', 'sad', 'shy'))
        #make_sprites_for('dv', 'bkrr_swim', ['mod:swim', 'es:<emotion>'], emotions=('angry', 'guilty', 'rage', 'sad', 'shy'))
        #make_sprites_for('dv', 'bkrr_swim_rose', ['es:body', 'mod:swim', 'mod:rose', 'es:<emotion>'], emotions=('angry', 'guilty', 'rage', 'sad', 'shy'), distances=['normal'])
        #make_sprites_for('dv', 'bkrr_swim_rose', ['es:body', 'es:swim', 'mod:rose', 'es:<emotion>'], emotions=['surprise'], distances=['normal'])
        #make_sprites_for('dv', 'pirate_with_hat', ['mod:pibody', 'es:<emotion>'])
        #make_sprites_for('dv', 'pirate', ['mod:pibody2', 'es:<emotion>'])
        #make_sprites_for('dv', 'pirate dress', ['mod:pidress', 'es:<emotion>'], emotions=['grin'], distances=['normal'])
        #make_sprites_for('dv', 'civil', ['es:body', 'mod:civil', 'es:<emotion>'])
        #
        #make_sprites_for('mz', 'bkrr_sport', ['mod:sport', 'es:<emotion>'])
        #make_sprites_for('mz', 'mask bkrr_sport', ['mod:sport', 'es:<emotion>', 'mod:mask'])
        #make_sprites_for('mz', 'zombie', ['mod:zomb'], emotions=['normal'], distances=['far'])
        #make_sprites_for('mz', 'glasses bkrr_sport', ['mod:sport', 'es:<emotion>', 'es:glasses'])
        #make_sprites_for('mz', 'glasses bkrr_dress', ['es:body', 'mod:dress', 'es:<emotion>', 'es:glasses'])
        #make_sprites_for('mz', 'bdsm', ['mod:bdsm', 'es:<emotion>'])  # не все эмоции доступны
        #
        #make_sprites_for('mt', 'bkrr_sport', ['es:body', 'mod:sport', 'es:<emotion>'])
        #make_sprites_for('mt', 'nightdress', ['mod:nightdress', 'es:<emotion>'])
        #make_sprites_for('mt', 'pioneer blood', ['es:body', 'es:pioneer', 'mod:blb', 'es:<emotion>'])
        #make_sprites_for('mt', 'pioneer blood2', ['es:body', 'es:pioneer', 'mod:blb', 'mod:blf', 'es:<emotion>'])
        #make_sprites_for('mt', 'torn', ['es:body', 'mod:torn', 'mod:blb', 'es:<emotion>'], distances=['normal'])
        #
        #make_sprites_for('sh', 'bathrobe', ['mod:bathrobe', 'es:<emotion>'])
        #make_sprites_for('sh', 'towel', ['mod:body', 'es:<emotion>'])
        #make_sprites_for('sh', 'towel', ['mod:body', 'mod:<emotion>'], emotions=['upset_nocry'], distances=['normal'])
        #make_sprites_for('sh', 'shirt', ['mod:shirt', 'es:<emotion>'])
        #make_sprites_for('sh', 'red_nose pioneer', ['es:body', 'es:<emotion>', 'mod:red_nose'])
        #
        #make_sprites_with_custom_emotions(['shy_smile'], 'un', 'bkrr_dress', ['es:body', 'mod:dress', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['shy_smile'], 'un', 'paint sport', ['es:body', 'es:sport', 'mod:pn', 'es:<emotion>'])
        #make_sprites_for('un', 'bra', ['mod:bra', 'es:<emotion>'], emotions=['cry', 'cry_smile', 'sad', 'scared', 'shocked', 'surprise'])
        #make_sprites_for('un', 'jacket', ['es:body', 'mod:jacket', 'es:<emotion>'])
        #make_sprites_for('un', 'pioneer', ['es:body', 'es:pioneer', 'mod:<emotion>'], emotions=['shy_smile'])
        #make_sprites_for('un', 'sport', ['es:body', 'es:sport', 'mod:<emotion>'], emotions=['shy_smile'])
        #
        #make_sprites_for('us', 'bra', ['mod:bra', 'es:<emotion>'])
        #make_sprites_for('us', 'bkrr_dress', ['mod:dress', 'es:<emotion>'])
        #make_sprites_for('us', 'swim', ['es:body', 'es:swim', 'mod:<emotion>'], emotions=['normal_dontlike_bkrr', 'evsmile'])
        #make_sprites_for('us', 'pioneer', ['es:body', 'es:pioneer', 'mod:<emotion>'], emotions=['normal_dontlike_bkrr', 'evsmile'])
        #make_sprites_for('us', 'sport', ['es:body', 'es:sport', 'mod:<emotion>'], emotions=['normal_dontlike_bkrr', 'evsmile'])
        #make_sprites_for('us', 'bdsm', ['mod:bdsm', 'es:<emotion>'])  # не все эмоции доступны
        #make_sprites_for('us', 'night_shirt', ['mod:night_shirt', 'es:<emotion>'])
        #make_sprites_for('us', 'night_shirt', ['mod:night_shirt', 'mod:<emotion>'], emotions=['yawn'])
        #make_sprites_for('us', 'backpack sport', ['es:body', 'es:sport', 'mod:backpack', 'es:<emotion>'], distances=['normal'])
        #make_sprites_for('us', 'pirate patch', ['mod:pibody', 'es:<emotion>', 'mod:pibody2'])
        #make_sprites_for('us', 'pirate patch', ['mod:pibody', 'mod:<emotion>', 'mod:pibody2'], emotions=['normal_dontlike_bkrr', 'evsmile'])
        #make_sprites_for('us', 'pirate', ['mod:pibody', 'es:<emotion>', 'mod:pibody3'])
        #make_sprites_for('us', 'pirate', ['mod:pibody', 'mod:<emotion>', 'mod:pibody3'], emotions=['normal_dontlike_bkrr', 'evsmile'])
        #
        #make_sprites_for('uv', 'pioneer', ['mod:pibody', 'mod:<emotion>', 'mod:pan'])
        #
        #make_sprites_with_custom_emotions(['sad'], 'cs', 'body', ['mod:body', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad'], 'cs', 'panties', ['mod:body', 'mod:panties', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad'], 'cs', 'robe', ['es:body', 'mod:noshirt', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad'], 'cs', 'civil', ['mod:body', 'mod:civil', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad'], 'cs', 'civil2', ['mod:body', 'mod:civil2', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad'], 'cs', 'dress', ['mod:body', 'mod:dress', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad'], 'cs', 'swim', ['mod:body', 'es:<emotion>', 'mod:swim'])
        #
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'bkrr_dress', ['mod:dress', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'wet pioneer', ['mod:wet_pioneer', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'swim_loo', ['mod:body_loo', 'es:swim', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'jacket', ['es:body', 'mod:underwear', 'mod:jacket', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'yukata', ['mod:yukata', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'pirate', ['mod:pirate', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'pioneer_loo', ['mod:body_loo', 'es:pioneer', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'underwear', ['es:body', 'mod:underwear', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'bkrr_sport', ['mod:sport', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'bkrr_sport_loo', ['mod:body_loo', 'mod:sport', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'apron', ['es:body', 'mod:apron', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'dirt apron', ['es:body', 'mod:apron', 'mod:apron_dirt', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'shorts', ['mod:body_loo', 'mod:shorts', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'shorts_hair', ['mod:body_loo', 'mod:shorts', 'mod:hair', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'body_loo', ['mod:body_loo', 'es:<emotion>'])
        #make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'body', ['es:body', 'es:<emotion>'])
        #
        #make_sprites_for('mi', 'sheet', ['mod:body_loo', 'mod:sheet', 'es:<emotion>'], distances=['close'])
        #make_sprites_for('mi', 'underwear loose', ['mod:body_loo', 'mod:underwear', 'es:<emotion>'], distances=['close'])
        #make_sprites_for('mi', 'underwear loose hair', ['mod:body_loo', 'mod:underwear', 'mod:hair', 'es:<emotion>'], distances=['close'])
        #make_sprites_for('mi', 'underwear loose towel hair', ['mod:body_loo', 'mod:underwear', 'mod:towel', 'mod:hair', 'es:<emotion>'], distances=['close'])
        #make_sprites_for('mi', 'panties', ['mod:body_loo', 'mod:panties', 'mod:hair', 'es:<emotion>'])
        #make_sprites_for('mi', 'panties naked', ['mod:body_loo', 'mod:panties', 'mod:hair_for_naked', 'es:<emotion>'], distances=['close'])
        #make_sprites_for('mi', 'panties dark', ['mod:body_loo', 'mod:panties', 'mod:hair', 'es:<emotion>'], sprite_define_func=_dark_sprite)
        #make_sprites_for('mi', 'panties yukata_hair dark', ['mod:panties_yukata_hair', 'es:<emotion>'], sprite_define_func=_dark_sprite)
        #make_sprites_for('mi', 'towel_only', ['mod:towel'], distances=['close'])
        #make_sprites_for('mi', 'hair_only', ['mod:hair'], distances=['close'])
        #make_sprites_for('mi', 'civil', ['mod:civil', 'es:<emotion>'])
        #make_sprites_for('mi', 'civil', ['mod:civil', 'mod:<emotion>'], emotions=['sad_smile'])
        #make_sprites_for('mi', 'pioneer', ['es:body', 'es:pioneer', 'mod:<emotion>'], emotions=['sad_smile'])
        #make_sprites_for('mi', 'swim', ['es:body', 'es:swim', 'mod:<emotion>'], emotions=['sad_smile'])
        #
        #make_sprites_for('mii', 'inside', ['mod:inside', 'mod:<emotion>'])
        #make_sprites_for('mii', 'outside', ['mod:outside', 'mod:<emotion>'], sprite_define_func=_miku_epilogue_sprite)
        #make_sprites_for('mii', 'outside snow', ['mod:outside', 'mod:snow', 'mod:<emotion>'], sprite_define_func=_miku_epilogue_sprite)
        #
        #make_sprites_for('sta', 'inside', ['mod:inside', 'mod:<emotion>'])
        #make_sprites_for('sta', 'outside', ['mod:outside', 'mod:<emotion>'])
        #
        ## Эл с фингалом
        #make_sprites_for('el', 'pioneer', ['es:body', 'es:pioneer', 'mod:<emotion>'])
        #
        ## Эл-ведроид
        #make_sprites_for('el', 'vedro', ['mod:vedro'], emotions=['sad_vedro'])
        #
        
        #make_sprites_for('ant', 'shirt', ['mod:body', 'mod:<emotion>'])
        #make_sprites_for('kla', 'sport', ['mod:body', 'mod:sport', 'mod:<emotion>'])
        #make_sprites_for('kla', 'pioneer', ['mod:body', 'mod:pioneer', 'mod:<emotion>'])
        #make_sprites_for('kla', 'pioneer claw_marks', ['mod:body', 'mod:pioneer', 'mod:claw_marks', 'mod:<emotion>'], distances=['normal'])
        #make_sprites_for('nt', 'cook', ['mod:cook', 'mod:<emotion>'], default=persistent.bkrr_old_sprites['nt'])
        #make_sprites_for('tol', 'pioneer', ['mod:pioneer', 'mod:<emotion>'], default=persistent.bkrr_old_sprites['tol'])
        #make_sprites_for('tr', 'pioneer', ['mod:pioneer', 'mod:<emotion>'])
        #make_sprites_for('tr', 'cas', ['mod:cas', 'mod:<emotion>'])
        #
        ## Спрайты, окрашенные в сепию
        #make_sprites_for('mi', 'pioneer sepia', ['es:body', 'es:pioneer', 'es:<emotion>'], exclude=['sad_smile'], sprite_define_func=_sepia_sprite)
        #make_sprites_for('mi', 'pioneer sepia', ['es:body', 'es:pioneer', 'mod:<emotion>'], emotions=['sad_smile'], sprite_define_func=_sepia_sprite)
        #make_sprites_for('dv', 'pioneer2 sepia', ['es:body', 'es:pioneer2', 'es:<emotion>'], sprite_define_func=_sepia_sprite)
        #make_sprites_for('us', 'pioneer sepia', ['es:body', 'es:pioneer', 'es:<emotion>'], sprite_define_func=_sepia_sprite)
        #make_sprites_for('us', 'dress sepia', ['es:body', 'es:dress', 'es:<emotion>'], sprite_define_func=_sepia_sprite)
    image chair = ConditionSwitch("persistent.sprite_time == 'sunset'", im.MatrixColor(blwnfh_OTHER + "chair.png", blwnfh_tint["sunset"]), "persistent.sprite_time == 'night'", im.MatrixColor(blwnfh_OTHER + "chair.png", blwnfh_tint["night"]), True, blwnfh_OTHER + "chair.png")

    image chair_l:
        "chair"
        left
        yalign 0.0

    image chair_c:
        "chair"
        center
        yalign 0.0

    image chair_r:
        "chair"
        right
        yalign 0.0

