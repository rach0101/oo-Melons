"""Classes for melon orders."""

class AbstractMelonOrder:
    """For all melon orders"""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
       

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        
        if self.species == 'Christmas Melon':
            base_price = 1.5 * base_price

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        self.order_type = "domestic"
        self.tax = 0.08
        super().__init__(species, qty)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17
        super().__init__(species, qty)

    def get_total(self):
        """Calculate price, including tax."""
        flat_fee = 0
        
        if self.qty < 10:
            flat_fee = 3
        
        return super().get_total() + flat_fee


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order made by the government"""
    
    def __init__(self, species, qty, passed):
        self.tax = 0
        self.passed = passed

        super().__init__(species, qty)


    def mark_inspection(self):
        """Takes boolean and updates whether or not melon has passed inspection"""
        
        passed_inspection = False

        if self.passed:
            print("YAAAAY I PASSED THE INSPECTION")
            passed_inspection = True 
        
        return passed_inspection