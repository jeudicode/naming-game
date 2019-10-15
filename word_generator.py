import random as rand

class Word_Generator:


    syllables = ["a", "e", "i", "o", "u", 
                "ba", "be", "bi", "bo", "bu",
                "ca", "ce", "ci", "co", "cu",
                "da", "de", "di", "do", "du",
                "fa", "fe", "fi", "fo", "fu",
                "ga", "ge", "gi", "go", "gu",
                "ha", "he", "hi", "ho", "hu",
                "ja", "je", "ji", "jo", "ju",
                "ka", "ke", "ki", "ko", "ku",
                "la", "le", "li", "lo", "lu",
                "ma", "me", "mi", "mo", "mu",
                "na", "ne", "ni", "no", "nu",
                "pa", "pe", "pi", "po", "pu",
                "ra", "re", "ri", "ro", "ru",
                "sa", "se", "si", "so", "su",
                "ta", "te", "ti", "to", "tu",
                "va", "ve", "vi", "vo", "vu",
                "wa", "we", "wi", "wo", "wu",
                "xa", "xe", "xi", "xo", "xu",
                "ya", "ye", "yi", "yo", "yu",
                "za", "ze", "zi", "zo", "zu",
                "bam", "bem", "bim", "bom", "bum",
                "ban", "ben", "bin", "bon", "bun",
                "bad", "bed", "bid", "bod", "bud",
                "bak", "bek", "bik", "bok", "buk",
                "bas", "bes", "bis", "bos", "bus",
                "bar", "ber", "bir", "bor", "bur",
                "cam", "cem", "cim", "com", "cum",
                "can", "cen", "cin", "con", "cun",
                "cad", "ced", "cid", "cod", "cud",
                "cak", "cek", "cik", "cok", "cuk",
                "cas", "ces", "cis", "cos", "cus",
                "car", "cer", "cir", "cor", "cur",
                "dam", "dem", "dim", "dom", "dum",
                "dan", "den", "din", "don", "dun",
                "dad", "ded", "did", "dod", "dud",
                "dak", "dek", "dik", "dok", "duk",
                "das", "des", "dis", "dos", "dus",
                "dar", "der", "dir", "dor", "dur",
                "fam", "fem", "fim", "fom", "fum",
                "fan", "fen", "fin", "fon", "fun",
                "fad", "fed", "fid", "fod", "fud",
                "fak", "fek", "fik", "fok", "fuk",
                "fas", "fes", "fis", "fos", "fus",
                "far", "fer", "fir", "for", "fur",
                "gam", "gem", "gim", "gom", "gum",
                "gan", "gen", "gin", "gon", "gun",
                "gad", "ged", "gid", "god", "gud",
                "gak", "gek", "gik", "gok", "guk",
                "gas", "ges", "gis", "gos", "gus",
                "gar", "ger", "gir", "gor", "gur",
                "lam", "lem", "lim", "lom", "lum",
                "lan", "len", "lin", "lon", "lun",
                "lad", "led", "lid", "lod", "lud",
                "lak", "lek", "lik", "lok", "luk",
                "las", "les", "lis", "los", "lus",
                "lar", "ler", "lir", "lor", "lur",
                "nam", "nem", "nim", "nom", "num",
                "nan", "nen", "nin", "non", "nun",
                "nad", "ned", "nid", "nod", "nud",
                "nak", "nek", "nik", "nok", "nuk",
                "nas", "nes", "nis", "nos", "nus",
                "nar", "ner", "nir", "nor", "nur",
                "pam", "pem", "pim", "pom", "pum",
                "pan", "pen", "pin", "pon", "pun",
                "pad", "ped", "pid", "pod", "pud",
                "pak", "pek", "pik", "pok", "puk",
                "pas", "pes", "pis", "pos", "pus",
                "par", "per", "pir", "por", "pur",
                "ram", "rem", "rim", "rom", "rum",
                "ran", "ren", "rin", "ron", "run",
                "rad", "red", "rid", "rod", "rud",
                "rak", "rek", "rik", "rok", "ruk",
                "ras", "res", "ris", "ros", "rus",
                "rar", "rer", "rir", "ror", "rur",
                "sam", "sem", "sim", "som", "sum",
                "san", "sen", "sin", "son", "sun",
                "sad", "sed", "sid", "sod", "sud",
                "sak", "sek", "sik", "sok", "suk",
                "sas", "ses", "sis", "sos", "sus",
                "sar", "ser", "sir", "sor", "sur",
                "tam", "tem", "tim", "tom", "tum",
                "tan", "ten", "tin", "ton", "tun",
                "tad", "ted", "tid", "tod", "tud",
                "tak", "tek", "tik", "tok", "tuk",
                "tas", "tes", "tis", "tos", "tus",
                "tar", "ter", "tir", "tor", "tur",
                "vam", "vem", "vim", "vom", "vum",
                "van", "ven", "vin", "von", "vun",
                "vad", "ved", "vid", "vod", "vud",
                "vak", "vek", "vik", "vok", "vuk",
                "vas", "ves", "vis", "vos", "vus",
                "var", "ver", "vir", "vor", "vur",
                "wam", "wem", "wim", "wom", "wum",
                "wan", "wen", "win", "won", "wun",
                "wad", "wed", "wid", "wod", "wud",
                "wak", "wek", "wik", "wok", "wuk",
                "was", "wes", "wis", "wos", "wus",
                "war", "wer", "wir", "wor", "wur",
                "xam", "xem", "xim", "xom", "xum",
                "xan", "xen", "xin", "xon", "xun",
                "xad", "xed", "xid", "xod", "xud",
                "xak", "xek", "xik", "xok", "xuk",
                "xas", "xes", "xis", "xos", "xus",
                "xar", "xer", "xir", "xor", "xur",
                "yam", "yem", "yim", "yom", "yum",
                "yan", "yen", "yin", "yon", "yun",
                "yad", "yed", "yid", "yod", "yud",
                "yak", "yek", "yik", "yok", "yuk",
                "yas", "yes", "yis", "yos", "yus",
                "yar", "yer", "yir", "yor", "yur",
                "zam", "zem", "zim", "zom", "zum",
                "zan", "zen", "zin", "zon", "zun",
                "zad", "zed", "zid", "zod", "zud",
                "zak", "zek", "zik", "zok", "zuk",
                "zas", "zes", "zis", "zos", "zus",
                "zar", "zer", "zir", "zor", "zur",
                "-", ""
                ] 
   
    @classmethod
    def generate_words(cls, number_of_words, ruleset):
        words = []
        for i in range (number_of_words):
            if ruleset == 1:
               length = rand.randint(1, 4) 
               s  = "a"
               for j in range(length):
                   s += cls.syllables[rand.randint(0, len(cls.syllables) - 1)]
               words.append(s)
            elif ruleset == 2:
                s  = ""
                length = rand.randint(1, 4) 
                for j in range(length):
                   s += cls.syllables[rand.randint(0, len(cls.syllables) - 1)]
                s += "a"
                words.append(s)
            elif ruleset == 3:
                s = ""
                length = rand.randint(2, 8)
                for j in range(int(length / 2)):
                   s += cls.syllables[rand.randint(0, len(cls.syllables) - 1)]
                s  += "zaka" 
                for j in range(int(length / 2)):
                   s += cls.syllables[rand.randint(0, len(cls.syllables) - 1)]
                words.append(s)
            elif ruleset == 4:
                s = ""
                length = rand.randint(2, 6)
                for j in range(int(length / 2)):
                   s += cls.syllables[rand.randint(0, len(cls.syllables) - 1)]
                s += "-"
                for j in range(int(length / 2)):
                   s += cls.syllables[rand.randint(0, len(cls.syllables) - 1)]
                words.append(s)
            else:
                print ("non-existent ruleset") 
        
        return words

