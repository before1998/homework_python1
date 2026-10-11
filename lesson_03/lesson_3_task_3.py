from address import Address
from mailing import Mailing


def main():
    from_address = Address("101000", "Москва", "ул. Тверская", "1", "10")
    to_address = Address(
        "190000",
        "Санкт-Петербург",
        "Невский проспект",
        "25",
        "5")

    my_mailing = Mailing(to_address, from_address, 350.50, "RU123456789")

    print(
        f"Отправление {my_mailing.track} "
        f"из {my_mailing.from_address} "
        f"в {my_mailing.to_address}. "
        f"Стоимость {my_mailing.cost} рублей."
    )


if __name__ == "__main__":
    main()
