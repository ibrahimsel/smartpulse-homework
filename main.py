import calculations as c


def main():
    print("EDW in total:",           c.calc_edw_in())
    print("EDW out total:",          c.calc_edw_out())
    print("EDW total:",              c.calc_edw_total())
    print("Manufacturer in total:",  c.calc_manufacturer_in())
    print("Manufacturer out total:", c.calc_manufacturer_out())
    print("Manufacturer total:",     c.calc_manufacturer_total())
    print("Total:", c.calc_total())

    print("hourly total:", c.hourly_total())


if __name__ == '__main__':
    main()
