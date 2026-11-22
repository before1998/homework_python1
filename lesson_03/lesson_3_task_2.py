from smartphone import Smartphone


def main():
    catalog = [
        Smartphone("Apple", "iPhone 14", "+79001112233"),
        Smartphone("Samsung", "Galaxy S23", "+79004445566"),
        Smartphone("Xiaomi", "Redmi Note 12", "+79007778899"),
        Smartphone("Google", "Pixel 7", "+79000001122"),
        Smartphone("OnePlus", "11", "+79003334455"),
    ]

    for phone in catalog:
        print(f"{phone.brand} - {phone.model}. {phone.phone_number}")


if __name__ == "__main__":
    main()
