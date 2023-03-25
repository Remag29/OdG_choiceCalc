
class Event:
    def __init__(self, name, tresorerie, competence, securite, bonus=[0, 0, 0], conditions=[0, 0, 0]):
        self.name = name
        self.tresorerie = tresorerie
        self.competence = competence
        self.securite = securite
        self.score = tresorerie + competence + securite
        self.bonus = bonus
        self.conditions = conditions

    def __str__(self):
        srting = self.name + " : " + str(self.tresorerie) + " " + str(self.competence) + " " + str(
            self.securite) + " Score : " + str(self.score)
        return srting


class Starter:
    def __init__(self, name, tresorerie, competence, securite):
        self.name = name
        self.tresorerie = tresorerie
        self.competence = competence
        self.securite = securite
        self.score = tresorerie + competence + securite
        self.bonus = [0, 0, 0]

    def __str__(self):
        srting = str(self.name) + " : " + str(self.tresorerie) + " " + str(self.competence) + " " + str(
            self.securite) + " Score : " + str(self.score)
        return srting

    def apply_bonus(self):
        self.tresorerie += self.bonus[0]
        self.competence += self.bonus[1]
        self.securite += self.bonus[2]


def apply_event(states_list, event_list):
    new_starter_list = []
    for states in states_list:
        for event in event_list:
            if __allow_conditions__:  # Si on autorise les conditions
                if states.tresorerie < event.conditions[0] or states.competence < event.conditions[1] or states.securite < event.conditions[2]:
                    continue
                else:
                    new_state = Starter(states.name, states.tresorerie, states.competence, states.securite)
                    new_state.name += "." + event.name
                    new_state.tresorerie += event.tresorerie
                    new_state.competence += event.competence
                    new_state.securite += event.securite
                    new_state.score = new_state.tresorerie + new_state.competence + new_state.securite
                    for i in range(0, 3):
                        new_state.bonus[i] = states.bonus[i] + event.bonus[i]
                    new_starter_list.append(new_state)
    return new_starter_list


def print_frequency(states_list):
    # Calculer les fréquences des scores
    score_freq = {}
    states_list = sort_by_score(states_list)
    for starter in states_list:
        if starter.score in score_freq:
            score_freq[starter.score] += 1
        else:
            score_freq[starter.score] = 1

    # Afficher le tableau des fréquences des scores
    print("Score\tFréquence")
    for score, freq in score_freq.items():
        print("{}\t{}".format(score, freq))


def sort_by_score(states_list):
    return sorted(states_list, key=lambda x: x.score, reverse=True)


if __name__ == '__main__':

    __gold_par_tour__ = 2
    __allow_conditions__ = True

    # STARTER ------------------------------------------
    starter1 = Starter("Starter1", 12, 3, 5)
    starter2 = Starter("Starter2", 8, 5, 7)
    starter3 = Starter("Starter3", 10, 7, 3)
    starter_list = [starter1, starter2, starter3]

    # CHOICE 1 ------------------------------------------
    choice11 = Event("Choice11", 0, 0, 0)
    choice12 = Event("Choice12", -2, 0, 2, [-1, 0, 0])
    choice13 = Event("Choice13", -3, 0, 3)
    choice14 = Event("Choice14", -8, 0, 1, [0, 0, 2])
    choice1 = [choice11, choice12, choice13, choice14]

    new_list = apply_event(starter_list, choice1)

    # EVENEMENT 1 ------------------------------------------
    covid = Event("Covid", -4, -2, -2)

    new_list = apply_event(new_list, [covid])

    # END TOUR 1 ------------------------------------------
    for starter in new_list:
        starter.tresorerie += __gold_par_tour__
        starter.score = starter.tresorerie + starter.competence + starter.securite
        starter.apply_bonus()

    print_frequency(new_list)

    # CHOICE 2 ------------------------------------------
    choice21 = Event("Choice21", 0, 0, 0)
    choice22 = Event("Choice22", -3, 0, 3, [0, 0, 2])
    choice23 = Event("Choice23", -5, 0, 3, [0, 0, 2])

    choice2 = [choice21, choice22, choice23]

    new_list = apply_event(new_list, choice2)

    # EVENEMENT 2 ------------------------------------------
    ransomware1 = Event("Ransomware", -2, 0, -3)
    ransomware2 = Event("Ransomware", -5, 0, 0)

    new_list = apply_event(new_list, [ransomware1, ransomware2])

    # END TOUR 2 ------------------------------------------
    for starter in new_list:
        starter.tresorerie += __gold_par_tour__
        starter.score = starter.tresorerie + starter.competence + starter.securite
        starter.apply_bonus()
    print_frequency(new_list)

    # CHOICE 3 ------------------------------------------
    choice31 = Event("Choice31", -2, 0, 0, [0, 0, 1])
    choice32 = Event("Choice32", 2, 0, -2)
    choice33 = Event("Choice33", -4, 0, 2, [0, 0, 2])

    choice3 = [choice31, choice32, choice33]

    new_list = apply_event(new_list, choice3)

    # EVENEMENT 3 ------------------------------------------
    hausse_prix1 = Event("Hausse_prix", 0, -2, 0)
    hausse_prix2 = Event("Hausse_prix", -2, 0, 0)

    new_list = apply_event(new_list, [hausse_prix1, hausse_prix2])

    # END TOUR 3 ------------------------------------------
    for starter in new_list:
        starter.tresorerie += __gold_par_tour__
        starter.score = starter.tresorerie + starter.competence + starter.securite
        starter.apply_bonus()
    print_frequency(new_list)

    # FIN -----------------------------------------------

    # for state in starters_sorted:
    #     print(state)

    print("Fin du jeu")
    print("Total de solution : ", len(new_list))
