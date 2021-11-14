#GAMEDATA
class CPerks():
    FIGHTINGMOOD = {
        "name":"Fighting Mood",
        "desc":"Can deal extra damage.",
        "heal":0,               #factor of heal
        "dmg":1.05,                #extra damage factor
        "negatechance":0,       #chance to negate hit
    }

    HEALINGMAGIC = {
        "name":"Healing Magic",
        "desc":"Has a chance to heal extra.",
        "heal":3,               #factor of heal
        "dmg":1,                #extra damage factor
        "negatechance":0,     #chance to negate hit
    }

    DODGE = {
        "name":"Dodge",
        "desc":"Chance to dodge hits.",
        "heal":0,               #factor of heal
        "dmg":1,                #extra damage factor
        "negatechance":15,       #chance to negate hit
    }


class CLASSLIST():
    NON = {
        "name":"Normal",
        "desc":"Select a class with `<selectclass [class]>`",
        "dmgm":1,   #class damage multiplyer
        "heal":0,       #class heal factor per round
        "tanks":1,      #class incoming damage multiplier
        "perks":"none",
    }

    FIGHTER = {
        "name":"Fighter",
        "desc":"Does more damage.",
        "dmgm":1.2,   #class damage multiplyer
        "heal":0,       #class heal factor per round
        "tanks":1,      #class incoming damage multiplier
        "perks":[CPerks.FIGHTINGMOOD]
    }

    MAGE = {
        "name":"Mage",
        "desc":"Can heal self but takes more damage and does less damage.",
        "dmgm":0.9,   #class damage multiplyer
        "heal":3,       #class heal factor per round
        "tanks":1.2,      #class incoming damage multiplier
        "perks":[CPerks.HEALINGMAGIC]
    }

    THIEF = {
        "name":"Thief",
        "desc":"Fast enough to dodge some hits.",
        "dmgm":1,   #class damage multiplyer
        "heal":0,       #class heal factor per round
        "tanks":1,      #class incoming damage multiplier
        "perks":[CPerks.DODGE]
    }

    TANK = {
        "name":"Tank",
        "desc":"Takes less damage.",
        "dmgm":1,   #class damage multiplyer
        "heal":0,       #class heal factor per round
        "tanks":0.8,      #class incoming damage multiplier
        "perks":"none",
    }

    DARKMAGE = {
        "name":"Dark Mage",
        "desc":"Uses magic to be stronger.",
        "dmgm":1.2,
        "heal":5,
        "tanks":1.5,
        "perks":"none",
    }
    
    ASSASSIN = {
        "name":"Assassin",
        "desc":"Does a lot of damage, but at what cost.",
        "dmgm":1.3,   #class damage multiplyer
        "heal":0,       #class heal factor per round
        "tanks":1.5,      #class incoming damage multiplier
        "perks":"none",
    }

class WPerks():
    BLADE = {
        "name":"Blade",
        "desc":"Shaaaaaaarp.",
        "dmg":0,        #extra dmg %
        "sharp":5,      #normal damage % added
        "shieldbreak":0,#% of normal damage ignoring shield/armor
        "heal":0,       #% heal per use
    }

    DOUBLESHOT = {
        "name":"Double Shot",
        "desc":"Its 2.",
        "dmg":10,       #extra dmg %
        "sharp":0,      #normal damage % added
        "shieldbreak":0,#% of normal damage ignoring shield/armor
        "heal":0,       #% heal per use
    }

    MAGICATK = {
        "name":"Magic Attack",
        "desc":"Nothing can protect against this.",
        "dmg":0,       #extra dmg %
        "sharp":0,      #normal damage % added
        "shieldbreak":100,#% of normal damage ignoring shield/armor
        "heal":0,       #% heal per use
    }

    PIERCE = {
        "name":"Pierce",
        "desc":"It can penetrate even the hardest armor.",
        "dmg":0,       #extra dmg %
        "sharp":0,      #normal damage % added
        "shieldbreak":50,#% of normal damage ignoring shield/armor
        "heal":0,       #% heal per use
    }

    FREEZE = {
        "name":"Freeze",
        "desc":"Makes the enemys shield weaker.",
        "dmg":5,       #extra dmg %
        "sharp":5,      #normal damage % added
        "shieldbreak":30,#% of normal damage ignoring shield/armor
        "heal":5,       #% heal per use
    }

    MANAFLUX = {
        "name":"Mana Flux",
        "desc":"Heals you using mana.",
        "dmg":0,       #extra dmg %
        "sharp":0,      #normal damage % added
        "shieldbreak":0,#% of normal damage ignoring shield/armor
        "heal":5,       #% heal per use
    }

    BURN = {
        "name":"Burn",
        "desc":"Burns enemies.",
        "dmg":15,       #extra dmg %
        "sharp":0,      #normal damage % added
        "shieldbreak":0,#% of normal damage ignoring shield/armor
        "heal":0,       #% heal per use
    }

    DIVINE = {
        "name":"Divine",
        "desc":"Heavenly power.",
        "dmg":5,       #extra dmg %
        "sharp":5,      #normal damage % added
        "shieldbreak":15,#% of normal damage ignoring shield/armor
        "heal":10,       #% heal per use
    }

    SLIFESTEAL = {
        "name":"Small Life Steal",
        "desc":"Smol.",
        "dmg":0,       #extra dmg %
        "sharp":0,      #normal damage % added
        "shieldbreak":0,#% of normal damage ignoring shield/armor
        "heal":5,       #% heal per use
    }

    DRAWLIFEFORCE = {
        "name":"Draw Life Force",
        "desc":"Gone.",
        "dmg":0,       #extra dmg %
        "sharp":0,      #normal damage % added
        "shieldbreak":0,#% of normal damage ignoring shield/armor
        "heal":15,       #% heal per use
    }


