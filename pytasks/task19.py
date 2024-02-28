# 1. Создайте класс BankAccount с атрибутами client_id, client_first_name, client_last_name, balance и методами
# add() и withdraw(), при помощи которых можно пополнять счет и выводить средства 
# со счета соответственно. Атрибут balance должен 
# инициализироваться по умолчанию значением 0.0 и меняться при срабатывании методов add() и withdraw().

class BankAccount:
    
    def __init__(self, client_id, client_first_name, client_last_name, balance = 0.0):
        self.client_id = id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance
    
    def add(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Недостаточно средств')
        else:
            self.balance -= amount
            return self.balance

new_account = BankAccount('22', 'Arsen', 'Tsadzikidze')
new_account.add(500)
print(new_account.balance)


