class priceChart (object): 
  
    __isSelf = None
  
    def __init__(self, rules): 
  
        """private constructor"""
        if priceChart.__isSelf == None:
            priceChart.__isSelf = self
            priceChart.__isSelf.price_rules = rules
            priceChart.__isSelf.prices = dict()
        else:
            raise Exception ("This class is a singleton!")

        priceChart.__isSelf.__parse_price_chart()

    def __parse_price_chart(self):
        """ Private function to map the prices against lead codes """

        for price in self.price_rules['price_chart']:
            self.prices[price['lead_code']] = float(price['Price'])
        return True

    def is_valid_lead(self, lead_code):
        """ Function to check whether the lead code is valid
            Returns Boolean 
        """
        if lead_code in self.prices:
            return True
        else:
            return False

    def get_lead_price(self, lead_item):
        """Function to get the lead price against lead code
           lead_code string
           returns float
        """
        return float(self.prices[lead_item])

    def get_bonus_amount(self, lead_item, lead_count):
        """ Function to retrieve the calculated total bonus against lead code and lead counts
            lead_code string, lead_count int
            returns float
        """
        bonus_amount = 0
        for bonus_item in self.price_rules['bonus_chart']:
            if lead_item == bonus_item['lead'] \
                and lead_count > bonus_item['quantity_more_than']:
                bonus_amount = bonus_item['bonus_amount'] \
                    if bonus_item['type'] == 'amount' \
                        else (self.prices[lead_item] * lead_count) \
                            * float(bonus_item['bonus_amount'])/100
        return float(bonus_amount)

    def close_chart(self):
        """ Initialize the singleton instance 
        """
        priceChart.__isSelf = None