class Weapons():
    STICK = {
        "name":"Stick",
        "desc":"Bonk.",
        "dmg":10,       #damage factor
        "perks":"none",   
        "rarity":"free",
    }

    SWORD = {
        "name":"Sword",
        "desc":"You can hit things with it.",
        "dmg":13,       #damage factor
        "perks":[WPerks.BLADE],
        "rarity":"common",
    }

    DAGGER = {
        "name":"Dagger",
        "desc":"Stab stab stab.",
        "dmg":10,       #damage factor
        "perks":[WPerks.BLADE, WPerks.PIERCE],
        "rarity":"common",
    }

    WEAKWAND = {
        "name":"Weak Wand",
        "desc":"It looks very damaged.",
        "dmg":9,       #damage factor
        "perks":[WPerks.MAGICATK],
        "rarity":"common",
    }

    SHORTSWORD = {
        "name":"Short Sword",
        "desc":"Tiny af.",
        "dmg":9,       #damage factor
        "perks":[WPerks.BLADE],
        "rarity":"common",
    }

    STEELSWORD = {
        "name":"Steel Sword",
        "desc":"Made from Steel.",
        "dmg":15,       #damage factor
        "perks":[WPerks.BLADE],   
        "rarity":"normal",
    }

    GIANTROCK = {
        "name":"Giant Rock",
        "desc":"Heavy enough to crush any enemy (if you could lift it properly).",
        "dmg":20,       #damage factor
        "perks":"none",   
        "rarity":"normal",
    }

    ENHANCEDSWORD = {
        "name":"Enhanced Sword",
        "desc":"Its a sword but better.",
        "dmg":13,       #damage factor
        "perks":[WPerks.BLADE, WPerks.PIERCE],   
        "rarity":"normal",
    }

    BONESWORD = {
        "name":"Bone Sword",
        "desc":"A sharp blade crafted from a bone. Is it human?!",
        "dmg":16,       #damage factor
        "perks":[WPerks.BLADE],   
        "rarity":"normal",
    }

    BOW = {
        "name":"Bow",
        "desc":"It shoots arrows.",
        "dmg":10,       #damage factor
        "perks":[WPerks.DOUBLESHOT],   
        "rarity":"uncommon",
    }

    PUREGOLDSWORD = {
        "name":"Pure Gold Sword",
        "desc":"Bling Bling.",
        "dmg":20,       #damage factor
        "perks":[WPerks.BLADE],   
        "rarity":"uncommon",
    }

    MANACATALYST = {
        "name":"Mana Catalyst",
        "desc":"It radiates magic energy.",
        "dmg":20,       #damage factor
        "perks":[WPerks.MANAFLUX],   
        "rarity":"uncommon",
    }

    VAMPIRETOOTH = {
        "name":"Vampire Tooth",
        "desc":"It from a real vampire.",
        "dmg":20,       #damage factor
        "perks":[WPerks.SLIFESTEAL],
        "rarity":"uncommon",
    }

    DAMAGEWAND = {
        "name":"Wand of Damage",
        "desc":"Passes straight through Armor.",
        "dmg":25,       #damage factor
        "perks":[WPerks.MAGICATK],   
        "rarity":"rare",
    }

    BIGCANNON = {
        "name":"Big Cannon",
        "desc":"It goes boom.",
        "dmg":30,       #damage factor
        "perks":"none",   
        "rarity":"rare",
    }

    FIREWAND = {
        "name":"Fire Wand",
        "desc":"Burn it down.",
        "dmg":15,       #damage factor
        "perks":[WPerks.BURN],   
        "rarity":"rare",
    }

    ICEWAND = {
        "name":"Ice Wand",
        "desc":"Brrrr cold.",
        "dmg":15,       #damage factor
        "perks":[WPerks.FREEZE],   
        "rarity":"rare",
    }

    STREAMWAND = {
        "name":"Stream Wand",
        "desc":"Water.",
        "dmg":20,       #damage factor
        "perks":"none",   
        "rarity":"rare",
    }

    FIRESWORD = {
        "name":"Burning Sword",
        "desc":"Its lit.",
        "dmg":20,       #damage factor
        "perks":[WPerks.BLADE,WPerks.BURN],   
        "rarity":"very rare",
    }

    CRYSTALSWORD = {
        "name":"Crystal Sword",
        "desc":"Reflections, refractions.",
        "dmg":25,       #damage factor
        "perks":[WPerks.BLADE,WPerks.PIERCE],   
        "rarity":"very rare",
    }

    WATERMANIPULATOR = {
        "name":"Water Manipulator",
        "desc":"Swooooosh.",
        "dmg":35,       #damage factor
        "perks":"none",   
        "rarity":"very rare",
    }

    SCYTHE = {
        "name":"Scythe",
        "desc":"Cool.",
        "dmg":35,       #damage factor
        "perks":"none",   
        "rarity":"very rare",
    }

    KATANA = {
        "name":"Katana",
        "desc":"The iron of this sword has been folded 20 times.",
        "dmg":35,       #damage factor
        "perks":"none",   
        "rarity":"very rare",
    }

    SPIRITSLICER = {
        "name":"Spirit Slicer",
        "desc":"A sword said to have killed many mythical beats. This Katana can freeze its enemies instantly.",
        "dmg":30,       #damage factor
        "perks":[WPerks.FREEZE],   
        "rarity":"epic",
    }

    LANCEOFSTARS = {
        "name":"Lance of Stars",
        "desc":"Uses the power of the stars to deal damage.",
        "dmg":45,       #damage factor
        "perks":[WPerks.PIERCE, WPerks.BLADE],   
        "rarity":"epic",
    }

    DARKORB = {
        "name":"Dark Orb",
        "desc":"Collects from the darkness to use its power.",
        "dmg":35,       #damage factor
        "perks":[WPerks.MAGICATK],   
        "rarity":"epic",
    }

    STEELGAUNTLETS = {
        "name":"Steel Gauntlets",
        "desc":"Hard and sturdy.",
        "dmg":50,       #damage factor
        "perks":"none",   
        "rarity":"epic",
    }

    MORNINGSTAR = {
        "name":"Morning Star",
        "desc":"A heavy duty weapon.",
        "dmg":50,       #damage factor
        "perks":"none",   
        "rarity":"epic",
    }

    DRAGONSWORD = {
        "name":"Dragon Sword",
        "desc":"This Sword was forged from a dragons blood.",
        "dmg":50,       #damage factor
        "perks":[WPerks.BLADE],   
        "rarity":"unstable",
    }

    AXEOFDESTRUCTION = {
        "name":"Axe of Destruction",
        "desc":"Swung by the right hands it can destroy the balance of heaven and hell.",
        "dmg":60,       #damage factor
        "perks":"none",   
        "rarity":"unstable",
    }

    HELLMETALSWORD = {
        "name":"Hellmetal Sword",
        "desc":"This Sword was forged in the depths of hell.",
        "dmg":45,       #damage factor
        "perks":[WPerks.BURN],   
        "rarity":"unstable",
    }

    SHURIKEN = {
        "name":"Shuriken",
        "desc":"Spikey.",
        "dmg":55,       #damage factor
        "perks":[WPerks.PIERCE],   
        "rarity":"unstable",
    }

    CLAYMORE = {
        "name":"Claymore",
        "desc":"Huge.",
        "dmg":50,       #damage factor
        "perks":[WPerks.BLADE],   
        "rarity":"unstable",
    }

    SUNRAY = {
        "name":"Pure Sunray",
        "desc":"The power of the sun captured by magic.",
        "dmg":60,       #damage factor
        "perks":[WPerks.MAGICATK],   
        "rarity":"corrupted",
    }

    LINKBREAKER = {
        "name":"Link Breaker",
        "desc":"This blade can seperate a soul from its body.",
        "dmg":75,       #damage factor
        "perks":"none",   
        "rarity":"corrupted",
    }

    DIVINESTAFF = {
        "name":"Divine Staff",
        "desc":"A gift from the heavens.",
        "dmg":45,       #damage factor
        "perks":[WPerks.DIVINE],   
        "rarity":"corrupted",
    }

    REAPERSCYTHE = {
        "name":"Reaper Scythe",
        "desc":"Spooky scary skeletons.",
        "dmg":70,       #damage factor
        "perks":"none",   
        "rarity":"corrupted",
    }

    NULLW = {
        "name":"Null",
        "desc":"This weapon does not exist. Or does it?",
        "dmg":70,       #damage factor
        "perks":"none",   
        "rarity":"corrupted",
    }

    BETASWORD = {
        "name":"Beta Sword",
        "desc":"Limited time only.",
        "dmg":35,       #damage factor
        "perks":"none",   
        "rarity":"limited",
    }

    AIRBLADE = {
        "name":"Air Blade",
        "desc":"A blade made from air.",
        "dmg":35,       #damage factor
        "perks":[WPerks.BLADE],   
        "rarity":"limited",
    }

    HIVESLICER = {
        "name":"Hive Slicer",
        "desc":"Pain.",
        "dmg":55,       #damage factor
        "perks":[WPerks.PIERCE],   
        "rarity":"unique",
    }

    LIFEEXTRACTOR = {
        "name":"Life Extractor",
        "desc":"It collects all the life force of the struck opponent.",
        "dmg":50,       #damage factor
        "perks":[WPerks.DRAWLIFEFORCE],   
        "rarity":"unique",
    }


