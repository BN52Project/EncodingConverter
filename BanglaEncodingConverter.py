#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re


class BanglaEncodingConverter:
    """Converts Bengali Text between Encodings"""

    def __target_secondary_convert__(self, source_encoding, target_encoding, in_text):
        
        if target_encoding == self.bijoy_classic:
            for k in self.bijoy_classic[3].keys():
                in_text = in_text.replace(k, self.bijoy_classic[3][k])

        elif source_encoding == self.bijoy_classic:
            for k in self.bijoy_classic[3].keys():
                in_text = in_text.replace(self.bijoy_classic[3][k], k)

        return in_text

    def __target_primary_convert__(self, source_encoding, target_encoding, in_text):
        """accepts a layout table tuple and a string.
        usage: __target_primary_convert__(source_encoding, target_encoding, in_text)"""

        # Every Encoding Table (tuple) has 3 sub-tuples.

        # Tuple 0 (encoding[0]) contains normal replace rules
        # Tuple 1 (encoding[1]) contains search regex patterns
        # Tuple 2 (encoding[2]) contains replace regex patterns

        for count in range(0, self.unicode[1].__len__()):
            in_text = re.sub(source_encoding[1][count], target_encoding[2][count], in_text)

        for count in range(0, self.unicode[0].__len__()):
            in_text = in_text.replace(source_encoding[0][count], target_encoding[0][count])

        

        return in_text

    def convert(self, source_encoding, target_encoding, in_text):
        """Returns a string encoded to target_encoding from source_encoding.
        Usage: convert(source_encoding, target_encoding, text)"""

        if source_encoding == self.bijoy_classic:
            in_text = self.__target_secondary_convert__(source_encoding, target_encoding, in_text)
            in_text = self.__target_primary_convert__(source_encoding, target_encoding, in_text)
        else:
            in_text = self.__target_primary_convert__(source_encoding, target_encoding, in_text)
            in_text = self.__target_secondary_convert__(source_encoding, target_encoding, in_text)

        return in_text

    def __init__(self):
        self.unicode = (('অ', 'আ', 'ই', 'ঈ', 'উ', \
                 'ঊ', 'ঋ‌', 'এ', 'ঐ', 'ও', \
                 'ঔ', \

                 'ক', 'খ', 'গ', 'ঘ', 'ঙ', \
                 'চ', 'ছ', 'জ', 'ঝ', 'ঞ', \
                 'ট', 'ঠ', 'ড', 'ঢ', 'ণ', \
                 'ত', 'থ', 'দ', 'ধ', 'ন', \
                 'প', 'ফ', 'ব', 'ভ', 'ম', \
                 'য', 'র', 'ল', \
                 'শ', 'স', 'ষ', 'হ', \
                 'য়', 'ড়', 'ঢ়', \
                 'ৎ', 'ং', 'ঃ', 'ঁ', \

                 '্', '।', \

                 '্র', '্য', '্ব', '্ম', \
                 '্প', \

                 'া', 'ী', 'ু', 'ূ', 'ৃ', 'ৗ', \
                 '০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'), \

                (r'(.)ি', r'(.)ে', r'(.)ৈ', r'(.)ো', r'(.)ৌ', r'র্(.)'), \
                (r'\1ি', r'\1ে', r'\1ৈ', r'\1ো', r'\1ৌ', r'র্\1'))

        self.bijoy_classic = (('A', 'Av', 'B', 'C', 'D', \
                 'E', 'F‌', 'G', 'H', 'I', \
                 'J', \
                 'K', 'L', 'M', 'N', 'O', \
                 'P', 'Q', 'R', 'S', 'T', \
                 'U', 'V', 'W', 'X', 'Y', \
                 'Z', '_', '`', 'a', 'b', \
                 'c', 'd', 'e', 'f', 'g', \
                 'h', 'i', 'j', \
                 'k', 'm', 'l', 'n', \
                 'q', 'o', 'p', \
                 'r', 's', 't', 'u', \

                 '&', '|', \

                 '«', '¨', '¡', '¥', 'ú', \

                 'v', 'x', 'y', '~', '…', 'Š', \
                 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), \
                 
                (r'w(.)', r'‡(.)', r'‰(.)', r'‡(.)v', r'‡(.)Š', r'(.)©'), \
                (r'w\1', r'‡\1', r'‰\1', r'‡\1v', r'‡\1Š', r'\1©'), \

                # This dictionary defines the transforms required for
                # displaying proper conjugant characters in Bijoy

                {'•ÿ„':'•ÿ…', '®‹„':'®‹…', '™¢„':'™¢…', 'š’„':'š’…', '¯‹¬y':'¯‹¬z', \
                '¯’„':'¯’…', '›`ªy':'›`ªæ', '›`ª~':'›`ªƒ', '®úª~':'®úÖƒ', '®úªy':'®úÖæ', \
                '¼«„':'¼«…', '™¢~':'™¢‚', '›U„':'›U…', 'š’~':'š’‚', 'Ü«„':'Ü«…', \
                '®Œ„':'®Œ„', '¯’~':'¯’‚', '”Q„':'”Q…', 'šÍ„':'šÍ…', '¯‹&j':'¯‹¬', \
                '¯‹~':'¯‹‚', '¯‹~':'¯‹‚', 'ÿè„':'ÿè…', '”P„':'”P…', '”T„':'”T…', \
                '•ÿ~':'•ÿ‚', '¯Í„':'¯Í…', '®‹~':'®‹‚', '™£~':'™£ƒ', '™£y':'™£æ', \
                'ÿè~':'ÿè‚', 'šÍ~':'šÍ‚', '¤ú&j':'¤úø', '›U~':'›U‚', '¯ú&j':'¯úø', \
                'š’y':'š’z', 'Ü«~':'Ü«‚', '”T~':'”T‚', '™¢y':'™¢z', 'Kè„':'Kè…', \
                'ù«~':'ù«‚', '¯Œ~':'¯Œ‚', '®úª':'®úÖ', '”Qª':'”Q«', '”Q&e':'”Q¡', \
                '¼«~':'¼«‚', '®Œ~':'®Œ‚', 'K¬„':'K¬…', 'd«„':'d«…', '¯‹y':'¯‹z', \
                '¯Í~':'¯Í‚', '¯’y':'¯’z', '™¢ª':'™£', '®‹y':'®‹z', '¯Í&e':'¯Í¡', \
                '”P~':'”P‚', '¯Œ~':'¯Œ‚', '”Q~':'”Q‚', 'd¬„':'d¬„', '•ÿy':'•ÿz', \
                '¯‹ª':'¯Œ', '›`&e':'›Ø', '÷~':'÷‚‚', 'ÿ~':'ÿ‚‚', 'ë~':'ë‚‚', \
                '®‹ª':'®Œ', 'ô„':'ô…', 'Ã„':'Ã…', 'õ„':'õ…', 'ó„':'ó…', \
                'µ„':'µ…', 'ÿ„':'ÿ…', '®Œy':'®Œz', 'ù„':'ù…', '¯Íy':'¯‘', \
                'Æ„':'Æ…', 'Ð„':'Ð…', 'Ë„':'Ë…', 'ò„':'ò…', 'K¬~':'K¬‚', \
                'þ„':'þ„', '¯Œy':'¯Œz', 'ñ„':'ñ…', 'ÿèy':'ÿèz', '³„':'³…', \
                'Â…':'Â…', 'Kè~':'Kè‚', 'É„':'É…', 'ë„':'ë…', '÷„':'÷…', \
                '±„':'±…', 'È„':'È…', '¯Íª':'¯¿', 'ù«y':'ù«z', '°„':'°…', \
                'Â‚':'Â‚', 'é„':'é…', 'd«~':'d«‚', 'Ü„':'Ü…', '›Uy':'›Uz', \
                'šÍª':'š¿', '¤¢ª':'¤£', 'ç„':'ç…', 'Á„':'Á…', 'î„':'î…', \
                '»„':'»…', '×„':'×…', '¼„':'¼…', 'Ç„':'Ç…', 'ä„':'ä…', \
                'ð„':'ð…', '¼«y':'¼«z', '”Py':'”Pz', 'šÍy':'š‘', '”Qy':'”Qz', \
                'Þ„':'Þ…', 'ß„':'ß…', 'Ú„':'Ú…', 'Û„':'Û…', 'd¬~':'d¬‚', \
                'À„':'À…', 'Ü«y':'Ü«z', '”Ty':'”Tz', 'cÖy':'cÖæ', 'aª~':'aªƒ', \
                'aªy':'aªæ', 'Nª~':'Nªƒ', 'MÖy':'MÖæ', 'Lª~':'Lªƒ', '˜M&y':'`&¸', \
                'Nªy':'Nªæ', 'kÖy':'kÖæ', '`ª~':'`ªƒ', 'Lªy':'Lªæ', '`ªy':'`ªæ', \
                'kÖ~':'kÖƒ', 'MÖ~':'MÖƒ', 'eªy':'eªæ', 'eª~':'eªƒ', '¼&l':'•ÿ', \
                'cÖ~':'cÖƒ', 'é~':'é‚', '¼ª':'¼«', 'õ~':'õ‚', 'ò~':'ò‚', \
                'f„':'f…', 'ä~':'ä‚', 'm&_':'¯’', 'S„':'S…', 'U„':'U…', \
                'm&K':'¯‹', 'Z„':'Z…', 'd¬y':'d¬z', 'Ë~':'Ë‚', '×~':'×‚', \
                'Ã~':'Ã‚', 'T„':'T…', '¾&e':'¾¡', 'P„':'P…', 'l&K':'®‹', \
                'd„':'d…', 'Æ~':'Æ‚', 'Á~':'Á‚', '¼~':'¼‚', 'ô~':'ô‚', \
                'ç~':'ç‚', 'K¬y':'K¬z', 'd«y':'d«z', '³~':'³‚', 'Þ~':'Þ‚', \
                'ù~':'ù‚', 'ùª':'ù«', 'Ë&e':'Ë¡', 'Üª':'Ü«', 'À~':'À‚', \
                'Ð~':'Ð‚', 'îª':'î«', 'ñ~':'ñ‚', 'µ~':'µ‚', 'É~':'É‚', \
                'ß~':'ß‚', '»~':'»‚', 'Q„':'Q…', 'ó~':'ó‚', 'Kèy':'Kèz', \
                'Ü~':'Ü‚', 'È~':'È‚', '(A)i':'(A)i', 'V„':'V…', 'ð~':'ð‚', \
                '±~':'±‚', 'W„':'W…', 'b&_':'š’', '`&f':'™¢', 'O„':'O…', \
                '³ª':'³«', '³ª':'³«', 'ÿ&b':'ÿè', 'X„':'X…', '°~':'°‚', \
                'Ú~':'Ú‚', 'K„':'K…', 'Ç~':'Ç‚', 'Û~':'Û‚', 'P&P':'”P', \
                'b&`':'›`', 'm&j':'¯ø', 'g&g':'¤§', 'P&T':'”T', 'm&c':'¯ú', \
                'm&Z':'¯Í', 'g&b':'¤œ', 'O&L':'•L', 'O&g':'•g', 'O&N':'•N', \
                'å~':'åƒ', 'P&Q':'”Q', 'b&Z':'šÍ', 'Î~':'Îƒ', 'l&g':'®§', \
                'gª':'¤ª', 'g&j':'¤ø', 'åy':'åæ', 'mª':'¯ª', 'Îy':'Îæ', \
                'b&U':'›U', 'l&c':'®ú', 'm&b':'¯œ', 'g&f':'¤¢', 'm&g':'¯§', \
                'g&c':'¤ú', 'n&e2':'n¡', 'oy':'o–', 'nª':'n«', '÷y':'÷z', \
                'þ~':'þ~', 'ëy':'ëz', 'ùy':'ùz', 'n&j':'n¬', 'ñy':'ñz', \
                'n„':'ü', 'k&b':'kœ', 'm&e':'¯^', 'c&b':'cœ', 'n&Y':'nè', \
                'dª':'d«', 'c&j':'cø', 'Þy':'Þz', 'b&b':'bœ', 'd~':'d‚', \
                'cª':'cÖ', 'n&e':'nŸ', 'þy':'þz', 'j&j':'jø', 'ðy':'ðz', \
                'j&g':'j¥', 'óy':'óz', 'kª':'kÖ', 'a&e':'aŸ', 'Èy':'Èz', \
                '_&e':'_¡', 'Ëy':'Ëz', 'Y&e':'Y¦', 'Ðy':'Ðz', 'Úy':'Úz', \
                'Z&b':'Zœ', 'Z&e':'Z¡', 'Y&b':'Yœ', 'Z&g':'Z¥', 'Éy':'Éz', \
                'X~':'X‚', 'õy':'õz', 'òy':'òz', 'k&g':'k¥', 'k&e':'k¦', \
                'ôy':'ôz', 'b&e':'š^', '×y':'×z', 'Z~':'Z‚', '`&M':'˜M', \
                'a&g':'a¥', '`&N':'˜N', 'äy':'äz', 'P~':'P‚', 'O~':'O‚', \
                'ÿy':'ÿz', 'M&b':'Mœ', 'µy':'µz', 'N&b':'Nœ', 'S~':'S‚', \
                'Áy':'Áz', 'Q~':'Q‚', 'Qª':'Q«', '¼y':'¼z', 'R&e':'R¡', \
                'Çy':'Çz', 'V~':'V‚', 'K~':'K‚', '°y':'°z', 'U~':'U‚', \
                'b&g':'b¥', 'U&e':'U¡', 'Æy':'Æz', 'K&e':'K¡', 'K&b':'Kè', \
                '±y':'±z', 'U&g':'U¥', 'K&j':'K¬', 'W~':'W‚', 'f&j':'fø', \
                'g&e':'¤^', 'çy':'çz', 'e&e':'eŸ', 'f~':'f‚', 'j&e':'j¦', \
                'ßy':'ßz', 'M&e':'M¦', 'd&j':'d¬', 'e&j':'eø', 'îy':'îz', \
                'éy':'éz', 'î~':'î~', 'Àz':'Àz', '»y':'»z', '³y':'³z', \
                'ÿ&g':'²', 'T~':'T‚', 'Üy':'Üz', 'Ãy':'Ãz', 'Ûy':'Ûz', \
                'M&j':'Mø', 'M&g':'M¥', 'Ây':'Âz', 'Mª':'MÖ', 'c&Z':'ß', \
                'b&m':'Ý', 'Y&U':'È', 'i~':'iƒ', 'j&M':'ê', 'e&`':'ã', \
                'c&U':'Þ', 'b&V':'Ú', '`&e':'Ø', 'j&U':'ë', 'b&W':'Û', \
                'R&R':'¾', 'R&S':'À', 'j&M':'ê', 'W&W':'Ç', 'iy':'i“', \
                'e&a':'ä', 'm&U':'÷', '`&`':'Ï', 'O&M':'½', 'e&R':'â', \
                'fª':'å', '`&a':'×', 'g&d':'ç', 'j&K':'é', 'Y&V':'É', \
                'j&c':'í', 'n&b':'ý', 'O&K':'¼', 'T&P':'Â', 'm&d':'ù', \
                'Y&W':'Ð', 'T&Q':'Ã', 'l&V':'ô', 'T&S':'Å', 'n&g':'þ', \
                'm&L':'ö', 'b&a':'Ü', 'T&R':'Ä', 'k&Q':'ñ', 'Z&_':'Ì', \
                'Zª':'Î', 'M&`':'º', '`&g':'Ù', 'k&P':'ð', 'M&a':'»', \
                'l&d':'õ', 'j&W':'ì', 'K&m':'·', 'j&d':'î', 'c&c':'à', \
                'K&g':'´', 'K&K':'°', 'R&T':'Á', 'l&Y':'ò', 'K&Z':'³', \
                'Kª':'µ', 'K&l':'ÿ', 'U&U':'Æ', 'l&U':'ó', 'Z&Z':'Ë', \
                'fy':'fz', 'Zy':'Zz', 'Xy':'Xz', 'My':'¸', 'ny':'û', \
                'Ky':'Kz', 'Ty':'Tz', 'Uy':'Uz', 'ky':'ï', 'Qy':'Qz', \
                'Wy':'Wz', 'Oy':'Oz', 'Vy':'Vz', '&.':'ž', 'dy':'dz', \
                'Py': 'Pz','Sy': 'Sz'})

        # WARNING: Boishakhi has not been implemented yet.

        self.boishakhi = (('A', 'Aw', 'B', 'C', 'D', \
                 'E', 'F‌', 'G', 'H', 'I', \
                 'J', \

                 'K', 'L', 'M', 'N', 'O', \
                 'P', 'Q', 'R', 'S', 'T', \
                 'U', 'V', 'W', 'X', 'Y', \
                 'Z', 'a', 'b', 'c', 'd', \
                 'e', 'f', 'g', 'h', 'i', \
                 'j', 'k', 'l', \
                 'm', 'o', 'n', 'p', \
                 't', 'r', 's', \
                 'u', 'v', ':', '^', \

                 'z', '|', \

                 'w', 'y', '×', 'Ô', 'Ú', '#', \
                 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), \
                (r'x(.)', r'Ë(.)', r'Ð(.)', r'Ë(.)w', r'Ë(.)#'), \
                (r'x\1', r'Ë\1', r'Ð\1', r'Ë\1w', r'Ë\1#'))