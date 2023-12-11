class SnakesCafe:
    def print_intro(self):
        print("**************************************")
        print("**    Welcome to the Snakes Cafe!   **")
        print("**    Please see our menu below.    **")
        print("** To quit at any time, type 'quit' **")
        print("**************************************\n")

    def print_menu(self):
        menu = {
            'Appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
            'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
            'Desserts': ['Ice Cream', 'Cake', 'Pie'],
            'Drinks': ['Coffee', 'Tea', 'Unicorn Tears']
        }
        for category, items in menu.items():
            print(f"{category}\n{'-' * len(category)}")
            print('\n'.join(items))
            print()

    def acknowledge_order(self, item, quantity):
        print(f"\n** {quantity} order{'s' if quantity > 1 else ''} of {item} has been added to your meal **\n")

    def take_orders(self):
        orders = {}
        while True:
            print("***********************************")
            print("** What would you like to order? **")
            print("***********************************")
            order = input("> ")
            if order.lower() == 'quit':
                print("Exiting")
                break

            orders[order] = orders.get(order, 0) + 1
            self.acknowledge_order(order, orders[order])

if __name__ == "__main__":
    snakes_cafe = SnakesCafe()
    snakes_cafe.print_intro()
    snakes_cafe.print_menu()
    snakes_cafe.take_orders()