class APerks():
    HARDENED = {
        "name":"Hardened",
        "desc":"Looks Solid.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.8, #incoming damage multiplier
        "negatechance":0,  #chance to negate hit 
        "returndmg":0,      #% of incoming damage returned
    }

    SMALLREFLECT = {
        "name":"Small Reflect",
        "desc":"It bounces back some attacks.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "negatechance":0,  #chance to negate hit 
        "returndmg":5,      #% of incoming damage returned
    }

    BURN = {
        "name":"Burn",
        "desc":"Ouch.",
        "dmg":20,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "negatechance":0,  #chance to negate hit 
        "returndmg":0,      #% of incoming damage returned
    }

    GAMBLE = {
        "name":"Gamble of Life",
        "desc":"The bet is your life.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "negatechance":50,  #chance to negate hit 
        "returndmg":200,      #% of incoming damage returned
    }

    REFRACT = {
        "name":"Refraction",
        "desc":"Send the damage away from you. sometimes.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "negatechance":5,  #chance to negate hit 
        "returndmg":0,      #% of incoming damage returned
    }

    ENERGY = {
        "name":"Energy",
        "desc":"It hurts to touch.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "negatechance":10,  #chance to negate hit 
        "returndmg":25,      #% of incoming damage returned
    }

    SPIKE = {
        "name":"Spike",
        "desc":"Did I just get stabbed by armor?",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "negatechance":10,  #chance to negate hit 
        "returndmg":25,      #% of incoming damage returned
    }


