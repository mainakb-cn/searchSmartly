from priceRules import priceChart

class Calculator( priceChart ) :

    def __init__(self, price_rules):
        """ Private initializer 
        """
        self.__added_leads = dict()
        self.lead_list = []
        self.total_price = 0
        priceChart.__init__(self, price_rules)

    def add(self, the_lead):
        """ Add lead item against a lead code
            the_lead string
            returns Boolean
        """
        if priceChart.is_valid_lead(self, the_lead):
            self.lead_list.append(the_lead)
            self.total_price += priceChart.get_lead_price(self, the_lead)
            if the_lead in self.__added_leads:
                self.__added_leads[the_lead] += 1
            else:
                self.__added_leads[the_lead] = 1
            return True
        else:
            raise Exception(f"The lead code {the_lead} is invalid")

    def total(self):
        """ Function to find total price including bonus for added leads
            returns float
        """
        bonus_amount = 0
        for lead, count in self.__added_leads.items():
            bonus_amount += priceChart.get_bonus_amount(self, lead, count)

        ''' initializing the singleton data object '''
        priceChart.close_chart(self)
        return self.total_price + bonus_amount