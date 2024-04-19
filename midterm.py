class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()

    def _initialize_seats(self):
        for row in range(1, self._rows + 1):
            self._seats[row] = ['O' for _ in range(self._cols)]

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)

    def book_seats(self, id, seat_list):
        for row, col in seat_list:
            if row not in self._seats or col not in range(1, self._cols + 1):
                raise ValueError("Invalid seat")
            if self._seats[row][col - 1] == 'X':
                raise ValueError(f"Seat {row}-{col} is already booked")
            self._seats[row][col - 1] = 'X'

    def view_show_list(self):
        print("Shows running in this hall:")
        for show_info in self._show_list:
            print(f"ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def view_available_seats(self, id):
        for row, seats in self._seats.items():
            print(f"Row {row}: ", end='')
            for col, seat_status in enumerate(seats, start=1):
                if seat_status == 'O':
                    print(f"{col} ", end='')
            print()


class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Cinema_System:
    def __init__(self):
        self.hall = Hall(rows=5, cols=10, hall_no=1)
        self.hall.entry_show(id='1', movie_name='Rajkumar', time='7:00 PM')
        self.hall.entry_show(id='2', movie_name='Priotoma', time='9:00 PM')
        Star_Cinema.entry_hall(self.hall)

    def run(self):
        while True:
            print("\nOptions:")
            print("1. View all shows today")
            print("2. View available seats")
            print("3. Book ticket")
            print("4. Exit")

            option = input("Enter option: ")

            if option == '1':
                self.hall.view_show_list()
            elif option == '2':
                id = input("Enter show ID: ")
                self.hall.view_available_seats(id)
            elif option == '3':
                id = input("Enter show ID: ")
                num_seats = int(input("Enter number of seats: "))
                seat_list = []
                for _ in range(num_seats):
                    row = int(input("Enter row: "))
                    col = int(input("Enter column: "))
                    seat_list.append((row, col))
                try:
                    self.hall.book_seats(id, seat_list)
                    print("Tickets booked successfully!")
                except ValueError as e:
                    print("Error:", e)
            elif option == '4':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    cinema_Hall_system = Cinema_System()
    cinema_Hall_system.run()