class Armor():
    NAKED = {
        "name":"Naked",
        "desc":"Broke.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1,   #incoming damage multiplier
        "perks":"none",
        "rarity":"free",
    }

    PANTS = {
        "name":"Pants",
        "desc":"At least you are wearing something.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.99,   #incoming damage multiplier
        "perks":"none",
        "rarity":"common",
    }

    ROBE = {
        "name":"Robe",
        "desc":"It looks cool.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.99,   #incoming damage multiplier
        "perks":"none",
        "rarity":"common",
    }

    UNDERPANTS = {
        "name":"Underpants",
        "desc":"Cover the pp.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.99,   #incoming damage multiplier
        "perks":"none",
        "rarity":"common",
    }

    BOOTS = {
        "name":"Boots",
        "desc":"Walk stable.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.99,   #incoming damage multiplier
        "perks":"none",
        "rarity":"common",
    }

    CHAINMAIL = {
        "name":"Chainmail Armor",
        "desc":"The Basics.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.9,   #incoming damage multiplier
        "perks":"none",
        "rarity":"normal",
    }

    STONEARMOR = {
        "name":"Stone Armor",
        "desc":"Heavy.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.9,   #incoming damage multiplier
        "perks":"none",
        "rarity":"normal",
    }

    WIND = {
        "name":"Wind",
        "desc":"The wind surrounds you to block attacks(it doesn't work).",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.95,   #incoming damage multiplier
        "perks":"none",
        "rarity":"normal",
    }

    WOOD = {
        "name":"Wood Armor",
        "desc":"Let the power of nature protect you.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.93,   #incoming damage multiplier
        "perks":"none",
        "rarity":"normal",
    }

    STEEL = {
        "name":"Steel Armor",
        "desc":"It feels Hard.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.9, #incoming damage multiplier
        "perks":[APerks.HARDENED],
        "rarity":"uncommon",
    }

    HARDENEDSTONE = {
        "name":"Hardened Stone Armor",
        "desc":"Its not THAT hard.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.8, #incoming damage multiplier
        "perks":"none",
        "rarity":"uncommon",
    }

    SWORDARMOR = {
        "name":"Sword Armor",
        "desc":"Armor made from swords.",
        "dmg":7,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "perks":"none",
        "rarity":"uncommon",
    }

    HARDENEDSKIN = {
        "name":"Hardened Skin",
        "desc":"Harden your skin.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.85, #incoming damage multiplier
        "perks":"none",
        "rarity":"uncommon",
    }

    HARDENEDSTEEL = {
        "name":"Hardened Steel Armor",
        "desc":"Hardened with a special furnace.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.85, #incoming damage multiplier
        "perks":[APerks.HARDENED],
        "rarity":"rare",
    }

    THINCRYSTAL = {
        "name":"Thin Crystal Armor",
        "desc":"If only it wasn't so thin.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.9, #incoming damage multiplier
        "perks":[APerks.REFRACT],
        "rarity":"rare",
    }

    VOLCANOARMOR = {
        "name":"Volcano Armor",
        "desc":"Steel armor dipped in lava.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.75, #incoming damage multiplier
        "perks":"none",
        "rarity":"rare",
    }

    PLATEDARMOR = {
        "name":"Plated Armor",
        "desc":"Steel armor with stone plates.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.75, #incoming damage multiplier
        "perks":"none",
        "rarity":"rare",
    }

    HARDENEDWATER = {
        "name":"Hardened Water Armor",
        "desc":"But how is he do it?",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.77, #incoming damage multiplier
        "perks":"none",
        "rarity":"rare",
    }

    MAGICROBE = {
        "name":"Magic Robes",
        "desc":"They look comfortable.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":5,   #healed % when hit
        "tank":0.90, #incoming damage multiplier
        "perks":[APerks.SMALLREFLECT],
        "rarity":"very rare",
    }

    MANTLEOFDEATH = {
        "name":"Mantle of Death",
        "desc":"Ouch.",
        "dmg":10,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.95, #incoming damage multiplier
        "perks":"none",
        "rarity":"very rare",
    }

    ENERGYARMOR = {
        "name":"Energy Armor",
        "desc":"Made from pure energy.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "perks":[APerks.ENERGY],
        "rarity":"very rare",
    }

    DARKMANTLE = {
        "name":"Dark Mantle",
        "desc":"Creep.",
        "dmg":20,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "perks":"none",
        "rarity":"very rare",
    }

    AURA = {
        "name":"Aura",
        "desc":"Your Aura is strong.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.85, #incoming damage multiplier
        "perks":"none",
        "rarity":"very rare",
    }

    CURSEDSTONE = {
        "name":"Cursed Stone Armor",
        "desc":"It stinks.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.7, #incoming damage multiplier
        "perks":"none",
        "rarity":"epic",
    }

    MAGICSTEEL = {
        "name":"Magic Steel Armor",
        "desc":"Mana infused steel.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":5,   #healed % when hit
        "tank":0.8, #incoming damage multiplier
        "perks":"none",
        "rarity":"epic",
    }

    DOUBLEARMOR = {
        "name":"Double Armor",
        "desc":"Its 2 armor sets. Why didn't we think of this earlier?",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.7, #incoming damage multiplier
        "perks":"none",
        "rarity":"epic",
    }

    MAGICARMOR = {
        "name":"Magic Armor",
        "desc":"It protects and heals.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":5,   #healed % when hit
        "tank":0.85, #incoming damage multiplier
        "perks":[APerks.SMALLREFLECT],
        "rarity":"epic",
    }

    SPIKEARMOR = {
        "name":"Spike Armor",
        "desc":"Like sword armor but better.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.85, #incoming damage multiplier
        "perks":[APerks.SPIKE],
        "rarity":"epic",
    }

    FIREGOLEM = {
        "name":"Armor of the Fire Golem",
        "desc":"This Armor is made from a dead Fire Golem.",
        "dmg":30,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.9, #incoming damage multiplier
        "perks":[APerks.BURN],
        "rarity":"unstable",
    }

    CRYSTALARMOR = {
        "name":"Crystal Armor",
        "desc":"It splits light and your enemies attacks.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.7, #incoming damage multiplier
        "perks":[APerks.REFRACT],
        "rarity":"unstable",
    }

    BLACKMAGICROBE = {
        "name":"Robe of Black Magic",
        "desc":"Radiates energy from the ones you have slain.",
        "dmg":20,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.85, #incoming damage multiplier
        "perks":"none",
        "rarity":"unstable",
    }

    TRIPLEARMOR = {
        "name":"Triple Armor",
        "desc":"3??!!.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.7, #incoming damage multiplier
        "perks":"none",
        "rarity":"unstable",
    }

    DRAGONMAIL = {
        "name":"Dragonmail Armor",
        "desc":"Made from a Dragons Skin.",
        "dmg":15,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.87, #incoming damage multiplier
        "perks":"none",
        "rarity":"unstable",
    }

    CORESMELTER = {
        "name":"Core Smelter Armor",
        "desc":"Legend has it this armor was made from the metals of THE EARTHS CORE.",
        "dmg":30,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.7, #incoming damage multiplier
        "perks":"none",
        "rarity":"corrupted",
    }

    GAMBLERS = {
        "name":"Gamblers Ruin Armor",
        "desc":"Its all in.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "perks":[APerks.GAMBLE],
        "rarity":"corrupted",
    }

    FIBREOFHATRED = {
        "name":"Fibre of Hatred",
        "desc":"Woven from a fine fibre made from tortured souls.",
        "dmg":40,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.9, #incoming damage multiplier
        "perks":"none",
        "rarity":"corrupted",
    }

    QUADRUPLEARMOR = {
        "name":"Quadruple Armor",
        "desc":"Its 4 Armor.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.6, #incoming damage multiplier
        "perks":"none",
        "rarity":"corrupted",
    }

    MANAARMOR = {
        "name":"Mana Armor",
        "desc":"Made from pure mana.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":20,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "perks":"none",
        "rarity":"corrupted",
    }

    BETAARMOR = {
        "name":"Beta Armor",
        "desc":"Limited time only.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":3,   #healed % when hit
        "tank":0.8, #incoming damage multiplier
        "perks":"none",
        "rarity":"limited",
    }

    OVERGROWN = {
        "name":"Overgrown Armor",
        "desc":"The power of nature.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":3,   #healed % when hit
        "tank":0.8, #incoming damage multiplier
        "perks":"none",
        "rarity":"limited",
    }

    WORLDARMOR = {
        "name":"World Armor",
        "desc":"It is made from the fabric of reality.",
        "dmg":30,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.7, #incoming damage multiplier
        "perks":"none",
        "rarity":"unique",
    }

    DEMONICARMOR = {
        "name":"Demonic Armor",
        "desc":"This armor can be forged at the death of a high demon.",
        "dmg":40,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":0.66, #incoming damage multiplier
        "perks":"none",
        "rarity":"unique",
    }


