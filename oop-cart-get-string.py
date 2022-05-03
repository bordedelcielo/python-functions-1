# Create a class called cart that retains items and has methods to add, remove, and show
class Cart():
    def __init__(self, inventory=[]):
        self.inventory = inventory
        
    def add(self):
        item = input('What would you like to add to your cart?').title()
        self.inventory.append(item)
        print(f'{item} was added to your cart.')
        
    def delete(self):
        item = input('What would you like to delete from your cart?').title()
        self.inventory.remove(item)
        print(f'{item} was removed from your cart.')
        
    def clear(self):
        confirm = input('Are you sure that you would like to clear your cart?').lower()
        if confirm == 'yes':
            self.inventory = []
            print('Your cart has been emptied.')
        else:
            print('Your cart has not been emptied.')
    
    def show(self):
        print(f'Here is your cart: {self.inventory}.')
    
    def quit(self):
        print(f'Thank you for shopping with us! Here is your order: {self.inventory}.')
        
    def run(self):
        running = True
        while running == True:
            decision = input('What would you like to do? Show/Add/Delete/Clear or Quit?').lower()
            if decision == 'quit':
                self.quit()
                running = False
            elif decision == 'show':
                self.show()
            elif decision == 'add':
                self.add()
            elif decision == 'delete':
                self.delete()
            elif decision == 'clear':
                self.clear()
            else:
                print('Please select a valid option.')

this_cart = Cart()
this_cart.run()

class GetString():
    def getString(self):
        self.string = input('What would you like this OOP to print?')
    def printString(self):
        print(f'Here is your string! {self.string}.')
        
string = GetString()
string.getString()
string.printString()