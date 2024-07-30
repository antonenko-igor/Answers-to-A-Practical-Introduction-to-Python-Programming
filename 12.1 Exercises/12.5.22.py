print("Game Mab Libs")
print("---All about birds---")
print()
adjective_0 = input("adjective - ")
plural_noun_1 = input("noun(pl) - ")
adjective_color_2 = input("adjective_color - ")
adjective_color_3 = input("adjective_color - ")
adjective_color_4 = input("adjective_color - ")
adjective_5 = input("adjective - ")
noun_6 = input("noun - ")
plural_noun_body_parts_7 = input("noun(pl), parts of the body - ")
verb_8 = input("verb - ")
verb_9 = input("verb - ")
adjective_10 = input("adjective - ")
plural_noun_animals_11 = input("noun(pl,animals - ")
verb_12 = input("verb - ")
noun_13 = input("verb - ")
verb_14 = input("verb - ")
plural_noun_animals_15 = input("noun(pl),animals - ")
plural_noun_16 = input("noun(pl) - ")
verb_17 = input("verb- ")
plural_noun_18 = input("noun(pl) - ")
plural_noun_19 = input("noun(pl) - ")

s = ""
lines = [line.strip() for line in open('mad_libs.txt')]
for line in lines:
	s += line
print()
print()
print(s.format(adjective_0,plural_noun_1,adjective_color_2,adjective_color_3,
	  adjective_color_4,adjective_5,noun_6,plural_noun_body_parts_7,verb_8,
	  verb_9,adjective_10,plural_noun_animals_11,verb_12,noun_13,verb_14,
	  plural_noun_animals_15,plural_noun_16,verb_17,plural_noun_18,plural_noun_19))  