class Extra():
    NOTHING = {
        "name":"Nothing",
        "desc":"Empty Handed.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"free"
    }

    LIGHTBUG = {
        "name":"Light Bug",
        "desc":"Bzzzzz.",
        "dmg":1,   #final damage multiplier
        "heal":1,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"common"
    }

    EYEPROTECTION = {
        "name":"Eye Protection",
        "desc":"Allways wear eye protection.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.98, #final incoming damage multiplier
        "rarity":"common"
    }

    WATER = {
        "name":"Water",
        "desc":"Its water.",
        "dmg":1.1,   #final damage multiplier
        "heal":1,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"common"
    }

    WORM = {
        "name":"Worm",
        "desc":"Its Mr. Worm.",
        "dmg":1,   #final damage multiplier
        "heal":1,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"common"
    }

    BLADESHARPENER = {
        "name":"Blade Sharpener",
        "desc":"A dull blade is no blade at all.",
        "dmg":1.1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"normal"
    }

    TURBOSHROOM = {
        "name":"Turboshroom",
        "desc":"We'll think about the health benefits later.",
        "dmg":1.1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"normal"
    }

    BEE = {
        "name":"Bee",
        "desc":"Sting.",
        "dmg":1.1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"normal"
    }

    LANTERN = {
        "name":"Lantern",
        "desc":"See where you strike.",
        "dmg":1.1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"normal"
    }

    LIGHTSHIELD = {
        "name":"Light Shield",
        "desc":"This will stop something.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.9, #final incoming damage multiplier
        "rarity":"uncommon"
    }

    TOOLBOX = {
        "name":"Toolbox",
        "desc":"Lets see what we can do.",
        "dmg":1.2,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"uncommon"
    }

    SPIDER = {
        "name":"Spider",
        "desc":"Your own spooder.",
        "dmg":1.15,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"uncommon"
    }

    BRIGHTLIGHT = {
        "name":"Bright Light",
        "desc":"Blind your opponent.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.95, #final incoming damage multiplier
        "rarity":"uncommon"
    }

    HEALWAND = {
        "name":"Healing Wand",
        "desc":"Bling Blong and your wounds are gone!",
        "dmg":1,   #final damage multiplier
        "heal":5,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"rare"
    }

    STRENGTHWAND = {
        "name":"Strength Wand",
        "desc":"I got the power.",
        "dmg":1.22,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"rare"
    }

    TIMEBENDER = {
        "name":"Timebender",
        "desc":"Warp time.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.9, #final incoming damage multiplier
        "rarity":"rare"
    }

    DOG = {
        "name":"Dog",
        "desc":"Helper.",
        "dmg":1.2,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"rare"
    }

    DMGGEM = {
        "name":"Damage Gem",
        "desc":"Small stone small damage.",
        "dmg":1.2,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"rare"
    }

    HEAVYSHIELD = {
        "name":"Heavy Shield",
        "desc":"Made from solid steel.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.8, #final incoming damage multiplier
        "rarity":"very rare"
    }

    RADIANCEWAND = {
        "name":"Radiance Wand",
        "desc":"Feel the power.",
        "dmg":1.15,   #final damage multiplier
        "heal":5,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"very rare"
    }

    PAINKILLER = {
        "name":"Painkiller",
        "desc":"It kills the pain.",
        "dmg":1,   #final damage multiplier
        "heal":8,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"very rare"
    }

    CAT = {
        "name":"Cat",
        "desc":"Meow.",
        "dmg":1.3,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"very rare"
    }

    CASTERAMULET = {
        "name":"Caster Amulet",
        "desc":"Casts different magic for you.",
        "dmg":1.1,   #final damage multiplier
        "heal":3,   #healed % per round
        "tank":0.97, #final incoming damage multiplier
        "rarity":"very rare"
    }

    SUPERSHIELD = {
        "name":"Supershield",
        "desc":"A magic protection bubble.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.7, #final incoming damage multiplier
        "rarity":"epic"
    }

    LIGHTCOLLECTOR = {
        "name":"Light Collector",
        "desc":"Collects light to heal you.",
        "dmg":1,   #final damage multiplier
        "heal":10,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"epic"
    }

    SHARDOFDARKNESS = {
        "name":"Shard of Darkness",
        "desc":"The energy it holds is incredible.",
        "dmg":1.3,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"epic"
    }

    HARDHAT = {
        "name":"Hardhat",
        "desc":"Its very hard.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.85, #final incoming damage multiplier
        "rarity":"epic"
    }

    BIOOVERCLOCKER = {
        "name":"Bio Overclocker",
        "desc":"Enhances your body.",
        "dmg":1.2,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.9, #final incoming damage multiplier
        "rarity":"epic"
    }

    CLONEATK = {
        "name":"Clone Attacker",
        "desc":"A copy of your weapon that strikes with you.",
        "dmg":2,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1.2, #final incoming damage multiplier
        "rarity":"unstable"
    }

    PUREHELL = {
        "name":"Pure Hell",
        "desc":"Lights your tools on fire.",
        "dmg":1.5,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"unstable"
    }

    DRAGONSCALE = {
        "name":"Dragon Scale",
        "desc":"It has the power of a dragon in it.",
        "dmg":1.2,   #final damage multiplier
        "heal":5,   #healed % per round
        "tank":0.9, #final incoming damage multiplier
        "rarity":"unstable"
    }

    MAGICMIRROR = {
        "name":"Magic Mirror",
        "desc":"Reflect damage away from you.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.75, #final incoming damage multiplier
        "rarity":"unstable"
    }

    CARBONSHIELD = {
        "name":"Carbon Shield",
        "desc":"Light and hard.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.75, #final incoming damage multiplier
        "rarity":"unstable"
    }

    BLACKMAGICWAND = {
        "name":"Black Magic Wand",
        "desc":"/§$%)§=%/%(&",
        "dmg":1.5,   #final damage multiplier
        "heal":10,   #healed % per round
        "tank":0.5, #final incoming damage multiplier
        "rarity":"corrupted"
    }

    CRIMSONDAGGER = {
        "name":"Crimson Dagger",
        "desc":"Sacrifice your blood for damage.",
        "dmg":1.4,   #final damage multiplier
        "heal":-7,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"corrupted"
    }

    MOONREFRACTOR = {
        "name":"Moon Refractor",
        "desc":"Absorb the moons power and turn it into damage.",
        "dmg":1.3,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"corrupted"
    }

    FIREORB = {
        "name":"Fire Orb",
        "desc":"Light your opponents on fire.",
        "dmg":1.28,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"corrupted"
    }

    ARM3 = {
        "name":"Arm 3",
        "desc":"A third arm.",
        "dmg":1.5,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"corrupted"
    }

    BETASHIELD = {
        "name":"Beta Shield",
        "desc":"Limited time only.",
        "dmg":1,   #final damage multiplier
        "heal":5,   #healed % per round
        "tank":0.9, #final incoming damage multiplier
        "rarity":"limited"
    }

    SIRENSSONG = {
        "name":"Sirens Song",
        "desc":"Laaaaaaaaaaalalalalla.",
        "dmg":1,   #final damage multiplier
        "heal":5,   #healed % per round
        "tank":0.9, #final incoming damage multiplier
        "rarity":"limited"
    }

    GOBLINCHARM = {
        "name":"Goblin Charm",
        "desc":"Ew.",
        "dmg":1,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":0.85, #final incoming damage multiplier
        "rarity":"unique"
    }

    POWERORB = {
        "name":"Power Orb",
        "desc":"Full of centuries worth of power.",
        "dmg":1.6,   #final damage multiplier
        "heal":0,   #healed % per round
        "tank":1, #final incoming damage multiplier
        "rarity":"unique"
    }


