class gym_manager:
    regimen = {}
    customers = dict()
    def_init_(self,s_id,s_name):
        self.s_id = s_idself.s_name = s_name

    @classmethod
    def addcustomer(cls, customer):
        gym_manager.customers[customer.getphoeno()] = customer
ob = gym_manager('s_1','Mayu')        
