__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2/28/2020 11:03 PM'

LABEL_NAME = [
    'Abyssal_Mask_item',
    'Adaptive_Helm_item',
    'Aegis_of_the_Legion_item',
    'Aether_Wisp_item',
    'Amplifying_Tome_item',
    "Archangel's_Staff_item",
    'Ardent_Censer_item',
    "Athene's_Unholy_Grail_item",
    'B.F.Sword_item',
    "Bami's_Cinder_item",
    "Banshee's_Veil_item",
    "Berserker's_Greaves_item",
    'Bilgewater_Cutlass_item',
    'Black_Cleaver_item',
    'Blade_of_the_Ruined_King_item',
    'Blasting_Wand_item',
    'Bloodrazor_item',
    'Bloodthirster_item',
    'Boots_of_Mobility_item',
    'Boots_of_Speed_item',
    'Boots_of_Swiftness_item',
    'Bramble_Vest_item',
    'Bulwark_of_the_Mountain_item',
    'Catalyst_of_Aeons_item',
    "Caulfield's_Warhammer_item",
    'Chain_Vest_item',
    'Chalice_of_Harmony_item',
    'Cinderhulk_item',
    'Cloak_of_Agility_item',
    'Cloth_Armor_item',
    'Control_Ward_item',
    'Corrupting_Potion_item',
    'Crystalline_Bracer_item',
    'Cull_item',
    'Dagger_item',
    'Dark_Seal_item',
    "Dead_Man's_Plate_item",
    "Death's_Dance_item",
    "Doran's_Blade_item",
    "Doran's_Ring_item",
    "Doran's_Shield_item",
    'Duskblade_of_Draktharr_item',
    'Edge_of_Night_item',
    'Elixir_of_Iron_item',
    'Elixir_of_Sorcery_item',
    'Elixir_of_Wrath_item',
    'Essence_Reaver_item',
    "Executioner's_Calling_item",
    'Eye_of_the_Herald_buff_item',
    'Faerie_Charm_item',
    'Farsight_Alteration_item',
    'Fiendish_Codex_item',
    'Forbidden_Idol_item',
    'Frostfang_item',
    'Frozen_Heart_item',
    'Frozen_Mallet_item',
    'Gargoyle_Stoneplate_item',
    "Giant's_Belt_item",
    'Glacial_Shroud_item',
    'Guardian_Angel_item',
    "Guinsoo's_Rageblade_item",
    'Harrowing_Crescent_item',
    'Haunting_Guise_item',
    'Health_Potion_item',
    'Hexdrinker_item',
    'Hextech_GLP-800_item',
    'Hextech_Gunblade_item',
    'Hextech_Protobelt-0_item',
    'Hextech_Revolver_item',
    "Hunter's_Machete_item",
    "Hunter's_Talisman_item",
    'Iceborn_Gauntlet_item',
    'Infinity_Edge_item',
    'Ionian_Boots_of_Lucidity_item',
    "Jaurim's_Fist_item",
    'Kindlegem_item',
    'Kircheis_Shard_item',
    "Knight's_Vow_item",
    'Last_Whisper_item',
    "Liandry's_Torment_item",
    'Lich_Bane_item',
    'Locket_of_the_Iron_Solari_item',
    'Long_Sword_item',
    "Lord_Dominik's_Regards_item",
    'Lost_Chapter_item',
    "Luden's_Echo_item",
    'Manamune_item',
    'Maw_of_Malmortius_item',
    "Mejai's_Soulstealer_item",
    'Mercurial_Scimitar_item',
    "Mercury's_Treads_item",
    "Mikael's_Crucible_item",
    'Morellonomicon_item',
    'Mortal_Reminder_item',
    "Nashor's_Tooth_item",
    'Needlessly_Large_Rod_item',
    'Negatron_Cloak_item',
    'Ninja_Tabi_item',
    'Null-Magic_Mantle_item',
    'Oracle_Lens_item',
    'Pauldrons_of_Whiterock_item',
    'Perfect_Hex_Core_item',
    'Phage_item',
    'Phantom_Dancer_item',
    'Pickaxe_item',
    'Prototype_Hex_Core_item',
    'Quicksilver_Sash_item',
    "Rabadon's_Deathcap_item",
    "Randuin's_Omen_item",
    'Rapid_Firecannon_item',
    'Ravenous_Hydra_item',
    'Recurve_Bow_item',
    'Redemption_item',
    'Refillable_Potion_item',
    'Rejuvenation_Bead_item',
    'Relic_Shield_item',
    'Righteous_Glory_item',
    'Rod_of_Ages_item',
    'Ruby_Crystal_item',
    "Runaan's_Hurricane_item",
    'Runesteel_Spaulders_item',
    'Runic_Echoes_item',
    "Rylai's_Crystal_Scepter_item",
    'Sanguine_Blade_item',
    'Sapphire_Crystal_item',
    "Seeker's_Armguard_item",
    "Seraph's_Embrace_item",
    'Serrated_Dirk_item',
    'Shard_of_True_Ice_item',
    'Sheen_item',
    "Shurelya's_Reverie_item",
    "Skirmisher's_Sabre_item",
    'Slightly_Magical_Boots_item',
    "Sorcerer's_Shoes_item",
    'Spectral_Sickle_item',
    "Spectre's_Cowl_item",
    'Spellbinder_item',
    "Spellthief's_Edge_item",
    'Spirit_Visage_item',
    "Stalker's_Blade_item",
    'Statikk_Shiv_item',
    'Steel_Shoulderguards_item',
    "Sterak's_Gage_item",
    'Stinger_item',
    'Stopwatch_item',
    'Stormrazor_item',
    'Sunfire_Cape_item',
    "Targon's_Buckler_item",
    'Tear_of_the_Goddess_item',
    'The_Black_Spear_item',
    'The_Hex_Core_mk-2_item',
    'The_Hex_Core_mk-_item',
    'Thornmail_item',
    'Tiamat_item',
    'Titanic_Hydra_item',
    'Total_Biscuit_of_Everlasting_Will_item',
    'Trinity_Force_item',
    'Twin_Shadows_item',
    'Umbral_Glaive_item',
    'Vampiric_Scepter_item',
    'Void_Staff_item',
    "Warden's_Mail_item",
    'Warding_Totem_item',
    "Warmog's_Armor_item",
    'Warrior_item',
    "Wit's_End_item",
    "Youmuu's_Ghostblade_item",
    'Zeal_item',
    "Zeke's_Convergence_item",
    "Zhonya's_Hourglass_item",
    'none',
    'oblivion_orb_item'
]