class MPerks():
    STICKY = {
        "name":"Sticky",
        "desc":"Disgusting.",
        "dmg":0,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1, #incoming damage multiplier
        "negatechance":1,  #chance to negate hit 
        "returndmg":0,      #% of incoming damage returned
    }

    BURN = {
        "name":"Burn",
        "desc":"So so hot.",
        "dmg":5,    #damage factor dealt back when hit
        "heal":0,   #healed % when hit
        "tank":1.2, #incoming damage multiplier
        "negatechance":0,  #chance to negate hit 
        "returndmg":0,      #% of incoming damage returned
    }

    SHATTER = {
        "name":"Shatter",
        "desc":"It shal break.",
        "dmg":25,
        "heal":0,
        "tank":1,
        "negatechance":0,
        "returndmg":0,
    }

    DEATH = {
        "name":"Death",
        "desc":"Looks can kill.",
        "dmg":0,
        "heal":0,
        "tank":1,
        "negatechance":0,
        "returndmg":75,
    }

    POISON = {
        "name":"Poison",
        "desc":"Don't taste test.",
        "dmg":0,
        "heal":0,
        "tank":1,
        "negatechance":0,
        "returndmg":50,
    }

    DIVINE = {
        "name":"Devine",
        "desc":"Godly blessing.",
        "dmg":0,
        "heal":50,
        "tank":1,
        "negatechance":0,
        "returndmg":0,
    }

    HELLISH = {
        "name":"Hellish",
        "desc":"Straight from hell.",
        "dmg":0,
        "heal":50,
        "tank":1,
        "negatechance":0,
        "returndmg":0,
    }


class Monster():
    SLIME = {
        "name":"Slime",
        "desc":"Slimey Slime.",
        "dmg":7,
        "heal":10,
        "hp":50,
        "tank":1,
        "perks":[MPerks.STICKY],
        "minlvl":0,
    }

    EVILMONK = {
        "name":"Evil Monk",
        "desc":"He prays for the death of his enemies.",
        "dmg":12,
        "heal":5,
        "hp":25,
        "tank":1,
        "perks":"none",
        "minlvl":0,
    }

    CURSEDROCK = {
        "name":"Cursed Rock",
        "desc":"A Rock that has been cursed to roll forever.",
        "dmg":5,
        "heal":5,
        "hp":50,
        "tank":0.8,
        "perks":"none",
        "minlvl":0,
    }

    EVILDOG = {
        "name":"Evil Dog",
        "desc":"Its will bite you.",
        "dmg":5,
        "heal":5,
        "hp":55,
        "tank":1,
        "perks":"none",
        "minlvl":0,
    }

    LIZARD = {
        "name":"Lizard",
        "desc":"It looks like a dragon.",
        "dmg":9,
        "heal":5,
        "hp":40,
        "tank":1,
        "perks":"none",
        "minlvl":0,
    }

    GOBLIN = {
        "name":"Goblin",
        "desc":"Greedy bastard.",
        "dmg":23,
        "heal":0,
        "hp":70,
        "tank":0.8,
        "perks":"none",
        "minlvl":5,
    }

    DRAGONFLY = {
        "name":"Dragonfly",
        "desc":"It sounds scary but its not.",
        "dmg":20,
        "heal":15,
        "hp":35,
        "tank":1.5,
        "perks":"none",
        "minlvl":5,
    }

    SKELETON = {
        "name":"Skeleton",
        "desc":"Spooky and scary.",
        "dmg":25,
        "heal":0,
        "hp":45,
        "tank":.8,
        "perks":"none",
        "minlvl":5,
    }

    LIGHTNING = {
        "name":"Lightning",
        "desc":"He will strike you(once).",
        "dmg":50,
        "heal":0,
        "hp":30,
        "tank":1,
        "perks":"none",
        "minlvl":5,
    }

    OGRE = {
        "name":"Ogre",
        "desc":"Big Man.",
        "dmg":20,
        "heal":0,
        "hp":30,
        "tank":0.75,
        "perks":"none",
        "minlvl":5,
    }

    STONEGOLEM = {
        "name":"Stone Golem",
        "desc":"Rock solid.",
        "dmg":30,
        "heal":0,
        "hp":90,
        "tank":0.75,
        "perks":"none",
        "minlvl":15,
    }

    SMOKE = {
        "name":"Smoke",
        "desc":"Blow it away.",
        "dmg":10,
        "heal":20,
        "hp":60,
        "tank":1.5,
        "perks":[MPerks.POISON],
        "minlvl":15,
    }

    ICEWIZARD = {
        "name":"Ice Wizard",
        "desc":"Cold Hearted.",
        "dmg":20,
        "heal":20,
        "hp":55,
        "tank":1.3,
        "perks":[MPerks.SHATTER],
        "minlvl":15,
    }

    FIREWIZARD = {
        "name":"Fire Wizard",
        "desc":"Hot (not in that way).",
        "dmg":30,
        "heal":20,
        "hp":55,
        "tank":1,
        "perks":[MPerks.BURN],
        "minlvl":15,
    }

    WIZARD = {
        "name":"Wizard",
        "desc":"Magic.",
        "dmg":35,
        "heal":25,
        "hp":55,
        "tank":1,
        "perks":"none",
        "minlvl":15,
    }

    FIREGOLEM = {
        "name":"Fire Golem",
        "desc":"It burns.",
        "dmg":40,
        "heal":0,
        "hp":110,
        "tank":0.8,
        "perks":[MPerks.BURN],
        "minlvl":25,
    }

    GIANTSPIDER = {
        "name":"Giant Spider",
        "desc":"Ewwwwwww.",
        "dmg":50,
        "heal":0,
        "hp":100,
        "tank":1,
        "perks":"none",
        "minlvl":25,
    }

    GHOST = {
        "name":"Ghost",
        "desc":"Boo.",
        "dmg":45,
        "heal":10,
        "hp":50,
        "tank":0.5,
        "perks":"none",
        "minlvl":25,
    }

    ANCIENTSPIRIT = {
        "name":"Ancient Spirit",
        "desc":"Put salt on it.",
        "dmg":45,
        "heal":15,
        "hp":55,
        "tank":0.5,
        "perks":"none",
        "minlvl":25,
    }

    VAMPIRE = {
        "name":"Vampire",
        "desc":"One garlic a day keeps the vampire away.",
        "dmg":50,
        "heal":25,
        "hp":50,
        "tank":1.2,
        "perks":"none",
        "minlvl":25,
    }

    BLACKDRAGON = {
        "name":"Black Dragon",
        "desc":"Scary.",
        "dmg":35,
        "heal":10,
        "hp":150,
        "tank":0.5,
        "perks":"none",
        "minlvl":45,
    }

    REAPER = {
        "name":"Reaper",
        "desc":"Death comes.",
        "dmg":15,
        "heal":0,
        "hp":100,
        "tank":1,
        "perks":[MPerks.DEATH],
        "minlvl":45,
    }

    ARCHANGEL = {
        "name":"Archangel",
        "desc":"Holy.",
        "dmg":10,
        "heal":10,
        "hp":60,
        "tank":1,
        "perks":[MPerks.DIVINE],
        "minlvl":45,
    }

    DEVILSMINION = {
        "name":"Devils Minion",
        "desc":"Hellish.",
        "dmg":10,
        "heal":10,
        "hp":60,
        "tank":1,
        "perks":[MPerks.HELLISH],
        "minlvl":45,
    }

    CORRUPTEDSPIRIT = {
        "name":"Corrupted Spirit",
        "desc":"A soul so evil it transformed into a spirit that can manifest and slaughter.",
        "dmg":15,
        "heal":25,
        "hp":60,
        "tank":1.2,
        "perks":"none",
        "minlvl":45,
    }


class Bosses():
    GIGAGOBLIN = {
        "name":"Gigagoblin",
        "desc":"Its VERY big.",
        "minlvl":3,
        "plvl":15,
        "returndmg":100,
        "drop":Extra.GOBLINCHARM,
        "summoncost":50000,
    }

    HIVESLAYER = {
        "name":"Hive Slayer",
        "desc":"A giant hivemind monster.",
        "minlvl":4,
        "plvl":25,
        "returndmg":200,
        "drop":Weapons.HIVESLICER,
        "summoncost":100000,
    }

    WORLDEATER = {
        "name":"World Eater",
        "desc":"A universal terror.",
        "minlvl":5,
        "plvl":35,
        "returndmg":300,
        "drop":Armor.WORLDARMOR,
        "summoncost":200000,
    }

    ANCIENTCASTER = {
        "name":"Ancient Magic Caster",
        "desc":"This evil monster has been sleeping for centuries collecting energy.",
        "minlvl":6,
        "plvl":45,
        "returndmg":400,
        "drop":Extra.POWERORB,
        "summoncost":300000,
    }

    LIFECOLLECTOR = {
        "name":"Life Collector",
        "desc":"He has come to claim what is his.",
        "minlvl":7,
        "plvl":55,
        "returndmg":400,
        "drop":Weapons.LIFEEXTRACTOR,
        "summoncost":350000,
    }

    DEVILSSON = {
        "name":"Devils Son",
        "desc":"His father has sent him.",
        "minlvl":8,
        "plvl":65,
        "returndmg":400,
        "drop":Armor.DEMONICARMOR,
        "summoncost":450000,
    }


class RandomLists():
    #weapons
    WEAPON_COMMON = [
        Weapons.SWORD,
        Weapons.DAGGER,
        Weapons.WEAKWAND,
        Weapons.SHORTSWORD,
    ]

    WEAPON_NORMAL = [
        Weapons.STEELSWORD,
        Weapons.GIANTROCK,
        Weapons.ENHANCEDSWORD,
        Weapons.BONESWORD,
    ]

    WEAPON_UNCOMMON = [
        Weapons.BOW,
        Weapons.PUREGOLDSWORD,
        Weapons.MANACATALYST,
        Weapons.VAMPIRETOOTH,
    ]

    WEAPON_RARE = [
        Weapons.DAMAGEWAND,
        Weapons.BIGCANNON,
        Weapons.FIREWAND,
        Weapons.ICEWAND,
        Weapons.STREAMWAND,
    ]

    WEAPON_VERYRARE = [
        Weapons.FIRESWORD,
        Weapons.CRYSTALSWORD,
        Weapons.WATERMANIPULATOR,
        Weapons.SCYTHE,
        Weapons.KATANA,
    ]

    WEAPON_EPIC = [
        Weapons.LANCEOFSTARS,
        Weapons.SPIRITSLICER,
        Weapons.DARKORB,
        Weapons.MORNINGSTAR,
        Weapons.STEELGAUNTLETS,
    ]

    WEAPON_UNSTABLE = [
        Weapons.DRAGONSWORD,
        Weapons.AXEOFDESTRUCTION,
        Weapons.HELLMETALSWORD,
        Weapons.SHURIKEN,
        Weapons.CLAYMORE,
    ]

    WEAPON_CORRUPTED = [
        Weapons.SUNRAY,
        Weapons.LINKBREAKER,
        Weapons.DIVINESTAFF,
        Weapons.REAPERSCYTHE,
        Weapons.NULLW,
    ]

    WEAPON_LIMITED = [
        Weapons.BETASWORD,
        Weapons.AIRBLADE,
    ]

    WEAPON_UNIQUE = [
        Weapons.HIVESLICER,
        Weapons.LIFEEXTRACTOR,
    ]

    #armor
    ARMOR_COMMON = [
        Armor.PANTS,
        Armor.ROBE,
        Armor.UNDERPANTS,
        Armor.BOOTS,
    ]

    ARMOR_NORMAL = [
        Armor.CHAINMAIL,
        Armor.STONEARMOR,
        Armor.WIND,
        Armor.WOOD,
    ]

    ARMOR_UNCOMMON = [
        Armor.STEEL,
        Armor.HARDENEDSTONE,
        Armor.SWORDARMOR,
        Armor.HARDENEDSKIN,
    ]

    ARMOR_RARE = [
        Armor.HARDENEDSTEEL,
        Armor.THINCRYSTAL,
        Armor.VOLCANOARMOR,
        Armor.PLATEDARMOR,
        Armor.HARDENEDWATER,
    ]

    ARMOR_VERYRARE = [
        Armor.MAGICROBE,
        Armor.MANTLEOFDEATH,
        Armor.ENERGYARMOR,
        Armor.DARKMANTLE,
        Armor.AURA,
    ]

    ARMOR_EPIC = [
        Armor.CURSEDSTONE,
        Armor.MAGICSTEEL,
        Armor.DOUBLEARMOR,
        Armor.MAGICARMOR,
        Armor.SPIKEARMOR,
    ]

    ARMOR_UNSTABLE = [
        Armor.FIREGOLEM,
        Armor.CRYSTALARMOR,
        Armor.BLACKMAGICROBE,
        Armor.TRIPLEARMOR,
        Armor.DRAGONMAIL,
    ]

    ARMOR_CORRUPTED = [
        Armor.CORESMELTER,
        Armor.GAMBLERS,
        Armor.FIBREOFHATRED,
        Armor.QUADRUPLEARMOR,
        Armor.MANAARMOR,
    ]

    ARMOR_LIMITED = [
        Armor.BETAARMOR,
        Armor.OVERGROWN,
    ]

    ARMOR_UNIQUE = [
        Armor.WORLDARMOR,
        Armor.DEMONICARMOR,
    ]

    #extras
    EXTRA_COMMON = [
        Extra.LIGHTBUG,
        Extra.EYEPROTECTION,
        Extra.WATER,
        Extra.WORM,
    ]

    EXTRA_NORMAL = [
        Extra.BLADESHARPENER,
        Extra.TURBOSHROOM,
        Extra.BEE,
        Extra.LANTERN,
    ]

    EXTRA_UNCOMMON = [
        Extra.LIGHTSHIELD,
        Extra.TOOLBOX,
        Extra.SPIDER,
        Extra.BRIGHTLIGHT,
    ]

    EXTRA_RARE = [
        Extra.HEALWAND,
        Extra.STRENGTHWAND,
        Extra.TIMEBENDER,
        Extra.DOG,
        Extra.DMGGEM,
    ]

    EXTRA_VERYRARE = [
        Extra.HEAVYSHIELD,
        Extra.RADIANCEWAND,
        Extra.PAINKILLER,
        Extra.CAT,
        Extra.CASTERAMULET,
    ]

    EXTRA_EPIC = [
        Extra.SUPERSHIELD,
        Extra.LIGHTCOLLECTOR,
        Extra.SHARDOFDARKNESS,
        Extra.HARDHAT,
        Extra.BIOOVERCLOCKER,
    ]

    EXTRA_UNSTABLE = [
        Extra.CLONEATK,
        Extra.PUREHELL,
        Extra.DRAGONSCALE,
        Extra.MAGICMIRROR,
        Extra.CARBONSHIELD,
    ]

    EXTRA_CORRUPTED = [
        Extra.BLACKMAGICWAND,
        Extra.CRIMSONDAGGER,
        Extra.MOONREFRACTOR,
        Extra.FIREORB,
        Extra.ARM3,
    ]

    EXTRA_LIMITED = [
        Extra.BETASHIELD,
        Extra.SIRENSSONG,
    ]

    EXTRA_UNIQUE = [
        Extra.GOBLINCHARM,
        Extra.POWERORB,
    ]

    #monsters
    LVL0 = [
        Monster.SLIME,
        Monster.EVILMONK,
        Monster.CURSEDROCK,
        Monster.EVILDOG,
        Monster.LIZARD,
    ]

    LVL5 = [
        Monster.GOBLIN,
        Monster.DRAGONFLY,
        Monster.SKELETON,
        Monster.LIGHTNING,
        Monster.OGRE,
    ]

    LVL15 = [
        Monster.STONEGOLEM,
        Monster.SMOKE,
        Monster.ICEWIZARD,
        Monster.FIREWIZARD,
        Monster.WIZARD,
    ]

    LVL25 = [
        Monster.FIREGOLEM,
        Monster.GIANTSPIDER,
        Monster.GHOST,
        Monster.ANCIENTSPIRIT,
        Monster.VAMPIRE,
    ]

    LVL45 = [
        Monster.BLACKDRAGON,
        Monster.REAPER,
        Monster.ARCHANGEL,
        Monster.DEVILSMINION,
        Monster.CORRUPTEDSPIRIT,
    ]

    BOSSES = [
        Bosses.GIGAGOBLIN,
        Bosses.HIVESLAYER,
        Bosses.WORLDEATER,
        Bosses.ANCIENTCASTER,
        Bosses.LIFECOLLECTOR,
        Bosses.DEVILSSON,
    ]


class Basics():
    RARITIES = [ #list of rarities for items (used for random drops ect)
        "free",
        "common",
        "normal",
        "uncommon",
        "rare",
        "very rare",
        "epic",
        "unstable",
        "corrupted",
    ]

    WORTH = {
        "free":0,
        "common":50,
        "normal":100,
        "uncommon":500,
        "rare":1500,
        "very rare":5000,
        "epic":10000,
        "unstable":25000,
        "corrupted":50000,
        "limited":7500,
        "unique":30000,
    }

    SHOPWEAPONS = [
        Weapons.BETASWORD,
        Weapons.AIRBLADE,
    ]

    SHOPARMOR = [
        Armor.BETAARMOR,
        Armor.OVERGROWN,
    ]

    SHOPEXTRA = [
        Extra.BETASHIELD,
        Extra.SIRENSSONG,
    ]

    RAREDROPS = {
        "a":[Monster.BLACKDRAGON,Extra.DRAGONSCALE,"extra"],
        "b":[Monster.CURSEDROCK,Armor.HARDENEDSTONE,"armor"],
        "c":[Monster.STONEGOLEM,Armor.CURSEDSTONE,"armor"],
        "d":[Monster.FIREGOLEM,Armor.FIREGOLEM,"armor"],
        "e":[Monster.REAPER,Weapons.REAPERSCYTHE,"weapon"],
        "f":[Monster.VAMPIRE,Weapons.VAMPIRETOOTH,"weapon"],
    }